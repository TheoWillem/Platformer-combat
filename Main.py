#importation et initialisation pygame
import pygame
pygame.init()

#ipmportation du module random
import random

#importation de la class Game
from Game import Game

#importation des rectangles 
from rects import wall
from rects import rect_trampo 
from rects import rect_plante_platforme


#elements a l'ecran et fenetre
pygame.display.set_caption('TheLittleWizard')
pygame.display.set_icon(pygame.image.load('Fonctionnement\Assets\Wizard Animations\WizardIdle\Icone.png'))

#variable d'affichage
screen = pygame.display.set_mode((1080, 720))
background = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Default mossy cavern.jpg')),(1080, 720))
forground = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Map.png')),(1080, 720))

plant_jump = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/PlantJump/JumpPlant_00.png')),(80,80))

teleporteur_v1 = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/teleporteur_Bleu.png')),(45,100))
teleporteur_v2 = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/teleporteur_Bleu.png')),(45,100))
teleporteur_h1 = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/teleporteur_violet.png')),(110,45))
teleporteur_h2 = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/teleporteur_violet.png')),(110,45))

plante_platforme = pygame.transform.scale((pygame.image.load('Fonctionnement/Assets/Plant Animations/Plant Animations/BlueFlower2/BluePlantClosed_00000.png')),(200,200))
plante_platforme = pygame.transform.flip(pygame.transform.rotozoom(plante_platforme,225,1),False,True)


font1 = pygame.font.SysFont("",37)
font2 = pygame.font.SysFont("",65)

#Nombre de fps 
clock = pygame.time.Clock()

#charger le jeu
game = Game(0,0,0,0)

#variables necessaires à la boucle de jeu
temp_move = 0
gravity = True 
nb_slime_vaincu,nb_slime_vaincu_max = 0,0
etat = 'invincible'
second_invincible = 0
run_pause = False

#boucle de jeu
run = True
while run == True:
    #nombre de fps
    clock.tick(30)
    
    if nb_slime_vaincu_max < nb_slime_vaincu:
        nb_slime_vaincu_max = nb_slime_vaincu
    
    #spone continuel de 3 slimes aleatoirement sur la map
    if len(game.slime.all_slime) < 3 and game.boss.boss_en_jeu == False:
        for rect in range(len(wall)):
            x = random.randint(75,1000)
            y = random.randint(75,680)
            if (wall[rect].colliderect(x,y,50,50) == False) and (len(game.slime.all_slime) < 3) and (game.player.rect.colliderect(x,y,50,50)==False):
                game.slime.spone_slime(x,y)
  
    
    #mise en place du fond 
    screen.blit(background,(0,0))
    screen.blit(forground,(0,0))
    
    for each_boss in game.boss.all_boss:   
        each_boss.attack_en_cour = False
        each_boss.attack_du_slime_prep_rect.y = game.player.rect.y
        each_boss.attack_du_slime_prep_rect.x = game.player.rect.x
        each_boss.attack_du_slime_rect.y = game.player.rect.y
        each_boss.attack_du_slime_rect.x = game.player.rect.x
        each_boss.fct_cooldown() 
        if each_boss.attack_en_prep == True:
            each_boss.gravit_attack_prep()
            temp_rect_x_player = game.player.rect.x
            screen.blit(each_boss.attack_du_slime_prep,(game.player.rect.x,each_boss.attack_du_slime_prep_rect.y ))
        if each_boss.attack_en_cour == True:
            each_boss.sprite = each_boss.sprite_charge_attack
            each_boss.gravit_attack()
            each_boss.attack_du_slime_rect.x = temp_rect_x_player
            each_boss.attack_du_slime_rect.y = each_boss.attack_du_slime_rect.y
            screen.blit(each_boss.attack_du_slime,(temp_rect_x_player,each_boss.attack_du_slime_rect.y))
        each_boss.change_sprite()

    
    text_nb_point = font1.render(f"Ennemis vaincus: {nb_slime_vaincu}",1,"White")
    screen.blit(text_nb_point,(10,10))
    text_point_max = font1.render(f"Meilleur score: {nb_slime_vaincu_max}",1,"White")
    screen.blit(text_point_max,(830,10))
    
    screen.blit(plant_jump,(345,590))
    
    screen.blit(plante_platforme,(525,190))
    
    screen.blit(game.plante_tireuse.sprite,(960,390))
    
    screen.blit(game.plante_vent.sprite,(30,0))
    
    screen.blit(game.plante_tireuse.projectile,(game.plante_tireuse.projectile_rect.x,420))
    game.plante_tireuse.move_projectile()
    
    screen.blit(game.plante_elect.sprite_d,(950,200))
    screen.blit(game.plante_elect.sprite_g,(500,200))

    screen.blit(game.plante_veneneuse.sprite,(600,500))
    
    game.plante_veneneuse.attack_en_cour = False
    if game.player.rect.colliderect(game.plante_veneneuse.sprite_rect):
        game.plante_veneneuse.ennemi_detecter = True
    if game.plante_veneneuse.ennemi_detecter == True:
        game.plante_veneneuse.time_prep_attack += 0.05
        if game.plante_veneneuse.time_prep_attack < 1:
            screen.blit(game.plante_veneneuse.poison_prep,(game.plante_veneneuse.poison_prep_rect.x,game.plante_veneneuse.poison_prep_rect.y))
            game.plante_veneneuse.poison_monte()
        if game.plante_veneneuse.time_prep_attack >= 1 :
            game.plante_veneneuse.attack_en_cour = True
            screen.blit(game.plante_veneneuse.poison_actif,(game.plante_veneneuse.poison_actif_rect.x,game.plante_veneneuse.poison_actif_rect.y))
            game.plante_veneneuse.poison_tombe()
        if game.plante_veneneuse.time_prep_attack > 4 :
            game.plante_veneneuse.time_prep_attack = 0
            game.plante_veneneuse.ennemi_detecter = False
            game.plante_veneneuse.reset()

    screen.blit(teleporteur_v1,(1000,550))
    screen.blit(teleporteur_v2,(45,300))
    screen.blit(teleporteur_h1,(710,625))
    screen.blit(teleporteur_h2,(900,50))

    game.player.all_projectile_right.draw(screen)
    game.player.all_projectile_left.draw(screen)  
        
    game.player.barre_vie()
    screen.blit(pygame.transform.scale(game.player.coeur1,(20,20)),(game.player.rect.x-10,game.player.rect.y-20))
    screen.blit(pygame.transform.scale(game.player.coeur2,(20,20)),(game.player.rect.x+10,game.player.rect.y-20))
    screen.blit(pygame.transform.scale(game.player.coeur3,(20,20)),(game.player.rect.x+30,game.player.rect.y-20))
          
    if game.plante_vent.zone_vent.colliderect(game.player.rect):
        game.player.rect.x += game.plante_vent.puissance_vent  
 
    #spone Boss
    if nb_slime_vaincu%10 == 0  and nb_slime_vaincu != 0 and game.boss.boss_en_jeu == False:
        for rect in range(len(wall)):
            x = random.randint(90,950)
            y = random.randint(90,650)
            if (wall[rect].colliderect(x,y,60,60) == False) and (game.player.rect.colliderect(x,y,50,50)==False) and game.boss.boss_en_jeu == False:       
                game.boss.boss_en_jeu = True
        game.boss.rect.x = x
        game.boss.rect.y = y
        game.boss.spone_boss(x,y,(nb_slime_vaincu**2)*10,(nb_slime_vaincu**2)*10)
    for each_boss in game.boss.all_boss:
        screen.blit(each_boss.sprite, (each_boss.rect.x,each_boss.rect.y))    
            
    #gravite + mouvement slime vert
    for each_slime in game.slime.all_slime:
        each_slime.update_barre_vie()
        screen.blit(each_slime.barre_vie,(each_slime.barre_vie_rect.x,each_slime.barre_vie_rect.y))
        each_slime.tombe = True
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(each_slime.rect.midbottom)== True):
                each_slime.tombe = False
                each_slime.temp_saut = 8
        if rect_plante_platforme.collidepoint(each_slime.rect.midbottom):
            each_slime.tombe = False 
        if each_slime.tombe == True: 
            each_slime.apply_gravity()
            each_slime.move_aleatoire()
        else: 
            each_slime.move_aleatoire()
            each_slime.gravity=0
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(each_slime.rect.center)) == True:
                each_slime.rect.y -= 20
        #saut aleatoire slime vert
        if each_slime.temp_saut > 7:
            each_slime.temp_saut = random.randint(1,1000)
        if float(each_slime.temp_saut) <= 7:
            for rect in range(len(wall)):
                if (wall[rect].collidepoint(each_slime.rect.midtop)) == True :
                    each_slime.temp_move += 1
                    each_slime.rect.y += 1
            if each_slime.temp_move == 0:
                each_slime.move_aleatoire()
                each_slime.rect.y -= each_slime.saut_monter
                for rect in range(len(wall)):
                    if wall[rect].collidepoint(each_slime.rect.midbottom) == True:
                        each_slime.temp_move = 1
                if each_slime.temp_move ==0:
                    each_slime.saut_monter -= 0.3  
            else : 
                each_slime.temp_move = 0 
                each_slime.temp_saut = 8
        else : 
            each_slime.saut_monter = 11
            
        if each_slime.rect.colliderect(rect_trampo):
            each_slime.trampo()
            
        if each_slime.rect.collidepoint(1000,625):
            each_slime.rect.x,each_slime.rect.y = 65,325
        if each_slime.rect.collidepoint(60,350):
            each_slime.rect.x,each_slime.rect.y = 955,550
        if each_slime.rect.collidepoint(750,625):
            each_slime.rect.x,each_slime.rect.y = 950,60  
            
            
            
    for each_boss in game.boss.all_boss:     
        each_boss.update_barre_vie()
        screen.blit(each_boss.barre_vie,(each_boss.barre_vie_rect.x+25,each_boss.barre_vie_rect.y))
        each_boss.tombe = True
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(each_boss.rect.midbottom)== True):
                each_boss.tombe = False
                each_boss.temp_saut = 8
        if rect_plante_platforme.collidepoint(each_boss.rect.midbottom):
            each_boss.tombe = False 
        if each_boss.tombe == True: 
            each_boss.apply_gravity()
            each_boss.move_aleatoire()
        else: 
            each_boss.move_aleatoire()
            each_boss.gravity=0
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(each_boss.rect.center)) == True:
                each_boss.rect.y -= 20
        #saut aleatoire slime vert
        if each_boss.temp_saut > 7:
            each_boss.temp_saut = random.randint(1,1000)
        if float(each_boss.temp_saut) <= 7:
            for rect in range(len(wall)):
                if (wall[rect].collidepoint(each_boss.rect.midtop)) == True :
                    each_boss.temp_move += 1
                    each_boss.rect.y += 1
            if each_boss.temp_move == 0:
                each_boss.move_aleatoire()
                each_boss.rect.y -= each_boss.saut_monter
                for rect in range(len(wall)):
                    if wall[rect].collidepoint(each_boss.rect.midbottom) == True:
                        each_boss.temp_move = 1
                if each_boss.temp_move ==0:
                    each_boss.saut_monter -= 0.3  
            else : 
                each_boss.temp_move = 0 
                each_boss.temp_saut = 8
        else : 
            each_boss.saut_monter = 11
                
        if each_boss.rect.colliderect(rect_trampo):
            each_boss.trampo()
            
        if each_boss.rect.collidepoint(1000,625):
            each_boss.rect.x,each_boss.rect.y = 80,325
        if each_boss.rect.collidepoint(60,350):
            each_boss.rect.x,each_boss.rect.y = 940,550
        if each_boss.rect.collidepoint(750,625):
            each_boss.rect.x,each_boss.rect.y = 950,60 
        
    #collision entre les slimes et projectiles et suppression en cas de plus de pv 
    for projectile in game.player.all_projectile_right:
        for each_boss in game.boss.all_boss:
            if each_boss.rect.colliderect(projectile.rect)== True:
                each_boss.healt -= 34
                game.player.all_projectile_right.remove(projectile)
                #suppression du slime quand il a plus de pv
                if each_boss.healt <= 0:
                    game.boss.boss_en_jeu = False
                    game.boss.all_boss.remove(each_boss)
                    nb_slime_vaincu += 1
                    game.item.spone_drop(each_boss.rect.x,each_boss.rect.y)
                
    for projectile in game.player.all_projectile_left:
        for each_boss in game.boss.all_boss:
            if each_boss.rect.colliderect(projectile.rect)== True:
                each_boss.healt -= 34
                game.player.all_projectile_left.remove(projectile)
                if each_boss.healt <= 0:
                    game.boss.boss_en_jeu = False
                    game.boss.all_boss.remove(each_boss)
                    nb_slime_vaincu += 1
                    game.item.spone_drop(each_boss.rect.x,each_boss.rect.y)

    if nb_slime_vaincu >=10 and game.boss.boss_en_jeu == False :
        for each_drop in game.item.all_drop:
            screen.blit(each_drop.drop,((each_drop.drop_rect.x,each_drop.drop_rect.y)))
            if game.player.rect.colliderect(each_drop.drop_rect):
                game.item.all_drop.remove(each_drop)
                game.player.health = game.player.max_health
    
            
                   
    if game.player.rect.collidepoint(1000,600):
        game.player.rect.x,game.player.rect.y = 65,300
    if game.player.rect.collidepoint(60,350):
        game.player.rect.x,game.player.rect.y = 955,550
    if game.player.rect.collidepoint(730,625) or game.player.rect.collidepoint(750,625) or game.player.rect.collidepoint(780,625):
        game.player.rect.x,game.player.rect.y = 925,60

        
    
    #collision entre les slimes et projectiles et suppression en cas de plus de pv
    for projectile in game.player.all_projectile_right:
        for each_slime in game.slime.all_slime:
            if each_slime.rect.colliderect(projectile.rect)== True:
                each_slime.healt -= 34
                game.player.all_projectile_right.remove(projectile)
                #suppression du slime quand il a plus de pv
                if each_slime.healt <= 0:
                    game.slime.all_slime.remove(each_slime)
                    nb_slime_vaincu += 1
    for projectile in game.player.all_projectile_left:
        for each_slime in game.slime.all_slime:
            if each_slime.rect.colliderect(projectile.rect)== True:
                each_slime.healt -= 34
                game.player.all_projectile_left.remove(projectile)
                if each_slime.healt <= 0:
                    game.slime.all_slime.remove(each_slime)
                    nb_slime_vaincu += 1
                    
    for each_slime in game.slime.all_slime:
        if (each_slime.rect.colliderect(game.player.rect) == True) and etat == 'vincible':
            game.player.health -= 1
            etat = 'invincible'
            
    for each_boss in game.boss.all_boss:
        if (each_boss.rect.colliderect(game.player.rect) == True) and etat == 'vincible':
            game.player.health -= 2
            etat = 'invincible'
                
    if game.plante_tireuse.projectile_rect.colliderect(game.player.rect) and etat == 'vincible':
        game.player.health -= 1
        etat = 'invincible'
        
    game.plante_elect.attack_en_cour = False
    if (game.plante_elect.sprite_d_rect.collidepoint(game.player.rect.midleft or game.player.rect.midright)) or (game.plante_elect.sprite_g_rect.collidepoint(game.player.rect.midleft or game.player.rect.midright)):
        game.plante_elect.ennemi_detecte = True
    if game.plante_elect.ennemi_detecte == True:
        game.plante_elect.time_prep_attack += 0.05
        screen.blit(game.plante_elect.electricity_prepare,((535,200)))
        if game.plante_elect.time_prep_attack >= 2:
            game.plante_elect.attack_en_cour = True
            screen.blit(game.plante_elect.electricity,(535,200))
        if game.plante_elect.time_prep_attack >= 3:
            game.plante_elect.time_prep_attack = 0
            game.plante_elect.ennemi_detecte = False
    
    
    for each_boss in game.boss.all_boss:
        if each_boss.attack_du_slime_rect.colliderect(game.player.rect) and (each_boss.attack_en_cour == True) and (etat == 'vincible'):
            game.player.health -= 2
            etat = 'invincible'
    
    if (game.plante_elect.electricity_rect.colliderect(game.player.rect)) and (game.plante_elect.attack_en_cour == True) and (etat == 'vincible'):
        game.player.health -= 1
        etat = 'invincible'
        
    if (game.plante_veneneuse.poison_actif_rect.colliderect(game.player.rect)) and  (game.plante_veneneuse.attack_en_cour == True) and (etat == 'vincible'):   
        game.player.health -= 1
        etat = 'invincible'
        
    if etat == 'invincible' :
        game.player.sprite = game.player.sprite_invincible
        second_invincible += 0.05
    if second_invincible >= 3:
        game.player.sprite = game.player.sprite_origine
        etat = 'vincible'
        second_invincible = 0
    

    if game.player.health <= 0:
        run_menu = True
    while run_menu :
        game.player.rect.x = 1080
        game.player.rect.y = 720
        screen.blit(game.menu.menu,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if game.menu.bouton_menu_jouer_rect.collidepoint(pygame.mouse.get_pos()) and game.menu.menu_regle_ouvert == False:
                    game.player.health = game.player.max_health
                    game.player.rect.x = 80
                    game.player.rect.y = 300
                    nb_slime_vaincu = 0
                    for each_slime in game.slime.all_slime:
                        each_slime.healt = each_slime.healt_max
                    for each_boss in game.boss.all_boss:
                        game.boss.all_boss.remove(each_boss)
                        game.boss.boss_en_jeu = False
                        game.boss.attack_en_cour = False
                        game.boss.attack_en_prep = False
                        game.boss.cooldown_en_cour = True
                    run_menu = False
                if game.menu.bouton_menu_regle_rect.collidepoint(pygame.mouse.get_pos()):
                    game.menu.menu_regle_ouvert = True
                if game.menu.bouton_menu_regle_menu_rect.collidepoint(pygame.mouse.get_pos()):
                    game.menu.menu_regle_ouvert = False
        if game.menu.menu_regle_ouvert == True:
            screen.blit(game.menu.bouton_menu_regle_regle,(350,50))
            screen.blit(font2.render("Règles",1,"white"),(430,65))
            screen.blit(game.menu.window_regle,(40,135))
            screen.blit(font1.render('-Utilisez "q" et "d" pour vous déplacer et "espace" pour sauter',1,"white"),(110,200))
            screen.blit(font1.render("-Tirez avec la flèche de droite et de gauche selon là où vous voulez tirer",1,"white"),(110,245))
            screen.blit(font1.render("-Vous possédez 3pv",1,"white"),(110,290))
            screen.blit(font1.render("-De nombreux monstres et plantes vous infligeront des dégats",1,"white"),(110,335))
            screen.blit(font1.render("-Après avoir subit des dégats vous êtes invulnérable pendant 3sec",1,"white"),(110,380))
            screen.blit(font1.render("-Tous les 10 monstres tués un boss de plus en plus puissant apparait",1,"white"),(110,425))
            screen.blit(font1.render("-La partie s'arrête lorsque vous n'avez plus de point de vie",1,"white"),(110,470))
            screen.blit(font1.render("-Le but du jeu est de vaincre le plus de monstres possibles",1,"white"),(110,515))
            screen.blit(font1.render("-Bonne chance !",1,"white"),(110,560))
            screen.blit(game.menu.bouton_menu_regle_menu,(350,625))
            screen.blit(font2.render("Menu",1,"white"),(440,645))
        if game.menu.menu_regle_ouvert == False :
            screen.blit(game.menu.bouton_menu_jouer,(10,425))
            screen.blit(game.menu.bouton_menu_regle,(10,525))
            screen.blit(game.menu.bouton_menu_grand,(260,175))
            screen.blit(game.menu.bouton_menu_grand,(260,75))
            screen.blit(font2.render("Jouer",1,"White"),(100,445))
            screen.blit(font2.render(f"Règles",1,"White"),(90,545))
            text_nb_point = font2.render(f"Ennemis vaincus: {nb_slime_vaincu}",1,"White")
            screen.blit(text_nb_point,(325,95))
            text_point_max = font2.render(f"Meilleur score: {nb_slime_vaincu_max}",1,"White")
            screen.blit(text_point_max,(325,195))
        pygame.display.flip()
         
    while run_pause == True :
        screen.blit(pygame.image.load('Fonctionnement/Assets/menu/menu_pause.png'),(0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.Rect(150,440,365,80).collidepoint(pygame.mouse.get_pos()):
                run_pause = False
            if pygame.Rect(555,440,365,80).collidepoint(pygame.mouse.get_pos()):
                run_pause = False
                game.player.health = 0
        

    #bouge le projectile
    for projectile in game.player.all_projectile_right:
            projectile.move_right()
    for projectile in game.player.all_projectile_left: 
            projectile.move_left()

    #sprite joueur
    screen.blit(game.player.sprite, game.player.rect)
    
    #sprite slime
    for each_slime in game.slime.all_slime:
        screen.blit(each_slime.sprite, each_slime.rect)
        
    #plante rebondisante
    if game.player.rect.colliderect(rect_trampo):
        game.player.trampo()

    #mouvement position x du joueur (prise en compte des collisions)
    if game.pressed.get(pygame.K_d):
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(game.player.rect.midright)) or (wall[rect].collidepoint(game.player.rect.topright))== True:
                temp_move += 1
        if temp_move == 0 : game.player.right()
        else : temp_move = 0
    elif game.pressed.get(pygame.K_q):
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(game.player.rect.midleft))or (wall[rect].collidepoint(game.player.rect.topleft))== True:
                temp_move += 1
        if temp_move == 0 : game.player.left()
        else : temp_move = 0

    #mouvement position y du joueur (prise en compte des collisions)
    if (game.pressed.get(pygame.K_SPACE) and game.player.saut_monter > 0) :
        for rect in range(len(wall)):
            if (wall[rect].collidepoint(game.player.rect.midtop))== True:
                temp_move += 1
                game.player.rect.y += 1
        if temp_move == 0 : 
            game.player.saut_monter -= 0.3
            game.player.rect.y -= game.player.saut_monter
        else : 
            temp_move = 0   
    else : game.player.saut_monter = 12
 
    #gravite
    gravity = True
    for rect in range(len(wall)):
        if (wall[rect].collidepoint(game.player.rect.midbottom)== True):
                gravity = False
    if rect_plante_platforme.collidepoint(game.player.rect.midbottom):
            gravity = False 
    if gravity == True: 
        game.player.apply_gravity()   
    else: game.player.gravity=0

    #detection d'evenement
    for event in pygame.event.get():
        #fermer la fenetre
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        #detection d'une touche est enfonce
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_RIGHT and game.player.tourne_d == 1:
                game.player.launch_projectile_right()
            if event.key == pygame.K_LEFT and game.player.tourne_g == 1:
                game.player.launch_projectile_left()
            if event.key == pygame.K_ESCAPE and run_menu == False:
                run_pause = True
        #detection d'une touche est relache
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        #detection boutton est enfoncé
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    #affichage des modification de l'écran
    pygame.display.flip()