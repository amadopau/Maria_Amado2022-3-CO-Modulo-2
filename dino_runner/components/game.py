import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, GAME_OVER, RESET, HEART
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager 
from dino_runner.components.message import draw_message


class Game:
    def __init__(self):
         pygame.init()
         pygame.display.set_caption(TITLE)
         pygame.display.set_icon(ICON)
         self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
         self.clock = pygame.time.Clock()
         self.playing = False
         self.game_speed = 20
         self.x_pos_bg = 0
         self.y_pos_bg = 380
         self.score = 0
         self.player = Dinosaur()
         self.obstacle_manager = ObstacleManager()
         self.running = False
         self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()


    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message('Press any key to restart...', self.screen)
        else:
            draw_message('Press any key to restart', self.screen)
            draw_message(f'your score: {self.score}', self.screen, pos_y_center = half_screen_width +50)
            draw_message(f'Death count: {self.death_count}', self.screen, pos_x_center = half_screen_height +100)
            self.screen.blit(GAME_OVER, (half_screen_height+80, half_screen_width-480))
            self.screen.blit(RESET, (half_screen_height+230, half_screen_width-420))
            self.screen.blit(HEART, (half_screen_height+190, half_screen_width-200))
            
        pygame.display.update()
        self.handle_event_on_menu()

    def handle_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def reset(self):
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20
        self.playing = True
    

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0 and self.game_speed < 500: self.game_speed += 5 
     
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    

