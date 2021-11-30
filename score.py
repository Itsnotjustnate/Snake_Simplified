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
    
class Score:
    def __init__(self, surface, length):
        self.font = pygame.font.SysFont('calibri', 40)
        self._length = length
        self._surface = surface

    def display_score(self):
        score = self.font.render(f"Score: {self._length}", True, (128, 0, 0))
        self._surface.blit(score, (600, 10))
