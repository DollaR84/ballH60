from aiogram import Router, types
from aiogram.filters.command import CommandStart

from barsik.aiogram.functions import get_user
from barsik.localisation import Localisation

from db import DB

from dishka.integrations.aiogram import FromDishka

from models import User

from services import BallH60Client

from ..keyboards import get_settings_keyboard


class CommandHandlers:

    @classmethod
    async def start_handler(
            cls, message: types.Message,
            db: FromDishka[DB],
            local: FromDishka[Localisation],
            ballH60: FromDishka[BallH60Client],
    ):
        user = User.from_schema(get_user(message))
        user = await db.get_and_update_user(user)
        settings = await ballH60.get_settings(user)

        message_text = await local.fs("phrases", "ball_menu", user.lang)
        keyboard = await get_settings_keyboard(user.lang, local, settings)

        await message.answer(message_text, reply_markup=keyboard, parse_mode="HTML")

    @classmethod
    def register(cls, router: Router, **kwargs):
        router.message.register(cls.start_handler, CommandStart())
