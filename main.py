from covid19_reader import Covid19Reader
from covid19_statistics import *

countries = Covid19Reader.covid19_data()

name_country = input("Please enter with a country name to check its info: ")

# SELECT COUNTRY/ TOTAL CASES INFO
country_total_info: List[Covid19Cases] = total_cases_info(select_country(countries, name_country))
print(country_total_info)

print()

# NON NULL VALUES/ AVERAGE RATE
print("Average rate considering first Corona cases until last computed day")
country_average_non_null: Tuple[float, float, float] = average_rate(non_null_values(select_country(countries,
                                                                                                   name_country)))
print("Confirmed: ", round(country_average_non_null[0], 3))
print("Deaths: ", round(country_average_non_null[1], 3))
print("Recovered: ", round(country_average_non_null[2], 3))

print()

# WEEK STATISTICS
print("Week Statistics")
country_week_statistics = week_statistics(non_null_values(select_country(countries, name_country)))
for case in country_week_statistics:
    print(case.date, ": ", case)
print()
print("Week growth rate of confirmed cases")
country_growth_rate_week = growth_rate(week_statistics(non_null_values(select_country(countries, name_country))))
print(round(country_growth_rate_week, 3))

print()

# MONTH STATISTICS
print("Month Statistics")
country_month_statistics = month_statistics(non_null_values(select_country(countries, name_country)))
for case in country_month_statistics:
    print(case.date, ": ", case)
print()
print("Month growth rate of confirmed cases")
country_growth_rate_month = growth_rate(month_statistics(non_null_values(select_country(countries, name_country))))
print(round(country_growth_rate_month, 3))

print()

# SECOND COUNTRY
name_country2 = input("Please enter with a country name to check its info: ")

# SELECT COUNTRY/ TOTAL CASES INFO
country_total_info2: List[Covid19Cases] = total_cases_info(select_country(countries, name_country2))
print('\n'.join(str(c) for c in country_total_info2))

print()

# NON NULL VALUES/ AVERAGE RATE
print("Average rate considering first Corona cases until last computed day")
country_average_non_null2: Tuple[float, float, float] = average_rate(non_null_values(select_country(countries,
                                                                                                   name_country2)))

print("Confirmed: ", round(country_average_non_null2[0], 3))
print("Deaths: ", round(country_average_non_null2[1], 3))
print("Recovered: ", round(country_average_non_null2[2], 3))

print()

# WEEK STATISTICS
print("Week Statistics")
country_week_statistics2 = week_statistics(non_null_values(select_country(countries, name_country2)))
for case in country_week_statistics2:
    print(case.date, ": ", case)
print()
print("Week growth rate of confirmed cases")
country_growth_rate_week2 = growth_rate(week_statistics(non_null_values(select_country(countries, name_country2))))
print(round(country_growth_rate_week2, 3))

print()
# MONTH STATISTICS
print("Month Statistics")
country_month_statistics2 = month_statistics(non_null_values(select_country(countries, name_country2)))
for case in country_month_statistics2:
    print(case.date, ": ", case)
print()
print("Month growth rate of confirmed cases")
country_growth_rate_month2 = growth_rate(month_statistics(non_null_values(select_country(countries, name_country2))))
print(round(country_growth_rate_month2, 3))

print()

# GROWTH SPREAD COMPARISON
print("Countries comparison growth spread rate")
country_growth_spread1 = growth_rate(non_null_values(select_country(countries, name_country)))
country_growth_spread2 = growth_rate(non_null_values(select_country(countries, name_country2)))
if country_growth_spread1 < country_growth_spread2:
    print(name_country, "has a better spread control than ", name_country2, ":", country_growth_spread1, "X",
          country_growth_spread2)

else:
    print(name_country2, "has a better spread control than ", name_country, ":", country_growth_spread2, "X",
          country_growth_spread1)

print()

# SELECTED RANGE
print("If you interested in comparing these two countries in a specific range, please follow the next instruction.")
first_date = input("Enter with first date. eg.:'2020-3-10': ")
second_date = input("Enter with second. eg.:'2020-4-5': ")

country_range = growth_rate(non_null_values(selected_range(select_country(countries, name_country),
                                                           first_date,
                                                           second_date)))
country_range2 = growth_rate(non_null_values(selected_range(select_country(countries, name_country2),
                                                           first_date,
                                                           second_date)))
print()
# COMPARISON RANGE GROWTH SPREAD
if country_range < country_range2:
    print("In this range selected", name_country, " has a better spread control than ", name_country2, ":",
          round(country_range, 3), "X", round(country_range2, 3))
else:
    print("In this range selected", name_country2, "has a better spread control than ", name_country, ":",
          round(country_range2, 3), "X", round(country_range,3))


