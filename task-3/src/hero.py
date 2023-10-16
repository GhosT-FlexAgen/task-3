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