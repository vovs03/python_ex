# Напишите программу, которая берет исходное количество евро, 
# записанное в переменную euros_count, 
# 
# переводит евро в доллары и выводит на экран. 
# 
# Затем полученное значение переводит в рубли и выводит на новой строчке.



# Пример вывода для 100 евро:

# 125.0
# 7500.0
# Считаем, что:

# 1 евро = 1.25 долларов
# 1 доллар = 60 рублей


euros_count = 100
dollars_count = euros_count * 1.25
rubles_count = dollars_count * 60

print(dollars_count)
print(dollars_count * 60)
