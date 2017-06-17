class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.images_character = []
        self.images_character.append("images/c1.gif")
        self.images_character.append("images/c2.gif")
        self.images_character.append("images/c3.gif")
        self.images_character.append("images/c4.gif")
        self.images_character.append("images/c5.gif")
        self.images_character.append("images/c6.gif")
        self.images_character.append("images/c7.gif")
        self.images_character.append("images/c8.gif")
        self.images_character.append("images/c9.gif")
        self.images_character.append("images/c10.gif")
        self.images_character.append("images/c11.gif")
        self.images_character.append("images/c12.gif")
        self.images_character.append("images/c13.gif")
        self.images_character.append("images/c14.gif")
        self.images_character.append("images/c15.gif")
        self.images_character.append("images/c16.gif")



    def move(self, dx, dy):
        self.x += dx
        self.y += dy


