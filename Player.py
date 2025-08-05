from os import system
from random import uniform

class Player:
    def __init__(self, name: str, strength: int, wisdom: int, max_health: int):
        self.name = name
        self.strength = strength
        self.wisdom = wisdom
        self.max_health = max_health
        self.level = 1
        self.xp = 0
        self.current_health = max_health
        self.display_stats


    def attack(self, target):
        target.current_health -= self.strength
        print(f"You dealt {self.strength} damage")
        if target.current_health <= 0:
            if target.name == "King of Thanes":
                input(f"You have defeated the {target.name}! The world bows before you.\n~ ")
                input("Thanks for playing!\n~ ")
                exit()
            print(f"You have defeated the {target.name}")
            xp_gain = round(uniform(0.5, 2) * target.difficulty)
            self.xp += xp_gain
            print(f"You gained {xp_gain} xp!")
            if self.xp >= self.level * 4:
                self.xp = 0
                self.level_up()
            else:
                print(f"\nYou have {self.xp} out of {self.level * 5} required to level up.")
                input("~ ")
        
        else:
            print(f"{target.name} now has {target.current_health} health remaining.\n")


    def rest(self):
        if self.current_health + self.wisdom >= self.max_health:
            print(f"\nFeeling already quite rested, you only heal {self.max_health - self.current_health} health")
            self.current_health = self.max_health
        else:
            print(f"You rest and heal {self.wisdom} health")
            self.current_health += self.wisdom
        print(f"You are now on {self.current_health}/{self.max_health} health\n")


    def display_stats(self):
        print(f"\n{self.name}, Level {self.level}")
        print(f"Health: {self.current_health}/{self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Wisdom: {self.wisdom}")


    def level_up(self):
        system('clear')
        print("\nYou level up, your max health increases by 2, and you heal to full health!")
        print(f"You are now level {self.level}")

        self.max_health += 2
        self.level += 1
        while True:
            stat_increase = input(f"Which stat would you like to increase?\ns: Strength ({self.strength} +1), w: Wisdom ({self.wisdom} +5), or m: Max Health ({self.max_health} +5)\n> ").lower()
            if stat_increase == "s":
                self.strength += 1
                break
            elif stat_increase == "w":
                self.wisdom += 5
                break
            elif stat_increase == "m":
                self.max_health += 5
                break
            else:
                print("Not a valid option.")

        
        self.current_health = self.max_health
        print("Your stats have increased!")
        self.display_stats()



    def death(self):
        print("\nThe enemy overpowered you,")
        print("Your blade clatters to the ground as you fall.")
        input("You have died.\n~ ")
        print("\n\t\tGAME OVER\n")
        exit()

