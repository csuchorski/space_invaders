import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        big_image = pygame.image.load("./images/enemy_ship.jpg")
        self.image = pygame.transform.scale(big_image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
