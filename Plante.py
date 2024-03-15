import pygame
pygame.init()

class Plante_tireuse(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/Plant 8 Poison/PlantPosion_00000.png')),(90,90))
        self.sprite = pygame.transform.flip(pygame.transform.rotozoom(self.sprite,270,1),False,False)
        self.projectile = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/Plant 8 Poison/Boule_jaune.png')),(25,25))
        self.projectile_rect = self.projectile.get_rect()
        self.projectile_rect.x = 940
        self.projectile_rect.y = 420
        
    def move_projectile(self):
        self.projectile_rect.x -= 5
        if self.projectile_rect.x <= 45:
            self.projectile_rect.x = 940
            
class Plante_elect(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite_g = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/Plant 7/plant_elect.png'),(70,100))
        self.sprite_g_rect = self.sprite_g.get_rect()
        self.sprite_g_rect.x = 490
        self.sprite_g_rect.y = 200
        
        self.sprite_d = pygame.transform.flip(self.sprite_g,True,False)
        self.sprite_d_rect = self.sprite_d.get_rect()
        self.sprite_d_rect.x = 930
        self.sprite_d_rect.y = 200
        
        self.ennemi_detecte = False
        self.time_prep_attack = 0
        self.attack_en_cour = False
        
        self.electricity = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/Plant 7/arc_electrique.png')),(445,80))
        self.electricity_rect = self.electricity.get_rect()
        self.electricity_rect.x = 535
        self.electricity_rect.y = 200
        
        self.electricity_prepare = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/Plant 7/arc_electrique_prepare.png')),(445,80))
        self.electricity_prepare_rect = self.electricity.get_rect()
        
class Plante_vent(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.transform.rotozoom(pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/plante_vent.png'),(300,300)),275,1)
        self.sprite_rect = self.sprite.get_rect()
        self.zone_vent = pygame.Rect(190,70,320,90)
        self.puissance_vent = 2

class Plante_veneneuse(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.transform.rotozoom(pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/plante_veneneuse.png'),(50,75)),5,1)
        self.sprite_rect =self.sprite.get_rect()
        self.sprite_rect.x = 600
        self.sprite_rect.y = 500
        self.poison_prep = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/spore_prep.png'),(35,60))
        self.poison_prep_rect = self.poison_prep.get_rect()
        self.poison_prep_rect.x = 600
        self.poison_prep_rect.y = 500
        self.poison_actif = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/spore.png'),(40,50))
        self.poison_actif_rect = self.poison_actif.get_rect()
        self.poison_actif_rect.x = 600
        self.poison_actif_rect.y = 400
        self.ennemi_detecter = False
        self.attack_en_cour = False
        self.time_prep_attack = 0
        
    def reset(self):
        self.poison_prep_rect.y = 500
        self.poison_actif_rect.y = 400
        
    def poison_monte(self):
        self.poison_prep_rect.y -= 5
    
    def poison_tombe(self):
        self.poison_actif_rect.y += 1.5