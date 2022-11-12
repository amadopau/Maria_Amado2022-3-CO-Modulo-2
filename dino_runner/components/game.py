import pygame
import random 
import sys

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE, GAME_OVER, RESET, HEART, DEFAULT_TYPE, CLOUD
from dino_runner.components.dinosaur import Dinosaur
from  dino_runner.components.powerUps.power_up_manager import  PowerUpManager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager 
from dino_runner.components.message import draw_message
from dino_runner.components.clouds import Cloud



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
         self.high_score = 0
         self.player = Dinosaur()
         self.obstacle_manager = ObstacleManager()
         self.power_up_manager = PowerUpManager() 
         self.running = False
         self.death_count = 0
         self.ground_x = 0
         

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
        self.power_up_manager.update(self)
        self.update_score()
        self.highest_score()
      #  self.event_cloud()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()


    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any key to start...", True, (198, 54, 54))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_height+270, half_screen_width-300)
            self.screen.blit(text, text_rect)
        else:
            self.screen.blit(GAME_OVER, (half_screen_height+80, half_screen_width-480))
            self.screen.blit(RESET, (half_screen_height+230, half_screen_width-420))
            self.screen.blit(HEART, (half_screen_height+200, half_screen_width-200))

            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any key to start again", True, (198, 54, 54))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_height+270, half_screen_width-300)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render(f'your score: {self.score}', True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_height+270, half_screen_width-250)
            self.screen.blit(text, text_rect)
        
            font.render(f"Highest score: {self.high_score}",True,(255, 0, 0))
            text_rect = text.get_rect()
            text_rect.x = (half_screen_width-100)
            text_rect.y = (half_screen_height+100)
            self.screen.blit(text, text_rect)

            font.render(f"Total deaths: {self.death_count}",True,(255, 0, 0))
            text_rect = text.get_rect()
            text_rect.x = (half_screen_width-100)
            text_rect.y = (half_screen_height+150)
            self.screen.blit(text, text_rect)

        pygame.display.update()
        self.handle_event_on_menu()

    def handle_event_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def event_cloud(self):
        cloud_group = pygame.sprite.Group() #devielve una tupla de los subgrupos
        self.CLOUD_EVENT = pygame.USEREVENT
        pygame.time.set_timer(self.CLOUD_EVENT, 3000)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() #provee acceso a variables 

                if event.type == self.CLOUD_EVENT:
                    current_cloud_y = random.randint(50, 3000)
                    current_cloud = Cloud(CLOUD, 1380, current_cloud_y)
                    cloud_group.add(current_cloud)

            self.ground_x -= self.game_speed

           
             
            pygame.display.update()
           

        
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def reset(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.score = 0
        self.game_speed = 20
        self.playing = True

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)
            if time_to_show >= 0:
                draw_message(
                    f'{self.player.type} enable for {time_to_show} seconds',
                    self.screen,
                    font_size=18,
                    pos_x_center = 500,
                    pos_y_center = 50
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
        
    def highest_score(self):
        if self.high_score>self.score:
            self.high_score = self.high_score

        elif self.high_score<= self.score:
            self.high_score = self.score



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
    

