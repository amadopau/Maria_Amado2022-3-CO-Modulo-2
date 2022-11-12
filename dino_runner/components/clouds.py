import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH



class Cloud(Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.x -= 1

    def draw(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos.y)) 
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        self.screen.blit(CLOUD, (half_screen_height+190, half_screen_width-200))
 