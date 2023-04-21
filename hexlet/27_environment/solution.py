# 27 solution.py

"""
Напишите функцию get_age_difference(),
которая принимает два года рождения
и возвращает строку с разницей в возрасте в виде The age difference is 11.
"""

# Пример работы функции:

"""
actual = get_age_difference(2001, 2018)
print(actual)  # => The age difference is 17
"""

def get_age_difference(born, year):
	return f"The age difference is {abs(year - born)}"

print(get_age_difference(1977, 2023))
print(get_age_difference(2048, 2023))
