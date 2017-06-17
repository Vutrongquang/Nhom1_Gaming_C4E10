class Creep:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_creep(self, dx, dy):
        self.x += dx
        self.y += dy
