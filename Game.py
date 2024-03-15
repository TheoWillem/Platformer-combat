import pygame
from Player import Player
from Projectile_BlueBall import BlueBall
from Slime import Slime
from Plante import Plante_tireuse
from Plante import Plante_elect
from Plante import Plante_vent
from Plante import Plante_veneneuse
from Menu import Menu
from Boss import Boss
from item import Item

class Game():
    def __init__(self,x,y,healt,healt_max) :
        self.player = Player()
        self.blueball = BlueBall(self.player)
        self.slime = Slime(x,y)
        self.plante_tireuse = Plante_tireuse()
        self.plante_elect = Plante_elect()
        self.plante_vent = Plante_vent()
        self.plante_veneneuse = Plante_veneneuse()
        self.menu = Menu()
        self.boss = Boss(x,y,healt,healt_max)
        self.item = Item(x,y)
        self.pressed = {}

