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

        self.font = pygame.font.Font('./fonts/Pixeltype.ttf', 40)

        self.resistorParts = [
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 30, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height, 
              'allowedColors': [
                [0, 0, 0],
                [160, 82, 45],
                [255, 0, 0],
                [255, 165, 0],
                [255, 255, 0],
                [0, 255, 0],
                [0, 0, 255],
                [128, 0, 128],
                [128, 128, 128],
                [255, 255, 255]
              ], 'meaning': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'text': None, 'textRect': None },
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 100, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height,
              'allowedColors': [
                [0, 0, 0],
                [160, 82, 45],
                [255, 0, 0],
                [255, 165, 0],
                [255, 255, 0],
                [0, 255, 0],
                [0, 0, 255],
                [128, 0, 128],
                [128, 128, 128],
                [255, 255, 255]
              ], 'meaning': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'text': None, 'textRect': None },
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 200, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height,
              'allowedColors': [
                [0, 0, 0],
                [160, 82, 45],
                [255, 0, 0],
                [255, 165, 0],
                [255, 255, 0],
                [0, 255, 0],
                [0, 0, 255],
                [255, 215, 0],
                [192, 192, 192]
               ], 'meaning': ['x1 Ohm', 'x10 Ohm', 'x100 Ohm', 'x1K Ohm', 'x10K Ohm', 'x100K Ohm', 'x1M Ohm', 'x0.1 Ohm', 'x0.01 Ohm'],
                'text': None, 'textRect': None },
            { 'color': [0, 0, 0], 'x': self.resistorRect.left + 300, 'y': self.resistorRect.top, 'width': 40, 'height': self.resistorRect.height,
              'allowedColors': [
                [160, 82, 45],
                [255, 0, 0],
                [255, 215, 0],
                [192, 192, 192]
               ], 'meaning': ['  +- 1%', '  +- 2%', '  +- 5%', '  +- 10%'], 'text': None, 'textRect': None }
        ]
    
    def compareColors(self, color1, color2):
        if color1[0] == color2[0] and color1[1] == color2[1] and color1[2] == color2[2]:
            return True
        return False

    def update(self, color):
        leftClick = pygame.mouse.get_pressed()[0]

        if leftClick:
            mousePos = pygame.mouse.get_pos()
            for part in self.resistorParts:
                if mousePos[0] >= part['x'] and mousePos[0] <= part['x'] + part['width'] and mousePos[1] >= part['y'] and mousePos[1] <= part['y'] + part['height']:
                    for i in range(0, len(part['allowedColors'])):
                        if self.compareColors(part['allowedColors'][i], color):
                            part['color'] = color
                            part['text'] = self.font.render(part['meaning'][i], False, 'black')
                            part['textRect'] = part['text'].get_rect( center = (part['x'] + part['width'] / 2, part['y'] - 15) )
                            break
                
    def draw(self, screen):
        screen.blit(self.resistorImg, self.resistorRect)

        for part in self.resistorParts:
            pygame.draw.rect(screen, part['color'], (part['x'], part['y'], part['width'], part['height']))
            if part['text'] != None:
                screen.blit(part['text'], part['textRect'])

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
            elif self.colorCode == color:
                self.focused = True
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