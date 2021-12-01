import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)

class Prompt:
    def __init__(self, surface, message, l, t, w, h, x, y):
        self._surface = surface
        self._message = message
        self._l = l
        self._t = t
        self._w = w
        self._h = h
        self._x = x
        self._y = y
        self.text_size = 3
        self.font = pygame.font.SysFont('calibri', 10 * self.text_size)


    def text(self):
        """displays text"""
        self.text = self.font.render(self._message, True, WHITE)
        self._surface.blit(self.text, (self._x, self._y))

    def button(self):
        """Creates a button given the proper parameters"""
        self.button = pygame.draw.rect(self._surface, WHITE, (self._l, self._t, self._w, self._h))
        self.text = self.font.render(self._message, True, BLACK)
        self._surface.blit(self.text, (self._x,self._y))