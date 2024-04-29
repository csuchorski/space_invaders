import pygame

from Player import Player 
  
background_colour = (50, 50, 50) 
screen = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption('Space invaders') 
screen.fill(background_colour) 
pygame.display.flip() 
  
player = Player()


running = True
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
    screen.fill(background_colour)
    screen.blit(player.image, (player.rect.x, player.rect.y))
    pygame.display.flip()
