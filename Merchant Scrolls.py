#Imports
from random import *
from time import *
import sys

#Loop if player wishes to keep playing
playagain = "y"
while playagain == "y":
    playagain = "n"

    #Game variables
    star = "*" * 150
    totalGold = 0
    totalResource = 0

    #Introduction
    print(star)
    print()
    print("MERCHANT SCROLLS")
    sleep(1)
    print()
    print("A game by: Aleck Bowen Sun")
    sleep(1)
    print()
    print("Survive and build your wealth through trading!")
    sleep(1)
    print()
    print(star)
    print()

    #Rules
    rules = input("Would you like to know the rules of the game? (y/n):   ")
    print()
    while rules not in ["y", "n"]:
        print("Sorry, that is an invalid option.")
        print("Select yes or no using the lower-case letter y or n.")
        print()
        rules = input("Would you like to know the rules of the game? (y/n):   ")
        print()
    #Rules
    if rules == "y":
        print(star)
        print()
        print("RULES:")
        print()
        sleep(1)
        print("Use full screen for the best gaming experience!")
        print()
        sleep(1)
        print("The objective of the game is to become as wealthy as possible!")
        print()
        sleep(1)
        print("You build your wealth by selecting a character and using him to collect resources.")
        print()
        sleep(1)
        print("Using your resources, you will make merchant deals with others.")
        print()
        sleep(1)
        print("The merchant deals will often be different and random, try to sell your resources when people are buying them at the highest price!")
        print()
        sleep(1)
        print("If you lose all your health points, you lose.")
        print()
        sleep(1)
        print("To beat the game buy the ultimate scroll! Good luck!")
        print()
        print(star)
        sleep(1)
        print()
        
    #Choosing classes
    print("BEGINNING GAME...")
    sleep(3)
    print()
    print("Please choose a class:")
    print()
    print("Paladin: Strong and fearless. They raid enemies and defend castles to earn treasures. A dangerous role with very high rewards!")
    print()
    sleep(1)
    print("Hunter: Swift and fast. They hunt birds from the sky with their archery skills and lucky touch. Some days, resources may be scarce, but high reward class!")
    print()
    sleep(1)
    print("Farmer: Dedicated and hard-working. Like everybody, says hardwork pays off *wink*. Slow and steady rewards, but very safe class.")
    print()
    sleep(1)
    charClass = input("(a) Paladin, (b) Hunter, (c) Farmer  : ")
    print()
    while charClass not in ["a", "b", "c"]:
      print("Sorry, that is an invalid options.")
      print("Select an option using the lowercase letters provided.")
      print()
      charClass = input("(a) Paladin, (b) Hunter, (c) Farmer  : ")
      print()
    print("Nice choice!")
    print()
    name = input("Before I send you on your journey can I have your name:   ")
    print()
    print("Be ready to enter the realm and good luck!")
    print()
    print(star)
    print()
    sleep(1)
    print("ENTERING REALM...")
    sleep(3)
    for blank in range(0, 75):
      print()

    #Game building based on class
    if charClass == "a":
      prefix = "sir"
      resourceTyp = "treasures"
      hp = 100
      timeFarm = 10
      resourceChance = 1
      dmgChance = 0
      
    elif charClass == "b":
      prefix = "huntmaster"
      resourceTyp = "animals"
      hp = 100
      timeFarm = 7
      resourceChance = 0
      dmgChance = 1
      
    else:
      prefix = "farmer"
      resourceTyp = "wheat"
      hp = 100
      timeFarm = 7
      resourceChance = 1
      dmgChance = 1

    name = (prefix + " " + name)
      
    #Choosing what the player is going to do
    print("Welcome finally to the game", str(name) + "!")
    print()
    sleep(1)
    while hp > 0 and playagain == "n":
        print("Would you like to enter the market or farm resources?")
        task = input("(a) Market   or    (b) Farm   :   ")
        print()
        while task not in ["a", "b"]:
            print("Sorry, that is an invalid options.")
            print("Select an option using the lowercase letters provided.")
            print()
            task = input("(a) Market   or    (b) Farm   :   ")
            print()

        #Player decides to do trading
        if task == "a":
            if totalResource > 0:
                market = randint(0, 2)

                #10% rate market
                if market == 1:
                    gold = totalResource/10
                    print("Would you like to exchange", resourceTyp, "for gold?")
                    trade = input("The rate right now is 10% of your resources. (y/n):   ")
                    print()
                    while trade not in ["y", "n"]:
                        print("Sorry, that is an invalid option.")
                        print("Select yes or no using the lower-case letter y or n.")
                        print()
                        print("Would you like to exchange", resourceTyp, "for gold?")
                        trade = input("The rate right now is 10% of your resources. (y/n):   ")
                        print()
                        
                    #Exchanges resource for gold
                    if trade == "y":
                        totalGold = gold + totalGold
                        totalResource = 0
                        print("You now have:", int(totalGold), "gold.")
                        print()
                        
                #5% rate market
                else:
                    gold = totalResource/20
                    print("Would you like to exchange", resourceTyp, "for gold?")
                    trade = input("The rate right now is 5% of your resources. (y/n):   ")
                    print()
                    while trade not in ["y", "n"]:
                        print("Sorry, that is an invalid option.")
                        print("Select yes or no using the lower-case letter y or n.")
                        print()
                        print("Would you like to exchange", resourceTyp, "for gold?")
                        trade = input("The rate right now is 5% of your resources. (y/n):   ")
                        print()
                    if trade == "y":
                        totalGold = gold + totalGold
                        totalResource = 0
                        print("You now have:", int(totalGold), "gold.")
                        print()

            #No resources
            else:
                print("Sorry you don't have enough resources to trade. Go farm some!")
                print()

            #Has enough gold to beat the game (buy ultimate scroll)
            if totalGold >= 100:
                end = input("You have enough to buy the ultimate scroll and beat the game. Would you like to do so? (y/n)):  ")
                print()
                while end not in ["y", "n"]:
                    print("Sorry, that is an invalid option.")
                    print("Select yes or no using the lower-case letter y or n.")
                    print()
                    end = input("You have enough to buy the ultimate scroll and beat the game. Would you like to do so? (y/n):  ")
                    print()
                if end == "y":
                    print("CONGRATULATIONS! You beat the game!")
                    print("Hope you had a fun time playing!")
                    print()
                    sleep(3)
                    playagain = input("Would you like to play again? (y/n):  ")
                    print()
                    while playagain not in ("y", "n"):
                        print("Invalid response. Please select using lower-case letter y or n.")
                        print()
                        playagain = input("Would you like to play again? (y/n):  ")
                        print()
                    if playagain == "n":
                        sys.exit()

        #Player decides to farm resources
        else:
            print("Time to farm some", resourceTyp + "!")
            print()
            print("FARMING RESOURCES...(please wait)")
            print()
            sleep(timeFarm)

            #Palading farming
            if dmgChance == 0:
                ifdmg = randint(1, 2)

                #If injured during battle or died
                if ifdmg == 1:
                    print("You were injured while defending the castle!")
                    print("Your hp dropped by 20.")
                    print()
                    hp = hp - 20
                    print("You now have", str(int(hp)) + "hp.")
                    print()
                    if hp == 0:
                        print("You have fought hard, tried your hardest to survive and grow your wealth.")
                        print("However, you were injured too often and have failed.")
                        print()
                        print("Your sacarfice will go down in history...")
                        print("GAME OVER")
                        print()
                        sleep(3)
                        playagain = input("Would you like to play again? (y/n):  ")
                        print()
                        while playagain not in ("y", "n"):
                            print("Invalid response. Please select using lower-case letter y or n.")
                            print()
                            playagain = input("Would you like to play again? (y/n):  ")
                            print()
                        if playagain == "n":
                            sys.exit()

                #Rewarding resources
                print("You have successfully completed the quest!")
                print("Your courage and bravery while defending the castle has caught the attention of the queen. As a gift, she has rewarded you 100 treasures!")
                print()
                totalResource = totalResource + 100

            #Hunter farming
            elif resourceChance == 0:
                #1/4 chance to get resources
                ifresource = randint(1, 4)
                if ifresource == 1:
                    print("You had great luck hunting today!")
                    print("The forest was filled with animals!")
                    print("You caught 80 animals!")
                    print()
                    totalResource = totalResource + 80
                else:
                    print("Sadly, today the weather drove the animals into their shelters.")
                    print("Try hunting again later.")
                    print()

            #Farming as farmer
            else:
                print("A days of hard work done.")
                print("You worked hard and grew 20 wheat.")
                print()
                totalResource = totalResource + 20

                #Special lucky bonus for farmers
                luckyday = randint(1, 10)
                if luckyday == 1:
                    print("WAIT! Something is happening...")
                    print()
                    sleep(3)
                    print("Your hardwork has admired an angel. She has appeared and enchanted all your wheat!")
                    print("Collect them fast before the enchanment runs out!")
                    print()

                    #Small minigame, press letter c and 'enter' to collect resources
                    print("To collect 20 wheat, type 'c' and then hit the 'enter' key. Collect as many as possible within 10 seconds! Good luck!")
                    ready = input("Click 'enter' key when ready:  ")
                    time1 = time()
                    collect = input("Type 'c' and click 'enter'!    ")
                    print()
                    if collect == "c":
                        print("Collected 20 wheat!")
                        print()
                        totalResource = totalResource + 20
                    else:
                        print("Make sure you are typing the letter c(lower-case)!")
                        print()
                    print("Keep going! grab as many wheat as you can in 10 seconds!")
                    print()
                    time2 = time()
                    while time2 - time1 < 10:
                        collect = input("Type 'c' and click 'enter'!    ")
                        print()
                        if collect == "c":
                            print("Collected 20 wheat!")
                            print()
                            totalResource = totalResource + 20
                        else:
                            print("Make sure you are typing the letter c(lower-case)!")
                            print()
                        print("Keep going! grab as many wheat as you can in 10 seconds!")
                        print()
                        time2 = time()
                    print("Times up!")
                    print()
                    sleep(3)

            #Total resources
            print("You now have", str(totalResource), str(resourceTyp) + "!")
            for Space in range (0,10):
                print()
