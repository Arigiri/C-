import pygame

#number_of_entities
number_of_mob_0 = 10
number_of_mob_1 = 1
number_of_mob_2 = 1
number_of_mob_3 = 0
number_of_mob_4 = 1
HEALTH_HEIGHT = 25
fps = 60
#main statistic
MAIN_SPEED = 1
MAIN_DAMAGE = 25
MC_HEALTH = 100
MC_IMMUNE_TIME = 25
FULL_STAMIA = 100
#Blade statistic
BLADE_DAMAGE = 8.5
MAIN_BLADE = 1
#MOBS statistic
MOBS_SPEED = 15
#bullet statistic
BULLET_SPEED = 100
BULLET_DAMAGE = 10
BULLET_LIFE_TIME = 60
BULLET_WAIT = 60
#mob1 statistic
ROAR_TIME = 50
#mob2 statistic
BIG_BULLET_SPEED = 45
BIG_BULLET_WAIT = 100
#mob 4 statistic
SPLASH_DAMAGE = 1.5
SPLASH_TIME = 15 #0.x second
#dash statistic
DASH_SPEED = 75
DASH_DISTANT = 50
DASH_RATIO = 3
DASH_TIME = DASH_DISTANT/DASH_SPEED
#entity ratio
RATIO = 70
#stamia consume
DASH_STAMIA = 25
STAMIA_RESTORE = 1
FIRE_STAMIA = 5
BG_SPEED = 25
BLADE_STAMIA = 25
image1 = pygame.image.load("HP1.png")
image2 = pygame.image.load("HP2.png")
image3 = pygame.image.load("HP3.png")
image4 = pygame.image.load("HP4.png")
image6 = pygame.image.load("HP4s.png")

