class Enemy:
    def __init__(self, name: str, strength: int, max_health: int, difficulty: int):
        self.name = name
        self.strength = strength
        self.max_health = max_health
        current_health = max_health
        self.difficulty = difficulty
    
    def attack(self, target):
        pass

    def death(self, xp_receiver):
        pass
