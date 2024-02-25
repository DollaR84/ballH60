from dataclasses import dataclass

from barsik.models.base import Base


@dataclass
class BallH60(Base):
    user_id: int
    id: int | None = None

    base: int = 9
    num_calc_numbers: bool = False
    num_calc_summer: bool = False
