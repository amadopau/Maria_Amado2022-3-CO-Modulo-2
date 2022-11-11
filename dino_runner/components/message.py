import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_COLOR = (126, 238, 94)
#FONT_COLOR_2 = (244, 177, 32)
#FONT_COLOR_3 = (32, 217,)
FONT_SIZE = 30
FONT_STYLE = 'freesansbold.ttf'

def draw_message(
    message,
    screen,
    font_color_1=FONT_COLOR,
   # font_color_2=FONT_COLOR_2,
   # font_color_3=FONT_COLOR_3,
    font_size=FONT_SIZE,
    pos_x_center= SCREEN_WIDTH // 2,
    pos_y_center= SCREEN_HEIGHT // 2
):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, font_color_1)
    text_rect = text.get_rect()
    text_rect.center = (pos_x_center, pos_y_center)
    screen.blit(text, text_rect)