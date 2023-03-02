from random import randrange, uniform

class Enemie():
    def __init__(self, char_level = 1):
        self.base_health = randrange(40, 150) + randrange(5,10) * char_level
        self.strength = randrange(10, 30) + randrange(1,5) * char_level
        self.agile = round(uniform(0, 0.3), 2) + round(uniform(0, 0.05), 2) * char_level
        self.health = self.base_health
        print('=======================')
        print(f'Strength - {self.strength}\nAgile - {round(self.agile * 100)}%\nHealth - {self.base_health}/{self.base_health}')
        print('=======================')

    def attack(self):
        out_attack = round(self.strength + self.strength * uniform(-0.2, 0.2) + self.strength * uniform(0, self.agile))
        return out_attack

    def get_damage(self, income_damage):
        unluck = round(uniform(0, 1), 2)
        if self.agile > unluck:
            get_damage = 0
        elif self.agile == unluck:
            get_damage = income_damage // 2
        else:
            get_damage = income_damage - income_damage * uniform(0, self.agile)
        self.health = self.health - get_damage
        return self.health
 
if __name__ == "__main__":
    print("This is a module for enemies.")
    input("\n\nPress the enter key to exit.")
