class GameView:
    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def draw(self, gamemodel):

        self.screen.blit(self.image, (gamemodel.x, gamemodel.y))
