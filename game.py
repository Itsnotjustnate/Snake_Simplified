
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800,800))
        self.surface.fill((255,255,255))

    def run(self):
        pygame.init()