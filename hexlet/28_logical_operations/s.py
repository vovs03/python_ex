# s.py

def has_upper_case(word):
	# if word := '':
	# 	False
	# res = not word.islower()
	# return res.isalpha()
	return word != word.lower()


print(has_upper_case('aSdf'))
print(has_upper_case('adfW'))
print(has_upper_case('ERWTRTWER'))

print('='* 25)
print("F -", has_upper_case(''))
print("F", has_upper_case('asadf'))