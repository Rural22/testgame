import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, resolution:tuple[int,int]):
        super().__init__()
        self.image = pygame.image.load("testgame/assets/collectable.png")
        self.resolution = resolution
        self.x,self.y = self.random_pos()
        self.size_x = self.image.get_width() / 2
        self.size_y = self.image.get_height() / 2
    
    def is_colliding(self, player_pos:tuple[int,int]):
        x,y = player_pos
        if x < self.x - self.size_x or x > self.x + self.size_x:
            return False
        if y < self.y - self.size_y or y > self.y + self.size_y:
            return False
        print(player_pos,self.x,self.y,self.size_x,self.size_y)
        return True

            
    def random_pos(self):
        x=random.randrange(self.resolution[0])
        y=random.randrange(self.resolution[1])
        
        return x,y 
    
    def render(self,screen):
        screen.blit(self.image,(self.x,self.y))