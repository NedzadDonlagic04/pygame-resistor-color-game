import pygame

class MyClock:
    def __init__(self, fps):
        self.FPS = fps
        self.CLOCK = pygame.time.Clock()
    
    def tick(self):
        self.CLOCK.tick(self.FPS)

class Resistor:
    def __init__(self, rectWidth, rectHeight, pos, color=[234, 182, 118]):
        self.resistorImg = pygame.Surface((rectWidth, rectHeight), pygame.SRCALPHA)
        pygame.draw.rect(self.resistorImg, color, (0, 0, rectWidth, rectHeight), border_radius=10)
        self.resistorRect = self.resistorImg.get_rect( center = pos )

        self.halfWidth = rectWidth / 2
        self.lineColor = (192, 192, 192)

        self.resistorParts = [
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 30, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height },
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 100, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height},
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 200, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height},
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 300, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height},
        ]

    def update(self, color):
        leftClick = pygame.mouse.get_pressed()[0]

        if leftClick:
            mousePos = pygame.mouse.get_pos()
            for part in self.resistorParts:
                if mousePos[0] >= part['x'] and mousePos[0] <= part['x'] + part['width'] and mousePos[1] >= part['y'] and mousePos[1] <= part['y'] + part['height']:
                    part['color'] = color
                    break
                

    def draw(self, screen):
        screen.blit(self.resistorImg, self.resistorRect)

        for part in self.resistorParts:
            pygame.draw.rect(screen, part['color'], (part['x'], part['y'], part['width'], part['height']))

        pygame.draw.line(screen, self.lineColor, (self.resistorRect.left - 150, self.resistorRect.centery), (self.resistorRect.left, self.resistorRect.centery), 20)
        pygame.draw.line(screen, self.lineColor, (self.resistorRect.right + 150, self.resistorRect.centery), (self.resistorRect.right, self.resistorRect.centery), 20)

class ColorButton:
    def __init__(self, x, y, color):
        self.rectWidth = 100
        self.rectHeight = 50

        self.x = x
        self.y = y
        self.focused = False

        self.text = None
        font = pygame.font.Font('./fonts/Pixeltype.ttf', 25)
        if(color[0] == 'White' or color[0] == 'Yellow' or color[0] == 'Green'):
            self.text = font.render(color[0], False, 'black')
        else:
            self.text = font.render(color[0], False, 'white')
        
        self.textRect = self.text.get_rect( center = (x + self.rectWidth / 2, y + self.rectHeight / 2) )

        self.background = color[1]
        
        if(color[0] == 'White'):
            self.lineColor = [0, 0, 0]
        else:
            self.lineColor = [255, 255, 255]

        self.colorCode = color[1]

    def update(self, color):
        leftClick = pygame.mouse.get_pressed()[0]

        if leftClick:
            mousePos = pygame.mouse.get_pos()
            if mousePos[0] >= self.x and mousePos[0] <= self.x + self.rectWidth and mousePos[1] >= self.y and mousePos[1] <= self.y + self.rectHeight:
                self.focused = True
                return self.colorCode
            else:
                self.focused = False
        return color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.background, (self.x, self.y, self.rectWidth, self.rectHeight))
        screen.blit(self.text, self.textRect)
        if self.focused:
            pygame.draw.line(screen, self.lineColor, (self.x, self.y - 5), (self.x + self.rectWidth, self.y - 5), 8)
            pygame.draw.line(screen, self.lineColor, (self.x, self.y + self.rectHeight), (self.x + self.rectWidth, self.y + self.rectHeight), 8)
            pygame.draw.line(screen, self.lineColor, (self.x - 2, self.y - 8), (self.x - 2, self.y + self.rectHeight + 4), 8)
            pygame.draw.line(screen, self.lineColor, (self.x + self.rectWidth + 2, self.y - 8), (self.x + self.rectWidth + 2, self.y + self.rectHeight + 4), 8)