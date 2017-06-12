import pygame
from Member.Character import Character
from Member.map import Map
from Member.Dest import Dest
from Member.Shoot import Shoot

class G4E:
    def __init__(self):
        pass

    def draw(self,screen):
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(self.map.image,(x * pixel,y * pixel))
        for self.dest in self.dests:
            self.draw_image_center(self.dest, screen)
        self.draw_image_center(self.character,screen)

    def draw_image_center(self, object,screen):
        w = (pixel - object.image.get_width())/2 + object.x*64
        h = (pixel - object.image.get_height())/2 + object.y*64
        screen.blit(object.image,(w,h))

    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.key == pygame.K_RIGHT:
            dx = 1
            self.character.image = pygame.image.load("images/pusher_right.png")
        elif event.key == pygame.K_LEFT:
            dx = -1
            self.character.image = pygame.image.load("images/pusher_left.png")
        elif event.key == pygame.K_DOWN:
            dy = 1
            self.character.image = pygame.image.load("images/pusher.png")
        elif event.key == pygame.K_UP:
            dy = -1
            self.character.image = pygame.image.load("images/pusher_up.png")
        else:
            pass
        return dx,dy


g4e = G4E()
g4e.map = Map(10, 5)
g4e.character = Character(1, 1)
g4e.dests = [Dest(0,0),Dest(0,1),Dest(0,2),Dest(0,3),Dest(0,4)]
g4e.shoot = Shoot(1, 100)
pixel = 64

g4e.character.image = pygame.image.load("images/pusher.png")
g4e.map.image = pygame.image.load("images/wall.png")
for dest in g4e.dests:
    dest.image = pygame.image.load("images/dest.png")


pygame.init()
screen = pygame.display.set_mode((800,600))
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            dx, dy = g4e.handle_input(event)
            g4e.character.move(dx, dy)
    g4e.draw(screen)
    pygame.display.flip()
