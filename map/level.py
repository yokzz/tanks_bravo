import pygame
import os
from settings import settings
from map.myrect import MyRect

class Level:
    (TILE_EMPTY, TILE_BRICK, TILE_WATER, TILE_STEEL, TILE_BUSH) = range(5)
    
    TILE_SIZE = 9
    
    def __init__(self, level = 'easy'):
        self.max_active_enemies = 4
        
        tile_images = [
            pygame.Surface((16, 16)),
            pygame.image.load('visual/images/tiles/brick.png').convert_alpha(),
            pygame.image.load('visual/images/tiles/water1.png').convert_alpha(),
            pygame.image.load('visual/images/tiles/water2.png').convert_alpha(),
            pygame.image.load('visual/images/tiles/steel.png').convert_alpha(),
            pygame.image.load('visual/images/tiles/bush.png').convert_alpha()
        ]
        self.tile_empty = tile_images[0]
        self.tile_brick = tile_images[1]
        self.tile_water = [tile_images[2], tile_images[3]]
        self.tile_steel = tile_images[4]
        self.tile_bush = tile_images[5]
        
        self.map = []
        
        self.update_obstacle_rects()
        
        # if level == None:
        #     level = 'easy'
            
        self.load_level(level)
                
    def load_level(self, level = 'easy'):
        filename  = "map/levels/"+str(level)
        if (not os.path.isfile(filename)):
            return False
        f = open(filename, "r")
        data = f.read().split("\n")
        x, y = 0, 0
        for row in data:
            for ch in row:
                if ch == "#":
                    self.map.append(MyRect(x, y, self.TILE_SIZE, self.TILE_SIZE, self.TILE_BRICK))
                elif ch == "@":
                    self.map.append(MyRect(x, y, self.TILE_SIZE, self.TILE_SIZE, self.TILE_STEEL))
                elif ch == "~":
                    self.map.append(MyRect(x, y, self.TILE_SIZE, self.TILE_SIZE, self.TILE_WATER))
                elif ch == "%":
                    self.map.append(MyRect(x, y, self.TILE_SIZE, self.TILE_SIZE, self.TILE_BUSH))
                x += self.TILE_SIZE
            x = 0
            y += self.TILE_SIZE
        return True
            
    def draw(self, screen, tiles=None):   
        if tiles == None:
            tiles = [self.TILE_BRICK, self.TILE_WATER, self.TILE_STEEL, self.TILE_BUSH]
        
        for tile in self.map:
            if tile.type in tiles:
                if tile.type == self.TILE_BRICK:
                    screen.blit(self.tile_brick, tile.topleft)
                if tile.type == self.TILE_WATER:
                    counter = 0
                    if counter > len(self.tile_water):
                        counter = 0
                    else:
                        screen.blit(self.tile_water[counter], tile.topleft)
                if tile.type == self.TILE_STEEL:
                    screen.blit(self.tile_steel, tile.topleft)
                if tile.type == self.TILE_BUSH:
                    screen.blit(self.tile_bush, tile.topleft)
                if tile.type == self.TILE_BRICK:
                    screen.blit(self.tile_brick, tile.topleft)
                    
    def update_obstacle_rects(self):
        self.cannotmove_rects = []
        for tile in self.map:
            if tile.type in (self.TILE_BRICK, self.TILE_STEEL, self.TILE_WATER):
                self.cannotmove_rects.append(tile)
            

pygame.display.update()
pygame.init()
