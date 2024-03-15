import pygame

class Menu():
    def __init__(self):
        self.menu = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/menu_foret.jpg'),(1080,720))
        
        self.bouton_menu_grand = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/bouton_menu_grand.png'),(550,80))
        
        self.bouton_menu_jouer = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/bouton_menu.png'),(300,75))
        self.bouton_menu_jouer_rect = self.bouton_menu_jouer.get_rect()
        self.bouton_menu_jouer_rect.x = 10
        self.bouton_menu_jouer_rect.y = 425
        
        self.window_regle = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/window_rules.png'),(1000,500))
        self.bouton_menu_regle = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/bouton_menu.png'),(300,75))
        self.bouton_menu_regle_rect = self.bouton_menu_regle.get_rect()
        self.bouton_menu_regle_rect.x = 10
        self.bouton_menu_regle_rect.y = 525
        self.menu_ouvert = True
        self.menu_regle_ouvert = False
        
        self.bouton_menu_regle_regle = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/bouton_menu.png'),(300,75))
        self.bouton_menu_regle_regle_rect = self.bouton_menu_regle_regle.get_rect()
        self.bouton_menu_regle_regle_rect.x = 375
        self.bouton_menu_regle_regle_rect.y = 50
        
        self.bouton_menu_regle_menu = pygame.transform.scale(pygame.image.load('Fonctionnement/Assets/menu/bouton_menu.png'),(300,75))
        self.bouton_menu_regle_menu_rect = self.bouton_menu_regle_menu.get_rect()
        self.bouton_menu_regle_menu_rect.x = 350
        self.bouton_menu_regle_menu_rect.y = 625
        