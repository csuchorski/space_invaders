import pygame

class Player():

    def __init__(self, screen_w, screen_h):
        width = 50
        height =  50
        self.rect = pygame.Rect(screen_w//2, round(screen_h*0.85), width, height) 
        self.speed = 1
        self.color = (0,0, 255)

    def move(self, value, screen_w):
        self.rect.x = (self.rect.x + self.speed*value) % screen_w 

    def draw(self,surf):
        pygame.draw.rect(surf, self.color,self.rect)
