import pygame
import random
import sys
PURPLE = (142, 68, 173)
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()

bullet = Bullet()
print(bullet.rect.width)

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([40, 40])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


boss_list = pygame.sprite.Group()
boss_top = pygame.sprite.Group()
boss_right = pygame.sprite.Group()
boss_left = pygame.sprite.Group()
boss_bottom = pygame.sprite.Group()
boss = Boss()
boss.rect.x = random.randint(425, 540)
boss.rect.y = random.randint(-50, 0)
boss_top.add(boss)

pygame.init()
screen = pygame.display.set_mode([1000, 800])
myfont = pygame.font.SysFont("8BIT WONDER", 30)
done = False

time_print_boss = 0
speed_boss = 0
k = 0
h = 0
j = 0
i = 0
random_sight = 0
distance = 0
test = True

while not done:
    if test:
        screen.fill((0, 0, 0))
        presstext = myfont.render("Press any key to begin...", 1, (255, 255, 255))
        screen.blit(presstext, (100, 100))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                test = False
    while not test:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        speed_boss += 1

        while speed_boss > 200:
            for boss in boss_top:
                boss.rect.x = random.randint(425, 540)
                boss.update(0, 5)
                distance = 300 - boss.rect.y
                random_sight = random.randint(1, 3)
                if k >= 10:
                    if random_sight == 1:
                        boss.rect.x = distance + 560
                        boss.rect.y = random.randint(320, 420)
                        boss_right.add(boss)
                        boss_top.remove(boss)
                        k = 0
                    elif random_sight == 2:
                        boss.rect.x = 410 - distance
                        boss.rect.y = random.randint(320, 420)
                        boss_left.add(boss)
                        boss_top.remove(boss)
                        k = 0

                    elif random_sight == 3:
                        boss.rect.y = 460 + distance
                        boss.rect.x = random.randint(425, 540)
                        boss_bottom.add(boss)
                        boss_top.remove(boss)
                        k = 0
                k += 1
            for boss in boss_right:
                boss.rect.y = random.randint(320, 420)
                boss.update(-5, 0)
                distance = boss.rect.x - 560
                h += 1
                random_sight = random.randint(1, 3)
                if h >= 10:
                    if random_sight == 1:
                        boss.rect.x = 410 - distance
                        boss.rect.y = random.randint(320, 420)
                        boss_left.add(boss)
                        boss_right.remove(boss)
                        h = 0
                    elif random_sight == 2:
                        boss.rect.y = distance
                        boss.rect.x = random.randint(425, 540)
                        boss_top.add(boss)
                        boss_right.remove(boss)
                        h = 0
                    elif random_sight == 3:
                        boss.rect.y = 460 + distance
                        boss.rect.x = random.randint(425, 540)
                        boss_bottom.add(boss)
                        boss_right.remove(boss)
                        h = 0


            for boss in boss_left:
                boss.rect.y = random.randint(320, 420)
                boss.update(5, 0)
                distance = 410 - boss.rect.x
                i += 1
                random_sight = random.randint(1, 3)
                if i >= 10:

                    if random_sight == 1:
                        boss.rect.x = 560 + distance
                        boss.rect.y = random.randint(320, 420)
                        boss_right.add(boss)
                        boss_left.remove(boss)
                        i = 0
                    elif random_sight == 2:
                        boss.rect.y = 300 - distance
                        boss.rect.x = random.randint(425, 540)
                        boss_top.add(boss)
                        boss_left.remove(boss)
                        i = 0
                    elif random_sight == 3:
                        boss.rect.y = 460 + distance
                        boss.rect.x = random.randint(425, 540)
                        boss_bottom.add(boss)
                        boss_right.remove(boss)
                        i = 0

            for boss in boss_bottom:
                boss.rect.x = random.randint(425, 540)
                boss.update(0, -5)
                distance = boss.rect.y - 460
                random_sight = random.randint(1, 3)
                j += 1
                if j >= 10:
                    if random_sight == 1:
                        boss.rect.x = distance + 560
                        boss.rect.y = random.randint(320, 420)
                        boss_right.add(boss)
                        boss_bottom.remove(boss)
                        j = 0
                    elif random_sight == 2:
                        boss.rect.x = 410 - distance
                        boss.rect.y = random.randint(320, 420)
                        boss_left.add(boss)
                        boss_bottom.remove(boss)
                        j = 0

                    elif random_sight == 3:
                        boss.rect.y = 300 - distance
                        boss.rect.x = random.randint(425, 540)
                        boss_top.add(boss)
                        boss_bottom.remove(boss)
                        j = 0

            speed_boss = 0

        print(boss.rect.x, boss.rect.y)
        screen.fill((255, 255, 255))
        boss_top.draw(screen)
        boss_right.draw(screen)
        boss_left.draw(screen)
        boss_bottom.draw(screen)
        pygame.display.flip()