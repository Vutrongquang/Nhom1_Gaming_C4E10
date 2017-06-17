import pygame

pixel = 64

class G4E:
    def __init__(self):
        pass

    def draw(self,screen):
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(self.map.image, (x * pixel, y * pixel))
        for self.dest in self.dests:
            self.draw_image_center(self.dest, screen)
        self.draw_image_center(self.character, screen)
        if len(self.creeps) != 0:
            for self.creep in self.creeps:
                self.draw_image_center(self.creep, screen)
        if len(self.shooted_left) != 0:
            for self.shoted in self.shooted_left:
                self.shoted.image = pygame.image.load("images/shoot_left.png")
                self.draw_image_center(self.shoted, screen)
        if len(self.shooted_right) != 0:
            for self.shoted in self.shooted_right:
                self.shoted.image = pygame.image.load("images/shoot.png")
                self.draw_image_center(self.shoted, screen)


    def draw_image_center(self, object,screen):
        w = (pixel - object.image.get_width())/2 + object.x*64
        h = (pixel - object.image.get_height())/2 + object.y*64
        screen.blit(object.image, (w, h))

    def in_map(self, dx, dy):
        if 1 <= self.character.x + dx < self.map.width and 0 <= self.character.y + dy < self.map.height:
            return True
        return False

    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.key == pygame.K_RIGHT:
            dx = 1
            self.a = 1
            self.character.image = pygame.image.load("images/character.png")
        elif event.key == pygame.K_LEFT:
            dx = -1
            self.a = -1
            self.character.image = pygame.image.load("images/character_left.png")
        elif event.key == pygame.K_DOWN:
            dy = 1

        elif event.key == pygame.K_UP:
            dy = -1

        else:
            pass

        return dx,dy
