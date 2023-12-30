import pygame
from settings import settings
from tanks.tank import *
from tanks.player import *
from tanks.bullet import *
from map.level import *
from tanks.explosion import *

FPS = 30
pygame.init()

screen = pygame.display.set_mode((settings.screen.width, settings.screen.height))
clock = pygame.time.Clock()

pygame.display.set_caption("Bravo Tanks")
icon = pygame.image.load('visual/images/icon.png').convert_alpha()
pygame.display.set_icon(icon)
screen.fill([0, 0, 0])
level1 = Level()
player1 = Player(level=level1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.fire()

        if event.type == pygame.QUIT:  # exit
            running = False

    player1.move()
    for bullet in player1.bullets:
        bullet.update()

    screen.fill((0, 0, 0))  # Очистить экран
    level1.draw(screen)
    player1.draw()
    for bullet in player1.bullets:
        bullet.draw()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
    
