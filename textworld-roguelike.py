import random
from sys import exit

####################
#fight system
def fightSystem(Uhr,Uhp,Uat,Uag,Mname,Mhp,Mat,Mag):
    Mhr = Mhp
    #main loop
    while (Uhr > 0) and (Mhr > 0):
        print("You | Health: {0}/{1} | Attack: {2} | Agility: {3}".format(Uhr,Uhp,Uat,Uag))
        print("{0} | Health: {1}/{2} | Attack: {3} | Agility: {4}".format(Mname,Mhr,Mhp,Mat,Mag))
	#player's turn
        print("You attack {0}.".format(Mname))
        roll1 = random.randrange(1,7)
        print("Rolled a {0} for {1} attack!".format(roll1, roll1 * Uat))
        print("{0} attempts a dodge.".format(Mname))
        roll2 = random.randrange(1,7)
        print("Rolled a {0} for {1} agility!".format(roll2, roll2 * Mag))
        if (roll2 * Mag) > (roll1 * Uat):
            print("The {0} dodged your attack.".format(Mname))
        else:
            print("The {0} takes the damage.".format(Mname))
            Mhr -= roll1 * Uat
        #monster's turn
        if Mhr > 0:
            print("{0} attacks you.".format(Mname))
            roll1 = random.randrange(1,7)
            print("Rolled a {0} for {1} attack!".format(roll1, roll1 * Mat))
            print("You attempt a dodge.".format(Mname))
            roll2 = random.randrange(1,7)
            print("Rolled a {0} for {1} agility!".format(roll2, roll2 * Uag))
            if (roll2 * Uag) > (roll1 * Mat):
                print("You dodged the attack.")
            else:
                print("You take the damage.")
                Uhr -= roll1 * Mat
    #if you win
    else:
        if Mhr < 1:
            print("YOU WIN")
            bg = (random.randrange(1,5) * 5)
            print("\nYou won {0} gold.".format(bg))
            return [bg,Uhr]
        #you lose
        else:
            print("YOU ARE DEAD")
            input("Press enter finish.")
            exit()

####################
#intro
print("GAME START")
print("A character and their stats will be generated for you randomly.\nYou can reroll if desired.")

#character gen
name1 = ["Ub","Tal","Fir","En","Kul","Rit","Fas","Mal","Hap","Dor","Ary","Erin","Seran","Celim","Bol","Bor","Moh","Isan","Ael","Ow","Dur"]
name2 = ["or","undil","illa","ma","end","ex","axe","","o","a","u","ia","illf","elf","etta"]
races = ["Human","Elf","Dwarf","Beastman","Undead"]

rollChar = False
while rollChar == False:
    print()
    print("Rolling character stats...")
    name = random.choice(name1) + random.choice(name2)
    race = random.choice(races)
    Uhp = 50 + (random.randrange(0,30)) * 5
    Uat = (random.randrange(1,7)) + (random.randrange(0,4))
    Uag = (random.randrange(1,7))
    gp = (random.randrange(0,10) * 10)
    print("{0} the {1}".format(name,race))
    print("Hitpoints: {0}".format(Uhp))
    print("Attack: {0}".format(Uat))
    print("Agility: {0}".format(Uag))
    print("{0} starting gold".format(gp))
    choice = input("Accept these stats? y/ n: ")
    if choice == "y":
        rollChar = True
        
game = True
stage = "Plains"
Uhr = Uhp
keys = 0
undeadLast = False
title = False

####################
#main game loop
while game == True:
    
    #achievements
    if title == False:
        if gp > 999:
            name += " the Gold"
            print("\nCongratulations, your wealth has earned you the title of {0}!".format(name))
            title = True
        if Uat > 9:
            name += " the Mighty"
            print("\nCongratulations, your strength has earned you the title of {0}!".format(name))
            title = True            
        if Uag > 6:
            name += " the Swift"
            print("\nCongratulations, your agility has earned you the title of {0}!".format(name))
            title = True
        if keys > 5:
            name += " the Keymaster"
            print("\nCongratulations, your strange obsession with key collecting has earned you the title of {0}!".format(name))
            title = True           

    #basic
    print("\nCurrent stage: {0}\n{1}/{2}hp | {3} gold | {4} key(s)".format(stage,Uhr,Uhp,gp,keys))
    input("Press enter to pick a card.")
    print("Picking a card...")
    print()
    event = random.randrange(0,22)        
    
    #single frequency events
    if event == 0:
        stage = "Plains"
        print("You enter the {0}.".format(stage))
        if race == "Beastman":
            print("This land makes you proud to be a Beastman.\nYou restore 5hp.")
            Uhr += 5
    if event == 1:
        stage = "Desert"
        print("You enter the {0}.".format(stage))
        print("It feels like you are burning.\nYou lose 5hp.")
        Uhr -= 5
    if event == 2:
        stage = "Swamp"
        print("You enter the {0}.".format(stage))
        if race == "Undead":
            print("It reeks of death, but this is perfect for an undead.\nYou restore 10hp.")
            Uhr += 10
        else:
            print("It swamp reeks of death.\nYou lose 5hp.")
            Uhr -= 5
    if event == 3:
        stage = "Forest"
        print("You enter the {0}.".format(stage))
        if race != "Undead":
            print("You forage for a while and find some things to eat.\nYou restore 10hp.")
            Uhr += 10
    if event == 4:
        print("You encounter a Slime Monster!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Slime Monster",30,2,2)
        gp += result[0]
        Uhr = result[1]
        undeadLast = False
    if event == 5:
        print("You encounter a Skeleton!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Skeleton",50,5,3)
        gp += result[0]
        Uhr = result[1]
        undeadLast = True
    if event == 6:
        print("You spend the night in a haunted inn.")
        if undeadLast == True:
            print("You encounter a Skeleton!\n")
            result = fightSystem(Uhr,Uhp,Uat,Uag,"Skeleton",50,5,3)
            gp += result[0]
            Uhr = result[1]
            undeadLast = True
        else:
            print("The night is thankfully uneventful.")
    if event == 7:
        print("You meet a herbalist who offers to restore you to full health for 100 gold.")
        if gp > 99:
            choice = input("Accept her offer? y/ n: ")
            if choice == "y":
                print("You hand over the coins and are healed to full health.")
                Uhr = Uhp
                gp -= 100
            else:
                print("You reject her offer and continue your journey.")
        else:
            print("You don't have enough money to accept her offer.")
    if event == 8:
        print("You meet a travelling merchant who offers to sell you a key for 50 gold.")
        if gp > 49:
            choice = input("Accept her offer? y/ n: ")
            if choice == "y":
                print("You hand over the coins and are given a key.")
                keys += 1
                gp -= 50
            else:
                print("You reject her offer and continue your journey.")
        else:
            print("You don't have enough money to accept her offer.")
    if event == 9:
        print("You get into a brawl with a rowdy villager.")
        skillCheck = random.randrange(4,6)
        print("Skill check... Villager attack: {0}.".format(skillCheck))
        if Uat < skillCheck:
            if gp > 70:
                gp -= 70
                print("The villager manages to get the upper hand and steals 70 gold pieces.")
            else:
                gp = 0
                Uhr -= 5
                print("The villager manages to get the upper hand and steals your gold purse.")
                print("You lose 5hp.")
        else:
            gp += 70
            print("You win the brawl and he apologetically hands over his coin purse with 70 gold.")
    if event == 10:
        print("You find a locked treasure chest.")
        if keys > 0:
            choice = input("Open the chest and spend 1 key? y/ n: ")
            if choice == "y":
                bg = random.randrange(5,30) * 5
                print("You spend the key and find {0} gold.".format(bg))
                keys -= 1
                gp += bg
            else:
                print("You leave this chest and continue your journey.")
        else:
            print("You don't have any keys to open the chest with.")
    if event == 11:
        print("You find a trapped chest.")
        choice = input("Attempt to open the chest and dodge the trap? y/ n: ")
        if choice == "y":
            skillCheck = random.randrange(1,12)
            print("Skill check... Trap level: {0}.".format(skillCheck))
            if Uag < skillCheck:
                bg = random.randrange(5,15) * 5
                print("You successfully avoid the trap and find {0} gold!".format(bg))
                gp += bg
            else:
                damage = skillCheck * 2
                print("You fail to avoid the trap and lose {0}hp.".format(damage))
                Uhr -= damage
        else:
            print("You leave this chest and continue your journey.")
    if event == 12:
        if race == "Elf":
            print("You meet some fellow elves who offer to restore your health points for free.")
            print("Health restored to full.")
            Uhr = Uhp
        else:
            print("You meet some elves, but they don't want much to do with outsiders.")
    if event == 13:
        print("You encounter a Wolf!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Wolf",40,5,5)
        gp += result[0]
        Uhr = result[1]
        undeadLast = False
    if event == 14:
        print("You encounter a Living Dead!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Living Dead",35,5,1)
        gp += result[0]
        Uhr = result[1]
        undeadLast = True
    if event == 15:
        print("You encounter a Highwayman!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Highwayman",50,6,4)
        gp += result[0]
        Uhr = result[1]
        undeadLast = False
    if event == 16:
        print("You encounter a Zombie Dog!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Zombie Dog",30,4,3)
        gp += result[0]
        Uhr = result[1]
        undeadLast = True
    if event == 17:
        print("You encounter a Black Knight!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Black Knight",65,7,3)
        gp += result[0]
        Uhr = result[1]
        undeadLast = False
    if event == 18:
        print("You encounter a Rogue!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Rogue",30,3,6)
        gp += result[0]
        Uhr = result[1]
        undeadLast = False
    if event == 19:
        print("You encounter a Unicorn!\n")
        result = fightSystem(Uhr,Uhp,Uat,Uag,"Unicorn",70,4,4)
        gp += result[0]
        Uhp += 5
        Uhr = Uhp
        print("Drinking unicorn blood raises your max health by 5 and restores it to full!")
        undeadLast = False
    if event == 20:
        print("You find a well where the water has healing properties.\nIt restores 20hp.")
        Uhr += 20
        if Uhr > Uhp:
            Uhr = Uhp
    if event == 21:
        print("You meet a sorcerer looking for someone to test an experimental potion on.\nIt has a 50/50 chance of making you stronger or weaker.")
        choice = input("Drink the potion? y/ n: ")
        if choice == "y":
            rand = random.randrange(0,2)
            if rand == 1:
                Uat += 1
                print("It goes well! You gain an attack point.")
            else:
                Uat -= 1
                print("It goes poorly! You lose an attack point.")
        else:
            print("You refuse the potion.")

    #dual frequency events
    ##NONE##

    #check if dead
    if Uhr < 1:
        print("You have no more healthpoints left.\nYOU ARE DEAD")
        input("Press enter to finish.")
        exit()
        
