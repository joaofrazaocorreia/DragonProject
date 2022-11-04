import random

#-----------------------------------------------------------------------------------------------
#VARIABLES AND LISTS - This part stores the die and all the characters available in the game.

d20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d8=[1,2,3,4,5,6,7,8]
d4=[1,2,3,4]

party=["Warrior","Priest","Rogue"]
fainted=[]
enemies=["Orc Warrior","Your mother"]

#-----------------------------------------------------------------------------------------------
#DICE ROLLS - Commands for rolling die.


def rolld20(x):
    templist=(random.sample(d20,x))
    return templist[0]
    
    
def rolld8(x):
    templist=(random.sample(d8,x))
    return templist[0]

def rolld4(x):
    templist=(random.sample(d4,x))
    return templist[0]

#-----------------------------------------------------------------------------------------------
#ALLY STATS - The stats of every available party member.

warrior=[32,5,2,5,2] #HP, MP, AP, WP, INIT
priest=[20,25,0,2,6]
rogue=[27,10,1,4,3]


#ENEMY STATS - The stats of every enemy encounterable.

orcw=[15,0,2,2,2] #HP, MP, AP, WP, INIT
yomama=[25,0,4,7,1]

#-----------------------------------------------------------------------------------------------
#BATTLE VALUES - These values determine the flow of the battles, such as turn order and stuff!

def init(x):     #INITIATION - Calls a fighter's init value.
    return int(x[4])

turnOrder= rolld20(1) + init(warrior) #TURN ORDER - Defines who goes first each turn during battle.

print(str(turnOrder))