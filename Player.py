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
            print(f"You have defeated the {target.name}")
            xp_gain = round(uniform(0.5, 2) * target.difficulty)
            self.xp += xp_gain
            print(f"You gained {xp_gain} xp!")
            if self.xp >= self.level * 5:
                self.xp = 0
                self.level_up()
            else:
                print(f"You have {self.xp} out of {self.level * 5} required to level up.")
        
        else:
            print(f"{target.name} now has {target.current_health} health remaining.")


    def rest(self):
        self.current_health += self.wisdom


    def display_stats(self):
        print(f"{self.name}, Level {self.level}")
        print(f"Health: {self.current_health}/{self.max_health}")
        print(f"Strength: {self.strength}")
        print(f"Wisdom: {self.wisdom}")
        print(f"You have {self.xp} out of {self.level * 5} required to level up.")


    def level_up(self):
        print("You level up and heal to full health!")

        # LEVEL UP CODE

        self.display_stats()
        self.current_health = self.max_health


    def death(self):
        print("The enemy overpowered you,")
        print("Your blade clatters to the ground as you fall.")
        print("You have died.")
        print("\t\tGAME OVER")

