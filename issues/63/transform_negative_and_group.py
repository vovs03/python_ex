# transform_negative_and_group.py

# https://github.com/Sergei089/python_ex/issues/63

# Написать функцию transform_negative_and_group(list_num), 
#берущую список чисел и (фильтрующую) возвращающую только отрицательные значения, 
# преобразуя их в положительные.

# Пример:

# transform_negative_and_group([20,25, -10, -18])
# # -> [10, 18]

def transform_negative_and_group(list_num):
	# tl, (transformed_list)
	tl =[]
	for i in list_num:
		if i < 0:
			tl.append(abs(i))
	return tl

print(transform_negative_and_group([20,25, -10, -18]))

list_num = [34,0,-200,-100,-5555, 3456,-10000]
print(transform_negative_and_group(list_num))
