import readchar
import os
from random import randint, choice
from enum import Enum

def lose():
    os.system('clear')
    print(r"     ____    _    __  __ _____ ", end="\n")
    print(r"    / ___|  / \  |  \/  | ____|", end='\n')
    print(r"   | | __  / _ \ | |\/| |  _|  ", end='\n')
    print(r"   | |_\ \/ ___ \| |  | | |___ ", end='\n')
    print(r"    \____/_/   \_\_|__|_|_____|", end='\n')
    print(r"     / _ \ \   / / ____|  _ \  ", end='\n')
    print(r"    | | | \ \ / /|  _| | |_) | ", end='\n')
    print(r"    | |_| |\ V / | |___|  _ <  ", end='\n')
    print(r"     \___/  \_/  |_____|_| \_| ", end='\n')

def win():
    os.system('clear')
    print(r"   __        ______ _    _     ", end='\n')
    print(r"   \ \      / /____| |  | |    ", end='\n')
    print(r"    \ \ /\ / /  _| | |  | |    ", end='\n')
    print(r"     \ V  V /| |___| |__| |__  ", end='\n')
    print(r"    __\_/\_/_|_____|____|____| ", end='\n')
    print(r"   |  _ \ / _ \| \ | | ____| | ", end='\n')
    print(r"   | | | | | | |  \| |  _| | | ", end='\n')
    print(r"   | |_| | |_| | |\  | |___|_| ", end='\n')
    print(r"   |____/ \___/|_| \_|_____(_) ", end='\n')
    print(r"                ◯             ", end='\n')
    print(r"                ┃              ", end='\n')
    print(r"             ╱☉▔☉▔☉╲           ", end='\n')
    print(r"           ▕╲▏┓---┏▕╱▏         ", end='\n')
    print(r"          ╭╮╲┉╰━━━╯┉╱╭╮        ", end='\n')
    print(r"         ╭┛┣━╲ --- ╱━┫┗╮       ", end='\n')
    print(r"         ╰━┻━╮▔▔▔▔▔╭━┻━╯       ", end='\n')

class MAP_ENTRY_TYPE(Enum):
    MAP_EMPTY = 0,
    MAP_BLOCK = 1,

class WALL_DIRECTION(Enum):
    WALL_LEFT = 0,
    WALL_UP = 1,
    WALL_RIGHT = 2,
    WALL_DOWN = 3,

class Map():
    def __init__(self, width, height, x, y):
        self.start = (x, y)
        self.finish = (height-2, width-2)
        self.win_flag = 0
        self.lose_flag = 0
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def setMap(self, x, y, value):
        if value == MAP_ENTRY_TYPE.MAP_EMPTY:
            self.map[y][x] = 0
        elif value == MAP_ENTRY_TYPE.MAP_BLOCK:
            self.map[y][x] = 1

    def isMovable(self, x, y):
        return self.map[y][x] != 1

    def isValid(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        return True

    def showMap(map, hero, enemy):
        if hero.X == map.finish[0] and hero.Y == map.finish[1]:
            map.win_flag = 1

        for i in range(len(map.map)):
            for j in range(len(map.map[i])):
                enemy_flag = 0
                for k in range(len(enemy.enemy)):
                    if hero.X == enemy.enemy[k][1] and hero.Y == enemy.enemy[k][0]:
                        map.lose_flag = 1
                    if i == enemy.enemy[k][1] and j == enemy.enemy[k][0]:
                        print('O', end=' ')
                        enemy_flag = 1
                if map.lose_flag != 1 and map.win_flag != 1:
                    if i == hero.X and j == hero.Y:
                        print('X', end=' ')
                    elif i == map.finish[0] and j == map.finish[1]:
                        print('F', end=' ')
                    elif enemy_flag:
                        continue
                    elif map.map[i][j] == 1:
                        print('#', end=' ')
                    else:
                        print(' ', end=' ')
            print()

class Hero():
    def __init__(self, position):
        self.X = position[0]
        self.Y = position[1]

    # Movers
    def move_W(self, map):
        if map.map[self.X-1][self.Y] != 1:
            self.X -= 1
    def move_S(self, map):
        if map.map[self.X+1][self.Y] != 1:
            self.X += 1
    def move_A(self, map):
        if map.map[self.X][self.Y - 1] != 1:
            self.Y -= 1
    def move_D(self, map):
        if map.map[self.X][self.Y + 1] != 1:
            self.Y += 1

class Enemy():
    def __init__(self, m, count):
        resq = []

        while count:
            x = randint(int(m.width/10), int(m.width*9/10))
            y = randint(int(m.height/10), int(m.height*9/10))

            if m.map[y][x] != 1 and (y, x) != m.finish:
                resq.append((x, y))
                count -= 1

        self.enemy = resq
    def move_enemy(self, m):
        for i in range(len(self.enemy)):
            move_flag = 0
            while True:
                direct = randint(0, 3)
                x = self.enemy[i][0]
                y = self.enemy[i][1]
                if direct == 0 and m.map[y-1][x] == 0:
                    self.enemy[i] = (x, y-1)
                    break
                elif direct == 1 and m.map[y][x+1] == 0:
                    self.enemy[i] = (x+1, y)
                    break
                elif direct == 2 and m.map[y+1][x] == 0:
                    self.enemy[i] = (x, y+1)
                    break
                elif direct == 3 and m.map[y][x-1] == 0:
                    self.enemy[i] = (x-1, y)
                    break
                move_flag += 1
                if move_flag == 100:
                    break

# recursive division algorithm
def recursiveDivision(map, x, y, width, height, wall_value):
    # start must be a odd number, wall_index must be a even number
    def getWallIndex(start, length):
        assert length >= 3
        wall_index = randint(start + 1, start + length - 2)
        if wall_index % 2 == 1:
            wall_index -= 1
        return wall_index

    # must check adjacent entry of four margin entries,
    # if adjacent entry is movable, must set the margin entry as the hole
    def generateHoles(map, x, y, width, height, wall_x, wall_y):
        holes = []

        hole_entrys = [(randint(x, wall_x -1), wall_y), (randint(wall_x + 1, x + width -1), wall_y),
                        (wall_x, randint(y, wall_y -1)), (wall_x, randint(wall_y + 1, y + height - 1))]
        margin_entrys = [(x, wall_y), (x+width-1, wall_y), (wall_x, y), (wall_x, y + height-1)]
        adjacent_entrys = [(x-1, wall_y), (x+width, wall_y), (wall_x, y - 1), (wall_x, y + height)]
        for i in range(4):
            adj_x, adj_y = (adjacent_entrys[i][0], adjacent_entrys[i][1])
            if map.isValid(adj_x, adj_y) and map.isMovable(adj_x, adj_y):
                map.setMap(margin_entrys[i][0], margin_entrys[i][1], MAP_ENTRY_TYPE.MAP_EMPTY)
            else:
                holes.append(hole_entrys[i])

        ignore_hole = randint(0, len(holes)-1)
        for i in range(0, len(holes)):
            if i != ignore_hole:
                map.setMap(holes[i][0], holes[i][1], MAP_ENTRY_TYPE.MAP_EMPTY)

    if width <= 1 or height <= 1:
        return

    #generate a row and a column wall index, they must be even number
    wall_x, wall_y = (getWallIndex(x, width), getWallIndex(y, height))

    #set horizontal and vertical lines to wall
    for i in range(x, x+width):
        map.setMap(i, wall_y, wall_value)
    for i in range(y, y+height):
        map.setMap(wall_x, i, wall_value)

    #create three holes
    generateHoles(map, x, y, width, height, wall_x, wall_y)

    recursiveDivision(map, x, y, wall_x - x, wall_y - y, wall_value)
    recursiveDivision(map, x, wall_y + 1, wall_x - x, y + height - wall_y -1, wall_value)
    recursiveDivision(map, wall_x + 1, y, x + width - wall_x -1, wall_y - y, wall_value)
    recursiveDivision(map, wall_x + 1, wall_y + 1, x + width - wall_x -1, y + height - wall_y -1, wall_value)

def doRecursiveDivision(map):
    # draw four margin wall lines
    for x in range(0, map.width):
        map.setMap(x, 0, MAP_ENTRY_TYPE.MAP_BLOCK)
        map.setMap(x, map.height-1, MAP_ENTRY_TYPE.MAP_BLOCK)

    for y in range(0, map.height):
        map.setMap(0, y, MAP_ENTRY_TYPE.MAP_BLOCK)
        map.setMap(map.width-1, y, MAP_ENTRY_TYPE.MAP_BLOCK)

    recursiveDivision(map, 1, 1, map.width - 2, map.height - 2, MAP_ENTRY_TYPE.MAP_BLOCK)

def game():
    map = Map(21, 21, 1, 1)
    hero = Hero(map.start)
    doRecursiveDivision(map)
    enemy = Enemy(map, 4)
    map.showMap(hero, enemy)
    while True:
        c = str(readchar.readchar())
        if c == 'w':
            hero.move_W(map)
        elif c == 's':
            hero.move_S(map)
        elif c == 'a':
            hero.move_A(map)
        elif c == 'd':
            hero.move_D(map)
        else:
            break

        enemy.move_enemy(map)
        map.showMap(hero, enemy)

        if map.lose_flag == 1:
            lose()
            exit()
        if map.win_flag == 1:
            win()
            exit()

if __name__ == "__main__":
    game()
