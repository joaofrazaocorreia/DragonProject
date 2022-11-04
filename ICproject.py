import random

d20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d8=[1,2,3,4,5,6,7,8]
d4=[1,2,3,4]

party=["Warrior","Priest","Rogue"]
fainted=[]
enemies=["Orc Warrior","Your mother"]

def init(x):
    return x[4]

dice_1d20= random.sample(d20,1)

#ALLY STATS
warrior=[32,5,2,5,2] #HP, MP, AP, WP, INIT
priest=[20,25,0,2,6]
rogue=[27,10,1,4,3]

#ENEMY STATS
orcw=[15,0,2,2,2] #HP, MP, AP, WP, INIT
yomama=[25,0,4,7,1]

turnOrder= dice_1d20[0]+ int(init(warrior))

print(str(turnOrder))