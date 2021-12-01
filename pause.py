import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT

from prompt import Prompt
BLACK = (0,0,0)

class Pause:
    def __init__(self, surface, game, mainmenu):
        self._surface = surface
        self._game = game
        self._mainmenu = mainmenu
        resume = "Resume Game"
        paused = "Game Paused"
        leaderboard = "High Scores"
        mainmenu = "Main Menu"
        exit = "Exit Game"
        self._paused = Prompt(self._surface, paused, 0, 0, 0, 0, 200, 100)
        self._resume = Prompt(self._surface, resume, 150, 150, 300, 80, 200, 190)
        self._leaderboard = Prompt(self._surface, leaderboard, 150, 250, 300, 80, 200, 290)
        self._mainscreen = Prompt(self._surface, mainmenu, 150, 350, 300, 80, 200, 390)
        self._exit = Prompt(self._surface, exit, 150, 450, 300, 80, 200, 490)

    def stop(self):
        self._display = pygame.draw.rect(self._surface, BLACK, (100,50,400,500))
        self._paused.text()
        self._resume.button()
        self._leaderboard.button()
        self._mainscreen.button()
        self._exit.button()
        pygame.display.flip()
        
        paused = True

        while paused:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button == 1 and pygame.mouse.get_pos()[0] >= 150 \
                        and pygame.mouse.get_pos()[1] >= 350 and pygame.mouse.get_pos()[0] <= 450 \
                        and pygame.mouse.get_pos()[1] <= 430:
                        self._mainmenu.screen()

                elif event.type == QUIT:
                    exit(1)