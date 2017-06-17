import pygame
import random

from G4E import G4E
from Member.Map import Map
from Member.Map import Dest
from Member.Shoot import Shoot
from Member.Character import Character
from Member.Creep import Creep
from Member.Map import Lose

# Khoi tao cac doi tuong
g4e = G4E()
g4e.map = Map(10, 5)

g4e.character = Character(1, 1)

g4e.lose = Lose()
g4e.creeps = []
g4e.creepingame = []
for i in range(50):
    g4e.creeps.append(Creep(10, random.randint(0,4)))

g4e.shooted = []
g4e.oldshoot = []
g4e.shoots = []
for i in range(50):
    g4e.shoots.append(Shoot(15,15))

g4e.dests = [Dest(0, 0), Dest(0, 1), Dest(0, 2), Dest(0, 3), Dest(0, 4)]
pixel = 64

# Xu li phan hinh anh co ban
for g4e.creep in g4e.creeps:
    g4e.creep.image = pygame.image.load("images/creep.png")
g4e.character.image = pygame.image.load("images/character.png")
g4e.map.image = pygame.image.load("images/Wall_Black.png")
g4e.lose.image = pygame.image.load("images/S2e16_You_lose.png")
for dest in g4e.dests:
    dest.image = pygame.image.load("images/dest.png")
for g4e.shoot in g4e.shoots:
    g4e.shoot.image = pygame.image.load("images/shoot.png")




pygame.init()
screen = pygame.display.set_mode((640,320))
done = False

pygame.mixer.music.load("helicopter.wav")
pygame.mixer.music.play(-1)

creep_speed = 0
creep_max_speed = 0
shoot_speed = 0
shoot_max_speed = 25
lose = False
k = 0



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            dx, dy = g4e.handle_input(event)
            if g4e.in_map(dx, dy):
                g4e.character.move(dx, dy)
            if event.key == pygame.K_SPACE:
                (g4e.shoots[len(g4e.shoots)-1].x, g4e.shoots[len(g4e.shoots)-1].y) = (g4e.character.x + 1, g4e.character.y )
                g4e.shooted.append(g4e.shoots[len(g4e.shoots)-1])
                g4e.shoots.pop()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("shoot_gun.wav")
                pygame.mixer.music.play(1)

        creep_speed += 1
    if k <= 10:
        creep_max_speed = 200
    elif 10 < k <= 20:
        creep_max_speed = 100
    elif 20 < k <=40:
        creep_max_speed = 50
    while creep_speed > creep_max_speed:
        g4e.creepingame.append(g4e.creeps[random.randint(1, len(g4e.creeps)-1)])
        for g4e.creep in g4e.creepingame:
            g4e.creep.move_creep(-1, 0)
            if g4e.creep.x < 0:
                g4e.creep.x = 10
                g4e.creep.y = random.randint(0,4)
                g4e.creepingame.remove(g4e.creep)

        creep_speed = 0

    shoot_speed += 1
    while shoot_speed > shoot_max_speed:
        for g4e.shoot in g4e.shooted:
            g4e.shoot.move(1, 0)

            if g4e.shoot.x > g4e.map.width+1:
                g4e.shoots.append(g4e.shoot)
                g4e.shooted.remove(g4e.shoot)
        shoot_speed = 0

    for g4e.creep in g4e.creepingame:
        for g4e.shoot in g4e.shooted:
            if g4e.shoot.x == g4e.creep.x and g4e.shoot.y == g4e.creep.y:
                g4e.creep.x = 10
                g4e.creep.y = random.randint(0,4)
                g4e.creepingame.remove(g4e.creep)
                g4e.shoots.append(g4e.shoot)
                g4e.shooted.remove(g4e.shoot)
                k += 1

    for g4e.dest in g4e.dests:
        for g4e.creep in g4e.creepingame:
            if g4e.creep.x == g4e.dest.x and g4e.dest.y == g4e.creep.y:
                g4e.dests.remove(g4e.dest)
                g4e.creep.x = 10
                g4e.creep.y = random.randint(0, 4)
                g4e.creepingame.remove(g4e.creep)
            if g4e.creep.x == g4e.character.x and g4e.creep.y == g4e.character.y:
                print("you lose")
                lose = True

    # if len(g4e.dests) == 0:
    #     done = True

    g4e.draw(screen)
    if lose:
        g4e.lose1(screen)

    pygame.display.flip()