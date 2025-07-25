from os import system
from random import choice
from Player import Player
from Enemy import Enemy

print("Hi!")

system('clear')

print("yo")

Thane = Player("Hero Guy", 4, 2, 10)
Rat = Enemy("Rat", 1, 2, 1)
Goblin = Enemy("Goblin", 2, 5, 1)
Enemy_list = [Goblin, Rat]

while True:
    current_enemy = choice(Enemy_list)
    Thane.attack(current_enemy)
    pass

