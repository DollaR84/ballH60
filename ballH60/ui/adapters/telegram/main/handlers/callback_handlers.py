from typing import Annotated

from aiogram import Bot, Router, types

from barsik.aiogram.functions import get_user
from barsik.localisation import Localisation

from db import DB

from dishka.integrations.aiogram import FromDishka, inject

from models import User

from services import BallH60Client

from ..callback_data import NumCalcCallbackData

from ..keyboards import get_settings_keyboard


class CallbackHandlers:

    @classmethod
    @inject
    async def num_calc_handler(
            cls, callback_query: types.CallbackQuery,
            callback_data: NumCalcCallbackData,
            bot: Annotated[Bot, FromDishka()],
            db: Annotated[DB, FromDishka()],
            local: Annotated[Localisation, FromDishka()],
            ballH60: Annotated[BallH60Client, FromDishka()],
    ):
        user = User.from_schema(get_user(callback_query))
        user = await db.get_user(user)
        settings = await ballH60.get_settings(user)

        if callback_data.field == "base":
            base_gen = ballH60.base_generator()
            for base in base_gen:
                if base == settings.base:
                    await ballH60.update_settings(settings, base=next(base_gen))
                    break

        elif callback_data.field == "numbers":
            current_value = settings.num_calc_numbers
            await ballH60.update_settings(settings, num_calc_numbers=not current_value)

        elif callback_data.field == "summer":
            current_value = bool(settings.num_calc_summer)
            await ballH60.update_settings(settings, num_calc_summer=not current_value)

        settings = await ballH60.get_settings(user)
        message_text = await local.fs("phrases", "ball_menu", user.lang)
        keyboard = await get_settings_keyboard(user.lang, local, settings)

        await callback_query.message.delete()
        await bot.send_message(user.chat_id, text=message_text, reply_markup=keyboard)
        await callback_query.answer()

    @classmethod
    def register(cls, router: Router, **kwargs):
        router.callback_query.register(cls.num_calc_handler, NumCalcCallbackData.filter())
