import pygame
from sys import exit
from classes import *

class Game:
    def __init__(self, width, height, title):
        pygame.init()

        self.SCREEN = pygame.display.set_mode((width, height))
        self.SCREEN_BG = 'Gray64'

        pygame.display.set_caption(title)

        self.CLOCK = MyClock(60)

        self.RESISTOR = Resistor(400, 150, (400, 200))

        x = self.RESISTOR.resistorRect.left - 100
        y = self.RESISTOR.resistorRect.bottom + 200

        colors = [
            ['Black', [0, 0, 0]],
            ['Brown', [160, 82, 45]],
            ['Red', [255, 0, 0]],
            ['Orange', [255, 165, 0]],
            ['Yellow', [255, 255, 0]],
            ['Green', [0, 255, 0]],
            ['Blue', [0, 0, 255]],
            ['Purple', [128, 0, 128]],
            ['Gray', [128, 128, 128]],
            ['White', [255, 255, 255]],
            ['Gold', [255, 215, 0]],
            ['Silver', [192, 192, 192]]
        ]

        self.colorBtn = []

        for i in range(0, 3):
            for j in range(0, 4):
                self.colorBtn.append( ColorButton(x, y, colors[i * 4 + j]) )
                x = x + self.colorBtn[i].rectWidth + 75
            x = self.RESISTOR.resistorRect.left - 100
            y = y + 100

        self.color = [1, 1, 1]

    def quit(self):
        pygame.quit()
        exit()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.SCREEN.fill(self.SCREEN_BG)

            self.RESISTOR.update(self.color)
            self.RESISTOR.draw(self.SCREEN)

            for btn in self.colorBtn:
                self.color = btn.update(self.color)
                btn.draw(self.SCREEN)

            pygame.display.update()
            self.CLOCK.tick()

if __name__ == '__main__':
    game = Game(800, 800, 'Resistor Color')
    game.run()