import pygame
from pygame import mixer
from tanks.tank import Tank
from tanks.bullet import Bullet
from map.level import *
from settings import settings
from tanks.explosion import *

SIZE = 13
screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
pygame.init()
mixer.init()


class Player(Tank):
    def __init__(self, x=0, y=0, direction=None, level = None):
        super().__init__()
        self.image = pygame.image.load('visual/images/player/player_up1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.level = level
        self.direction = direction
        self.player_speed = 2
        self.counter = 0
        self.bullets = []
        self.level = level if level is not None else Level()
        self.level.update_obstacle_rects()
        
        
        self.lives = 3
        
        mixer.music.load('visual/sounds/background.ogg')
        
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
            pygame.transform.rotate(self.player_left[0], 180),
            pygame.transform.rotate(self.player_left[1], 180)
        ]
        
        
        if x is not None:
            self.rect.x = x
        else:
            self.rect.x = 0

        if y is not None:
            self.rect.y = y
        else:
            self.rect.y = 0
            
        
    def move(self):
        keys = pygame.key.get_pressed()
        new_rect = self.rect.copy()
        
        if keys[pygame.K_w]:
            self.direction = self.DIR_UP
            new_rect.y -= self.player_speed
            self.check_collision(new_rect)
            self.counter +=1
            if self.counter >= len(self.player_up):
                self.counter = 0
            self.image = self.player_up[self.counter]
                
        elif keys[pygame.K_s]:
            self.direction = self.DIR_DOWN
            new_rect.y += self.player_speed
            self.check_collision(new_rect)
            self.counter +=1
            if self.counter >= len(self.player_down):
                self.counter = 0
            self.image = self.player_down[self.counter]
        
        elif keys[pygame.K_a]:
            self.direction = self.DIR_LEFT
            new_rect.x -= self.player_speed
            self.check_collision(new_rect)
            self.counter += 1
            if self.counter >= len(self.player_left):
                self.counter = 0
            self.image = self.player_left[self.counter]
        
        elif keys[pygame.K_d]:
            self.direction = self.DIR_RIGHT
            new_rect.x += self.player_speed
            self.check_collision(new_rect)
            self.counter += 1
            if self.counter >= len(self.player_right):
                self.counter = 0
            self.image = self.player_right[self.counter]
    
    def check_collision(self, new_rect):
        for obstacle in self.level.cannotmove_rects:
            if new_rect.colliderect(obstacle):
                return
            
        self.rect = new_rect
        
    def fire(self):
        bullet = Bullet(self.rect.topleft[0], self.rect.topleft[1], self.direction)
        self.bullets.append(bullet)
            
    
    def draw(self):
        screen.blit(self.image, self.rect.topleft)
