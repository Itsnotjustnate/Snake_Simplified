import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT
BLACK = (0,0,0)

class Pause:
    def __init__(self, surface, game):
        self._surface = surface
        self._game = game

    def stop(self):
        self._display = pygame.draw.rect(self._surface, BLACK, (100,50,400,500))
        pygame.display.flip()
        
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self._game.run()
                if event.type == QUIT:
                    exit(1)