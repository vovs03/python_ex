import random as r

candidates = ["rolf", "martin", "Rikke", "Putin", "bravo"]

name = r.choice(candidates)
print(name[0])

def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == "R" or name[0] == "r":
      print(name + " plays banjo" )
    elif name[0] != "R" or name[0] != "r":
       print(name + " does not play banjo")



are_you_playing_banjo(name)