import random

#-----------------------------------------------------------------------------------------------
#VARIABLES AND LISTS - This part stores the die and all the characters available in the game.

d20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  #20 sided dice
d8=[1,2,3,4,5,6,7,8]  #8 sided dice
d6=[1,2,3,4,5,6]  #6 sided dice
d4=[1,2,3,4]  #4 sided dice

allies=["Warrior","Priest","Rogue"]  #ALLIES - Allies in the party (More can be added later)

fainted=[]  #FAINTED - group for storing and registering characters who have been killed.

wave1=["Orc Warrior A","Orc Warrior B", "Orc Archer"]  #WAVE1 - Enemies in the first wave of monsters (More can be added later)

#-----------------------------------------------------------------------------------------------
#DICE ROLLS - Commands for rolling die.

def rolld20():
    templist=(random.sample(d20,1))      #Rolls a d20 dice.
    return templist[0]
    
def rolld8():
    templist=(random.sample(d8,1))       #Rolls a d8 dice.
    return templist[0]

def rolld6():
    templist=(random.sample(d6,1))       #Rolls a d6 dice.
    return templist[0]

def rolld4():
    templist=(random.sample(d4,1))       #Rolls a d4 dice.
    return templist[0]

#-----------------------------------------------------------------------------------------------
#ALLY STATS - The stats of every available party member.

warrior=[32,5, 2,5,2] #HP, MP, AP, WP, INIT     ID=1
priest= [20,25,0,2,6]                         # ID=2
rogue = [27,10,1,4,4]                         # ID=3


#-----------------------------------------------------------------------------------------------
#ENEMY STATS - The stats of every enemy encounterable.

orcw1=[15,0,2,2,2] #HP, MP, AP, WP, INIT      ID=4
orcw2=[15,0,2,2,2]                          # ID=5
orca =[5, 0,1,4,4]                          # ID=6


#-----------------------------------------------------------------------------------------------
#BATTLE VALUES - These values determine the flow of the battles, such as turn order and stuff

def init(x):   #INIT - Calls a fighter's initiation value.
    return int(x[4])

def turnOrder(x):   #TURN ORDER - Defines who goes first each turn during battle. Used to calculate Init rolls.
    return rolld20() + init(x)

def chooseEnemy():  #CHOOSE ENEMY - Allows the player to choose an enemy target. Changes the "target" variable to an enemy of choice.
    global target
    print("")
    print("Target an enemy!")
    print(str(wave1))
    target=input()
    target=target.lower()

def chooseAlly():  #CHOOSE ALLY - Allows the player to choose an allied target. Changes the "target" variable to an ally of choice.
    global target
    print("")
    print("Target an ally!")
    print(str(allies))
    target=input()
    target=target.lower()

def chooseSpell(charID):  #CHOOSE SPELL - Allows the player to choose a spell. Displays different options depending on the character ID given.
    global spell
    print("Choose a spell.")

    if charID == 1:
        print("RUSHDOWN")

    elif charID == 2:
        print("MEND / EXORCISM")

    elif charID == 3:
        print("SHARPEN")

    spell=input()
    spell=spell.lower()


def calculateDamage(WP,AP):  #CALCULATE DAMAGE - Subtracts the given AP from the given WP. If the result is negative, it will return 0 instead.
    damage= WP-AP
    if damage<0:             #(Used for ATTACK combat.)
        damage=0
    return damage

def calculateValues(spell, WP):  #CALCULATE VALUES - Depending on the spell given (and on the given WP), calculates the spell's damage / healing.
    if spell=="rushdown":
        spellEffectValue= -1 * (WP+rolld4()) #(Used for MAGIC combat.)

    elif spell=="mend":
        spellEffectValue= WP + rolld6()  #Positive values heal, Negative values deal damage (damage calculation uses a sum).

    elif spell=="exorcism":
        spellEffectValue= -2 * rolld4()

    return spellEffectValue


#-----------------------------------------------------------------------------------------------
#INITIATION PHASE - Command for the init phase

def initphase(allies,wave):

    global order
    order=[]
    order.clear()  #Preemptively clears the list before rerolling, just in case of an error.

    if "Warrior" not in fainted:  #Warrior rolls for init if he's alive.
        x=warrior
        global warriorInit
        warriorInit=turnOrder(x)
        print("Warrior rolled "+str(warriorInit))

    if "Rogue" not in fainted:  #Rogue rolls for init if he's alive.                     
        x=rogue
        global rogueInit
        rogueInit=turnOrder(x)                          
        print("Rogue rolled "+str(rogueInit))

    if "Priest" not in fainted:  #Priest rolls for init if he's alive.
        x=priest
        global priestInit
        priestInit=turnOrder(x)
        print("Priest rolled "+str(priestInit))


    if "Orc Warrior A" not in fainted:  #Orc Warrior A rolls for init if he's alive.
        x=orcw1
        global orcwarriorAInit
        orcwarriorAInit=turnOrder(x)
        print("Orc Warrior A rolled "+str(orcwarriorAInit))
            
    if "Orc Warrior B" not in fainted:  #Orc Warrior B rolls for init if he's alive.
        x=orcw2
        global orcwarriorBInit
        orcwarriorBInit=turnOrder(x)
        print("Orc Warrior B rolled "+str(orcwarriorBInit)) 

    if "Orc Archer" not in fainted:  #Orc Archer rolls for init if he's alive.
        x=orca
        global orcarcherInit
        orcarcherInit=turnOrder(x)
        print("Orc Archer rolled "+str(orcarcherInit))
            
    

    if "Warrior" not in fainted:
        order.append(warriorInit)

    while orcwarriorAInit in order:
        orcwarriorAInit+=0.1
    if "Orc Warrior A" not in fainted:
        order.append(orcwarriorAInit)

    while orcwarriorBInit in order:
        orcwarriorBInit+=0.1
    if "Orc Warrior B" not in fainted:
        order.append(orcwarriorBInit)  #Adds all alive characters' init values to the "order" list, and adds 0.1 if the value already exists.

    while orcarcherInit in order:      #The fighters at the top have less priority than the fighters below them (i.e. Orc Archer has less priority than Rogue)
        orcarcherInit+=0.1
    if "Orc Archer" not in fainted: 
        order.append(orcarcherInit)

    while rogueInit in order:          #IMPORTANT NOTE - DON'T CHANGE THIS ORDER!!!! THEY'RE BASED ON INIT VALUES, FROM LOWEST TO HIGHEST
        rogueInit+=0.1
    if "Rogue" not in fainted:
        order.append(rogueInit)

    while priestInit in order:
        priestInit+=0.1
    if "Priest" not in fainted:
        order.append(priestInit)

    order.sort()  #Sorts the list from smallest to biggest values
    print(str(order))
    print("")


#-----------------------------------------------------------------------------------------------
#ATTACK PHASE - Command for the attack phase

def attackphase(characterID):

    if characterID==1:
        WP=warrior[3]
        MP=warrior[1]

    elif characterID==2:  #Assigns WP and MP values according to the ally character ID given.
        WP=priest[3]
        MP=priest[1]

    elif characterID==3:
        WP=rogue[3]
        MP=rogue[1]

    print("")
    print("What will you do?")
    print("ATTACK / MAGIC")   #Prompts the player's choice for a battle command.
    command=input()
    command=command.lower()
    print("")

    turn=True  #Variable for looping until the turn successfully ends.

#-----------------------------------------------------------------------------------------------
    if command=="attack":  #loop for the ATTACK command.

        while turn:

            chooseEnemy()  #The player chooses an enemy and their stats will be used for melee combat.
            print("")

            if target=="orc warrior a" and "Orc Warrior A" not in fainted:  #Can only target orc warrior A if he's alive
                AP=orcw1[2]
                dmg=calculateDamage(WP,AP)
                orcw1[0]-=dmg              #Calculates and subtracts damage from the target's hp.
                print("Orc Warrior A took "+str(dmg)+" damage!")
                print("")
                if orcw1[0]<=0:
                    wave1.remove("Orc Warrior A")   #Faints if health drops below 0
                    fainted.append("Orc Warrior A")
                    print("Orc Warrior A fainted!")
                    print("")
                turn=False

            elif target=="orc warrior b" and "Orc Warrior B" not in fainted:  #Can only target orc warrior B if he's alive
                AP=orcw2[2]
                dmg=calculateDamage(WP,AP)
                orcw2[0]-=dmg              #Calculates and subtracts damage from the target's hp.
                print("Orc Warrior B took "+str(dmg)+" damage!")
                print("")
                if orcw2[0]<=0:
                    wave1.remove("Orc Warrior B")   #Faints if health drops below 0
                    fainted.append("Orc Warrior B")
                    print("Orc Warrior B fainted!")
                    print("")
                turn=False

            elif target=="orc archer" and "Orc Archer" not in fainted:  #Can only target orc archer if he's alive
                AP=orca[2]
                dmg=calculateDamage(WP,AP)
                orca[0]-=dmg              #Calculates and subtracts damage from the target's hp.
                print("Orc Archer took "+str(dmg)+" damage!")
                print("")
                if orca[0]<=0:
                    wave1.remove("Orc Archer")   #Faints if health drops below 0
                    fainted.append("Orc Archer")
                    print("Orc Archer fainted!")
                    print("")
                turn=False

            else:
                print("That's not an enemy.") #Causes error if the target input is unknown, and loops back to the prompt.            
                print("")


#-----------------------------------------------------------------------------------------------
    elif command=="magic": #loop for the MAGIC command.
        
        while turn:
            chooseSpell(characterID)
            print("")
            if spell == "rushdown" and characterID==1:   #--RUSHDOWN-- spell
                spellcost=5

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    warrior[1]-=spellcost  #Removes the mana cost

                    effectValue=calculateValues("rushdown",WP)
                    chooseEnemy()
                    print("")
                    if target=="orc warrior a" and "Orc Warrior A" not in fainted:

                        orcw1[0]+=effectValue  #Adds the spell's value to the target's HP. Negative values deal damage, Positive values heal.
                        print("Orc Warrior A took "+str(-effectValue)+" damage!")
                        print("")
                        if orcw1[0]<=0:
                            wave1.remove("Orc Warrior A")   #Faints if health drops below 0
                            fainted.append("Orc Warrior A")
                            print("Orc Warrior A fainted!")
                            print("")
                        turn=False

                    elif target=="orc warrior b" and "Orc Warrior B" not in fainted:

                        orcw2[0]+=effectValue  #Adds the spell's value to the target's HP. Negative values deal damage, Positive values heal.

                        print("Orc Warrior B took "+str(-effectValue)+" damage!")
                        print("")
                        if orcw2[0]<=0:
                            wave1.remove("Orc Warrior B")   #Faints if health drops below 0
                            fainted.append("Orc Warrior B")
                            print("Orc Warrior B fainted!")
                            print("")
                        turn=False

                    elif target=="orc archer" and "Orc Archer" not in fainted:

                        orca[0]+=effectValue  #Adds the spell's value to the target's HP. Negative values deal damage, Positive values heal.

                        print("Orc Archer took "+str(-effectValue)+" damage!")
                        print("")
                        if orca[0]<=0:
                            wave1.remove("Orc Archer")   #Faints if health drops below 0
                            fainted.append("Orc Archer")
                            print("Orc Archer fainted!")
                            print("")
                        turn=False

            elif spell == "rushdown":   #Causes error if not used by Warrior.
                print("This character can't use this spell!")


            elif spell == "mend" and characterID==2:   #--MEND-- spell
                spellcost=3

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    priest[1]-=spellcost  #Removes the mana cost
                    
                    effectValue=calculateValues("mend",WP)
                    chooseAlly()
                    print("")

            elif spell == "mend":   #Causes error if not used by Priest.
                print("This character can't use this spell!")


            elif spell == "exorcism" and characterID==2:  #--EXORCISM-- spell
                spellcost=5

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    priest[1]-=spellcost  #Removes the mana cost

                    effectValue=calculateValues("exorcism",WP)
                    chooseEnemy()
                    print("")
                    if target=="orc warrior a" and "Orc Warrior A" not in fainted:

                        orcw1[0]+=effectValue  #Adds the spell's value to the target's HP. Negative values deal damage, Positive values heal.
                        print("Orc Warrior A took "+str(-effectValue)+" damage!")
                        print("")
                        if orcw1[0]<=0:
                            wave1.remove("Orc Warrior A")   #Faints if health drops below 0
                            fainted.append("Orc Warrior A")
                            print("Orc Warrior A fainted!")
                            print("")
                        turn=False

                    elif target=="orc warrior b" and "Orc Warrior B" not in fainted:

                        orcw2[0]+=effectValue  #Adds the spell's value to the target's HP. Negative values deal damage, Positive values heal.

                        print("Orc Warrior B took "+str(-effectValue)+" damage!")
                        print("")
                        if orcw2[0]<=0:
                            wave1.remove("Orc Warrior B")   #Faints if health drops below 0
                            fainted.append("Orc Warrior B")
                            print("Orc Warrior B fainted!")
                            print("")
                        turn=False

                    elif target=="orc archer" and "Orc Archer" not in fainted:

                        orca[0]+=effectValue  #Adds the spell's value to the target's HP. Negative values deal damage, Positive values heal.

                        print("Orc Archer took "+str(-effectValue)+" damage!")
                        print("")
                        if orca[0]<=0:
                            wave1.remove("Orc Archer")   #Faints if health drops below 0
                            fainted.append("Orc Archer")
                            print("Orc Archer fainted!")
                            print("")
                        turn=False

            elif spell == "exorcism":   #Causes error if not used by Priest.
                print("This character can't use this spell!")


            elif spell == "sharpen" and characterID==3:  #--SHARPEN-- spell
                spellcost=10

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    rogue[1]-=spellcost #Removes the mana cost.

                    rogue[3]+=2
                    WP+=2   #Gives Rogue +2 WP for the rest of the battle.

                    print("Rogue sharpens his weapon. +2 Weapon Power")
                    print("")
                    turn=False

            elif spell == "sharpen":   #Causes error if not used by Rogue.
                print("This character can't use this spell!")

            else:
                print("That's not a known spell.")   #Causes error if the spell input is unknown, and loops back to the prompt.
    
    else:
        print("Unknown Command.")  #Causes error if the battle command is unknown, and lopps back to the prompt.
        attackphase(characterID)


        
        

    
  

#-----------------------------------------------------------------------------------------------
#GAME LOOP - Keeps the game going until a win/lose condition is met.

game=True

while game:
    print("")
    print("Turn Start!")
    print("")

    initphase(allies,wave1)

    while len(order)>0:  #Loops until all characters have ended their attack phase.

        if warriorInit==order[-1]:  #Starts the Warrior's turn if he's alive.
            if "Warrior" not in fainted:
                print("It's Warrior's turn.")
                attackphase(1)
            order.remove(order[-1])

        
        elif priestInit==order[-1]:  #Starts the Priests's turn if he's alive.
            if "Priest" not in fainted:
                print("It's Priest's turn.")
                attackphase(2)
            order.remove(order[-1])
                
        
        elif rogueInit==order[-1]:  #Starts the Rogue's turn if he's alive.
            if "Rogue" not in fainted:
                print("It's Rogue's turn.")
                attackphase(3)
            order.remove(order[-1])

        elif orcwarriorAInit==order[-1]:  #Starts the Orc Warrior A's turn if he's alive.
            if "Orc Warrior A" not in fainted:
                print("It's Orc Warrior A's turn.")
            order.remove(order[-1])
                
        elif orcwarriorBInit==order[-1]:  #Starts the Orc Warrior B's turn if he's alive.
            if "Orc Warrior B" not in fainted:
                print("It's Orc Warrior B's turn.")
            order.remove(order[-1])

        elif orcarcherInit==order[-1]:   #Starts the Orc Archer's turn if he's alive.
            if "Orc Archer" not in fainted:
                print("It's Orc Archer's turn.")
            order.remove(order[-1])

    if len(allies)==0: #DEFEAT CHECK - If the "allies" list is empty, the game ends and the player loses.
        game=False
        print("You have no more allies than can fight.")
        print("You lost the battle!")
        break
 
    if len(wave1)==0:  #VICTORY CHECK - If the "wave1" list is empty, the game ends and the player wins.
        game=False
        print("All enemies have been defeated.")
        print("You won the battle!")
        break          #(Defeat checks before Victory, so the player can't win with an empty party.)
