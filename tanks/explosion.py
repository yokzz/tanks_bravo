import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [
            pygame.image.load('visual/images/explosion/explode1.png').convert_alpha(),
            pygame.image.load('visual/images/explosion/explode2.png').convert_alpha()
        ]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.explosion_speed = 5
        self.counter = 0
        
    def update(self):
        self.counter +=1
        if self.counter >= self.explosion_speed:
            self.index +=1
            if self.index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.index]
        
        