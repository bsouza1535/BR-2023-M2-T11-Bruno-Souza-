import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    def __init__(self, image, bird_y):
        self.type = random.randint(0, 1)
        super().__init__(image, self.type)
        if bird_y == 0:
            self.rect.y = 415
        else:
            self.rect.y = 460
        
        self.step_index = 0 
        self.direction = 2 
        
    def draw(self, screen):
        if self.step_index >= 9: 
            self.step_index = 0 
        screen.blit(self.image[self.step_index//5], self.rect) 
        self.step_index += 1
        
        self.rect.y += self.direction 
        
        if self.rect.y <= 415:  
            self.direction = 2  
        elif self.rect.y >= 460: 
            self.direction = -2 