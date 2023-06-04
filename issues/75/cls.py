# cls.py
# 2023-06-04 11:30

s = 'FFFooOxxXXXXX>>>>>>oosssssjustOOOODFSGFGDFGDFGDFdoitXCZREGAERGoooooox==XOOXxOOxoooxoXOXOxOoxOxFdsaDsDS'

def cls(s):
	c = 0
	ll = []
	for i in s:
		if s[c].islower():
			ll.append(i)
		c += 1

	# Преобразование из списка в строку
	print(''.join(ll))

cls(s)

#__END__

"""
Итоги
Преобразовать список в строку можно с помощью цикла, 
но для этого есть и более удобный инструмент — метод join().
"""
