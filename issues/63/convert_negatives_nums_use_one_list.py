# delete.py

list_num = [45, 67, 2, -3, -555, 7, 0]

"""
## 	Использовать будем только один список!
## 	удалить все положительные числа
## 	ко всем отрицательным, оставляемым в списке,
## 	вычислим модуль числа (из отрицательного в положительное = преобразование)
"""

def transform_negative_and_group(list_num):
	"""
	# 	Для прохода по всему списка перебираем элементы по индексу,
	# 	начиная с нулевого индекса
	"""
	index = 0

	# Условием перебора будет выполняемый цикл
	# пока индекс меньше длины (элементов списка)
	while index < len(list_num):

		# Проверяем число из списка если оно положительное,
		# т.е. больше или равно нулю
		if list_num[index] >= 0:
			# Удаляем его из списка (по индексу)
			list_num.pop(index)
		else:
			# Иначе это число преобразуем в положительное
			# https://all-python.ru/osnovy/modul-chisla.html
			list_num[index] = abs(list_num[index])
			# Увеличиваем счётчик индексов списка
			index += 1
	# Функция возвращает список отобранных отрицательных чисел,
	# с последующим преобразованием в положительные
	return list_num

#  Печатаем преобразованный список, вызвав функцию с переданным в неё списком
print(transform_negative_and_group(list_num)) # -> [3, 555]
