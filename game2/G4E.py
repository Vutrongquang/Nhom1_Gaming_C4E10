import pygame
pixel = 64

class G4E:
    def __init__(self):
        pass

    def draw_image_center(self, object,screen):
        w = (pixel - object.image.get_width())/2 + object.x*64
        h = (pixel - object.image.get_height())/2 + object.y*64
        screen.blit(object.image, (w, h))

    def draw_map(self, screen):
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(self.map.image, (x*pixel, y*pixel))
        self.draw_image_center(self.character, screen)
        for self.wall in self.wall_left:
            self.draw_image_center(self.wall, screen)
        for self.wall in self.wall_right:
            self.draw_image_center(self.wall, screen)
        for self.wall in self.wall_top:
            self.draw_image_center(self.wall, screen)
        for self.wall in self.wall_bottom:
            self.draw_image_center(self.wall, screen)
        if len(self.shoot_right) != 0:
            for self.shoot in self.shoot_right:
                self.shoot.image = pygame.image.load("images/shoot.png")
                self.draw_image_center(self.shoot, screen)
        if len(self.shoot_left) != 0:
            for self.shoot in self.shoot_left:
                self.shoot.image = pygame.image.load("images/shoot.png")
                self.draw_image_center(self.shoot, screen)
        if len(self.shoot_up) != 0:
            for self.shoot in self.shoot_up:
                self.shoot.image = pygame.image.load("images/shoot_vertical.png")
                self.draw_image_center(self.shoot, screen)
        if len(self.shoot_down) != 0:
            for self.shoot in self.shoot_down:
                self.shoot.image = pygame.image.load("images/shoot_vertical.png")
                self.draw_image_center(self.shoot, screen)
        if len(self.oppingame_right) != 0:
            for self.opp in self.oppingame_right:
                self.draw_image_center(self.opp, screen)
        if len(self.oppingame_left) != 0:
            for self.opp in self.oppingame_left:
                self.draw_image_center(self.opp, screen)
        if len(self.oppingame_top) != 0:
            for self.opp in self.oppingame_top:
                self.draw_image_center(self.opp, screen)
        if len(self.oppingame_bottom) != 0:
            for self.opp in self.oppingame_bottom:
                self.draw_image_center(self.opp, screen)

    def in_box(self, dx, dy):
        if 6 < self.character.x + dx < 11 and 5 < self.character.y + dy < 10:
            return True
        return False

    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.key == pygame.K_RIGHT:
            dx = 1
            self.a = 1
            self.b = 0
            self.character.image = pygame.image.load("images/character_right.png")
        elif event.key == pygame.K_LEFT:
            dx = -1
            self.a = -1
            self.b = 0
            self.character.image = pygame.image.load("images/character_left.png")
        elif event.key == pygame.K_UP:
            dy = -1
            self.a = 0
            self.b = -1
            self.character.image = pygame.image.load("images/character_up.png")
        elif event.key == pygame.K_DOWN:
            dy = 1
            self.a = 0
            self.b = 1
            self.character.image = pygame.image.load("images/character_down.png")
        else:
            pass

        return dx, dy