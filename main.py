import pygame
from settings import settings
from tanks.player import Player
from map.level import Level

pygame.init()

screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
pygame.display.set_caption("Bravo Tanks")
icon = pygame.image.load('Visual/images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

running = True
while running:
    # player1 = Player()
    # player1.draw()
    # player1.move()
    level1 = Level()
    level1.draw()
    
    pygame.display.update()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # exit
            running = False
            
    