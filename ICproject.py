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

warrior=[32,5, 2,5,2] #HP, MP, AP, WP, INIT    ID=1
priest= [20,25,0,2,6]                         #ID=2
rogue = [27,10,1,4,4]                          #ID=3


#ENEMY STATS - The stats of every enemy encounterable.

orcw1=[15,0,2,2,2] #HP, MP, AP, WP, INIT      ID=4
orcw2=orcw1                                  #ID=5
orca=[5,0,1,4,4]                             #ID=6

#-----------------------------------------------------------------------------------------------
#BATTLE VALUES - These values determine the flow of the battles, such as turn order and stuff

def init(x):        #INITIATION - Calls a fighter's init value.
    return int(x[4])

def turnOrder(x):             #TURN ORDER - Defines who goes first each turn during battle.
    return rolld20(1) + init(x)

def chooseEnemy():
        global target
        print("")
        print("Target an enemy!")
        print(str(wave1))
        target=input()
        target=target.lower()

def calculateDamage(WP,AP):
    damage= WP-AP
    if damage<0:
        damage=0
    return damage

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
            global orcwarriorAInit
            orcwarriorAInit=turnOrder(x)
            print(str(i)+" rolled "+str(orcwarriorAInit))
            
        if i == wave[1]:
            x=orcw2
            global orcwarriorBInit
            orcwarriorBInit=turnOrder(x)
            print(str(i)+" rolled "+str(orcwarriorBInit)) 

        elif i == wave[2]:
            x=orca
            global orcarcherInit
            orcarcherInit=turnOrder(x)
            print(str(i)+" rolled "+str(orcarcherInit))
            
    

    order.append(warriorInit)

    while orcwarriorAInit in order:
        orcwarriorAInit+=0.1
    order.append(orcwarriorAInit)

    while orcwarriorBInit in order:
        orcwarriorBInit+=0.1
    order.append(orcwarriorBInit)     #Adds all init values to the order list, adds 0.1 if the value already exists

    while orcarcherInit in order:
        orcarcherInit+=0.1
    order.append(orcarcherInit)

    while rogueInit in order:        #IMPORTANT NOTE - DON'T CHANGE THE FREAKING ORDER!!!! THEY'RE BASED ON INIT VALUES
        rogueInit+=0.1
    order.append(rogueInit)

    while priestInit in order:
        priestInit+=0.1
    order.append(priestInit)

    order.sort()            #Sorts the list from smallest to biggest values
    print(str(order))

def attackphase(characterID):
    print("")
    print("What will you do?")
    print("ATTACK / MAGIC")
    command=input()
    command=command.lower()

    if characterID==1:
        WP=warrior[3]
    elif characterID==2:
        WP=priest[3]
    elif characterID==3:
        WP=rogue[3]


    if command=="attack":

        attack=True
        while attack:

            chooseEnemy()

            if target=="orc warrior a":
                AP=orcw1[2]
                dmg=calculateDamage(WP,AP)
                orcw1[0]-=dmg
                print("Orc Warrior A took "+str(dmg)+" damage!")
                if orcw1[0]<=0:
                    wave1.remove("Orc Warrior A")
                    fainted.append("Orc Warrior A")
                    print("Orc Warrior A fainted!")
                attack=False

            elif target=="orc warrior b":
                AP=orcw2[2]
                dmg=calculateDamage(WP,AP)
                orcw2[0]-=dmg
                print("Orc Warrior B took "+str(dmg)+" damage!")
                if orcw2[0]<=0:
                    wave1.remove("Orc Warrior B")
                    fainted.append("Orc Warrior B")
                    print("Orc Warrior B fainted!")
                attack=False

            elif target=="orc archer":
                AP=orca[2]
                dmg=calculateDamage(WP,AP)
                orca[0]-=dmg
                print("Orc Archer took "+str(dmg)+" damage!")
                if orca[0]<=0:
                    wave1.remove("Orc Archer")
                    fainted.append("Orc Archer")
                    print("Orc Archer fainted!")
                attack=False

            else:
                print("That's not an enemy.")
        
        

    
  

#-----------------------------------------------------------------------------------------------
#GAME LOOP - Keeps the game going

game=True
defeat=False 
victory=False   #Variables to check the game state

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
        print("")
        print("Turn Start!")
        print("")

        initphase(allies,wave1)

        while len(order)>0:
            if warriorInit==order[-1]:
                print("It's Warrior's turn.")
                order.remove(order[-1])
                attackphase(1)
        
            elif priestInit==order[-1]:
                print("It's Priest's turn.")
                order.remove(order[-1])
                attackphase(2)
        
            elif rogueInit==order[-1]:
                print("It's Rogue's turn.")
                order.remove(order[-1])
                attackphase(3)

            elif orcwarriorAInit==order[-1]:
                print("It's Orc Warrior A's turn.")
                order.remove(order[-1])
                
            
            elif orcwarriorBInit==order[-1]:
                print("It's Orc Warrior B's turn.")
                order.remove(order[-1])

            elif orcarcherInit==order[-1]:
                print("It's Orc Archer's turn.")
                order.remove(order[-1])

        if len(allies)==0:                            #DEFEAT CHECK - If the "allies" list is empty, it will not reset the defeat variable, and the game ends.
            defeat=True
 
        if len(wave1)==0:                           #VICTORY CHECK - If the "wave1" list is empty, it will not reset the victory variable, and the game ends.
            victory=True                            #Defeat checks before victory, so you can't win with an empty party.


    print(str(orca))
    game=False #for testing purposes, remove later

                                                     



