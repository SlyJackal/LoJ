from random import randrange

class World():
    def __init__(self):
        generate_map_size = randrange(12, 22)
        self.map = list(range(generate_map_size))
        self.clear_rooms = list()
        self.enemie_rooms = list()
        self.position = self.map[len(self.map)//2]
        self.clear_rooms.append(self.position)

    def visualistion(self):
        result = str()
        for i in range(len(self.map)):
            if i == self.map[0] or i == self.map[-1]:
                result += '_'
            elif i == self.position:
                result += 'V'
            elif i in self.clear_rooms:
                result += 'O'
            elif i in self.enemie_rooms:
                result += 'X'
            else:
                result += '#'
        print(result)

    def clear_room(self):
        self.clear_rooms = self.clear_rooms.append(self.position)
        if self.position in self.enemie_rooms:
            self.enemie_rooms.remove(self.position)
        return self.clear_rooms, self.enemie_rooms

    def with_enemy_room(self):
        self.enemie_rooms = self.enemie_rooms.append(self.position)
        return self.enemie_rooms
    

        

if __name__ == "__main__":
    print("This is a module for world creation.")
    input("\n\nPress the enter key to exit.")
