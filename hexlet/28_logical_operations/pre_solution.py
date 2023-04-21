# solution.py

# Реализуйте функцию has_upper_case(), 
# которая определяет, содержит ли строка заглавные буквы. 

# Функция должна вернуть булево значение:




def has_upper_case(word):
	if word == None:
		True
	#res == word
	return not word.islower()

print(has_upper_case(''))  # False
print(has_upper_case('python')) # False
print(has_upper_case('pyThon'))  # True

def has_res(word):
	# for ch in word:
	# 	if ch.isupper():
	# 		True

	# return word == ch.isupper()

	res = False
	char_list = list(word)
	i = 0
	print(char_list)

	cnt = 0
	for c in char_list:
		#print(char_list[cnt])
		if c == char_list[cnt].isupper():
			res = True
			#print(c)
			cnt += 1
			break

	#res = char_list[i].isupper()
	

	return res



	# for char_list[i] in char_list:
	# # 	#symbol = char_list[i].upper
	# 	if char_list[i].isupper:
	# 		break 


print("")
print(has_res('Asdf'))
print(has_res('asdfA'))

print(has_res(''))
print(has_res('aanldlskfnlskjfsdklfjalskdjfkdW'))
print(has_res('nkjldkjfnlsdkjfndkjfnaRlkmladfldms'))