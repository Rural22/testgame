import pygame
from sprite import Sprite
from food import Food

RESOLUTION = (1920, 1080)
print(RESOLUTION)
print(type(RESOLUTION))
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True
dt = 0
score_text = pygame.font.SysFont('VCR OSD MONO', 60, bold=True)
score_value = 0

def create_food(amount:int) -> list[Food]:
    food = []
    for i in range(amount):
        food.append(Food(RESOLUTION))
        
    return food

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

sprite = Sprite()
# food = Food(RESOLUTION)
food = create_food(3)
bg = pygame.image.load("testgame/assets/wallpaper.png")
bg = pygame.transform.scale(bg,RESOLUTION)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))
    
    # pygame.draw.circle(screen, "Pink", player_pos, 40)
    screen.blit(sprite.image,player_pos)
    eaten_food = []
    for i,f in enumerate(food):
        if f.is_colliding(player_pos):
            print("FOOD COLLIDE")
            eaten_food.append(i)
            
        f.render(screen)
    for i in eaten_food:
        food.pop(i)
        score_value += 1
    # food.render(screen)
    render_surface = score_text.render(f'SCORE = {score_value}', False, pygame.Color(25, 255, 255))
    screen.blit(render_surface, (5,5))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        
    if keys[pygame.K_ESCAPE]:
        running = False
            
    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()