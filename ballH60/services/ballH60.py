from itertools import cycle

from barsik.localisation import Localisation

from config import Config

from db import DB

from models import BallH60, User

from .api import num_calc as api


class BallH60Client:
    def __init__(self, config: Config, db: DB):
        self.db: DB = db
        self.cfg = config.services

        self.answers = {}

    async def init(self, local: Localisation):
        self.answers[9] = await local.get_data(local.current, "A9", "answers")
        self.answers[12] = await local.get_data(local.current, "A12", "answers")
        self.answers[36] = [str(i) for i in range(1, 36+1)]
        self.answers[54] = [str(i) for i in range(1, 54+1)]
        self.answers[78] = [str(i) for i in range(1, 78+1)]

    async def get_settings(self, user: User):
        ball = BallH60(user_id=user.id)
        settings = await self.db.get_ballh60_settings(ball)
        if not settings:
            settings = await self.db.create_ballh60_settings(ball)
        return settings

    async def update_settings(self, ball: BallH60, **kwargs):
        return await self.db.update_ballh60_settings(ball, **kwargs)

    def base_generator(self):
        for base in cycle(self.cfg.ballH60_base):
            yield base

    async def calc(self, user: User, question: str) -> str:
        settings = await self.get_settings(user)
        base = settings.base
        num_digits = settings.num_calc_numbers

        res = api.calc(question, base, num_digits)
        return self.answers[base][res-1]
