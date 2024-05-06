import pygame

from Player import Player 
from Enemy import Enemy
from Projectile import Projectile  
background_colour = (50, 50, 50) 
screen_w, screen_h = 500, 500
screen = pygame.display.set_mode((screen_w, screen_h)) 
clock = pygame.time.Clock()

pygame.display.set_caption('Space invaders') 
screen.fill(background_colour) 
pygame.display.flip() 
  
player = Player(screen_w, screen_h)
enemies = [Enemy(x, y*60) for x in range(screen_w//4, 3*screen_w//4, 60) for y in range(1,4)]
bullets = []


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
    if keys[pygame.K_SPACE]:
        bullets.append(Projectile(player.rect.x + player.rect.width//2, player.rect.y))
    screen.fill(background_colour)

    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.y -= bullet.speed
        pygame.draw.circle(screen, bullet.color, (bullet.x, bullet.y), bullet.radius)
        circle_rect = pygame.Rect(bullet.x - bullet.radius, bullet.y - bullet.radius, bullet.radius*2, bullet.radius*2)
        hit_id = circle_rect.collidelist([enemy.rect for enemy in enemies])
        if hit_id != -1:
            enemies.pop(hit_id) 
            bullets.remove(bullet)
    if len(enemies) == 0:
        running = False
    pygame.display.flip()

