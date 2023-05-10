# ex30.py

def is_leap_year(year):
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(is_leap_year(2018))  # False
print(is_leap_year(2017))  # False
print(is_leap_year(2016))  # True