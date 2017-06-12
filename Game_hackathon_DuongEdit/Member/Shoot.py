import pygame
class Shoot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw_shoot(self, dx, dy):
        self.shoot.move(dx, dy)
        # g4e.draw_image_center(g4e.shoot, screen)

    def moveShoot(self, dx, dy):

        if dx > 0 and dy == 0:
            for i in range(self.map.width):
                while self.shoot.x < self.map.x + 1:
                    self.draw_shoot(dx + i, dy)
        elif dx < 0 and dy == 0:
            for i in range(self.map.width):
                while self.shoot.x >= 0:
                    self.draw_shoot(dx - i, dy)
        elif dx == 0 and dy > 0:
            for i in range(self.map.height):
                while self.shoot.y < self.map.y + 1:
                    self.draw_shoot(dx, dy + i)
        elif dx == 0 and dy < 0:
            for i in range(self.map.height):
                while self.shoot.y >= 0:
                    self.draw_shoot(dx, dy - i)