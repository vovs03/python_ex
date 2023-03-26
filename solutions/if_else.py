from random import randint as r

x = r(41,44)
# print(x)

def choose(x):
    if x==42:
      # блок выполнится, если x==42 истинно
      print("real truth")
    elif x>0:
      # иначе блок, если лог. выражение x > 0 истинно
      print("be positive", x)

choose(x)