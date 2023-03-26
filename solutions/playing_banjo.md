# Моё решение

> Очень усложнено(костыльно) конструкцией
> `./playingbanjo.py`

## Элегантные решение имхо

```python
import random as r

candidates = ["rolf", "martin", "Rikke", "Putin", "bravo"]
name = r.choice(candidates)

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return print( name + ' plays banjo')
    else:
        return print ( name + ' does not play banjo')

areYouPlayingBanjo(name)
```

```python
def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";
```

```python
def areYouPlayingBanjo(name):
    if name.startswith('R') or name.startswith('r'):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
```
