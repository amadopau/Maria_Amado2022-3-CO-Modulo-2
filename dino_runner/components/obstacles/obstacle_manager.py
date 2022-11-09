import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed-5, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
               cactus_second = Cactus(LARGE_CACTUS)
               self.obstacles.append(cactus_second)
               obstacle.rect.y = 325


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed-5, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


                  #  if len(self.obstacles) == 0:
       #     if random.randint(0, 2) == 0:
        #        self.obstacles.append(small_cactus(SMALL_CACTUS))
         #   elif random.randint(0, 2) == 1:
          #      self.obstacles.append(large_cactus(LARGE_CACTUS))
           # elif random.randint(0, 2) == 2:
            #    self.obstacles.append(bird(BIRD))
