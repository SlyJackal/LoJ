from random import randrange, uniform, choice, triangular
class Character():
    '''Character generator'''
    def __init__(self, name):
        self.name = name
        self.base_health = randrange(40, 150)
        self.strength = randrange(10, 30)
        self.agile = round(uniform(0, 0.3), 2)
        self.level = 1
        self.health = self.base_health
        print(self.name)
        print('=======================')
        print(f'Strength - {self.strength}\nAgile    - {round(self.agile * 100)}%\nHealth   - {self.base_health}/{self.base_health}')
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

    def level_up(self):
        self.level += 1
        print(f'self.level = {self.level}')
        self.strength += randrange(1,5)
        self.agile += round(uniform(0, 0.05), 2)
        self.base_health += randrange(5,10)
        print('-------------------------------------------------')
        print(f'Your characteristics was upgraded:\nStrenght - {self.strength}\nAgile - {round(self.agile * 100)}%\nHealh - {self.base_health}')
        print('-------------------------------------------------')

    def elixir_upgrade(self, elixir_type = choice(['small', 'medium', 'big'])):
        if elixir_type == 'small':
            upgrade = uniform(0, 0.1)
            print(f'You find small bottle with something...')
        elif elixir_type == 'medium':
            upgrade = uniform(0.1, 0.2)
            print(f'You find medium bottle with something...')
        elif elixir_type == 'big':
            upgrade = uniform(0.2, 0.3)
            print(f'You find big bottle with something...')
        
        elixir_or_poison = randrange(1,10)
        if elixir_or_poison < 4:
            upgrade = upgrade * -1
            
        choice = input('What do you want to do with bottle:\n1 - Drink\n2 - Drop out\n') 
        if choice == '1':
            #update random characteristic
            random_characteristic = randrange(1,3)
            if random_characteristic == 1:
                self.base_health = round(self.base_health + self.base_health * upgrade)
                self.health = self.base_health
            elif random_characteristic == 2:
                self.strength = round(self.strength + self.strength * upgrade)
            elif random_characteristic == 3:
                self.agile = round(self.agile + self.agile * upgrade, 2)
            else:
                print("You drop the bottle. Fortune favours the brave, but it's not about you!")
                
            print('****************************************')
            print(f'Your characteristics:\nStrenght - {self.strength}\nAgile - {self.agile}\nHealh - {self.base_health}')
            print('****************************************')

    def change_position(self, side, position):
        if side == 'right':
            position = position + 1
        elif side == 'left':
            position = position - 1
        return position
        

if __name__ == "__main__":
    print("This is a module for character.")
    input("\n\nPress the enter key to exit.")

