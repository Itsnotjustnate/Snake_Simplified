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
from pygame.locals import *
from food import Food
from gameover import GameOver
from score import Score
from snake import SIZE, Snake
import time

class Game:
    def __init__(self, mainmenu):
        """Initializing variables of game"""
        self.length = 1
        self._mainmenu = mainmenu
        self.snake = Snake(self._mainmenu.surface, self.length)
        self.snake.draw()
        self.food = Food(self._mainmenu.surface)
        self.score = Score(self._mainmenu.surface, self.length)
        self.gameover = GameOver(self._mainmenu.surface, self.length, self, self._mainmenu)

    def is_collision(self, x1, y1, x2, y2):
        """Finds collision of the leading block"""
        if x1 == x2 and x1 < x2 + SIZE:
            if y1 == y2 and y1 < y2 + SIZE:
                return True
        
        return False
    
    def display_score(self):
        font = pygame.font.SysFont('calibri', 10)
        score = font.render(f"Score: {self.snake.length}", True, (0,0,0))
        self._mainmenu.surface.blit(score, (300, 10))

    def logic(self):

        if not self.is_collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.move()
            self.food.draw()
            

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.food.x, self.food.y):
            self.snake.increase()
            self.snake.move()
            self.food.move()
        
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.gameover.message()
            
        self.display_score()
        pygame.display.flip()
        

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

            self.logic()

            time.sleep(0.2)
    
    def reset(self):
        self.length = 1
        self.snake = Snake(self._mainmenu.surface, self.length)
        self.snake.draw()
        self.food = Food(self._mainmenu.surface)
        self.score = Score(self._mainmenu.surface, self.length)
        self.gameover = GameOver(self._mainmenu.surface, self.length, self, self._mainmenu)
