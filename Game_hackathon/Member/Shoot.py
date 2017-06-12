class Shoot:
    def __init__(self, levelShoot, damageShoot):
        self.levelShoot = levelShoot
        self.damageShoot = damageShoot
        self.counter = 0

    def moveShoot(self, x, y):
        self.x = x
        self.y = y
