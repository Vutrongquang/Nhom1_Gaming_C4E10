import pygame
import random
from G4E import G4E
from member.map import *
from member.character import Character
from member.shoot import Shoot
from member.opposition import Opp


g4e = G4E()
g4e.map = Map(20,20)
g4e.wall_left = []
for i in range(6, 10):
    g4e.wall_left.append(Wall(6, i))
g4e.wall_right = []
for i in range(6, 10):
    g4e.wall_right.append(Wall(11, i))
g4e.wall_top = []
for i in range(7, 11):
    g4e.wall_top.append(Wall(i, 5))
g4e.wall_bottom = []
for i in range(7, 11):
    g4e.wall_bottom.append(Wall(i, 10))

g4e.character = Character(random.randint(7,9),random.randint(7,9))
g4e.shoots = []
for i in range(100):
    g4e.shoots.append(Shoot(30,30))
g4e.shoot_up = []
g4e.shoot_down = []
g4e.shoot_right = []
g4e.shoot_left = []
g4e.a = 0
g4e.b = 0

g4e.opp_right = []
g4e.oppingame_right = []
for i in range(50):
    g4e.opp_right.append(Opp(19, random.randint(6, 9)))
g4e.opp_left = []
g4e.oppingame_left = []
for i in range(50):
    g4e.opp_left.append(Opp(-1, random.randint(6, 9)))
g4e.opp_top = []
g4e.oppingame_top = []
for i in range(50):
    g4e.opp_top.append(Opp(random.randint(7, 10), -1))
g4e.opp_bottom = []
g4e.oppingame_bottom = []
for i in range(50):
    g4e.opp_bottom.append(Opp(random.randint(7, 10), 19))



g4e.character.image = pygame.image.load("images/character_up.png")
g4e.map.image = pygame.image.load("images/background.png")
for g4e.shoot in g4e.shoots:
    g4e.shoot.image = pygame.image.load("images/shoot.png")

for g4e.wall in g4e.wall_left:
    g4e.wall.image = pygame.image.load("images/wall_vertical.png")
for g4e.wall in g4e.wall_right:
    g4e.wall.image = pygame.image.load("images/wall_vertical.png")
for g4e.wall in g4e.wall_top:
    g4e.wall.image = pygame.image.load("images/wall.png")
for g4e.wall in g4e.wall_bottom:
    g4e.wall.image = pygame.image.load("images/wall.png")

for g4e.opp in g4e.opp_right:
    g4e.opp.image = pygame.image.load("images/opp.png")
for g4e.opp in g4e.opp_left:
    g4e.opp.image = pygame.image.load("images/opp.png")
for g4e.opp in g4e.opp_top:
    g4e.opp.image = pygame.image.load("images/opp.png")
for g4e.opp in g4e.opp_bottom:
    g4e.opp.image = pygame.image.load("images/opp.png")


pygame.init()
screen = pygame.display.set_mode((1152, 1152))
done = False
pixel = 64

shoot_speed = 0
opp_right_speed = 0
opp_left_speed = 0
opp_top_speed = 0
opp_bottom_speed = 0
g4e.a = 0
g4e.b = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            dx, dy = g4e.handle_input(event)
            if g4e.in_box(dx, dy):
                g4e.character.move(dx, dy)
            if event.key == pygame.K_SPACE:
                if g4e.a == 1:
                    (g4e.shoots[len(g4e.shoots) - 1].x, g4e.shoots[len(g4e.shoots) - 1].y) = (g4e.character.x + g4e.a, g4e.character.y)
                    g4e.shoot_right.append(g4e.shoots[len(g4e.shoots)-1])
                    g4e.shoots.pop()
                elif g4e.a == -1:
                    (g4e.shoots[len(g4e.shoots) - 1].x, g4e.shoots[len(g4e.shoots) - 1].y) = (g4e.character.x + g4e.a, g4e.character.y)
                    g4e.shoot_left.append(g4e.shoots[len(g4e.shoots)-1])
                    g4e.shoots.pop()
                elif g4e.b == 1:
                    (g4e.shoots[len(g4e.shoots) - 1].x, g4e.shoots[len(g4e.shoots) - 1].y) = (g4e.character.x , g4e.character.y + g4e.b)
                    g4e.shoot_down.append(g4e.shoots[len(g4e.shoots)-1])
                    g4e.shoots.pop()
                elif g4e.b == -1:
                    (g4e.shoots[len(g4e.shoots) - 1].x, g4e.shoots[len(g4e.shoots) - 1].y) = (g4e.character.x, g4e.character.y + g4e.b)
                    g4e.shoot_up.append(g4e.shoots[len(g4e.shoots)-1])
                    g4e.shoots.pop()
                else:
                    pass

    opp_right_speed += 1
    opp_left_speed += 1
    opp_top_speed += 1
    opp_bottom_speed += 1
    while opp_right_speed > random.randint(45,60):
        g4e.oppingame_right.append(g4e.opp_right[random.randint(1, len(g4e.opp_right)-1)])
        for g4e.opp in g4e.oppingame_right:
            g4e.opp.move(-1, 0)
        opp_right_speed = 0

    while opp_left_speed > random.randint(45,60):
        g4e.oppingame_left.append(g4e.opp_left[random.randint(1,len(g4e.opp_left)-1)])
        for g4e.opp in g4e.oppingame_left:
            g4e.opp.move(1, 0)
        opp_left_speed = 0

    while opp_top_speed > random.randint(45,60):
        g4e.oppingame_top.append(g4e.opp_top[random.randint(1,len(g4e.opp_top)-1)])
        for g4e.opp in g4e.oppingame_top:
            g4e.opp.move(0, 1)
        opp_top_speed = 0

    while opp_bottom_speed > random.randint(45,60):
        g4e.oppingame_bottom.append(g4e.opp_bottom[random.randint(1,len(g4e.opp_bottom)-1)])
        for g4e.opp in g4e.oppingame_bottom:
            g4e.opp.move(0, -1)
        opp_bottom_speed = 0

    shoot_speed += 1
    while shoot_speed >5:
        for g4e.shoot in g4e.shoot_right:
            g4e.shoot.move(1, 0)
            if g4e.shoot.x > g4e.map.width:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_right.remove(g4e.shoot)

        for g4e.shoot in g4e.shoot_left:
            g4e.shoot.move(-1, 0)
            if g4e.shoot.x < 0:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_left.remove(g4e.shoot)

        for g4e.shoot in g4e.shoot_up:
            g4e.shoot.move(0, -1)
            if g4e.shoot.y < 0:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_up.remove(g4e.shoot)

        for g4e.shoot in g4e.shoot_down:
            g4e.shoot.move(0, 1)
            if g4e.shoot.x > g4e.map.height:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_down.remove(g4e.shoot)

        shoot_speed = 0

    for g4e.shoot in g4e.shoot_right:
        for g4e.opp in g4e.oppingame_right:
            if g4e.shoot.x == g4e.opp.x and g4e.shoot.y == g4e.opp.y:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_right.remove(g4e.shoot)
                g4e.opp.x = 19
                g4e.opp.y = random.randint(6, 9)
                g4e.oppingame_right.remove(g4e.opp)

    for g4e.shoot in g4e.shoot_left:
        for g4e.opp in g4e.oppingame_left:
            if g4e.shoot.x == g4e.opp.x and g4e.shoot.y == g4e.opp.y:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_left.remove(g4e.shoot)
                g4e.opp.x = -1
                g4e.opp.y = random.randint(6, 9)
                g4e.oppingame_left.remove(g4e.opp)

    for g4e.shoot in g4e.shoot_up:
        for g4e.opp in g4e.oppingame_top:
            if g4e.shoot.x == g4e.opp.x and g4e.shoot.y == g4e.opp.y:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_up.remove(g4e.shoot)
                g4e.opp.x = random.randint(7, 10)
                g4e.opp.y = -1
                g4e.oppingame_top.remove(g4e.opp)

    for g4e.shoot in g4e.shoot_down:
        for g4e.opp in g4e.oppingame_bottom:
            if g4e.shoot.x == g4e.opp.x and g4e.shoot.y == g4e.opp.y:
                g4e.shoots.append(g4e.shoot)
                g4e.shoot_down.remove(g4e.shoot)
                g4e.opp.x = random.randint(7, 10)
                g4e.opp.y = 19
                g4e.oppingame_bottom.remove(g4e.opp)

    for g4e.wall in g4e.wall_right:
        for g4e.opp in g4e.oppingame_right:
            if g4e.wall.x == g4e.opp.x and g4e.wall.y == g4e.opp.y:
                g4e.oppingame_right.remove(g4e.opp)
                g4e.opp.x = -1
                g4e.opp.y = random.randint(7, 10)

    for g4e.wall in g4e.wall_left:
        for g4e.opp in g4e.oppingame_left:
            if g4e.wall.x == g4e.opp.x and g4e.wall.y == g4e.opp.y:
                g4e.oppingame_left.remove(g4e.opp)
                g4e.opp.x = 25
                g4e.opp.y = random.randint(7, 10)

    for g4e.wall in g4e.wall_top:
        for g4e.opp in g4e.oppingame_top:
            if g4e.wall.x == g4e.opp.x and g4e.wall.y == g4e.opp.y:
                g4e.oppingame_top.remove(g4e.opp)
                g4e.opp.x = random.randint(7, 10)
                g4e.opp.y = -25

    for g4e.wall in g4e.wall_bottom:
        for g4e.opp in g4e.oppingame_bottom:
            if g4e.wall.x == g4e.opp.x and g4e.wall.y == g4e.opp.y:
                g4e.oppingame_bottom.remove(g4e.opp)
                g4e.opp.x = random.randint(7, 10)
                g4e.opp.y = 25

    g4e.draw_map(screen)
    pygame.display.flip()