import pygame

class Creep(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect.x =  x
        self.rect.y = y

    def checkCollision(self, shoot, creepGroup, screen):
        if pygame.sprite.spritecollide(shoot, creepGroup, False):
            self.draw_image_center(self.character, screen)


    def move_creep(self, dx, dy):
        self.x += dx
        self.y += dy