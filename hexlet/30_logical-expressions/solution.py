# 30 solution.py

# Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается строка yes, иначе no.

# string_or_not('Hexlet') # yes
# string_or_not(10)       # no
# string_or_not('')       # yes
# string_or_not(False)    # no
# Подсказки
# Проверить, что значение является строкой, можно с помощью функции isinstance():

def string_or_not(val):
	if isinstance(val, str):
		print("yes")
	elif not isinstance(val, str):
		print("no")

	return val


string_or_not("Hex")
string_or_not("")
string_or_not(12)
string_or_not(True)

