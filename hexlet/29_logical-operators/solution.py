# 29 solution.py
# https://ru.hexlet.io/courses/python-basics/lessons/logical-operators/exercise_unit

# Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным.

# Год будет високосным, если
# 1 - он делится без остатка на 400,
# 2 - или он одновременно делится без остатка на 4 и не делится на 100:


def is_leap_year(year):
	if year % 400 == 0:
		res = print(f"{year} - True")

	elif year % 4 == 0 and year % 100 != 0:
		res = print(f"{year} - True")
	else:
		#False
		res = print(f"{year} - False")
	return res

is_leap_year(2018) # False
is_leap_year(2017) # False
is_leap_year(2016) # True
is_leap_year(2000) # True