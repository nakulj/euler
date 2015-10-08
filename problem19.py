# returns the days of the firsts of each month, relative to the day of 1st Jan
def get_days_of_firsts(month_lengths):
	sum_ = 0
	out = []
	for month_length in month_lengths:
		out.append(sum_)
		sum_ += month_length % 7
	return out

def is_leap(year):
	if year % 4 != 0:
		return False
	if year % 100 == 0 and year % 400 != 0:
		return False
	return True

DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_PER_MONTH_L = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

DAYS_OF_FIRSTS = get_days_of_firsts(DAYS_PER_MONTH)
DAYS_OF_FIRSTS_L = get_days_of_firsts(DAYS_PER_MONTH_L)

def count_sundays_on_firsts(year, first_day_of_year):
	leap = is_leap(year)
	days_of_firsts = DAYS_OF_FIRSTS_L if leap else DAYS_OF_FIRSTS
	days_of_firsts = [(first_day_of_year + day) % 7 for day in days_of_firsts]
	return sum(1 for day in days_of_firsts if day == 6)

def get_first_day_of_next_year(year, first_day_of_year):
	num_days = 366 if is_leap(year) else 365
	return (first_day_of_year + num_days) % 7

FIRST_DAY_OF_1900 = 0

first_day_of_year = get_first_day_of_next_year(1900, FIRST_DAY_OF_1900)
sundays_on_firsts = 0
for year in range(1901, 2001):
	sundays_on_firsts += count_sundays_on_firsts(year, first_day_of_year)
	first_day_of_year = get_first_day_of_next_year(year, first_day_of_year)


print sundays_on_firsts
