import pygame
import random

from G4E import G4E
from Member.map import Map
from Member.map import Dest
from Member.Shoot import Shoot
from Member.Character import Character
from Member.Creep import Creep


g4e = G4E()
g4e.map = Map(10, 5)
g4e.character = Character(1, 1)
g4e.creep = []
for i in range(10):
    g4e.creep.append(Creep(random.randint(10, 0),random.randint(10, 4)) )
# g4e.shoots = [Shoot(15, 15), Shoot(15, 15), Shoot(15, 15),
#               Shoot(15, 15), Shoot(15, 15), Shoot(15, 15),
#               Shoot(15, 15), Shoot(15, 15), Shoot(15, 15),
#               Shoot(15, 15), Shoot(15, 15), Shoot(15, 15),
#              ]
g4e.dests = [Dest(0, 0), Dest(0, 1), Dest(0, 2), Dest(0, 3), Dest(0, 4)]
pixel = 64

g4e.creep.image = pygame.image.load("images/box.png")
g4e.character.image = pygame.image.load("images/pusher.png")
g4e.map.image = pygame.image.load("images/wall.png")
for dest in g4e.dests:
    dest.image = pygame.image.load("images/dest.png")
# for g4e.shoot in g4e.shoot:
#     g4e.shoot.image = pygame.image.load("images/box.png")

g4e.shooted = []



pygame.init()
screen = pygame.display.set_mode((640,320))
g4e.shootGroup = pygame.sprite.Group()
g4e.shootSingle = pygame.sprite.GroupSingle()
g4e.creepSingle = pygame.sprite.GroupSingle()

done = False
counter = 0
counter_shot = 0
i = 1

# def startgame():
#     g4e.shootPath = ['images/dest.png', 'images/dest1.png']
#     for i in range(3):
#         g4e.shootPath = g4e.shootPath[random.randrange(0, len(g4e.shootPath))]
#         g4e.shootSpeed = [random.randrange(1, 8), 0]
#         g4e.shoot = Shoot(g4e.shootPath, g4e.shootSpeed)
#         g4e.shootGroup.add(g4e.shoot)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            dx, dy = g4e.handle_input(event)
            if g4e.in_map(dx, dy):
                g4e.character.move(dx, dy)
            # if event.key == pygame.K_SPACE:
            #     (g4e.shoot[len(g4e.shoot)-1].x, g4e.shoot[len(g4e.shoot)-1].y) = (g4e.character.x, g4e.character.y)
            #     g4e.shooted.append(g4e.shoot[len(g4e.shoot)-1])
            #     g4e.shoot.pop()
    for shoot in g4e.shootGroup:
        g4e.creep.checkCollision(g4e.shoot, g4e.creepSingle, screen)

    counter += 1
    while counter > 100:
        g4e.creep.move_creep(-1,0)
        counter = 0

    counter_shot += 1
    while counter_shot >50:
        for g4e.shoot in g4e.shooted:
            g4e.shoot.move(i, 0)
            if g4e.shoot.x > g4e.map.width+1:
                g4e.shoots.append(g4e.shoot)
                g4e.shooted.remove(g4e.shoot)

        counter_shot = 0
    # startgame()
    g4e.draw(screen)
    pygame.display.flip()
startgame()