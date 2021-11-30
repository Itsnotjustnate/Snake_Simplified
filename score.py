#
# Nathan Eduvala
# CPSC 386-01
# 2021-11-29
# nathaneduvala@csu.fullerton.edu
# @Itsnotjustnate
#
# Lab 02
#

import pygame
import time
    
class Score:
    def __init__(self, surface, game):
        self.font = pygame.font.SysFont('calibri', 20)
        self._game = game
        self._surface = surface

    def display_score(self):
        self.score = self.font.render(f"Score: {self._game.snake._length}", True, (128, 0, 0))
        self._surface.blit(self.score, (300, 10))
        pygame.display.flip()
