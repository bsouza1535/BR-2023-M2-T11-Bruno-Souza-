import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FUNDO_MENU, FUNDO_MENU2
from dino_runner.utils.sons import MENU, CLICK

class Menu:

    def display_menu(self, game):
        game.screen.fill((255, 255, 255))
        
        if game.death_count >= 1:
            self.secondary_menu_event_handler(game)
        else:
            self.main_menu_event_handler(game)
        pygame.display.flip()
    
    def main_menu_event_handler(self, game):
        game.screen.blit(FUNDO_MENU, (0, 0))
        if game.som_menu == False:
            MENU.play()
            game.som_menu = True
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        text = game.draws.generate_text("Press any key to start", 22)
        text_rect = game.draws.text_rect(x_text_pos + 15, y_text_pos + 18, game)
        game.screen.blit(text, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.executing = False
                game.playing = False
            elif event.type == pygame.KEYDOWN:
                CLICK.play()
                game.run()
            
    def secondary_menu_event_handler(self, game):
        game.screen.blit(FUNDO_MENU2, (50, 0))
        x_text_pos = SCREEN_WIDTH//2
        y_text_pos = SCREEN_HEIGHT//2
        if game.death_count >= 1:
            text = game.draws.generate_text("Press space to restart ", 18)
            text_rect = game.draws.text_rect(x_text_pos , y_text_pos + 30, game)
            game.screen.blit(text, text_rect)

            text3 = game.draws.generate_text("Press c to exit", 18)
            text3_rect = game.draws.text_rect(x_text_pos , y_text_pos - 130, game)
            game.screen.blit(text3, text3_rect)

            text2 = game.draws.generate_text(f"Score/Death: {game.maior_score}/{game.death_count}", 18)
            text_rect2 = game.draws.text_rect(x_text_pos , y_text_pos - 170, game)
            game.screen.blit(text2, text_rect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.executing = False
                game.playing = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    CLICK.play()
                    #game.death_count = 0
                    game.reset_game()
                    game.run()
                elif event.key == pygame.K_c:
                    exit()
                    