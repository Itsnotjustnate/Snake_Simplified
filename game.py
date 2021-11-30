
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800,800))
        self.surface.fill((255,255,255))

    def run(self):
        pygame.init()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False