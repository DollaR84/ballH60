from dataclasses import dataclass

from barsik.config.adapters.services import ServicesAdapter


@dataclass
class ServicesData:
    ballH60_base = [9, 12, 36, 54, 78,]


ServicesAdapter.data = ServicesData
