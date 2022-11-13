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
        pygame.draw.rect(self.resistorImg, color, (0, 0, rectWidth, rectHeight))
        self.resistorRect = self.resistorImg.get_rect( center = pos )

        self.halfWidth = rectWidth / 2
        self.lineColor = (192, 192, 192)

    def draw(self, screen):
        screen.blit(self.resistorImg, self.resistorRect)
        pygame.draw.line(screen, self.lineColor, (self.resistorRect.left - 150, self.resistorRect.centery), (self.resistorRect.left, self.resistorRect.centery), 20)
        pygame.draw.line(screen, self.lineColor, (self.resistorRect.right + 150, self.resistorRect.centery), (self.resistorRect.right, self.resistorRect.centery), 20)