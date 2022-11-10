import random

#-----------------------------------------------------------------------------------------------
#VARIABLES AND LISTS - This part stores the die and all the characters available in the game.

d20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d8=[1,2,3,4,5,6,7,8]
d6=[1,2,3,4,5,6]
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

def rolld6(x):
    templist=(random.sample(d6,x))
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
orcw2=[15,0,2,2,2]                           #ID=5
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

def chooseAlly():
    global target
    print("")
    print("Target an ally!")
    print(str(allies))
    target=input()
    target=target.lower()

def chooseSpell(charID):
    global spell
    print("")
    print("Choose a spell.")
    if charID == 1:
        print("RUSHDOWN")
    elif charID == 2:
        print("MEND / EXORCISM")
    elif charID == 3:
        print("SHARPEN")

    spell=input()
    spell=spell.lower()


def calculateDamage(WP,AP):
    damage= WP-AP
    if damage<0:
        damage=0
    return damage

def calculateValues(spell, WP):
    if spell=="rushdown":
        spellEffectValue= -1 * (WP+rolld4(1))
    elif spell=="mend":
        spellEffectValue= WP + rolld6(1)
    elif spell=="exorcism":
        spellEffectValue= -2 * rolld4(1)
    return spellEffectValue


#-----------------------------------------------------------------------------------------------
#BATTLE PHASES - Functions for the battle phases

def initphase(allies,wave):

    global order                                #Command for the init phase
    order=[]
    order.clear()

    if "Warrior" in allies:
        x=warrior
        global warriorInit
        warriorInit=turnOrder(x)
        print("Warrior rolled "+str(warriorInit))

    if "Rogue" in allies:                                 
        x=rogue
        global rogueInit
        rogueInit=turnOrder(x)                          
        print("Rogue rolled "+str(rogueInit))

    if "Priest" in allies:
        x=priest
        global priestInit
        priestInit=turnOrder(x)
        print("Priest rolled "+str(priestInit))


    if "Orc Warrior A" in wave:
        x=orcw1
        global orcwarriorAInit
        orcwarriorAInit=turnOrder(x)
        print("Orc Warrior A rolled "+str(orcwarriorAInit))
            
    if "Orc Warrior B" in wave:
        x=orcw2
        global orcwarriorBInit
        orcwarriorBInit=turnOrder(x)
        print("Orc Warrior B rolled "+str(orcwarriorBInit)) 

    if "Orc Archer" in wave:
        x=orca
        global orcarcherInit
        orcarcherInit=turnOrder(x)
        print("Orc Archer rolled "+str(orcarcherInit))
            
    

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

    while rogueInit in order:        #IMPORTANT NOTE - DON'T CHANGE THIS ORDER!!!! THEY'RE BASED ON INIT VALUES, FROM HIGHEST TO LOWEST
        rogueInit+=0.1
    order.append(rogueInit)

    while priestInit in order:
        priestInit+=0.1
    order.append(priestInit)

    order.sort()            #Sorts the list from smallest to biggest values
    print(str(order))

def attackphase(characterID):        #Command for the attack phase

    if characterID==1:
        WP=warrior[3]
    elif characterID==2:               #Assigns WP according to the ID given
        WP=priest[3]
    elif characterID==3:
        WP=rogue[3]

    print("")
    print("What will you do?")
    print("ATTACK / MAGIC")
    command=input()
    command=command.lower()
    print("")


    turn=True

    if command=="attack":

        while turn:

            chooseEnemy()                      #player inputs an enemy and their stats will be used for combat
            print("")

            if target=="orc warrior a" and "Orc Warrior A" not in fainted:
                AP=orcw1[2]
                dmg=calculateDamage(WP,AP)
                orcw1[0]-=dmg
                print("Orc Warrior A took "+str(dmg)+" damage!")
                print("")
                if orcw1[0]<=0:
                    wave1.remove("Orc Warrior A")
                    fainted.append("Orc Warrior A")
                    print("Orc Warrior A fainted!")
                    print("")
                turn=False

            elif target=="orc warrior b" and "Orc Warrior B" not in fainted:
                AP=orcw2[2]
                dmg=calculateDamage(WP,AP)
                orcw2[0]-=dmg
                print("Orc Warrior B took "+str(dmg)+" damage!")
                print("")
                if orcw2[0]<=0:
                    wave1.remove("Orc Warrior B")
                    fainted.append("Orc Warrior B")
                    print("Orc Warrior B fainted!")
                    print("")
                turn=False

            elif target=="orc archer" and "Orc Archer" not in fainted:
                AP=orca[2]
                dmg=calculateDamage(WP,AP)
                orca[0]-=dmg
                print("Orc Archer took "+str(dmg)+" damage!")
                print("")
                if orca[0]<=0:
                    wave1.remove("Orc Archer")
                    fainted.append("Orc Archer")
                    print("Orc Archer fainted!")
                    print("")
                turn=False

            else:
                print("That's not an enemy.")           #doesn't turn "attack" into false so it loops back.            
                print("")
    
    elif command=="magic":
        
        while turn:
            chooseSpell(characterID)
            if spell == "rushdown" and characterID==1:
                effectValue=calculateValues("rushdown",warrior[3])

            if spell == "mend" and characterID==2:
                effectValue=calculateValues("mend",priest[3])


        
        

    
  

#-----------------------------------------------------------------------------------------------
#GAME LOOP - Keeps the game going

game=True
defeat=False 
victory=False   #Variables to check the game state

while game:
    print("")
    print("Turn Start!")
    print("")

    initphase(allies,wave1)

    while len(allies)>0:
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

    if len(allies)==0:                            #DEFEAT CHECK - If the "allies" list is empty, the game ends.
        game=False
        print("You have no more allies than can fight.")
        print("You lost the battle!")
        break
 
    if len(wave1)==0:                              #VICTORY CHECK - If the "wave1" list is empty, the game ends.
        game=False
        print("All enemies have been defeated.")
        print("You won the battle!")
        break                           #Defeat checks before victory, so you can't win with an empty party.
