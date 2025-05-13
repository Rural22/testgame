import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self, resolution:tuple[int,int]):
        super().__init__()
        self.image = pygame.image.load("testgame/assets/collectable.png")
        self.resolution = resolution
        self.x,self.y = self.random_pos()

    
    
    def random_pos(self):
        x=random.randrange(self.resolution[0])
        y=random.randrange(self.resolution[1])
        
        return x,y 
    
    def render(self,screen):
        screen.blit(self.image,(self.x,self.y))