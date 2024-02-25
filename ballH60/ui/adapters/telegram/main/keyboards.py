from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from barsik.localisation import Localisation
from barsik.utils.keyboards import active_button

from models import BallH60

from .callback_data import NumCalcCallbackData


async def get_settings_keyboard(lang: str, local: Localisation, settings: BallH60) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    button_text = ": ".join([await local.fs("btn", "num_base", lang), str(settings.base)])
    builder.button(text=button_text, callback_data=NumCalcCallbackData(field="base"))

    button_text = await local.fs("btn", "chk_numbers", lang)
    if settings.num_calc_numbers:
        button_text = active_button(button_text)
    builder.button(text=button_text, callback_data=NumCalcCallbackData(field="numbers"))

    button_text = await local.fs("btn", "chk_summer", lang)
    if settings.num_calc_summer:
        button_text = active_button(button_text)
    builder.button(text=button_text, callback_data=NumCalcCallbackData(field="summer"))

    builder.adjust(3)
    return builder.as_markup()
