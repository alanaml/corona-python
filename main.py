from typing import List, Tuple
from covid19_cases import Covid19Cases
from covid19_reader import Covid19Reader
from covid19_statistics import *

countries = Covid19Reader.covid19_data()

name_country = input("Please enter with a country name to check its info: ")

# testing SELECT COUNTRY and TOTAL CASES INFO
country_total_info: List[Covid19Cases] = total_cases_info(select_country(countries, name_country))
print('\n'.join(str(c) for c in country_total_info))  ##melhorar o print

print()

# testing NON NULL VALUES and AVERAGE RATE
print("Average rate considering first Corona cases until last computed day")
country_average_non_null: Tuple[float, float, float] = average_rate(non_null_values(select_country(countries,
                                                                                                   name_country)))

print("Confirmed: ", country_average_non_null[0])
print("Deaths: ", country_average_non_null[1])
print("Recovered: ", country_average_non_null[2])

print()

# testing WEEK STATISTICS
print("Week Statistics")
country_week_statistics = week_statistics(non_null_values(select_country(countries, name_country)))
for case in country_week_statistics:
    print(case.date, ": ", case)

print()

# testing MONTH STATISTICS
print("Month Statistics")
country_month_statistics = month_statistics(non_null_values(select_country(countries, name_country)))
for case in country_month_statistics:
    print(case.date, ": ", case)

print()

# testing GROWTH RATE
print("Week growth rate of confirmed cases")

country_growth_rate_week = growth_rate(week_statistics(non_null_values(select_country(countries, name_country))))
print(round(country_growth_rate_week, 3))

print()

# testing GROWTH RATE
print("Month growth rate of confirmed cases")

country_growth_rate_month = growth_rate(month_statistics(non_null_values(select_country(countries, name_country))))
print(round(country_growth_rate_month, 3))

print()

# testing SELECTED RANGE

first_date = input("Please, enter with first date ")
second_date = input("Please, enter with second  ")

country_range = growth_rate(non_null_values(selected_range(select_country(countries, name_country),
                                                           first_date,
                                                           second_date)))
print("The Growth rate in this specific range is: ", round(country_range, 3))

print()

# SECOND COUNTRY
name_country2 = input("Please enter with a country name to check its info: ")

# testing SELECT COUNTRY and TOTAL CASES INFO
country_total_info2: List[Covid19Cases] = total_cases_info(select_country(countries, name_country2))
print('\n'.join(str(c) for c in country_total_info2))  ##melhorar o print

print()

# testing NON NULL VALUES and AVERAGE RATE
print("Average rate considering first Corona cases until last computed day")
country_average_non_null2: Tuple[float, float, float] = average_rate(non_null_values(select_country(countries,
                                                                                                   name_country2)))

print("Confirmed: ", country_average_non_null2[0])
print("Deaths: ", country_average_non_null2[1])
print("Recovered: ", country_average_non_null2[2])

print()

# testing WEEK STATISTICS
print("Week Statistics")
country_week_statistics2 = week_statistics(non_null_values(select_country(countries, name_country2)))
for case in country_week_statistics2:
    print(case.date, ": ", case)

print()

# testing MONTH STATISTICS
print("Month Statistics")
country_month_statistics2 = month_statistics(non_null_values(select_country(countries, name_country2)))
for case in country_month_statistics2:
    print(case.date, ": ", case)

print()

# testing GROWTH RATE
print("Week growth rate of confirmed cases")

country_growth_rate_week2 = growth_rate(week_statistics(non_null_values(select_country(countries, name_country2))))
print(round(country_growth_rate_week2, 3))

print()

# testing GROWTH RATE
print("Month growth rate of confirmed cases")

country_growth_rate_month2 = growth_rate(month_statistics(non_null_values(select_country(countries, name_country2))))
print(round(country_growth_rate_month2, 3))

print()

country_range2 = growth_rate(non_null_values(selected_range(select_country(countries, name_country2),
                                                           first_date,
                                                           second_date)))
print("The Growth rate in this specific range is: ", round(country_range2, 3))