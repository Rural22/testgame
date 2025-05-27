import pygame
from sprite import Sprite
from food import Food
import logging
from food_logic import FoodManager


logging.basicConfig(filename='game.log', level=logging.DEBUG)

RESOLUTION = (1920, 1080)
print(RESOLUTION)
print(type(RESOLUTION))
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True
dt = 0
debug_text = pygame.font.SysFont('VCR OSD MONO', 30)
score_text = pygame.font.SysFont('VCR OSD MONO', 60, bold=True)
score_value = 0

sprite = Sprite(screen)
food = FoodManager(1, RESOLUTION)
bg = pygame.image.load("testgame/assets/wallpaper.png")
bg = pygame.transform.scale(bg,RESOLUTION)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))
    
    # pygame.draw.circle(screen, "Pink", sprite.player_pos, 40)
    screen.blit(sprite.image,sprite.player_pos)
    # eaten_food = []
    # for i,f in enumerate(food):
    #     if f.is_colliding(sprite.player_pos):
    #         print("FOOD COLLIDE")
    #         eaten_food.append(i)
    score_value += food.collision(sprite)
    
    #     f.render(screen)
    # for i in eaten_food:
    #     food.pop(i)
    #     score_value += 1
    #     food.append(Food(RESOLUTION))
    # food.render(screen)
    food.render_screen(screen)
    render_surface = score_text.render(f'SCORE = {score_value}', False, pygame.Color(25, 255, 255))
    screen.blit(render_surface, (5,5))
    render_surface = debug_text.render(f'pos: {sprite.player_pos.x = } : {sprite.player_pos.y = }', False, pygame.Color(25, 25, 255))
    screen.blit(render_surface, (5,90))
    
    keys = pygame.key.get_pressed()
    sprite.movement(keys,dt)
    
    if keys[pygame.K_ESCAPE]:
        running = False
            
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()