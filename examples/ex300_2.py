# ex300_2.py
def fizbuzz():
	fizz = []
	buzz = []

	for i in range(1,101):
		if i % 3 == 0:
			fizz.append(i)
		elif i % 5 == 0:
			buzz.append(i)

	# 1st thread
	print("Fizz (3):")
	print("{}\n".format(fizz))

	# 2nd thread
	print("Buzz (5):")
	print(buzz)

	#print("Ok!")

fizbuzz()