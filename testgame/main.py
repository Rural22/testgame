import pygame
from sprite import Sprite

RESOLUTION = (1920, 1080)
print(RESOLUTION)
print(type(RESOLUTION))
pygame.init()
screen = pygame.display.set_mode()
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

sprite = Sprite()
bg = pygame.image.load("testgame/assets/wallpaper.png")
bg = pygame.transform.scale(bg,RESOLUTION)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg,(0,0))
    
    # pygame.draw.circle(screen, "Pink", player_pos, 40)
    screen.blit(sprite.image,player_pos)
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