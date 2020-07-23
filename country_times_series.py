from typing import List, NamedTuple
from covid19_cases import Covid19Cases


class CountryTimesSeries(NamedTuple):
    daily_cases: List[Covid19Cases]
    country_name: str




