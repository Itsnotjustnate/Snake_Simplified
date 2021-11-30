import pygame

class Snake:
    def __init__(self, surface):
        self._surface = surface
        self.skin = pygame.image.load("resources/Snake_Block_1.jpg").convert()
        self.x = 400
        self.y = 400

    def draw(self):
        self._surface.fill((255,255,255))
        self._surface.blit(self.skin, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 40

    def move_right(self):
        self.x += 40

    def move_up(self):
        self.y -= 40

    def move_down(self):
        self.y += 40

