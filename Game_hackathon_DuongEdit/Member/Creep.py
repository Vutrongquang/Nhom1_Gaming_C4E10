class Creep:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health

    def draw_self(self):
        while self.creep.x < self.map.x + 1:
            for self.y in range (self.map.y):
                for self.x in range (self.map.x):
                    if self.x == self.creep.x and self.y == self.creep.y:
                        print(self.creep, end = "")
                    else:
                        print()
                print()
                self.creep.x +=1





    def move(self,dx, dy):
        self.x += dx
        self.y += dy






