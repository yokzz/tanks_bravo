import pygame
from settings import settings

screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))

class Bullet():
    (DIR_UP, DIR_DOWN, DIR_LEFT, DIR_RIGHT) = range(4)
    (STATE_ACTIVE, STATE_EXPLODING) = range(2)
        
    def __init__(self, x=0, y=0, direction=None, speed=3, damage=100):
        self.images = [
            pygame.image.load('visual/images/tank/bullet_up.png').convert_alpha(),
            pygame.image.load('visual/images/tank/bullet_down.png').convert_alpha(),
            pygame.image.load('visual/images/tank/bullet_left.png').convert_alpha(),
            pygame.image.load('visual/images/tank/bullet_right.png').convert_alpha()
        ]

        self.image = self.images[direction]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.damage = damage
        self.state = self.STATE_ACTIVE
        self.direction = direction
            
        self.explosion_images = [
            # Ваши изображения для взрыва
        ]
            
    def update(self):
        if self.direction == self.DIR_UP:
            self.rect.topleft = ((self.rect.left - 8), (self.rect.top - self.speed))
        elif self.direction == self.DIR_DOWN:
            self.rect.topleft = (self.rect.left, self.rect.top + self.speed)
        elif self.direction == self.DIR_LEFT:
            self.rect.topleft = (self.rect.left + self.speed, self.rect.top)
        elif self.direction == self.DIR_RIGHT:
            self.rect.topleft = (self.rect.left - self.speed, self.rect.top)

    def draw(self):
        if self.state == self.STATE_ACTIVE:
            screen.blit(self.image, self.rect.topleft)