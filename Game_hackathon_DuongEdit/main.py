import pygame

from G4E import G4E
from Member.map import Map
from Member.Dest import Dest
from Member.Shoot import Shoot
from Member.Character import Character
from Member.gameviews import GameView
from Member.gamecontrollers import GameController


g4e = G4E()
g4e.map = Map(10, 5)
g4e.character = Character(1, 1)
g4e.dests = [Dest(0,0),Dest(0,1),Dest(0,2),Dest(0,3),Dest(0,4)]

pixel = 64

# g4e.shoot.image = pygame.image.load("images/box.png")
g4e.character.image = pygame.image.load("images/pusher.png")
g4e.map.image = pygame.image.load("images/wall.png")
for dest in g4e.dests:
    dest.image = pygame.image.load("images/dest.png")

counter = 0
pygame.init()
screen = pygame.display.set_mode((640,320))
done = False

g4e.shoot = Shoot(g4e.character.x, g4e.character.y)
g4e.shootview = GameView(pygame.image.load("images/box.png"), screen)
g4e.shoots = GameController(g4e.shoot, g4e.shootview)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            dx, dy = g4e.handle_input(event)
            if g4e.in_map(dx,dy):
                g4e.character.move(dx, dy)
            # if g4e.character.collide(g4e.dests, dx, dy):
            #     g4e.character.move(dx, dy)

    g4e.draw(screen)
    pygame.display.flip()