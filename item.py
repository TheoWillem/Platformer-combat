import pygame
from Boss import Boss

class Item(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.drop = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/vie/coeur_plein.png')),(50,45))
        self.drop_rect = self.drop.get_rect()
        self.drop_rect.x = x
        self.drop_rect.y = y
        self.all_drop = pygame.sprite.Group()
    
    def spone_drop(self,x,y):
        self.all_drop.add(Item(x,y))