from typing import List, Tuple
from country_times_series import CountryTimesSeries
from covid19_cases import Covid19Cases
from datetime import datetime


def select_country(countries: List[CountryTimesSeries], country_name: str) -> List[Covid19Cases]:
    for country in countries:
        if country_name == country.country_name:
            return country.daily_cases


def total_cases_info(all_cases: List[Covid19Cases]) -> List[Covid19Cases]:
    last_info = [all_cases[-1]]
    return last_info


def non_null_values(all_cases: List[Covid19Cases]) -> List[Covid19Cases]:
    # non_null_case: List[Covid19Cases] = []
    # for case in all_cases:
    #     if case.confirmed > 0:
    #         non_null_case.append(case)
    return [case for case in all_cases if case.confirmed > 0]


def average_rate(all_cases: List[Covid19Cases]) -> Tuple[float, float, float]:
    date_first = all_cases[0].date
    date_last = all_cases[0].date

    confirmed_first = 0
    recovered_first = 0
    deaths_first = 0
    confirmed_last = 0
    death_last = 0
    recovered_last = 0

    for case in all_cases:
        date = case.date
        confirmed = case.confirmed
        death = case.deaths
        recovered = case.recovered
        if date < date_first:
            confirmed_first = confirmed
            deaths_first = death
            recovered_first = recovered
            date_first = date

        if date > date_last:
            confirmed_last = confirmed
            death_last = death
            recovered_last = recovered
            date_last = date

    delta_t = (date_last - date_first).days
    delta_confirmed = confirmed_last - confirmed_first
    delta_death = death_last - deaths_first
    delta_recovered = recovered_last - recovered_first
    confirmed_result: float = delta_confirmed / delta_t
    death_result: float = delta_death / delta_t
    recovered_result: float = delta_recovered / delta_t

    return confirmed_result, death_result, recovered_result


def month_statistics(all_cases: List[Covid19Cases]) -> List[Covid19Cases]:
    month_cases: List[Covid19Cases] = []

    for case in all_cases:
        if case.date.day == 1:
            month_cases.append(case)

    return month_cases


def week_statistics(all_cases: List[Covid19Cases]) -> List[Covid19Cases]:
    week_cases: List[Covid19Cases] = []

    for case in all_cases:
        if case.date.isoweekday() == 7:
            week_cases.append(case)

    return week_cases


def growth_rate(all_cases: List[Covid19Cases]) -> float:
    first = all_cases[0].confirmed
    last = all_cases[-1].confirmed
    size = (len(all_cases) - 1)

    result = (last / first) ** (1 / size)

    return result


def selected_range(all_cases: List[Covid19Cases], date1: str, date2: str) -> List[Covid19Cases]:
    date_first = datetime.strptime(date1, '%Y-%m-%d')
    date_second = datetime.strptime(date2, '%Y-%m-%d')
    range: List[Covid19Cases] = []
    for case in all_cases:
        if date_first < case.date < date_second:
            range.append(case)
    return range
