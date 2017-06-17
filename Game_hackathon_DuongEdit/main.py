import pygame

from G4E import G4E
from Member.map import Map
from Member.map import Dest
from Member.Shoot import Shoot
from Member.Character import Character
from Member.Creep import Creep


g4e = G4E()
g4e.map = Map(10, 5)
g4e.character = Character(1, 1)
g4e.dests = [Dest(0,0),Dest(0,1),Dest(0,2),Dest(0,3),Dest(0,4)]
g4e.creeps = [Creep(9,4, 50, 1), Creep(9,1,20,3),]
pixel = 64

# g4e.shoot.image = pygame.image.load("images/box.png")
g4e.character.image = pygame.image.load("images/pusher.png")
g4e.map.image = pygame.image.load("images/wall.png")
for creep in g4e.creeps:
    creep.image = pygame.image.load("images/Creep.png")
for dest in g4e.dests:
    dest.image = pygame.image.load("images/dest.png")


pygame.init()
screen = pygame.display.set_mode((640,320))
done = False

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
                g4e.shoot = Shoot(g4e.character.x, g4e.character.y)
                g4e.shoot.moveShoot(dx, dy)

    g4e.draw(screen)
    pygame.display.flip()