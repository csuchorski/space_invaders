import pygame

from Player import Player 
from Enemy import Enemy  
background_colour = (50, 50, 50) 
screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h)) 
clock = pygame.time.Clock()

pygame.display.set_caption('Space invaders') 
screen.fill(background_colour) 
pygame.display.flip() 
  
player = Player(screen_w, screen_h)
enemies = [Enemy(x, y*60) for x in range(screen_w//4, 3*screen_w//4, 60) for y in range(1,4)]

running = True
while running: 
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            running = False
    if keys[pygame.K_LEFT]:
        player.move(-5, screen_w)
    if keys[pygame.K_RIGHT]:
        player.move(5, screen_w)
            
    screen.fill(background_colour)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
    pygame.display.flip()

