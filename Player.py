import pygame

class Player():

    def __init__(self, screen_w, screen_h, health = 3):
        width = 50
        height =  50
        self.rect = pygame.Rect(screen_w//2, round(screen_h*0.85), width, height) 
        self.speed = 1
        self.color = (0,0, 255)
        self.cooldown = 500
        self.last = pygame.time.get_ticks()
        self.health = health

    def move(self, value, screen_w):
        self.rect.x = (self.rect.x + self.speed*value) % screen_w 
    
    def can_shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            return True 
        return False

    def draw(self,surf):
        pygame.draw.rect(surf, self.color,self.rect)
