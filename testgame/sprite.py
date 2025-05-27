import pygame
import logging
from pygame import Surface


class Sprite(pygame.sprite.Sprite):
    def __init__(self, screen: Surface):
        super().__init__()
        self.image = pygame.image.load("testgame/assets/sprite.png")
        self.screen = screen
        self.player_pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2
        )

    def movement(self, keys: dict, dt):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.player_pos.y -= 350 * dt
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.player_pos.y += 350 * dt
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player_pos.x -= 350 * dt
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player_pos.x += 350 * dt
        self.check_bounds()

    def check_bounds(self):
        if self.player_pos.x < 0:
            self.player_pos.x = self.screen.get_width()
            
        if self.player_pos.y < 0:
            self.player_pos.y = self.screen.get_height()
            
        if self.player_pos.x > self.screen.get_width():
            self.player_pos.x = 0
            
        if self.player_pos.y > self.screen.get_height():
            self.player_pos.y = 0
            
        logging.debug(self.player_pos.y)
        logging.debug(self.player_pos.x)