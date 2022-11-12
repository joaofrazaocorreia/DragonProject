import random

#-----------------------------------------------------------------------------------------------
#VARIABLES AND LISTS - This part stores the die and all the characters available in the game.

d20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]  #20 sided dice
d8=[1,2,3,4,5,6,7,8]  #8 sided dice
d6=[1,2,3,4,5,6]  #6 sided dice
d4=[1,2,3,4]  #4 sided dice

allies=["Warrior","Priest","Rogue","Paladin"]  #ALLIES - Allies in the party (More can be added later)

fainted=[]  #FAINTED - array for storing and registering characters who have been killed.

#WAVE1 - Enemies in the first wave of monsters (More waves and enemies can be added later)
wave1=["Orc Warrior A","Orc Warrior B","Orc Archer A","Orc Archer B"] 



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
rogue = [23,10,1,4,4]                         # ID=3
paladin=[45,15,3,3,1]                         # ID=4


#-----------------------------------------------------------------------------------------------
#ENEMY STATS - The stats of every enemy encounterable.

orcw1=[15,0,2,2,2] #HP, MP, AP, WP, INIT      ID=5
orcw2=[15,0,2,2,2]                          # ID=6
orca1=[5, 0,0,4,4]                          # ID=7
orca2=[5, 0,0,4,4]                          # ID=8


#-----------------------------------------------------------------------------------------------
#BATTLE VALUES - These values determine the flow of the battles, such as turn order and stuff

def init(x):   #INIT - Calls a fighter's initiation value.
    return int(x[4])

def turnOrder(x):   #TURN ORDER - Defines who goes first each turn during battle. Used to calculate Init rolls.
    return rolld20() + init(x)

def chooseEnemy():  #CHOOSE ENEMY - Allows the player to choose an enemy target. Changes the "target" variable to an enemy of choice.
    global target
    print("Target an enemy!")
    print(str(wave1))
    target=input()
    target=target.lower()
    print("--------------------------------------")

def chooseAlly():  #CHOOSE ALLY - Allows the player to choose an allied target. Changes the "target" variable to an ally of choice.
    global target
    print("Target an ally!")
    print(str(allies))
    target=input()
    target=target.lower()
    print("--------------------------------------")

def chooseSpell(charID):  #CHOOSE SPELL - Allows the player to choose a spell. Displays different options depending on the character ID given.
    global spell
    print("Choose a spell.")

    if charID == 1:
        print("RUSHDOWN")

    elif charID == 2:
        print("MEND / EXORCISM")

    elif charID == 3:
        print("SHARPEN")

    elif charID == 4:
        print("MEND / JUDGEMENT")

    spell=input()
    spell=spell.lower()
    print("--------------------------------------")


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

    elif spell=="judgement":
        spellEffectValue= -1 * (WP+rolld6())

    return spellEffectValue


def updateValuesMelee(character,stats,WP): #UPDATE VALUES MELEE - Deals damage to the target using WP and AP. Used for the ATTACK command.

    AP=stats[2]
    dmg=calculateDamage(WP,AP)
    stats[0]-=dmg              #Calculates and subtracts damage from the target's hp.
    print(character+" took "+str(dmg)+" damage!")
    print("--------------------------------------")
    if stats[0]<=0:
        wave1.remove(character)   #Faints if health drops below 0
        fainted.append(character)
        print(character+" fainted!")
        print("--------------------------------------")

def updateValuesMagic(character,stats,effectValue): #UPDATE VALUES MAGIC - Deals/Heals damage to the target using effectValue. Used for the MAGIC command.

    if effectValue<=0:  # If effectValue is negative or 0, it's considered a damaging spell.

        stats[0]+=effectValue
        print(character+" took "+str(-effectValue)+" damage!")
        print("--------------------------------------")
        if stats[0]<=0:
            wave1.remove(character)     #Faints the target if their health drops below 0.
            fainted.append(character)
            print(character+" fainted!")
            print("--------------------------------------")
    
    elif effectValue>0:  # If effectValue is positive, it's considered a healing spell.

        stats[0]+=effectValue  
        print(character+" healed for "+str(effectValue)+" HP!")
        print("--------------------------------------")

        if warrior[0]>32:
            warrior[0]=32

        if priest[0]>20:
            priest[0]=20
                            #If the target gets overhealed, their hp resets to it's maximum.
        if rogue[0]>27:
            rogue[0]=27

        if paladin[0]>45:
            paladin[0]=45

def castSpell(spellcost,charID,stats):

    global success
    success=False

    WP=stats[3]
    MP=stats[1]

    if MP<spellcost:
        print("You don't have enough mana to use that spell.")
        attackphase(charID) #Resets to the previous menu since there's no mana
        success=True
                
    else:
        stats[1]-=spellcost  #Removes the mana cost

        effectValue=calculateValues("judgement",WP)
        chooseEnemy()

        if target=="orc warrior a" and "Orc Warrior A" not in fainted:

            updateValuesMagic("Orc Warrior A",orcw1,effectValue)
            success=True

        elif target=="orc warrior b" and "Orc Warrior B" not in fainted:

            updateValuesMagic("Orc Warrior B",orcw2,effectValue)
            success=True

        elif target=="orc archer a" and "Orc Archer A" not in fainted:

            updateValuesMagic("Orc Archer A",orca1,effectValue)
            success=True
                        
        elif target=="orc archer b" and "Orc Archer B" not in fainted:

            updateValuesMagic("Orc Archer B",orca2,effectValue)
            success=True



#-----------------------------------------------------------------------------------------------
#INITIATION PHASE - Command for the init phase

def initphase():
    

    global order
    order=[]
    order.clear()  #Preemptively clears the list before rerolling, just in case of an uncleared value.

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

    if "Paladin" not in fainted:  #Paladin rolls for init if he's alive.
        x=paladin
        global paladinInit
        paladinInit=turnOrder(x)
        print("Paladin rolled "+str(paladinInit))

    print("")

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

    if "Orc Archer A" not in fainted:  #Orc Archer A rolls for init if he's alive.
        x=orca1
        global orcarcherAInit
        orcarcherAInit=turnOrder(x)
        print("Orc Archer A rolled "+str(orcarcherAInit))
            
    if "Orc Archer B" not in fainted:  #Orc Archer B rolls for init if he's alive.
        x=orca2
        global orcarcherBInit
        orcarcherBInit=turnOrder(x)
        print("Orc Archer B rolled "+str(orcarcherBInit))

    print("--------------------------------------")


    #Adds all alive characters' init values to the "order" list, and adds 0.1 if the value already exists.
    #The fighters at the top have less priority than the fighters below them (i.e. Orc Archer has less priority than Rogue)

    if "Paladin" not in fainted:
        order.append(paladinInit)

    while warriorInit in order:
        warriorInit+=0.1
    if "Warrior" not in fainted:
        order.append(warriorInit)

    while orcwarriorAInit in order:
        orcwarriorAInit+=0.1
    if "Orc Warrior A" not in fainted:
        order.append(orcwarriorAInit)

    while orcwarriorBInit in order:
        orcwarriorBInit+=0.1
    if "Orc Warrior B" not in fainted:
        order.append(orcwarriorBInit)

    while orcarcherAInit in order:
        orcarcherAInit+=0.1
    if "Orc Archer A" not in fainted: 
        order.append(orcarcherAInit)

    while orcarcherBInit in order:
        orcarcherBInit+=0.1
    if "Orc Archer B" not in fainted: 
        order.append(orcarcherBInit)

    while rogueInit in order:          #IMPORTANT NOTE - DON'T CHANGE THIS ORDER!!!! THEY'RE BASED ON INIT VALUES, FROM LOWEST TO HIGHEST
        rogueInit+=0.1
    if "Rogue" not in fainted:
        order.append(rogueInit)

    while priestInit in order:
        priestInit+=0.1
    if "Priest" not in fainted:
        order.append(priestInit)

    order.sort()  #Sorts the list from smallest to biggest values

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

    elif characterID==4:
        WP=paladin[3]
        MP=paladin[1]


    print("What will you do?")
    print("ATTACK / MAGIC")   #Prompts the player's choice for a battle command.
    command=input()
    command=command.lower()
    print("--------------------------------------")

    turn=True  #Variable for looping until the turn successfully ends.

#-----------------------------------------------------------------------------------------------
    if command=="attack":  #loop for the ATTACK command.

        while turn:

            chooseEnemy()  #The player chooses an enemy and their stats will be used for melee combat.

            if target=="orc warrior a" and "Orc Warrior A" not in fainted:  #Can only target orc warrior A if he's alive

                updateValuesMelee("Orc Warrior A",orcw1,WP)
                turn=False

            elif target=="orc warrior b" and "Orc Warrior B" not in fainted:  #Can only target orc warrior B if he's alive
                
                updateValuesMelee("Orc Warrior B",orcw2,WP)
                turn=False

            elif target=="orc archer a" and "Orc Archer A" not in fainted:  #Can only target orc archer A if he's alive
                
                updateValuesMelee("Orc Archer A",orca1,WP)
                turn=False
            
            elif target=="orc archer b" and "Orc Archer B" not in fainted:  #Can only target orc archer B if he's alive
                
                updateValuesMelee("Orc Archer B",orca2,WP)
                turn=False

            else:
                print("That's not an enemy.") #Causes error if the target input is unknown, and loops back to the prompt.            
                print("--------------------------------------")


#-----------------------------------------------------------------------------------------------
    elif command=="magic": #loop for the MAGIC command.
        
        while turn:
            chooseSpell(characterID)

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
                    if target=="orc warrior a" and "Orc Warrior A" not in fainted:

                        updateValuesMagic("Orc Warrior A",orcw1,effectValue)
                        turn=False

                    elif target=="orc warrior b" and "Orc Warrior B" not in fainted:

                        updateValuesMagic("Orc Warrior B",orcw2,effectValue)
                        turn=False

                    elif target=="orc archer a" and "Orc Archer A" not in fainted:

                        updateValuesMagic("Orc Archer A",orca1,effectValue)
                        turn=False
                        
                    elif target=="orc archer b" and "Orc Archer B" not in fainted:

                        updateValuesMagic("Orc Archer B",orca2,effectValue)
                        turn=False

                    else:
                        print("That's not an enemy.") #Causes error if the target input is unknown, and loops back to the prompt.            
                        print("--------------------------------------")

            elif spell == "rushdown":   #Causes error if not used by Warrior.
                print("This character can't use this spell!")
                print("--------------------------------------")


            elif spell == "mend" and characterID==2:   #--MEND-- priest spell
                spellcost=3

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    priest[1]-=spellcost  #Removes the mana cost
                    
                    effectValue=calculateValues("mend",WP)
                    chooseAlly()

                    if target=="warrior" and "Warrior" not in fainted:

                        updateValuesMagic("Warrior",warrior,effectValue)
                        turn=False

                    elif target=="priest" and "Priest" not in fainted:

                        updateValuesMagic("Priest",priest,effectValue)
                        turn=False

                    elif target=="rogue" and "Rogue" not in fainted:

                        updateValuesMagic("Rogue",rogue,effectValue)
                        turn=False

                    elif target=="paladin" and "Paladin" not in fainted:

                        updateValuesMagic("Paladin",paladin,effectValue)
                        turn=False

                    else:
                        print("That's not an ally.") #Causes error if the target input is unknown, and loops back to the prompt.            
                        print("--------------------------------------")

            elif spell == "mend" and characterID==4:   #--MEND-- paladin spell
                spellcost=3

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    paladin[1]-=spellcost  #Removes the mana cost
                    
                    effectValue=calculateValues("mend",WP)
                    chooseAlly()
                    
                    if target=="warrior" and "Warrior" not in fainted:

                        updateValuesMagic("Warrior",warrior,effectValue)
                        turn=False

                    elif target=="priest" and "Priest" not in fainted:

                        updateValuesMagic("Priest",priest,effectValue)
                        turn=False

                    elif target=="rogue" and "Rogue" not in fainted:

                        updateValuesMagic("Rogue",rogue,effectValue)
                        turn=False

                    elif target=="paladin" and "Paladin" not in fainted:

                        updateValuesMagic("Paladin",paladin,effectValue)
                        turn=False

                    else:
                        print("That's not an ally.") #Causes error if the target input is unknown, and loops back to the prompt.            
                        print("--------------------------------------")

            elif spell == "mend":   #Causes error if not used by Priest or Paladin.
                print("This character can't use this spell!")
                print("--------------------------------------")

            
            elif spell == "jjudgement" and characterID==4:  #--JUDGEMENT-- spell
                spellcost=9

                if MP<spellcost:
                    print("You don't have enough mana to use that spell.")
                    attackphase(characterID) #Resets to the previous menu since there's no mana
                    turn=False
                
                else:
                    paladin[1]-=spellcost  #Removes the mana cost

                    effectValue=calculateValues("judgement",WP)
                    chooseEnemy()

                    if target=="orc warrior a" and "Orc Warrior A" not in fainted:

                        updateValuesMagic("Orc Warrior A",orcw1,effectValue)
                        turn=False

                    elif target=="orc warrior b" and "Orc Warrior B" not in fainted:

                        updateValuesMagic("Orc Warrior B",orcw2,effectValue)
                        turn=False

                    elif target=="orc archer a" and "Orc Archer A" not in fainted:

                        updateValuesMagic("Orc Archer A",orca1,effectValue)
                        turn=False
                        
                    elif target=="orc archer b" and "Orc Archer B" not in fainted:

                        updateValuesMagic("Orc Archer B",orca2,effectValue)
                        turn=False

                    else:
                        print("That's not an enemy.") #Causes error if the target input is unknown, and loops back to the prompt.            
                        print("--------------------------------------")
                    
            elif spell == "judgement":   #Causes error if not used by Paladin.
                print("This character can't use this spell!")
                print("--------------------------------------")


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
                    
                    if target=="orc warrior a" and "Orc Warrior A" not in fainted:

                        updateValuesMagic("Orc Warrior A",orcw1,effectValue)
                        turn=False

                    elif target=="orc warrior b" and "Orc Warrior B" not in fainted:

                        updateValuesMagic("Orc Warrior B",orcw2,effectValue)
                        turn=False

                    elif target=="orc archer a" and "Orc Archer A" not in fainted:

                        updateValuesMagic("Orc Archer A",orca1,effectValue)
                        turn=False
                        
                    elif target=="orc archer b" and "Orc Archer B" not in fainted:

                        updateValuesMagic("Orc Archer B",orca2,effectValue)
                        turn=False

                    else:
                        print("That's not an enemy.") #Causes error if the target input is unknown, and loops back to the prompt.            
                        print("--------------------------------------")

            elif spell == "exorcism":   #Causes error if not used by Priest.
                print("This character can't use this spell!")
                print("--------------------------------------")


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

                    print("Rogue sharpens their weapon. +2 Weapon Power")
                    print("--------------------------------------")
                    turn=False

            elif spell == "sharpen":   #Causes error if not used by Rogue.
                print("This character can't use this spell!")
                print("--------------------------------------")

            else:
                print("That's not a known spell.")   #Causes error if the spell input is unknown, and loops back to the prompt.
                print("--------------------------------------")
    
    else:
        print("Unknown Command.")  #Causes error if the battle command is unknown, and lopps back to the prompt.
        attackphase(characterID)


        
        

    
  

#-----------------------------------------------------------------------------------------------
#GAME LOOP - Keeps the game going until a win/lose condition is met.

game=True

while game:
    print("--------------------------------------")
    print(">> Turn Start! <<")
    print("--------------------------------------")

    initphase()

    while len(order)>0:  #Loops until all characters have ended their attack phase.

        if warriorInit==order[-1]:  #Starts the Warrior's turn if they're alive.
            if "Warrior" not in fainted and len(wave1)!=0:
                print("It's Warrior's turn.")
                print("")
                attackphase(1)
            order.remove(order[-1])

        
        elif priestInit==order[-1]:  #Starts the Priests's turn if they're alive.
            if "Priest" not in fainted and len(wave1)!=0:
                print("It's Priest's turn.")
                print("")
                attackphase(2)
            order.remove(order[-1])
                
        
        elif rogueInit==order[-1]:  #Starts the Rogue's turn if they're alive.
            if "Rogue" not in fainted and len(wave1)!=0:
                print("It's Rogue's turn.")
                print("")
                attackphase(3)
            order.remove(order[-1])

        
        elif paladinInit==order[-1]:  #Starts the Paladin's turn if they're alive.
            if "Paladin" not in fainted and len(wave1)!=0:
                print("It's Paladin's turn.")
                print("")
                attackphase(4)
            order.remove(order[-1])


        elif orcwarriorAInit==order[-1]:  #Starts the Orc Warrior A's turn if they're alive.
            if "Orc Warrior A" not in fainted and len(allies)!=0:
                print("It's Orc Warrior A's turn.")
                print("")
            order.remove(order[-1])
                

        elif orcwarriorBInit==order[-1]:  #Starts the Orc Warrior B's turn if they're alive.
            if "Orc Warrior B" not in fainted and len(allies)!=0:
                print("It's Orc Warrior B's turn.")
                print("")
            order.remove(order[-1])


        elif orcarcherAInit==order[-1]:   #Starts the Orc Archer's turn if they're alive.
            if "Orc Archer A" not in fainted and len(allies)!=0:
                print("It's Orc Archer A's turn.")
                print("")
            order.remove(order[-1])


        elif orcarcherBInit==order[-1]:   #Starts the Orc Archer's turn if they're alive.
            if "Orc Archer B" not in fainted and len(allies)!=0:
                print("It's Orc Archer B's turn.")
                print("")
            order.remove(order[-1])


    if len(allies)==0: #DEFEAT CHECK - If the "allies" list is empty, the game ends and the player loses.
        game=False
        print("--------------------------------------")
        print("You have no more allies than can fight.")
        print("You lost the battle!")
        print("--------------------------------------")
        break
 
    if len(wave1)==0:  #VICTORY CHECK - If the "wave1" list is empty, the game ends and the player wins.
        game=False
        print("--------------------------------------")
        print("All enemies have been defeated.")
        print("You won the battle!")
        print("--------------------------------------")
        break          #(Defeat checks before Victory, so the player can't win with an empty party.)
