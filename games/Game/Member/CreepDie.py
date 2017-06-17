class CreepDie:
    def __init__(self, images, screen):
        self.images = images
        self.screen = screen
        self.current_img = 0
        self.time = 50
        self.counter_img_creep = 0
        self.active = True

    def draw(self, creepx, creepy):
        self.counter_img_creep += 1
        if self.counter_img_creep >= self.time:
            self.current_img += 1
            if self.current_img >= len(self.images):
                self.current_img = 0
                self.active = False
            self.counter_img_creep = 0

        if self.active:
            self.screen.blit(self.images[self.current_img], (creepx, creepy))