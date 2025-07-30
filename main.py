from os import system
from random import choice
from Player import Player
from Enemy import Enemy

system('clear')

# Prints a cool title
print(''' ________                        ___  _____           __        __ 
/_  __/ /  ___ ____  ___   ___  / _/ / ___/__  __ _  / /  ___ _/ /_
 / / / _ \/ _ `/ _ \/ -_) / _ \/ _/ / /__/ _ \/  ' \/ _ \/ _ `/ __/
/_/ /_//_/\_,_/_//_/\__/  \___/_/   \___/\___/_/_/_/_.__/\_,_/\__/ 
                                                                   \n\n''')

# Instantiating the player object
your_name = str(input("What is your name, dear Thane?\n> "))
Thane = Player(your_name, 4, 2, 10)

# Instantiate all the enemy objects
# Name, Strength, Max_Health, Difficulty

enemies_raw = [
    ["Rat", 1, 2, 1], ["Goblin", 2, 5, 1], ["Ooze", 1, 5, 1],
    ["Spider", 3, 4, 2], ["Bandit", 3, 6, 2], ["Gnoll", 4, 5, 2],
    ["Skeleton", 4, 9, 3], ["Shaman", 4, 8, 3],
    ["Fey", 4, 10, 4], ["Wolf", 7, 4, 4],
    ["Orc", 6, 12, 5], ["Wisp", 5, 10, 5], ["Cultist", 6, 9, 5],
    ["Wraith", 6, 13, 6], ["Boar", 6, 12, 6],
    ["Acolyte", 6, 13, 7], ["Serpent", 7, 12, 7],
    ["Imp", 7, 13, 8], ["Specter", 6, 14, 8],
    ["Elemental", 6, 14, 9],
    ["Berserker", 9, 17, 10], ["Golem", 8, 18, 10], ["Minotaur", 8, 16, 10],
    ["Wraith", 9, 17, 11],
    ["Troll", 7, 14, 12],
    ["Lich", 11, 22, 13], ["Manticore", 10, 20, 13],
    ["Demon", 11, 21, 14], ["Basilisk", 12, 20, 14],
    ["Giant", 12, 23, 15], ["Cyclops", 12, 22, 15],
    ["Colossus", 13, 26, 16], ["Banshee", 12, 25, 16],
    ["Djinn", 14, 27, 17], ["Chimera", 15, 26, 17],
    ["Wyvern", 16, 29, 18], ["Celestial", 15, 28, 18], ["Assassin", 16, 27, 18],
    ["Titan", 18, 32, 19], ["Primordial", 17, 30, 19],
    ["Dragon", 20, 35, 20], ["Archdemon", 22, 38, 20],
    ["King of Thanes", 51, 51, 21]
]

Enemy_list = []

for name, strength, max_health, difficulty in enemies_raw:
    Enemy_list.append(Enemy(name, strength, max_health, difficulty))

Thane.display_stats()

input("Are you ready for trials of Combat?\n~ ")

# The main game loop
while True:
    system('clear')
    #current_enemy = Enemy_list[1] # FOR TESTING
    while True:
        current_enemy = choice(Enemy_list)
        if current_enemy.difficulty <= Thane.level and Thane.level - current_enemy.difficulty <= 3:
            break
    
    print(f"\nYou are now fighting {current_enemy.name}!")

    while True:
        while True:
            move = input("what would you like to do? (a: attack, r: rest)\n> ").lower()
            if move == "a":
                Thane.attack(current_enemy)
                break
            elif move == "r":
                if Thane.current_health == Thane.max_health:
                    print("You are already fully rested.")
                else:
                    Thane.rest()
                    break
            else:
                print("Invalid choice.")
            
        if current_enemy.current_health <= 0:
            break

        input(f"The {current_enemy.name} now attacks!\n~ ")
        current_enemy.attack(Thane)


