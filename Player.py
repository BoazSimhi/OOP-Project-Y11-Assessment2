class Player:
    def __init__(self, name: str, strength: int, wisdom: int, max_health: int, level: int, xp: int):
        self.name = name
        self.strength = strength
        self.wisdom = wisdom
        self.max_health = max_health
        self.level = level
        self.xp = xp
        current_health = max_health
    
    def attack(self, target):
        pass

    def rest(self):
        pass

    def display_stats(self):
        pass

    def level_up(self):
        pass

    def death(self):
        pass
