import random as r

candidates = ["rolf", "martin", "Rikke", "Putin", "bravo"]
name = r.choice(candidates)

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return print( name + ' plays banjo')
    else:
        return print ( name + ' does not play banjo')

areYouPlayingBanjo(name)