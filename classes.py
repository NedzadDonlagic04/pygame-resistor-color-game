import pygame

class MyClock:
    def __init__(self, fps):
        self.FPS = fps
        self.CLOCK = pygame.time.Clock()
    
    def tick(self):
        self.CLOCK.tick(self.FPS)