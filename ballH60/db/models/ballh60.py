from barsik.db.models.base import Base
from barsik.db.mixins import BaseDBModel

import sqlalchemy as sa
import sqlalchemy.orm as so


class BallH60(BaseDBModel, Base):
    __tablename__ = "ballh60s"

    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey("users.id"))
    user: so.Mapped["User"] = so.relationship(foreign_keys=user_id)

    base: so.Mapped[int] = so.mapped_column(nullable=False, default=9)
    num_calc_numbers: so.Mapped[bool] = so.mapped_column(nullable=False, default=False)
    num_calc_summer: so.Mapped[bool] = so.mapped_column(nullable=False, default=False)

    GET_FIELDS = ["id", "user_id"]
    NO_UPDATE_FIELDS = ["id", "user_id"]
