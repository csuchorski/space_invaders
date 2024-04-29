import pygame

from Player import Player 
  
background_colour = (50, 50, 50) 
screen = pygame.display.set_mode((500, 500)) 
clock = pygame.time.Clock()

pygame.display.set_caption('Space invaders') 
screen.fill(background_colour) 
pygame.display.flip() 
  
player = Player()


running = True
while running: 
    clock.tick(60)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]: 
            running = False
    if keys[pygame.K_LEFT]:
        player.move(-5)
    if keys[pygame.K_RIGHT]:
        player.move(5)
            
    screen.fill(background_colour)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.flip()
