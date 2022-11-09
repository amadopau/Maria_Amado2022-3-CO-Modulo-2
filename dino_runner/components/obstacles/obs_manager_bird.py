from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD

count =+ 0
class ObstacleManBird:
    def __init__(self):
        self.obstacles =  []


    def update(self, game):
        if len(self.obstacles) == 0:
            bird = Bird(BIRD)
            self.obstacles.append(bird)

        for obstacle in self.obstacles:
            if count >= 10: 
                obstacle = True 
            obstacle.update(game.game_speed+10, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        
      