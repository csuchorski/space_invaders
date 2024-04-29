import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        big_image = pygame.image.load("./images/player_ship.png") 
        self.image = pygame.transform.scale(big_image, (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50 
        
        self.speed = 1


    def move(self, value):
        self.rect.x += value * self.speed
