from barsik.db.models.base import Base
from barsik.db.models.user import BaseUser
from barsik.db.mixins import BaseDBModel


class User(BaseUser, BaseDBModel, Base):
    ...
