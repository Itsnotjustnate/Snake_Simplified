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
import random

from pygame import display

from snake import SIZE

class Food:
    def __init__(self, surface):
        self.burger = pygame.image.load("resources/Snake_Food_1.png").convert()
        self._surface = surface
        self.x = random.randint(1, 13) * SIZE
        self.y = random.randint(1, 13) * SIZE
    
    def draw(self):
        self._surface.blit(self.burger, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 13) * SIZE
        self.y = random.randint(1, 13) * SIZE

