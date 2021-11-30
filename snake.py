import pygame
from game import surface

SIZE = 40

class Snake:
    def __init__(self, surface, length):
        self.length = length
        self._surface = surface
        self.skin = pygame.image.load("resources/Snake_Block_1.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = ''

    def draw(self):
        self._surface.fill((255,255,255))
        for i in range(self.length):
            self._surface.blit(self.skin, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'left':
            self.x[0] -= 40
        if self.direction == 'right':
            self.x[0] += 40
        if self.direction == 'up':
            self.y[0] -= 40
        if self.direction == 'down':
            self.y[0] += 40

        self.draw()
