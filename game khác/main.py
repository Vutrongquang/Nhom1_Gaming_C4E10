import pygame
import random


from g4e import G4E
from data.map import Map
from data.creep import Creep
from data.creep_top import CreepTop

g4e = G4E()
g4e.map = Map(12, 12)
g4e.creeps_right = []
# g4e.creeps_top = []
# g4e.creeps_left = []
# g4e.creeps_bot = []
g4e.creep_ingame = []
# g4e.creep_top_ingame = []
# g4e.creep_left_ingame = []
# g4e.creep_bot_ingame = []
for i in range(50):
    g4e.creeps_right.append(Creep(12, random.randint(4,8)))
    # g4e.creeps_top.append(CreepTop(random.randint(4, 8), 0))
    # g4e.creeps_left.append(Creep(random.randint(4, 8), 10))
    # g4e.creeps_bot.append(Creep(1, random.randint(4, 8)))




pygame.init()
screen = pygame.display.set_mode((800,800))
pixel = 64
done = False

g4e.map.image = pygame.image.load("images/wall.png")
for g4e.creep in g4e.creeps_right:
    g4e.creep.image = pygame.image.load("images/creep.png")
# for g4e.creep in g4e.creeps_top:
#     g4e.creep.image = pygame.image.load("images/creep.png")
# for g4e.creep in g4e.creeps_left:
#     g4e.creep.image = pygame.image.load("images/creep.png")
# for g4e.creep in g4e.creeps_bot:
#     g4e.creep.image = pygame.image.load("images/creep.png")

creep_speed = 0
creep_max_speed = 0
# creep_top_speed = 0
# creep_top_max_speed = 0
# creep_left_speed = 0
# creep_left_max_speed = 0
# creep_bot_speed = 0
# creep_bot_max_speed = 0
k = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    creep_speed += 1
    # if k <= 10:
    #     creep_max_speed = 200
    # elif 10 < k <= 20:
    #     creep_max_speed = 100
    # elif 20 < k <= 40:
    #     creep_max_speed = 50
    # k += 1
    while creep_speed > 50:
        g4e.creep_ingame.append(g4e.creeps_right[random.randint(1, len(g4e.creeps_right) - 1)])
        for g4e.creep_right in g4e.creep_ingame:
            g4e.creep.move_creep(-1, 0)
        creep_speed = 0



    # while creep_top_speed > creep_top_max_speed:
    #     g4e.creep_ingame_top.append(g4e.creeps_top[random.randint(1, len(g4e.creeps_top) - 1)])
    #     for g4e.creep_top in g4e.creep_ingame_top:
    #         g4e.creep_top.move_creep(0, 1)
    #     creep_top_speed = 0

    # while creep_left_speed > creep_left_max_speed:
    #     g4e.creep_ingame_left.append(g4e.creeps_left[random.randint(1, len(g4e.creeps_left) - 1)])
    #     for g4e.creep_left in g4e.creep_ingame_left:
    #         g4e.creep.move_creep(1, 0)
    #     creep_left_speed = 0
    # while creep_bot_speed > creep_bot_max_speed:
    #     g4e.creep_ingame_bot.append(g4e.creeps_bot[random.randint(1, len(g4e.creeps_bot) - 1)])
    #     for g4e.creep_bot in g4e.creep_ingame_bot:
    #         g4e.creep.move_creep(0, -1)
    #     creep_bot_speed = 0
    g4e.draw(screen)
    pygame.display.flip()