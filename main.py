import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        self.SCREEN = pygame.display.set_mode((width, height))
        self.SCREEN_BG = 'black'

        pygame.display.set_caption(title)

        self.CLOCK = MyClock(60)

        self.RESISTOR = Resistor(400, 150, (400, 200))

    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.SCREEN.fill(self.SCREEN_BG)

            self.RESISTOR.draw(self.SCREEN)

            pygame.display.update()
            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(800, 600, 'Resistor Color')
    game.run()