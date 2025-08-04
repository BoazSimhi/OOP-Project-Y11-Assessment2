class Enemy:
    def __init__(self, name: str, strength: int, max_health: int, difficulty: int):
        self.name = name
        self.strength = strength
        self.max_health = max_health
        self.current_health = max_health
        self.difficulty = difficulty


    def attack(self, target):
        print(f"{self.name} dealt {self.strength} damage!\n")
        target.current_health -= self.strength
        if target.current_health <= 0:
            target.death()
        else:
            target.display_stats()

