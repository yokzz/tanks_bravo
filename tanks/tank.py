import pygame 
from settings import settings
from tanks.bullet import Bullet


screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
pygame.init()

class Tank(pygame.sprite.Sprite):
    # направления
    (DIR_UP, DIR_DOWN, DIR_RIGHT, DIR_LEFT) = range(4)
    # состояния
    (STATE_ALIVE, STATE_DEAD, STATE_RESPAWNING) = range(3)
    
    def __init__(self, x=None, y=None, direction=None):
        super().__init__()
        self.health = 100 # здоровье танка
        self.speed = 2 # скорость танка
        self.max_active_bullets = 1 # максимально пуль одновременно
        self.shielded = False # танк неуязвим
        self.image = None
        self.bullets = []

        self.spawn_images = [
            pygame.image.load('visual/images/respawning/spawn1.png').convert_alpha(),
            pygame.image.load('visual/images/respawning/spawn2.png').convert_alpha(),
        ]
        
        self.shield_images = [
            pygame.image.load('visual/images/spawning_shield/spawning_shield1.png').convert_alpha(),
            pygame.image.load('visual/images/spawning_shield/spawning_shield2.png').convert_alpha()
        ]
            
        if x and y != None:
            self.rect = pygame.Rect((x, y), (26, 26))
        else:
            self.rect = pygame.Rect(0, 0, 26, 26)    
            
        if direction == None:
            self.direction = self.DIR_UP
    
        else:
            direction = self.direction
        
        self.state = self.STATE_RESPAWNING
        
        
        self.spawn_img_timer = pygame.USEREVENT+1
        pygame.time.set_timer(self.spawn_img_timer, 100)
        self.end_spawn_timer = pygame.USEREVENT+1
        pygame.time.set_timer(self.end_spawn_timer, 100)
        for event in pygame.event.get():
            if event.type == self.spawn_img_timer:
                self.toggle_spawn_image()
            if event.type == self.end_spawn_timer:
                self.end_spawning()
    
    # игрок становиться уязвимимым
    def end_spawning(self):
        self.state = self.STATE_ALIVE
    
    # включение картинки спавна
    def toggle_spawn_image(self):
        if self.state != self.STATE_RESPAWNING:
            return
        
        self.spawn_index +=1
                
        if self.spawn_index >len(self.images)-1:
            self.spawn_index = 0
        
        self.spawn_image = self.spawn_images[self.spawn_index]
        
    def toggle_shield_image(self):
        if self.state != self.STATE_RESPAWNING:
            return
        
        if self.shielded:
            self.shield_index +=1
            if self.shield_index > len(self.shield_images)-1:
                self.shield_index = 0
            self.shield_image = self.shield_images[self.shield_index]
        
    def fire(self):
        global bullets 
        active_bullets = 0

        for bullet in bullets:
            if bullet.state == Bullet.STATE_ACTIVE:
                active_bullets += 1

        if active_bullets < self.max_active_bullets:
            bullet = Bullet(self.rect.topleft[0], self.rect.topleft[1], self.direction)
            self.bullets.append(bullet)
        
            
    def explode(self):
        pass
    
    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
        
        
        
    
        
    
    
        
            
            
        
        
    
