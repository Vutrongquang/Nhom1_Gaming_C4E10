import pygame

class Game:
    def __init__(self):
        pass

    def draw(self):
        while self.character.x < self.map.x+1:
            for self.y in range(self.map.y):
                for self.x in range(self.map.x):
                    if self.x == self.character.x and self.y == self.character.y:
                        print(" * ", end="")
                    else:
                        print(" - ", end="")
                print()
            print()
            self.character.x += 1


class Member:
    def __init__(self, x ,y):
        self.x = x
        self.y = y


game = Game()

game.character = Member(1,1)

game.map = Member(10,5)

game.draw()