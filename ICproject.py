import random

#-----------------------------------------------------------------------------------------------
#VARIABLES AND LISTS - This part stores the die and all the characters available in the game.

d20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d8=[1,2,3,4,5,6,7,8]
d4=[1,2,3,4]

allies=["Warrior","Priest","Rogue"]
fainted=[]
wave1=["Orc Warrior A","Orc Warrior B", "Orc Archer"]

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
rogue=[27,10,1,4,4]


#ENEMY STATS - The stats of every enemy encounterable.

orcw1=[15,0,2,2,2] #HP, MP, AP, WP, INIT
orcw2=orcw1
orca=[5,0,2,3,4]

#-----------------------------------------------------------------------------------------------
#BATTLE VALUES - These values determine the flow of the battles, such as turn order and stuff

def init(x):        #INITIATION - Calls a fighter's init value.
    return int(x[4])

def turnOrder(x):             #TURN ORDER - Defines who goes first each turn during battle.
    return rolld20(1) + init(x) 
#-----------------------------------------------------------------------------------------------
#BATTLE PHASES - Functions for the battle phases

def initphase(allies,wave):

    global order
    order=[]
    order.clear()

    for i in allies:
        if i == allies[0]:
            x=warrior
            global warriorInit
            warriorInit=turnOrder(x)
            print(str(i)+" rolled "+str(warriorInit))

        elif i == allies[2]:                                 #THESE ARE PLACEHOLDERS!!!!!!!!!!!!!
            x=rogue
            global rogueInit
            rogueInit=turnOrder(x)                          #We'll replace the allies and the enemies strings with the actual battle waves once they're added
            print(str(i)+" rolled "+str(rogueInit))

        elif i == allies[1]:
            x=priest
            global priestInit
            priestInit=turnOrder(x)
            print(str(i)+" rolled "+str(priestInit))


    for i in wave:
        if i == wave[0]:
            x=orcw1
            global orcwarrior1Init
            orcwarrior1Init=turnOrder(x)
            print(str(i)+" rolled "+str(orcwarrior1Init))

        if i == wave[1]:
            x=orcw2
            global orcwarrior2Init
            orcwarrior2Init=turnOrder(x)
            print(str(i)+" rolled "+str(orcwarrior2Init))

        elif i == wave[2]:
            x=orca
            global orcarcherInit
            orcarcherInit=turnOrder(x)
            print(str(i)+" rolled "+str(orcarcherInit))
    
    order.append(warriorInit)
    order.append(priestInit)
    order.append(rogueInit)

    order.append(orcwarrior1Init)
    order.append(orcwarrior2Init)     #Adds all init values to the order list
    order.append(orcarcherInit)

    order.sort()            #Sorts the list from smallest to biggest valuess




initphase(allies,wave1)
print(str(order))

#-----------------------------------------------------------------------------------------------
#GAME LOOP - Keeps the game going

game=True
defeat=False #Variables to check the game state
victory=False

while game:

    if defeat:
        game=False
        print("You have no more allies than can fight.")
        print("You lost the battle!")
        break
    
    elif victory:
        game=False
        print("All enemies have been defeated.")
        print("You won the battle!")
        break

    else:
        #initphase(party,wave1)



        if not defeat:                            #DEFEAT CHECK - If the "allies" list is empty, it will not reset the defeat variable, and the game ends.
            defeat=True
            for i in allies:
                defeat=False
                print("There's still allies.")
        
        if not victory:                           #VICTORY CHECK - If the "wave1" list is empty, it will not reset the victory variable, and the game ends.
            victory=True
            for i in wave1:
                victory=False
                print("There's still enemies.")   #Defeat checks before victory, so you can't win with an empty party.



