#importation et initialisation pygame
import pygame
pygame.init()
from Projectile_BlueBall import BlueBall


clock = pygame.time.Clock()
collision = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 0
        self.max_health = 6
        self.attack = 34
        self.velocity = 7
        self.sprite = pygame.image.load('Fonctionnement/Assets/Wizard Animations/WizardIdle/Chara1.png').convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite,(40,60))
        self.sprite_origine = self.sprite
        self.sprite_invincible = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Wizard Animations/WizardIdle/domaged_wizard.png')),(37,60)).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.x = 80
        self.rect.y = 300
        self.saut_monter = 10
        self.gravity = 0
        self.all_projectile_right = pygame.sprite.Group()
        self.all_projectile_left = pygame.sprite.Group()
        self.tourne_g = 0
        self.tourne_d = 1

        self.coeur_plein = pygame.transform.flip(pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/vie/coeur_plein.png')),(50,45)),True,False)
        self.coeur_moitier_plein = pygame.transform.flip(pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/vie/coeur_moitier_plein.png')),(50,45)),True,False)
        self.coeur_vide = pygame.transform.flip(pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/vie/coeur_vide.png')),(50,45)),True,False)
        self.coeur1 = self.coeur_plein
        self.coeur2 = self.coeur_plein
        self.coeur3 = self.coeur_plein
        
    def barre_vie(self):
        if self.health == 6:
            self.coeur1,self.coeur2,self.coeur3 = self.coeur_plein,self.coeur_plein,self.coeur_plein
        if self.health == 5:
            self.coeur1,self.coeur2,self.coeur3 = self.coeur_moitier_plein,self.coeur_plein,self.coeur_plein
        if self.health == 4:
            self.coeur1,self.coeur2,self.coeur3 = self.coeur_vide,self.coeur_plein,self.coeur_plein
        if self.health == 3:
            self.coeur1,self.coeur2,self.coeur3 = self.coeur_vide,self.coeur_moitier_plein,self.coeur_plein
        if self.health == 2:
            self.coeur1,self.coeur2,self.coeur3 = self.coeur_vide,self.coeur_vide,self.coeur_plein
        if self.health == 1:
            self.coeur1,self.coeur2,self.coeur3 = self.coeur_vide,self.coeur_vide,self.coeur_moitier_plein
            
    def right(self):
        if self.tourne_d == 0:
            self.tourne_d = 1
            self.tourne_g = 0
            self.sprite = pygame.transform.flip(self.sprite,True,False)
            self.sprite_origine = pygame.transform.flip(self.sprite_origine,True,False)
            self.sprite_invincible = pygame.transform.flip(self.sprite_invincible,True,False)
        self.rect.x += self.velocity
    
    def left(self):
        if self.tourne_g == 0:
            self.tourne_g = 1
            self.tourne_d = 0
            self.sprite = pygame.transform.flip(self.sprite,True,False)
            self.sprite_origine = pygame.transform.flip(self.sprite_origine,True,False)
            self.sprite_invincible = pygame.transform.flip(self.sprite_invincible,True,False)
        self.rect.x -= self.velocity

    def apply_gravity(self):
        #a mettree en definitif a 0.25
        self.gravity += 0.25
        self.rect.y += self.gravity

    def trampo(self):
        self.gravity -= 3.4
        self.apply_gravity()

    def launch_projectile_right(self):
        self.all_projectile_right.add(BlueBall(self))
    def launch_projectile_left(self):
        self.all_projectile_left.add(BlueBall(self))