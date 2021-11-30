import pygame
from pygame.locals import *


class GameOver:
    def __init__(self, surface, length, game, mainmenu):
        self.black = (0,0,0)
        self.white = (255,255,255)
        self._surface = surface
        self._length = length
        self._game = game
        self._mainmenu = mainmenu
        self.text_size = 3
        self.font = pygame.font.SysFont('calibri', 10 * self.text_size)

    
    def message(self):
        self._display = pygame.draw.rect(self._surface, self.black, (100,50,400,500))

        gameover_text = self.font.render(f"You Died!", True, self.white)
        self._surface.blit(gameover_text, (220, 100))

        score_text = self.font.render(f"Score: {self._length}", True, self.white)
        self._surface.blit(score_text, (220, 150))

        self.mainmenu_button = pygame.draw.rect(self._surface, self.white, (150,200,300,80))
        mainmenu_text = self.font.render(f"Main Menu", True, self.black)
        self._surface.blit(mainmenu_text, (225, 220))

        self.playagain_button = pygame.draw.rect(self._surface, self.white, (150,300,300,80))
        playagain_text = self.font.render(f"Play Again", True, self.black)
        self._surface.blit(playagain_text, (223, 320))

        self.exit_button = pygame.draw.rect(self._surface, self.white, (150,400,300,80))
        exit_text = self.font.render(f"Exit Game", True, self.black)
        self._surface.blit(exit_text, (225, 420))

        pygame.display.flip()
        death = True

        while death:
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit(1)
                elif event.type == pygame.MOUSEBUTTONDOWN:  #150,200,300,80
                    if event.button == 1 and pygame.mouse.get_pos()[0] >= 150 \
                        and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[0] <= 450 \
                        and pygame.mouse.get_pos()[1] <= 280:
                        self._mainmenu.screen()

                    #150,300,300,80
                    if event.button == 1 and pygame.mouse.get_pos()[0] >= 150 \
                        and pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[0] <= 450 \
                        and pygame.mouse.get_pos()[1] <= 380:
                        self._game.reset()
                        self._game.run()
                    
                    if event.button == 1 and pygame.mouse.get_pos()[0] >= 150 \
                        and pygame.mouse.get_pos()[1] >= 400 and pygame.mouse.get_pos()[0] <= 450 \
                        and pygame.mouse.get_pos()[1] <= 480:
                        exit(1)

                elif event.type == QUIT:
                    exit(1)
                    


        