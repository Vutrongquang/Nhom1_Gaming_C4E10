import pygame
import random
import sys
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (243, 156, 18)
BLUE = (44, 62, 80)
GREY = (127, 140, 141)
PURPLE = (142, 68, 173)

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("images/character_down.png")
        self.rect = self.image.get_rect()

        self.rect.x = 480
        self.rect.y = 370

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.key == pygame.K_RIGHT:
            dx = 20
            self.a = 1
            self.b = 0
            self.image = pygame.image.load("images/character_right.png")
        elif event.key == pygame.K_LEFT:
            dx = -20
            self.a = -1
            self.b = 0
            self.image = pygame.image.load("images/character_left.png")
        elif event.key == pygame.K_UP:
            dy = -20
            self.a = 0
            self.b = -1
            self.image = pygame.image.load("images/character_up.png")
        elif event.key == pygame.K_DOWN:
            dy = 20
            self.a = 0
            self.b = 1
            self.image = pygame.image.load("images/character_down.png")
        else:
            pass
        return dx, dy

    # kiem tra co o trong box khong
    def in_box(self, list1, list2, list3, list4, dx, dy):
        for left in list1:
            for right in list2:
                for top in list3:
                    for bottom in list4:
                        if left.rect.x  < self.rect.x + dx < right.rect.x - 30 and top.rect.y < self.rect.y + dy < bottom.rect.y - 30:
                            return True
        return False


class Creep_Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Bullet_vertical(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([6, 10])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Bullet_horizontal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([10, 6])
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect()

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Creep(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

    def update(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

class Wall_vertical(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

class Wall_horizontal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40, 10])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

def dectectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2+ w2 >= x1 > x2 and y2+h2 >= y1 >= y2):
        return True
    elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1 >= y2):
        return True
    elif (x2+w2 >= x1 >= x2 and y2+h2 >= y1+h1 >= y2):
        return True
    elif (x2+w2 >= x1+w1 >= x2 and y2+h2 >= y1+h1 >= y2):
        return True
    else:
        return False



character = Character()
# bullet
bullet_right_list = pygame.sprite.Group()
bullet_left_list = pygame.sprite.Group()
bullet_up_list = pygame.sprite.Group()
bullet_down_list = pygame.sprite.Group()
# Wall
all_walls = pygame.sprite.Group()
wall_left_list = pygame.sprite.Group()
wall_top_list = pygame.sprite.Group()
wall_bottom_list = pygame.sprite.Group()
wall_right_list = pygame.sprite.Group()
# Creep
creep_right_list = pygame.sprite.Group()
creep_left_list = pygame.sprite.Group()
creep_top_list = pygame.sprite.Group()
creep_bottom_list = pygame.sprite.Group()
# Creep Boss
creep_boss_1 = pygame.sprite.Group()
creep_boss_2 = pygame.sprite.Group()
creep_boss_3 = pygame.sprite.Group()
creep_boss_4 = pygame.sprite.Group()
creep_boss_bottom = pygame.sprite.Group()
# All sprites
all_sprites = pygame.sprite.Group()


# Ve tuong ben trai
for i in range(4):
    wall = Wall_vertical()
    wall.rect.x = 410
    wall.rect.y = 300 + i * 40
    all_walls.add(wall)
    wall_left_list.add(wall)
    all_sprites.add(wall)

# Ve tuong ben tren
for i in range(4):
    wall = Wall_horizontal()
    wall.rect.x = 410 + i * 40
    wall.rect.y = 300
    all_walls.add(wall)
    wall_top_list.add(wall)
    all_sprites.add(wall)

# Ve tuong ben duoi
for i in range(4):
    wall = Wall_horizontal()
    wall.rect.x = 410 + i * 40
    wall.rect.y = 460
    all_walls.add(wall)
    wall_bottom_list.add(wall)
    all_sprites.add(wall)

# Ve tuong ben phai
for i in range(4):
    wall = Wall_vertical()
    wall.rect.x = 560
    wall.rect.y = 300 + i * 40
    all_walls.add(wall)
    wall_right_list.add(wall)
    all_sprites.add(wall)

all_sprites.add(character)

pygame.init()
screen = pygame.display.set_mode([1000, 800])
myfont = pygame.font.SysFont("8BIT WONDER", 30)
level1 = pygame.image.load("images/level1.png")
level2 = pygame.image.load("images/level2.png")
level = "Level 1"
# set a,b de tim huong dan
character.a = 0
character.b = 0
# set time print creep
time_creep_right = 0
time_creep_left = 0
time_creep_top = 0
time_creep_bottom = 0
# set speed of creeps
print_creep_right = True
speed_creep_right = 0
print_creep_left = True
speed_creep_left = 0
print_creep_top = True
speed_creep_top = 0
speed_creep_bottom = 0
#set speed of creels boss
speed_boss_2 = 0
speed_boss_1 = 0
speed_boss_3 = 0
speed_boss_4 = 0

# these lists is for last boss
boss4_top = pygame.sprite.Group()
boss4_left = pygame.sprite.Group()
boss4_right = pygame.sprite.Group()
boss4_bottom = pygame.sprite.Group()
distance = 0
k = 0
h = 0
i = 0
j = 0
random_sight = 0

#set va cham wall
wall_right_collide = 0
wall_left_collide = 0
wall_top_collide = 0
wall_bottom_collide = 0

count = 0
count_wall = 0
score = 0
done = False
began = True
time_began = 0
shot_boss = 0
shot_boss4 = 0
boss1_on = False
boss2_on = False
boss3_on = False
boss4_on = False

check_win = False
check_win_image = pygame.image.load("images/win.png")
check_lose = False
check_lose_image = pygame.image.load("images/lose.png")

screen_image = pygame.image.load("images/Ready.png")

while not done:
    # sound
    def Sound(filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()


    while began:
        screen.blit(screen_image, (0, 0))
        pygame.display.flip()
        time.sleep(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                began = False
            if event.type == pygame.KEYDOWN:
                Sound("sound/open_battle.wav")
                began = False

    # Khoi tao list creep di tu ben phai
    while not began:
        if print_creep_right:
            time_creep_right += 1
            while time_creep_right >= 2000:
                for i in range(2):
                    creep = Creep()
                    creep.rect.x = random.randint(1000, 1050)
                    creep.rect.y = random.randint(320, 420)
                    creep_right_list.add(creep)
                    all_sprites.add(creep)
                time_creep_right = 0

        # Huong dan
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                dx, dy = character.handle_input(event)
                if character.in_box(wall_left_list, wall_right_list, wall_top_list, wall_bottom_list, dx, dy):
                    character.move(dx, dy)
                if event.key == pygame.K_SPACE:
                    if character.a == 1:
                        # Neu nhan vat quay ve ben phai thi them dan vao list dan phai
                        bullet = Bullet_horizontal()
                        (bullet.rect.x, bullet.rect.y) = (character.rect.x+40, character.rect.y+17)
                        bullet_right_list.add(bullet)
                        all_sprites.add(bullet)
                        Sound("sound/bullet.wav")
                    elif character.a == -1:
                        # Neu nhan vat quay ve ben trai thi them dan vao list dan trai
                        bullet = Bullet_horizontal()
                        (bullet.rect.x, bullet.rect.y) = (character.rect.x, character.rect.y + 17)
                        bullet_left_list.add(bullet)
                        all_sprites.add(bullet)
                        Sound("sound/bullet.wav")
                    elif character.b == 1:
                        # Neu nhan vat quay xuong duoi thi them dan vao list dan ben duoi
                        bullet = Bullet_vertical()
                        (bullet.rect.x, bullet.rect.y) = (character.rect.x + 17, character.rect.y + 40)
                        bullet_down_list.add(bullet)
                        all_sprites.add(bullet)
                        Sound("sound/bullet.wav")
                    elif character.b == -1:
                        # Neu nhan vat quay len tren thi them dan vao list dan ben tren
                        bullet = Bullet_vertical()
                        (bullet.rect.x, bullet.rect.y) = (character.rect.x + 17, character.rect.y)
                        bullet_up_list.add(bullet)
                        all_sprites.add(bullet)
                        Sound("sound/bullet.wav")

        # Di chuyen creep tu ben phai vao
        speed_creep_right += 1
        while speed_creep_right >= 200:
            for creep in creep_right_list:
                creep.update(-5, 0)
            speed_creep_right = 0


        #  Xu li va cham giua list dan ben phai va creep, moi khi va cham creep thi score + them 1, creep boss + 5
        for bullet in bullet_right_list:
            bullet.update(1, 0)
            creep_right_hit_list = pygame.sprite.spritecollide(bullet, creep_right_list, True)
            for creep in creep_right_hit_list:
                bullet_right_list.remove(bullet)
                all_sprites.remove(bullet)
                count += 1
                score += 1
                Sound("sound/creep_remove.wav")
            for boss in boss4_right:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, boss.rect.x, boss.rect.y, boss.rect.width, boss.rect.height):
                    bullet_right_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss4 += 1
                    Sound("sound/collide.wav")
                if shot_boss4 >= 40:
                    check_win = True
                    boss4_right.remove(boss)
                    all_sprites.remove(boss)
                    Sound("sound/boss_remove.wav")
            for creep in creep_boss_1:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, creep.rect.x, creep.rect.y, creep.rect.width, creep.rect.height):
                    bullet_right_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss += 1
                    Sound("sound/collide.wav")
                if shot_boss >= 10:
                    creep_boss_1.remove(creep)
                    all_sprites.remove(creep)
                    print_creep_right = True
                    shot_boss = 0
                    count += 3
                    score += 3
                    Sound("sound/boss_remove.wav")
                    level = "Level 2"
                    screen_image = pygame.image.load("images/level2.png")
                    Sound("sound/next_level.wav")
                    began = True


            # Xu li dan bay ra khoi man hinh
            if bullet.rect.y > 1000:
                bullet_right_list.remove(bullet)
                all_sprites.remove(bullet)


        # boss lv1
        if count == 10:
            count += 1
            boss1_on = True
        if boss1_on:
            Sound("sound/boss_start.wav")
            print_creep_right = False
            creep_boss = Creep_Boss()
            creep_boss.rect.x = random.randint(1000, 1050)
            creep_boss.rect.y = random.randint(320, 340)
            creep_boss_1.add(creep_boss)
            all_sprites.add(creep_boss)
            boss1_on = False


        # Boss di chuyen tu ben phai
        speed_boss_1 += 1
        while speed_boss_1 >= 200:
            for creep_boss in creep_boss_1:
                # creep_boss.rect.y = random.randint(320, 360)
                creep_boss.update(-5, 0)
            speed_boss_1 = 0

        # Khi score lon hon 12 thi them creep phia ben trai
        if count >= 14:
            if print_creep_left:
                time_creep_left += 1
                while time_creep_left >= 2000:
                    for j in range(2):
                        creep = Creep()
                        creep.rect.x = random.randint(-50, 0)
                        creep.rect.y = random.randint(320, 420)
                        creep_left_list.add(creep)
                        all_sprites.add(creep)
                    time_creep_left = 0

        # Di chuyen creep tu trai vao
        speed_creep_left += 1
        while speed_creep_left >= 100:
            for creep in creep_left_list:
                creep.update(+5, 0)
            speed_creep_left = 0

        # Khi score lon hon 20 thi them boss tu ben trai di vao
        if count == 25:
            count += 1
            boss2_on = True
            print_creep_left = False
            print_creep_right = False
        if boss2_on:
            Sound("sound/boss_start.wav")
            creep_boss = Creep_Boss()
            creep_boss.rect.x = random.randint(-50, 0)
            creep_boss.rect.y = random.randint(320, 420)
            creep_boss_2.add(creep_boss)
            all_sprites.add(creep_boss)
            boss2_on = False

        # Boss di chuyen tu ben trai
        speed_boss_2 += 1
        while speed_boss_2 >= 100:
            for creep_boss in creep_boss_2:
                creep_boss.rect.y = random.randint(320, 420)
                creep_boss.update(5, 0)
            speed_boss_2 = 0

        # Xu li va cham giua creep va list dan ben trai, moi khi ban trung creep thi score lai cong them 1, creep boss + 5
        for bullet in bullet_left_list:
            bullet.update(-1, 0)
            creep_left_hit_list = pygame.sprite.spritecollide(bullet, creep_left_list, True)
            for creep in creep_left_hit_list:
                bullet_left_list.remove(bullet)
                all_sprites.remove(bullet)
                count += 1
                score += 1
                Sound("sound/creep_remove.wav")
            for boss in creep_boss_2:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, boss.rect.x, boss.rect.y, boss.rect.width, boss.rect.height):
                    bullet_left_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss += 1
                    Sound("sound/collide.wav")
                if shot_boss >= 20:
                    creep_boss_2.remove(boss)
                    all_sprites.remove(boss)
                    print_creep_left = True
                    print_creep_right = True
                    shot_boss = 0
                    count += 3
                    score += 3
                    Sound("sound/boss_remove.wav")
                    level = "Level 3"
                    screen_image = pygame.image.load("images/level3.png")
                    Sound("sound/next_level.wav")
                    began = True

            for boss in boss4_left:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, boss.rect.x, boss.rect.y, boss.rect.width, boss.rect.height):
                    bullet_left_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss4 += 1
                    Sound("sound/collide.wav")
                if shot_boss4 >= 40:
                    Sound("sound/boss_remove.wav")
                    boss4_left.remove(boss)
                    all_sprites.remove(boss)
                    check_win = True


            if bullet.rect.y < 0:
                bullet_left_list.remove(bullet)
                all_sprites.remove(bullet)

        # Khi score lon hon 30 thi them creep tu ben tren va ben duoi
        if count > 30:
            if print_creep_top:
                time_creep_top += 1
                while time_creep_top >= 2000:
                    creep = Creep()
                    creep.rect.x = random.randint(420, 540)
                    creep.rect.y = random.randint(-50, 0)
                    creep_top_list.add(creep)
                    all_sprites.add(creep)
                    time_creep_top = 0

                time_creep_bottom += 1
                while time_creep_bottom >= 2000:
                    creep = Creep()
                    creep.rect.x = random.randint(420, 540)
                    creep.rect.y = random.randint(800, 850)
                    creep_bottom_list.add(creep)
                    all_sprites.add(creep)
                    time_creep_bottom = 0

        #  di chuyen creep tu ben tren xuong
        speed_creep_top += 1
        while speed_creep_top >= 200:
            for creep in creep_top_list:
                creep.update(0, 5)
            speed_creep_top = 0

        # Khi score lon hon 30 thi them boss tu ben tren di vao
        if count == 40:
            count += 1
            boss3_on = True

        if boss3_on:
            Sound("sound/boss_start.wav")
            print_creep_top = False
            print_creep_right = False
            print_creep_left = False
            for i in range(2):
                creep_boss = Creep_Boss()
                creep_boss.rect.x = random.randint(350, 570)
                creep_boss.rect.y = random.randint(800, 850)
                creep_boss_3.add(creep_boss)
                all_sprites.add(creep_boss)
            boss3_on = False

        # Boss di chuyen tu ben tren
        speed_boss_3 += 1
        while speed_boss_3 >= 100:
            for creep_boss in creep_boss_3:
                creep_boss.rect.x = random.randint(350, 570)
                creep_boss.update(0, -5)
            speed_boss_3 = 0


        # di chuyen creep tu duoi len
        speed_creep_bottom += 1
        while speed_creep_bottom >= 300:
            for creep in creep_bottom_list:
                creep.update(0, -5)
            speed_creep_bottom = 0

        # xu li va cham giua bullet va creep ben duoi, khi ban trung thi score + 1
        for bullet in bullet_down_list:
            bullet.update(0, 1)
            creep_bottom_hit_list = pygame.sprite.spritecollide(bullet, creep_bottom_list, True)
            for creep in creep_bottom_hit_list:
                bullet_down_list.remove(bullet)
                all_sprites.remove(bullet)
                count += 1
                score += 1
                Sound("sound/creep_remove.wav")
            for boss in creep_boss_3:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, boss.rect.x, boss.rect.y, boss.rect.width, boss.rect.height):
                    bullet_down_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss += 1
                    Sound("sound/collide.wav")
                if shot_boss >= 10:
                    creep_boss_3.remove(boss)
                    all_sprites.remove(boss)
                    shot_boss = 0
                    Sound("sound/boss_remove.wav")
                    if len(creep_boss_3) == 0:
                        print_creep_top = True
                        print_creep_left = True
                        print_creep_right = True
                        count += 5
                        score += 5

                        level = "Level 4"
                        Sound("sound/next_level.wav")
                        screen_image = pygame.image.load("images/level4.png")
                        began = True

            for boss in boss4_bottom:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, boss.rect.x, boss.rect.y, boss.rect.width, boss.rect.height):
                    bullet_left_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss4 += 1
                    Sound("sound/collide.wav")
                if shot_boss4 >= 40:
                    Sound("sound/boss_remove.wav")
                    boss4_bottom.remove(boss)
                    all_sprites.remove(boss)
                    check_win = True
            if bullet.rect.x > 800:
                bullet_down_list.remove(bullet)
                all_sprites.remove(bullet)

        # xu li va cham giua bullet va creep ben tren, khi ban trung thi score + 1
        for bullet in bullet_up_list:
            bullet.update(0, -1)
            creep_top_hit_list = pygame.sprite.spritecollide(bullet, creep_top_list, True)
            for creep in creep_top_hit_list:
                bullet_up_list.remove(bullet)
                all_sprites.remove(bullet)
                count += 1
                score += 1
                Sound("sound/creep_remove.wav")
            for boss in boss4_top:
                if dectectCollisions(bullet.rect.x, bullet.rect.y, bullet.rect.width, bullet.rect.height, boss.rect.x, boss.rect.y, boss.rect.width, boss.rect.height):
                    bullet_left_list.remove(bullet)
                    all_sprites.remove(bullet)
                    shot_boss4 += 1
                    Sound("sound/collide.wav")
                if shot_boss4 >= 40:
                    Sound("sound/boss_remove.wav")
                    boss4_top.remove(boss)
                    all_sprites.remove(boss)
                    check_win = True

            if bullet.rect.x < 0:
                bullet_up_list.remove(bullet)
                all_sprites.remove(bullet)

        if 60 <= count <= 70:
            count += 15
            boss4_on = True

        if boss4_on:
            Sound("sound/boss_start.wav")
            print_creep_right = False
            print_creep_left = False
            print_creep_top = False
            boss = Creep_Boss()
            boss.image = pygame.Surface([40, 40])
            boss.image.fill(PURPLE)
            boss.rect = boss.image.get_rect()
            boss.rect.x = random.randint(425, 540)
            boss.rect.y = 0
            boss4_top.add(boss)
            all_sprites.add(boss)
            boss4_on = False


        # Xu li toan bo thong tin ve con boss cuoi
        speed_boss_4 += 1
        while speed_boss_4 > 50:
            if len(boss4_top) != 0:
                for boss in boss4_top:
                    boss.rect.x = random.randint(425, 540)
                    boss.update(0, 2)
                    distance = 300 - boss.rect.y
                    if distance <= 40:
                        Sound("sound/collide_wall.wav")
                        check_lose = True
                    random_sight = random.randint(1, 3)
                    if k >= 5:
                        if random_sight == 1:
                            boss.rect.x = distance + 560
                            boss.rect.y = random.randint(320, 420)
                            boss4_right.add(boss)
                            boss4_top.remove(boss)
                            k = 0
                            distance = 0
                        elif random_sight == 2:
                            boss.rect.x = 410 - distance
                            boss.rect.y = random.randint(320, 420)
                            boss4_left.add(boss)
                            boss4_top.remove(boss)
                            k = 0
                            distance = 0

                        elif random_sight == 3:
                            boss.rect.y = 460 + distance
                            boss.rect.x = random.randint(425, 540)
                            boss4_bottom.add(boss)
                            boss4_top.remove(boss)
                            k = 0
                            distance = 0
                    k += 1
            if len(boss4_right) != 0:
                for boss in boss4_right:
                    boss.rect.y = random.randint(320, 420)
                    boss.update(-2, 0)
                    distance = boss.rect.x - 560
                    if distance <= 10:
                        Sound("sound/collide_wall.wav")
                        check_lose = True
                    h += 1
                    random_sight = random.randint(1, 3)
                    if h >= 5:
                        if random_sight == 1:
                            boss.rect.x = 410 - distance
                            boss.rect.y = random.randint(320, 420)
                            boss4_left.add(boss)
                            boss4_right.remove(boss)
                            h = 0
                            distance = 0
                        elif random_sight == 2:
                            boss.rect.y = distance
                            boss.rect.x = random.randint(425, 540)
                            boss4_top.add(boss)
                            boss4_right.remove(boss)
                            h = 0
                            distance = 0
                        elif random_sight == 3:
                            boss.rect.y = 460 + distance
                            boss.rect.x = random.randint(425, 540)
                            boss4_bottom.add(boss)
                            boss4_right.remove(boss)
                            h = 0
                            distance = 0

            if len(boss4_left) != 0:
                for boss in boss4_left:
                    boss.rect.y = random.randint(320, 420)
                    boss.update(2, 0)
                    distance = 410 - boss.rect.x
                    if distance <= 40:
                        Sound("sound/collide_wall.wav")
                        check_lose = True
                    i += 1
                    random_sight = random.randint(1, 3)
                    if i >= 5:

                        if random_sight == 1:
                            boss.rect.x = 560 + distance
                            boss.rect.y = random.randint(320, 420)
                            boss4_right.add(boss)
                            boss4_left.remove(boss)
                            i = 0
                            distance = 0
                        elif random_sight == 2:
                            boss.rect.y = 300 - distance
                            boss.rect.x = random.randint(425, 540)
                            boss4_top.add(boss)
                            boss4_left.remove(boss)
                            i = 0
                            distance = 0
                        elif random_sight == 3:
                            boss.rect.y = 460 + distance
                            boss.rect.x = random.randint(425, 540)
                            boss4_bottom.add(boss)
                            boss4_right.remove(boss)
                            i = 0
                            distance = 0


            if len(boss4_bottom) != 0:
                for boss in boss4_bottom:
                    boss.rect.x = random.randint(425, 540)
                    boss.update(0, -2)
                    distance = boss.rect.y - 460
                    if distance <= 5:
                        Sound("sound/collide_wall.wav")
                        check_lose = True
                    random_sight = random.randint(1, 3)
                    j += 1
                    if j >= 5:
                        if random_sight == 1:
                            boss.rect.x = distance + 560
                            boss.rect.y = random.randint(320, 420)
                            boss4_right.add(boss)
                            boss4_bottom.remove(boss)
                            j = 0
                            distance = 0
                        elif random_sight == 2:
                            boss.rect.x = 410 - distance
                            boss.rect.y = random.randint(320, 420)
                            boss4_left.add(boss)
                            boss4_bottom.remove(boss)
                            j = 0
                            distance = 0

                        elif random_sight == 3:
                            boss.rect.y = 300 - distance
                            boss.rect.x = random.randint(425, 540)
                            boss4_top.add(boss)
                            boss4_bottom.remove(boss)
                            j = 0
                            distance = 0

            speed_boss_4 = 0
        #   End moving boss part



        # xu li creep + boss va vao wall ben phai, dang lam remove wall o day
        for wall in wall_right_list:
            wall_creep_right_collide_list = pygame.sprite.spritecollide(wall, creep_right_list, True)
            wall_creep_boss_right_collide_list = pygame.sprite.spritecollide(wall, creep_boss_1, True)
            for creep in wall_creep_right_collide_list:
                # if dectectCollisions(wall.rect.x, wall.rect.y, wall.rect.width, wall.rect.height, creep.rect.x, creep.rect.y, creep.rect.width, creep.rect.height):
                creep_right_list.remove(creep)
                all_sprites.remove(creep)
                count_wall += 1
                Sound("sound/collide_wall.wav")
                # wall_right_collide += 1
                # if wall_right_collide >= 5:
                #     wall_right_list.remove(wall)
                #     all_sprites.remove(wall)
            for creep_boss in wall_creep_boss_right_collide_list:
                Sound("sound/collide_wall.wav")
                count_wall += 10
                creep_boss_1.remove(creep_boss)

            # for boss in boss4_right:
            #     Sound("sound/collide_wall.wav")
            #     if boss.rect.x - 40 <= 560:
            #         count_wall += 10
            #         boss4_right.remove(boss)
            #         all_sprites.remove(boss)
            #         check_lose = True

        #xu li creep + boss va vao wall ben trai
        for wall in wall_left_list:
            wall_creep_left_collide_list = pygame.sprite.spritecollide(wall, creep_left_list, True)
            wall_creep_boss_left_collide_list = pygame.sprite.spritecollide(wall, creep_boss_2, True)
            for creep in wall_creep_left_collide_list:
                creep_left_list.remove(creep)
                count_wall += 1
                Sound("sound/collide_wall.wav")
            for creep_boss in wall_creep_boss_left_collide_list:
                creep_boss_2.remove(creep_boss)
                count_wall += 10
                Sound("sound/collide_wall.wav")

            # for boss in boss4_left:
            #     Sound("sound/collide_wall.wav")
            #     if boss.rect.x + 80 > 410:
            #         count_wall += 10
            #         boss4_left.remove(boss)
            #         all_sprites.remove(boss)
            #         check_lose = True

        #xu li creep + boss va vao wall bottom
        for wall in wall_bottom_list:
            wall_creep_bottom_collide_list = pygame.sprite.spritecollide(wall, creep_bottom_list, True)
            wall_creep_boss_bottom_collide_list = pygame.sprite.spritecollide(wall, creep_boss_3, True)
            for creep in wall_creep_bottom_collide_list:
                creep_bottom_list.remove(creep)
                all_sprites.remove(creep)
                count_wall += 1
                Sound("sound/collide_wall.wav")
            for creep_boss in wall_creep_boss_bottom_collide_list:
                creep_boss_3.remove(creep_boss)
                count_wall += 10
                Sound("sound/collide_wall.wav")
            # for boss in boss4_bottom:
            #     Sound("sound/collide_wall.wav")
            #     if boss.rect.y - 40 <= 460:
            #         count_wall += 10
            #         boss4_bottom.remove(boss)
            #         all_sprites.remove(boss)
            #         check_lose = True

        #  xu li va cham giua creep top va wall top
        for wall in wall_top_list:
            wall_creep_top_collide_list = pygame.sprite.spritecollide(wall, creep_top_list, True)
            for creep in wall_creep_top_collide_list:
                creep_top_list.remove(creep)
                all_sprites.remove(creep)
                count_wall += 1
                Sound("sound/collide_wall.wav")
            # for boss in boss4_top:
            #     Sound("sound/collide_wall.wav")
            #     if boss.rect.y + 40 >= 300:
            #         count_wall += 10
            #         boss4_top.remove(boss)
            #         all_sprites.remove(boss)
            #         check_lose = True

        if count_wall >= 3:
            for wall in all_walls:
                wall.image.fill(GREY)
        if count_wall >= 5:
            for wall in all_walls:
                # wall_right_list.remove(wall)
                all_walls.remove(wall)
                all_sprites.remove(wall)
                Sound("sound/end_battle.wav")
            check_lose = True

        # khi score = 300, end game
        if count >= 300:
            check_win = True


        screen.fill(WHITE)
        all_sprites.draw(screen)
        leveltext = myfont.render(level, 1, BLACK)
        screen.blit(leveltext, (10, 10))
        if check_lose:
            screen.blit(check_lose_image, (0, 0))
        if check_win:
            screen.blit(check_win_image, (0, 0))
        # Hien thi diem neu muon :))
        scoretext = myfont.render("Score = " + str(score), 1, BLACK)
        screen.blit(scoretext, (10, 40))
        pygame.display.flip()