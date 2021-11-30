import pygame
from pygame.locals import *
from game import Game

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
class MainMenu:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((600,600))
        self.surface.fill((255,255,255))
        self.text_size = 5
        self.font = pygame.font.SysFont('arial', 10 * self.text_size)

    def screen(self):
        self._display = pygame.draw.rect(self.surface, GREEN, (40,40,520,520))
        
        title_text = self.font.render(f"Snake Game", True, WHITE)
        self.surface.blit(title_text, (150, 100))

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