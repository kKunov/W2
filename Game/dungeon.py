from types import *
from hero import Hero
from orc import Orc


class Dungeon:

    def __init__(self, file_path):
        self.file_path = file_path
        self.orc_player = 0
        self.hero_player = 0
        self.orc = 0
        self.hero = 0
        self.the_map = []
        self.copy_map()

    def copy_map(self):
        file = open(self.file_path, "r")
        for index, line in enumerate(file):
            self.the_map.append([])
            for index2, symbol in enumerate(line):
                if symbol != '\n':
                    self.the_map[index].append(symbol)
        file.close()

    def print_map(self):
        for line in self.the_map:
            print("".join(line))
        return True

    def spawn(self, player_name, entity):
        for index, line in enumerate(self.the_map):
            for index2, symbol in enumerate(line):
                if (symbol == "S" and isinstance(entity, Hero)
                        and self.hero_player == 0):
                    self.hero_player = player_name
                    self.hero = entity
                    self.the_map[index][index2] = "H"
                    self.print_map()
                    return True
                elif (symbol == "S" and isinstance(entity, Orc)
                        and self.orc_player == 0):
                    self.orc_player = player_name
                    self.orc = entity
                    self.the_map[index][index2] = "O"
                    self.print_map()
                    return True
        return False

    def swap(self, a, b):
        c = a
        a = b
        b = c

    def move(self, player_namem, direction):
        directions_move = [0, 0]
        if direction == "right":
            directions_move[1] = 1
        elif direction == "left":
            directions_move[1] = -1
        elif direction == "up":
            directions_move[0] = -1
        elif direction == "down":
            directions_move[1] = 1
        else:
            print ("Error: Invalid direction!!!")
        if player_namem == orc_player:
            possition_index = [0, 0]
            for index, line in enumerate(self.the_map):
                for index2, symbol in enumerate(line):
                    if symbol == O:
                        possition_index[0] = [index]
                        possition_index[1] = [index2]
            new_pos_i = [possition_index[0] + directions_move[0]], [possition_index[0] + directions_move[1]]
            swap(the_map[possition_index[0]][possition_index[1]], the_map[new_pos_i[0], new_pos_i[1]])
