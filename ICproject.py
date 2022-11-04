import random

def init(x):
    return x[4]

d20= random.sample([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],1)

party=["Warrior","Priest","Rogue"]
fainted=[]
enemies=["Orc Warrior","Your mother"]

warrior=[32,5,2,5,2] #hp, mp, ap, wp, init
priest=[20,25,0,2,6]
rogue=[27,10,1,4,3]

orcw=[15,0,2,2,2]
yomama=[25,0,4,7,1]

turnOrder= d20+ int(init(warrior))


print(str(turnOrder))