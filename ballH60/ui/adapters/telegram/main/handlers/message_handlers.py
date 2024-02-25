from typing import Annotated

from aiogram import F, types
from aiogram import Router

from barsik.aiogram.functions import get_user

from db import DB

from dishka.integrations.aiogram import Depends, inject

from models import User

from services import BallH60Client


class MessageHandlers:

    @classmethod
    @inject
    async def message_handler(
            cls, message: types.Message,
            db: Annotated[DB, Depends()],
            ballH60: Annotated[BallH60Client, Depends()],
    ):
        user = User.from_schema(get_user(message))
        user = await db.get_user(user)

        if not hasattr(message, "text"):
            return

        message_text = await ballH60.calc(user, message.text)
        await message.answer(message_text, parse_mode="HTML")

    @classmethod
    def register(cls, router: Router, **kwargs):
        router.message.register(cls.message_handler, F.text)
