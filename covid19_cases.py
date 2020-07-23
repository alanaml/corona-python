from datetime import date
from typing import NamedTuple


class Covid19Cases(NamedTuple):
    date: date
    confirmed: int
    deaths: int
    recovered: int
