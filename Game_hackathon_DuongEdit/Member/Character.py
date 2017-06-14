class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    #
    # def collide(self, object, dx, dy):
    #     if self.x + dx == object.x and self.y + dy == object.y:
    #         return True
    #     else:
    #         return False


