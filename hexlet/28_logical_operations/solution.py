# solution.py

def has_upper_case(word):
	return any(s.isupper() for s in word)

# Like tests
print( has_upper_case("Hexlet"))
print( has_upper_case("TIME"))
print( has_upper_case("city of New York"))
print( not has_upper_case(""))
print( has_upper_case(""))
print( not has_upper_case("python"))