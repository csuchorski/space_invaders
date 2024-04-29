import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_w, screen_h):
        pygame.sprite.Sprite.__init__(self)
        big_image = pygame.image.load("./images/player_ship.png") 
        self.image = pygame.transform.scale(big_image, (50, 50)) 
        self.rect = self.image.get_rect()
        self.rect.x = screen_w//2
        self.rect.y = screen_h * 0.85
        
        self.speed = 1


    def move(self, value, screen_w):
        self.rect.x = (self.rect.x + self.speed*value) % screen_w 
