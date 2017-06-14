import pygame
class GameController:
    def __init__(self, shoot, gameview):
        self.shoot = shoot
        self.gameview = gameview
        self.counter = 0

    def draw(self):
        self.gameview.draw(self.shoot)

    def move(self, dx, dy):
        self.shoot.move(dx, dy)
