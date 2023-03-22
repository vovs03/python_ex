import random as r

vars = ("Да", "Нет")

def get_random_vars(vars):
	# генератор 0,1 g <- generator
	g = r.randint(0,1)
	print(vars[g])
	
get_random_vars(vars)
