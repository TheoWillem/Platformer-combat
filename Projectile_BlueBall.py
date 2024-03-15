import pygame
from rects import wall

class BlueBall(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.player = player
        self.velocity = 10
        self.image = pygame.image.load('Fonctionnement\Assets\Wizard Animations\BlueBall.png')
        self.image = pygame.transform.scale(self.image,(20,20)) 
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.centerx -10
        self.rect.y = player.rect.centery -5
        self.angle = 0
        self.sprite_base = self.image

    def rotate(self):
        self.angle = self.angle + 5
        self.image = pygame.transform.rotozoom(self.sprite_base,self.angle,1)

    def verify_collision_right(self):
        for rect in range(len(wall)) :
            if wall[rect].colliderect(self):
                self.player.all_projectile_right.remove(self)

    def verify_collision_left(self):
        for rect in range(len(wall)) :
            if wall[rect].colliderect(self):
                self.player.all_projectile_left.remove(self)

    def move_right(self):
        self.rotate()
        self.verify_collision_right()
        self.player.vers_d = 1
        self.rect.x += self.velocity

    def move_left(self):
        self.rotate()
        self.verify_collision_left()
        self.player.vers_g = 1
        self.rect.x -= self.velocity