import pygame

from G4E import G4E
from Member.Map import Map
from Member.Map import Dest
from Member.Shoot import Shoot
from Member.Character import Character
from Member.Creep import Creep


g4e = G4E()
g4e.map = Map(10, 5)
g4e.character = Character(1, 1)
g4e.creep = Creep(10, 1)
g4e.shoot = Shoot(15, 15)
g4e.dests = [Dest(0, 0), Dest(0, 1), Dest(0, 2), Dest(0, 3), Dest(0, 4)]
pixel = 64

g4e.shoot.image = pygame.image.load("images/box.png")
g4e.creep.image = pygame.image.load("images/box.png")
g4e.character.image = pygame.image.load("images/pusher.png")
g4e.map.image = pygame.image.load("images/wall.png")
for dest in g4e.dests:
    dest.image = pygame.image.load("images/dest.png")


pygame.init()
screen = pygame.display.set_mode((640,320))
done = False
counter = 0
counter_shot = 0
k = 0
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            dx, dy = g4e.handle_input(event)
            if g4e.in_map(dx,dy):
                g4e.character.move(dx, dy)
            if event.key == pygame.K_SPACE:
                (g4e.shoot.x,g4e.shoot.y) = (g4e.character.x,g4e.character.y)

    counter += 1
    while counter > 100:
        g4e.creep.move_creep(-1,0)
        counter = 0
    counter_shot += 1
    while counter_shot > 10:
        g4e.shoot.move(1, 0)
        counter_shot = 0


    g4e.draw(screen)
    pygame.display.flip()