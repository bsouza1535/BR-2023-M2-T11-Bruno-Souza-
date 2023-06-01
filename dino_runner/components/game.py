import pygame
import random

from dino_runner.utils.sons import FINAL_GAME, SOM_DE_FUNDO
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, IMG_BACK
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.menus import Menu
from dino_runner.components.draws import Draws




class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False

        self.x_pos_bg = 0
        self.y_pos_bg = 540
        self.x_pos_back = 0
        self.y_pos_back = 0

        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.maior_score = 0

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.menu = Menu()
        self.draws = Draws()

        self.som_menu = False
        self.som_de_fundo = False


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                print("Chegou!")
                self.menu.display_menu(self)
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        if self.som_de_fundo == False:
            SOM_DE_FUNDO.play()
            self.som_de_fundo = True
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        else:
            pygame.time.delay(500)
            SOM_DE_FUNDO.stop()
            FINAL_GAME.play()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.draws.update_score(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # "#FFFFFF"
        self.draws.draw_background(self)
        self.draws.draw_score(self)
        #self.draws.draw_speed(self)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draws.draw_score(self)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        self.screen.blit(IMG_BACK, (self.x_pos_back, self.y_pos_back))
        
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def reset_game(self):
        self.click = False
        self.som_de_fundo = False
        self.som_menu = False
        self.obstacle_manager.reset_obstacles()
        self.player = Dinosaur()
        self.score = 0
        self.game_speed = 15