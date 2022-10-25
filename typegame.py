


# Run the main loop
import random


def main():

    # Initialize player
    playerGold = 0
    damage = 1


    # Set up enemy
    class Enemy:

        def __init__(self, name, health, maxhealth, goldDrop):
            self.name = name
            self.health = health
            self.maxhealth = maxhealth
            self.goldDrop = goldDrop

        def reduceHealth(self, damage):
            self.health = self.health - damage
            print("You've struck the", self.name)

        def getHealth(self):
            print(self.health)

    class Weapon:

        def __init__(self, name, price, dps, equipped):
            self.name = name
            self.price = price
            self.dps = dps
            self.equipped = equipped

        def equip(self, damage):
            self.equipped += 1
            damage += self.dps
            return damage



    # Define all weapons
    dagger = Weapon("Dagger", 5, 3, 0)
    longsword = Weapon("Longsword", 20, 14, 0)
    mace = Weapon("Mace", 40, 40, 0)
    crossbow = Weapon("Crossbow", 100, 120, 0)
    battleaxe = Weapon("Battleaxe", 500, 700, 0)
    warhammer = Weapon("Warhammer", 1000, 1550, 0)
    katana = Weapon("Katana", 2500, 4000, 0)


    # Define all enemies
    gnome = Enemy("Gnome", 10, 10, 1)
    elf = Enemy("Elf", 30, 30, 3)
    troll = Enemy("Troll", 50, 50, 10)
    orc = Enemy("Orc", 100, 100, 25)
    priest = Enemy("Evil Priest", 250, 250, 80)
    wizard = Enemy("Fire Wizard", 900, 900, 350)
    dwarf = Enemy("Dwarven King", 2000, 2000, 850)
    medusa = Enemy("Medusa", 12500, 14000, 5000)


    # Define the chooseEnemy function to assign the enemy the player is fighting
    def chooseEnemy():

        # Print menu selections
        print()
        print("Which enemy would you like to fight?")
        print()
        print("Gnome")
        print("Elf")
        print("Troll")
        print("Orc")
        print("Evil Priest")
        print("Wizard")
        print("Dwarf")
        print("Medusa")
        print()

        # Take input from user to get desired enemy
        enemySelection = input()

        # Spawn the enemy chosen by user and set health to max
        if enemySelection == "gnome" or enemySelection == "Gnome":
            enemyConfirm = gnome
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Elf" or enemySelection == "elf":
            enemyConfirm = elf
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Troll" or enemySelection == "troll":
            enemyConfirm = troll
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Orc" or enemySelection == "orc":
            enemyConfirm = orc
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Evil Priest" or \
            enemySelection == "evil priest" or \
            enemySelection == "priest" or \
            enemySelection == "Priest" or \
            enemySelection == "Evil priest":
            enemyConfirm = priest
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Wizard" or enemySelection == "wizard":
            enemyConfirm = wizard
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Dwarf" or enemySelection == "dwarf":
            enemyConfirm = dwarf
            enemyConfirm.health = enemyConfirm.maxhealth
        elif enemySelection == "Medusa" or enemySelection == "medusa":
            enemyConfirm = medusa
            enemyConfirm.health = enemyConfirm.maxhealth
        else:
            print("You must select an enemy to fight.")
            enemyConfirm = chooseEnemy()


        return enemyConfirm

    # Set current enemy
    currentEnemy = chooseEnemy()


    # Define the killEnemy function to give the player gold
    def killEnemy(playerGold, currentEnemy):
        playerGold = playerGold + currentEnemy.goldDrop
        print("You have slain", currentEnemy.name, "and gained", currentEnemy.goldDrop, "gold.")

        # Spawn the next enemy
        if currentEnemy == gnome:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == elf:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == troll:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == orc:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == priest:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == wizard:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == dwarf:
            currentEnemy.health = currentEnemy.maxhealth
        elif currentEnemy == medusa:
            currentEnemy.health = currentEnemy.maxhealth

        return playerGold, currentEnemy

    # Define the shop function
    def shopText():
        print("Welcome to the shop!")
        print("Here's what we have for sale:")
        print("Dagger - 5 gold - 3 damage")
        print("Longsword - 20 gold - 14 damage")
        print("Mace - 40 gold - 40 damage")
        print("Crossbow - 100 gold - 120 damage")
        print("Battleaxe - 500 gold - 700 damage")
        print("Warhammer - 1000 gold - 1550 damage")
        print("Katana - 2500 gold - 4000 damage")
        print("Type the name of an item to purchase it, or type 'exit' to leave the shop.")
        print("You currently have", playerGold, "gold.")

    # Run the actual logic for the shop
    def shopFunction(playerGold, damage):

        # take input from user and give them the weapon, take gold
        userPick = input()

        # Allow user to leave
        if userPick == "exit":
            print("Come back soon.")
            return playerGold, damage

        # Determine what the user wants to buy
        elif userPick == "Dagger" or userPick == "dagger":
            if playerGold >= dagger.price:
                damage = dagger.equip(damage)
                playerGold = playerGold - dagger.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        elif userPick == "Longsword" or userPick == "longsword":
            if playerGold >= longsword.price:
                damage = longsword.equip(damage)
                playerGold = playerGold - longsword.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        elif userPick == "Mace" or userPick == "mace":
            if playerGold >= mace.price:
                damage = mace.equip(damage)
                playerGold = playerGold - mace.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        elif userPick == "Crossbow" or userPick == "crossbow":
            if playerGold >= crossbow.price:
                damage = crossbow.equip(damage)
                playerGold = playerGold - crossbow.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        elif userPick == "Battleaxe" or userPick == "battleaxe":
            if playerGold >= battleaxe.price:
                damage = battleaxe.equip(damage)
                playerGold = playerGold - battleaxe.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        elif userPick == "Warhammer" or userPick == "warhammer":
            if playerGold >= warhammer.price:
                damage = warhammer.equip(damage)
                playerGold = playerGold - warhammer.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        elif userPick == "Katana" or userPick == "katana":
            if playerGold >= katana.price:
                damage = katana.equip(damage)
                playerGold = playerGold - katana.price
                print("Would you like to buy anything else?")
                print("You have", playerGold, "gold remaining.")
                playerGold, damage = shopFunction(playerGold, damage)
            else:
                print("You have insufficient funds.")
                playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage
        else:
            playerGold, damage = shopFunction(playerGold, damage)
            return playerGold, damage

    # Assign an initial wordproblem length
    problemLength = 1

    # Define the generateProblem() function to generate a sentence for the user to type
    def generateProblem(currentEnemy):

        # List of random words for the problem generator to choose from
        wordList = ['dance', 'the', 'if', 'and', 'about', 'around', 'capture', 'drama', 'tactic', 'sheep', 'elect', 'flu', 'cord', 'stretch', 'access', 'elapse', 'presentation',
                    'therapist', 'shock', 'lift', 'foster', 'parade', 'act', 'formulate', 'bridge', 'bind', 'learn', 'revival', 'vehicle',
                    'fold', 'evaluate', 'introduction', 'patient', 'explicit', 'accent', 'inject', 'benefit', 'like', 'pleasure', 'floor', 'trait',
                    'talented', 'fruit', 'collar', 'kidnap', 'night', 'secretion', 'sunshine', 'lock', 'forestry', 'graduate', 'feed', 'dependence', 'extinct',
                    'because', 'yet', 'number', 'tree', 'calculate', 'precise', 'knife', 'cut', 'chew', 'lazy', 'pray', 'approval','branch','school','bedroom']

        # Determining problem length based on enemy
        if currentEnemy == gnome:
            problemLength = 1
        elif currentEnemy == elf:
            problemLength = 3
        elif currentEnemy == troll:
            problemLength = 7
        elif currentEnemy == orc:
            problemLength = 10
        elif currentEnemy == priest:
            problemLength = 13
        elif currentEnemy == wizard:
            problemLength = 16
        elif currentEnemy == dwarf:
            problemLength = 18
        elif currentEnemy == medusa:
            problemLength = 20

        # Creating the problem using a for loop to select random words from the list
        wordProblem = wordList[random.randint(0, len(wordList) - 1)]
        for i in range(problemLength):
            wordProblem += (" " + wordList[random.randint(0, len(wordList) - 1)])

        # Return the completed phrase
        return(wordProblem)

        # Run the main while loop


    print("Type the correct phrase to attack, type 'gold' to see your gold, type 'enemy' to select your enemy, or type 'quit' to exit.")
    running = True
    while running:

        # Generate the problem
        wordProblem = generateProblem(currentEnemy)

        # Accept input from player
        print(wordProblem)
        status = input("")

        # Check to see intent of player
        if status == wordProblem:
            currentEnemy.reduceHealth(damage)
            if currentEnemy.health <= 0:
                playerGold, currentEnemy = killEnemy(playerGold, currentEnemy)
        elif status == "gold":
            print("You have", playerGold, "gold.")
        elif status == "shop":
            shopText()
            playerGold, damage = shopFunction(playerGold, damage)
        elif status == "damage":
            print("You currently deal", damage, "damage per strike.")
        elif status == "enemy":
            currentEnemy = chooseEnemy()
        elif status == "quit":
            running = False


main()