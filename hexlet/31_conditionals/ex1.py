# ex1.py

def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    return 'question' if last_char == '?' else 'normal'

print(get_type_of_sentence("Aloha."))
print(get_type_of_sentence("Wich month is now?"))
