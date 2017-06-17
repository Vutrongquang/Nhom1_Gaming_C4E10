import pygame

pixel = 64

class G4E:
    def __init__(self):
        pass

    def draw_image_center(self, object, screen):
        w = (pixel - object.image.get_width()) / 2 + object.x * 64
        h = (pixel - object.image.get_height()) / 2 + object.y * 64
        screen.blit(object.image, (w, h))

    def draw(self,screen):
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(self.map.image, (x * pixel, y * pixel))

        if len(self.creeps_right) != 0:
            for self.creep in self.creeps_right:
                self.draw_image_center(self.creep, screen)

        # if len(self.creeps_top) != 0:
        #     for self.creep in self.creeps_top:
        #         self.draw_image_center(self.creep, screen)
        #
        # if len(self.creeps_left) != 0:
        #     for self.creep in self.creeps_left:
        #         self.draw_image_center(self.creep, screen)
        #
        # if len(self.creeps_bot) != 0:
        #     for self.creep in self.creeps_bot:
        #         self.draw_image_center(self.creep, screen)
