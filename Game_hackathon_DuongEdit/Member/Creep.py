import pygame

class Creep(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    def move_creep(self, dx, dy):
        self.x += dx
        self.y += dy

        def checkCollision(self, creep, creepSingle):
            if pygame.sprite.Spritecollide(creep, creepSingle, False):
                self.draw_shoot(self.character, screen)