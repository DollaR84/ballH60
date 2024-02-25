from config import Config

from barsik.db import BaseDB

from models import BallH60, User

from .adapters import *

from .mapper import DataMapper


class DB(BaseDB):

    def __init__(self, cfg: Config, *names: list[str]):
        super().__init__(cfg, *names)
        self.mapper = DataMapper(self.adapter)

    async def get_ballh60_settings(self, ball: BallH60):
        return await self.mapper.get(ball)

    async def create_ballh60_settings(self, ball: BallH60):
        return await self.mapper.create(ball)

    async def update_ballh60_settings(self, ball: BallH60, **kwargs):
        return await self.mapper.update(ball, **kwargs)
