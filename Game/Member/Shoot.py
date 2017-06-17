import pygame
k = 0
class Shoot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw_shoot(self, shoot):
        for self.shoot in shoot:
            self.shoot.move(1, 0)
            if self.shoot.x > self.map.width:
                self.shoots.append(self.shoot)
                self.shooted.remove(self.shoot)



        # if dx > 0 and dy == 0:
        #     for i in range(self.map.width):
        #         while self.shoot.x < self.map.x + 1:
        #             self.draw_shoot(dx + i, dy)
        # elif dx < 0 and dy == 0:
        #     for i in range(self.map.width):
        #         while self.shoot.x >= 0:
        #             self.draw_shoot(dx - i, dy)
        # elif dx == 0 and dy > 0:
        #     for i in range(self.map.height):
        #         while self.shoot.y < self.map.y + 1:
        #             self.draw_shoot(dx, dy + i)
        # elif dx == 0 and dy < 0:
        #     for i in range(self.map.height):
        #         while self.shoot.y >= 0:
        #             self.draw_shoot(dx, dy - i)