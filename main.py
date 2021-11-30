import pygame
from pygame.locals import *
from game import Game

def main():
    game = Game
    game.run()



    surface = pygame.display.set_mode((800,800))
    surface.fill((255,255,255))
    pygame.display.flip()


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False


if __name__ == __main__:
    main()