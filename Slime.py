from re import X
import pygame
import random
from rects import wall

class Slime(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.healt = 100
        self.healt_max = 100
        self.attack = 1
        self.velocity = 5
        self.sprite = pygame.image.load("Fonctionnement\Assets\Slimes\SlimeGreen\Slime0.png")
        self.sprite = pygame.transform.scale(self.sprite,(40,40))
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.all_slime = pygame.sprite.Group()
        self.tombe = False
        self.gravity = 0
        self.saut_monter = 11
        self.temp_move = 0
        self.temp_saut = 8
        
        self.barre_100pv = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Vie/Barre_100pv.png"),(70,25))
        self.barre_66pv = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Vie/Barre_66pv.png"),(70,25))
        self.barre_33pv = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Vie/Barre_33pv.png"),(70,25))
        self.barre_vie = self.barre_100pv
        self.barre_vie_rect = self.barre_vie.get_rect()
        self.barre_vie_rect.x = self.rect.x - 15
        self.barre_vie_rect.y = self.rect.y - 10

    def spone_slime(self,x,y):
        self.all_slime.add(Slime(x,y)) 
        
    def update_barre_vie(self):
        self.barre_vie_rect.x = self.rect.x - 15
        self.barre_vie_rect.y = self.rect.y - 10
        if self.healt > 66 :
            self.barre_vie =self.barre_100pv
        if self.healt <= 66 :
            self.barre_vie = self.barre_66pv
        if self.healt <= 33 :
            self.barre_vie = self.barre_33pv

    def apply_gravity(self):
        self.gravity += 0.2
        self.rect.y += self.gravity
        
    def trampo(self):
        self.gravity -= (random.randint(27,36)/10)
        self.rect.y += self.gravity

    def verify_right(self):
        for rect in range(len(wall)) :
            if (wall[rect].collidepoint(self.rect.topright)==True):
                if self.velocity > 0: 
                    self.velocity = (self.velocity*-1)
                    
    def verify_left(self):
        for rect in range(len(wall)) :
            if (wall[rect].collidepoint(self.rect.topleft)==True):
                if self.velocity < 0: 
                    self.velocity = (self.velocity*-1)

    def move_aleatoire(self):
        self.verify_left()
        self.verify_right()
        self.rect.x += self.velocity  