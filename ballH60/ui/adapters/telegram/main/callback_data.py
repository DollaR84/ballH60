from aiogram.filters.callback_data import CallbackData


class NumCalcCallbackData(CallbackData, prefix="num_calc"):
    field: str
