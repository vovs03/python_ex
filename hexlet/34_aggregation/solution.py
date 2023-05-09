#!/usr/bin/env python3
# solution.py

# Реализуйте функцию join_numbers_from_range(), 
# которая объединяет все числа из диапазона в строку 
# и возвращает получившуюся строку:

# join_numbers_from_range(1, 1)  # 1
# join_numbers_from_range(2, 3)  # 23
# join_numbers_from_range(5, 10)  # 5678910

def join_numbers_from_range(num1, num2):

	i = num1
	res = ''
	while i <= num2:
		res = res + str(i)
		i += 1
	return res



print(join_numbers_from_range(1, 1))
print(join_numbers_from_range(2, 3))
print(join_numbers_from_range(5, 10))