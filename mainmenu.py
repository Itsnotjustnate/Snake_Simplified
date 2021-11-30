import pygame
from pygame.locals import *
from game import Game

BLACK = (0,0,0)

class MainMenu:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600,600))
        self.surface.fill((255,255,255))

    def screen(self):
        self._display = pygame.draw.rect(self.surface, BLACK, (50,25,500,550))
        
        pygame.display.flip()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    
                elif event.type == QUIT:
                    running = False
                    
        self.game = Game(self)
        self.game.run()