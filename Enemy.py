import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        #big_image = pygame.image.load("./images/enemy_ship.jpg")
        #self.image = pygame.transform.scale(big_image, (50,50))
        pygame.sprite.Sprite.__init__(self)
        width = 50
        height = 50
        self.color = (255, 0 ,0)
        self.rect = pygame.Rect(start_x, start_y,width,height) 
        self.direction = 1
        self.speed = 50

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect)
    
    def move(self):
        self.rect.x += self.speed * self.direction 

    def update(self, direction):
        pygame.sprite.Sprite.update(self)
        self.direction = direction
        self.move()


