import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD, MARTELO, SHIELD_SOM, EXPLODIR, HEART_SOM


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            choice = random.choice([True, False])
            if choice == True:  
                obstacle_type = random.choice([SMALL_CACTUS, LARGE_CACTUS])  
                self.obstacles.append(Cactus(obstacle_type))  
            else:  
                bird_y = random.randint(0, 2)
                self.obstacles.append(Bird(BIRD, bird_y))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.som_de_fundo = False
                    EXPLODIR.play()
                elif game.player.shield:
                    SHIELD_SOM.play()
                    continue
                elif game.player.hammer:
                    MARTELO.play()
                    self.obstacles.remove(obstacle)
                elif game.player.heart:
                    HEART_SOM.play()
                    game.score += 1 

    def draw(self, screen): 
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
