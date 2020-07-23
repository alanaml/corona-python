import json
from datetime import datetime
from country_times_series import CountryTimesSeries
from covid19_cases import Covid19Cases
from typing import List, Dict


class Covid19Reader:
    @staticmethod
    def covid19_data(file_name: str = "covid19.json") -> List[CountryTimesSeries]:
        with open(file_name, "r") as f:
            data: Dict[str, List[Dict]] = json.load(f)
        coutry_covid_cases: List[CountryTimesSeries] = []
        for country_name, cases in data.items():
            covide_cases = []
            for case in cases:
                str_date = case['date']
                date_type = datetime.strptime(str_date, '%Y-%m-%d')
                confirmed = case['confirmed']
                deaths = case['deaths']
                recovered = case['recovered']
                covide_cases.append(Covid19Cases(date_type, confirmed, deaths, recovered))
            coutry_covid_cases.append(CountryTimesSeries(covide_cases, country_name))
        return coutry_covid_cases
