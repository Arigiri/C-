from Game import *
from entity import *
from bg import *
from MC import *

import pygame
from pygame.locals import *
from random import *
import time
Game = game()#1366, 768)
number_of_fish = 5
st = (Game.width/2, Game.height/2)
Fish1 = mc(st, "ca2", Game, bg, 100)
Fish = [fish((randint(0, Game.width * 6 // 8), randint(0, Game.height * 6 // 8)), "ca3", Game, bg, 100)  for i in range(number_of_fish)]
bg = bg(-10, -10, Game)

MAX_SPEED = 1000
yet = False
Time = pygame.time.Clock()
Time.tick(60)
time.sleep(0.005)
while(1):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == KEYDOWN and event.key == K_F4:
			exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			Fish1.Fire(bg)


		# if pygame.mouse.get_pos()[0] <= 0 or pygame.mouse.get_pos()[0] + Fish1.w >= Game.width or pygame.mouse.get_pos()[1] <= 0 or pygame.mouse.get_pos()[1] + Fish1.h >= Game.height:
		# 	print(pygame.mouse.get_pos())
		# 	pygame.mouse.set_pos(st)

	yet = True
	bg.update(Fish1)
	 

	bg.draw(Game.screen)
	for Fish2 in Fish:
		if Fish1.hit(Fish2):
			Fish2.health -= 1
			exit()
			if Fish2.health == 0:
				Fish2.kill()
	for Fish2 in Fish:
		for Bullet in Fish1.bullet:
			if Bullet.name != "" and Fish2.hit(Bullet):
				Bullet.kill()
				Fish2.health -= 1
				if Fish2.health == 0:
					Fish2.kill()

	Fish1.update(bg)
	for Fish2 in Fish:
		Fish2.run()
		Fish2.update(bg, Fish1)


	
	
	for bullet in Fish1.bullet:
		if bullet.name != "":
			bullet.hitbox.draw(Game.screen)
	for Fish2 in Fish:
		Fish2.draw()
	Fish1.draw()
	# Fish1.hitbox.draw(Game.screen)
	# Fish2.hitbox.draw(Game.screen)
	pygame.display.update()	

