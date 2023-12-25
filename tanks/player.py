import pygame
from tanks.tank import Tank
from tanks.sprite import Sprite
from settings import settings

class Player(Tank):
    def __init__(self, x = None, y = None, direction=None):
        super().__init__(self, x, y, direction)
        self.rect = Sprite.draw()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.player_speed = 2
        self.screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
        
        self.player_up = [
            pygame.image.load('visual/images/player/player_up1.png').convert_alpha(),
            pygame.image.load('visual/images/player/player_up2.png').convert_alpha()
        ]
        
        self.player_left = [
            pygame.image.load('visual/images/player/player_left1.png').convert_alpha(),
            pygame.image.load('visual/images/player/player_left2.png').convert_alpha()
        ]
        
        self.player_down = [
            pygame.transform.rotate(self.player_up[0], 180),
            pygame.transform.rotate(self.player_up[1], 180)
        ]
        
        self.player_right = [
            pygame.transform.rotate(self.player_up[0], 270),
            pygame.transform.rotate(self.player_up[1], 270)
        ]
        
        if direction == self.DIR_UP:
            counter = 0
            if len(self.player_up) > 1:
                counter = 0
            else:
                self.image = self.player_up[counter]
                counter +=1
                
        if direction == self.DIR_DOWN:
            counter = 0
            if len(self.player_down) > 1:
                counter = 0
            else:
                self.image = self.player_down[counter]
                counter +=1
        
            if x is not None:
                self.rect.x = x
        else:
            self.rect.x = 0

        if y is not None:
            self.rect.y = y
        else:
            self.rect.y = 0

        if direction is None:
            self.direction = self.DIR_UP
            
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction = self.DIR_UP
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.direction = self.DIR_DOWN
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.direction = self.DIR_LEFT
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.direction = self.DIR_RIGHT
            self.rect.x += self.speed
            
    
    def draw(self):
        super().draw()
        self.screen.blit(self.image, self.rect.topleft)