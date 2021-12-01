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

SIZE = 40

class Snake:
    def __init__(self, surface, length):
        self._length = length
        self._surface = surface
        self.skin = pygame.image.load("resources/Snake_Block_1.jpg").convert()

        self.x = [SIZE * 6] * self._length
        self.y = [SIZE * 6] * self._length
        self.direction = 'right'

    def draw(self):
        self._surface.fill((255,255,255),(40,40,520,520))
        for i in range(self._length):
            self._surface.blit(self.skin, (self.x[i], self.y[i]))
        pygame.display.flip()
    
    def increase(self):
        self._length += 1
        self.x.insert(self._length,self.skin)
        self.y.insert(self._length,self.skin)
        

    def move_left(self):
        if not self.direction == 'right':
            self.direction = 'left'

    def move_right(self):
        if not self.direction == 'left':
            self.direction = 'right'

    def move_up(self):
        if not self.direction == 'down':
            self.direction = 'up'

    def move_down(self):
        if not self.direction == 'up':
            self.direction = 'down'

    def move(self):

        for i in range(self._length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()
