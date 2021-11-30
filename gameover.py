import pygame
from pygame.locals import *
BLACK = (0,0,0)
WHITE = (255,255,255)

class GameOver:
    def __init__(self, surface, game, mainmenu):
        self._surface = surface
        self._game = game
        self._mainmenu = mainmenu
        self.text_size = 3
        self.font = pygame.font.SysFont('calibri', 10 * self.text_size)

    
    def message(self):
        self._display = pygame.draw.rect(self._surface, BLACK, (100,50,400,500))

        gameover_text = self.font.render(f"You Died!", True, WHITE)
        self._surface.blit(gameover_text, (220, 100))

        score_text = self.font.render(f"Score: {self._game.snake._length}", True, WHITE)
        self._surface.blit(score_text, (220, 150))

        self.mainmenu_button = pygame.draw.rect(self._surface, WHITE, (150,200,300,80))
        mainmenu_text = self.font.render(f"Main Menu", True, BLACK)
        self._surface.blit(mainmenu_text, (225, 220))

        self.playagain_button = pygame.draw.rect(self._surface, WHITE, (150,300,300,80))
        playagain_text = self.font.render(f"Play Again", True, BLACK)
        self._surface.blit(playagain_text, (223, 320))

        self.exit_button = pygame.draw.rect(self._surface, WHITE, (150,400,300,80))
        exit_text = self.font.render(f"Exit Game", True, BLACK)
        self._surface.blit(exit_text, (225, 420))

        pygame.display.flip()
        death = True

        while death:
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit(1)
                elif event.type == pygame.MOUSEBUTTONDOWN:  
                    if event.button == 1 and pygame.mouse.get_pos()[0] >= 150 \
                        and pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[0] <= 450 \
                        and pygame.mouse.get_pos()[1] <= 280:
                        self._mainmenu.screen()

                    
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
                    


        