import pygame
import random
from rects import wall

class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y,healt,healt_max):
        super().__init__()
        self.healt = healt
        self.healt_max = healt_max
        self.attack = 2
        self.original_velocity = 4.5
        self.velocity = 4.5
        self.sprite_original = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Slimes/SlimeOrange/SlimeOrange_00014.png').convert_alpha(),(100,70))
        self.sprite_charge_attack = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Slimes/SlimeOrange/SlimeOrange_attack_prep.png').convert_alpha(),(100,90))
        self.sprite = self.sprite_original
        self.rect = self.sprite.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.boss_en_jeu = False
        self.tombe = False
        self.gravity = 0
        self.saut_monter = 11
        self.temp_move = 0
        self.temp_saut = 8
        self.all_boss = pygame.sprite.Group()
    
        self.barre_100pv = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Vie/Barre_100pv.png"),(70,25))
        self.barre_66pv = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Vie/Barre_66pv.png"),(70,25))
        self.barre_33pv = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Vie/Barre_33pv.png"),(70,25))
        self.barre_vie = self.barre_100pv
        self.barre_vie_rect = self.barre_vie.get_rect()
        self.barre_vie_rect.x = self.rect.x + 30
        self.barre_vie_rect.y = self.rect.y - 10
        
        self.attack_du_slime_prep = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Slimes/SlimeOrange/attack_prep.png"),(40,60))
        self.attack_du_slime_prep_rect = self.attack_du_slime_prep.get_rect()
        self.attack_du_slime_prep_rect.x = 100
        self.attack_du_slime_prep_rect.y = 100
        self.attack_du_slime = pygame.transform.scale(pygame.image.load("Fonctionnement/Assets/Slimes/SlimeOrange/attack_actif.png"),(40,60))
        self.attack_du_slime_rect = self.attack_du_slime.get_rect()
        self.attack_du_slime_rect.x = 100
        self.attack_du_slime_rect.y = 100
        self.time_prep_attack = 0
        self.attack_en_prep = False
        self.attack_en_cour = False
        self.cooldown_en_cour = True
        self.cooldown = 180

    def change_sprite(self):
        if self.attack_en_cour == True:
            self.sprite = self.sprite_charge_attack
            self.velocity = 0
        else : 
            self.sprite = self.sprite_original
            self.velocity = self.original_velocity
    
    def gravit_attack(self):
        collision = False
        while collision == False:
            for rect in range(len(wall)) :
                if wall[rect].colliderect(self.attack_du_slime_rect) == True :
                    collision = True
            if collision == False :
                self.attack_du_slime_rect.y += 5
                      
    def gravit_attack_prep(self):
        collision = False
        while collision == False:
            for rect in range(len(wall)) :
                if wall[rect].colliderect(self.attack_du_slime_prep_rect) == True :
                    collision = True
            if collision == False :
                self.attack_du_slime_prep_rect.y += 10
            
    def fct_cooldown(self):
        if self.cooldown_en_cour == True:
            self.cooldown -= 1
            if self.cooldown >= 100:
                self.attack_en_cour = False
            if 45 <= self.cooldown <= 90:
                self.attack_en_prep = True
            if self.cooldown <= 15:
                self.attack_en_prep = False
                self.attack_en_cour = True
            if self.cooldown == 0:
                self.cooldown = 180
        
        
    def prepare_attack(self):
        if self.cooldown <= 1:
            self.attack_en_cour = True
        
    def spone_boss(self,x,y,healt,healt_max):
        self.all_boss.add(Boss(x,y,healt,healt_max))
        
    def update_barre_vie(self):
        self.barre_vie_rect.x = self.rect.x - 15
        self.barre_vie_rect.y = self.rect.y - 10
        if self.healt > ((self.healt_max/3)*2) :
            self.barre_vie =self.barre_100pv
        if self.healt <= ((self.healt_max/3)*2) :
            self.barre_vie = self.barre_66pv
        if self.healt <= (self.healt_max/3) :
            self.barre_vie = self.barre_33pv

    def apply_gravity(self):
        self.gravity += 0.2
        self.rect.y += self.gravity
        
    def trampo(self):
        self.gravity -= (random.randint(26,34)/10)
        self.rect.y += self.gravity

    def verify_right(self):
        for rect in range(len(wall)) :
            if (wall[rect].collidepoint(self.rect.topright)==True):
                if self.velocity > 0: 
                    self.velocity = (self.velocity*-1)
                    self.original_velocity = (self.original_velocity*-1)
                    
    def verify_left(self):
        for rect in range(len(wall)) :
            if (wall[rect].collidepoint(self.rect.topleft)==True):
                if self.velocity < 0: 
                    self.velocity = (self.velocity*-1)
                    self.original_velocity = (self.original_velocity*-1)

    def move_aleatoire(self):
        self.verify_left()
        self.verify_right()
        self.rect.x += self.velocity
