from barsik.localisation import Localisation

from config import Config

from db import DB

from dishka import Provider, Scope, provide

from services import BallH60Client


class ServiceProvider(Provider):

    def __init__(self, config: Config, db: DB):
        super().__init__()

        self.ballH60: BallH60Client = BallH60Client(config, db)

    async def init(self, localisation: Localisation):
        await self.ballH60.init(localisation)

    @provide(scope=Scope.APP)
    def get_ballH60(self) -> BallH60Client:
        return self.ballH60
