
import pygame
from pygame import surface
from pygame.locals import *
from snake import Snake
import time

class Game:
    def __init__(self):
        pygame.init()
        self.length = 6
        self.surface = pygame.display.set_mode((400,400))
        self.surface.fill((255,255,255))
        self.snake = Snake(self.surface, self.length)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                elif event.type == QUIT:
                    running = False
            self.snake.move()
            time.sleep(0.2)