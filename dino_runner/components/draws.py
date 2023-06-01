import pygame
import random
from dino_runner.utils.constants import FONT_STYLE, BG


class Draws:
    def generate_text(self, textt, font_size):
        font = pygame.font.Font(FONT_STYLE, font_size)
        text = font.render(textt, True, (0,0,0))
        return text
    
    def text_rect(self, x, y, game):
        text = self.generate_text("Press any key to start", 22)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        return text_rect
    
    def draw_score(self, game):
        text = self.generate_text(f"Score: {game.score}", 22)
        text_rect = self.text_rect(1000, 50, game)
        game.screen.blit(text, text_rect)

    def update_score(self, game):
        game.score += 1
        game.maior_score = game.score
        if game.score % 100 == 0:
            game.game_speed = game.game_speed + random.randint(1, 3)

    def draw_background(self, game):
        image_width = BG.get_width()
        game.screen.blit(BG, (game.x_pos_bg, -200))
        game.screen.blit(BG, (image_width + game.x_pos_bg, -200))
        if game.x_pos_bg <= -image_width:
            game.screen.blit(BG, (image_width + game.x_pos_bg, -200))           
            game.x_pos_bg = 0
        game.x_pos_bg -= game.game_speed