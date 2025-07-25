class Enemy:
    def __init__(self, name: str, strength: int, max_health: int, difficulty: int):
        self.name = name
        self.strength = strength
        self.max_health = max_health
        current_health = max_health
        self.difficulty = difficulty


    def attack(self, target):
        print(f"{self.name} attacks!")
        print(f"{self.name} dealt {self.damage} damage!")
        target.current_health -= self.damage
        if target.current_health <= 0:
            target.death()
        else:
            target.display_stats()


#    def death(self, xp_receiver):
#        pass
