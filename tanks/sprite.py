import pygame

class Sprite(pygame.sprite.Sprite): 
    def __init__(self, size, x, y, image = pygame.image.load('visual/images/player/player_up1.png')): 
        super().__init__()
        self.width, self.height = size
        self.image = pygame.transform.scale(pygame.image.load(image), size)
        self.rect = self.image.get_rect(x = x, y = y)
        self.px, self.py = self.rect.x, self.rect.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)