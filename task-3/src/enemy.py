from random import randint

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