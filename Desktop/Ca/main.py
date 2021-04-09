from Game import *
from entity import *
from bg import *
from MC import *

import pygame
from pygame.locals import *
from random import *
import time


Game = game()#1366, 768)
number_of_fish = 10
st = (Game.width/2, Game.height/2)	

mobs = pygame.sprite.Group()
Bullet_list = pygame.sprite.Group()
Main_Fish = pygame.sprite.GroupSingle()


Fish1 = mc(st, "ca2", Game, bg, 100)
Fish = [fish((randint(0, Game.width * 6 // 8), randint(0, Game.height * 6 // 8)), "ca3", Game, bg, 100)  for i in range(number_of_fish)]

for fish in Fish:
	mobs.add(fish)
Main_Fish.add(Fish1)
bg = bg(-500, -500, Game)
fps = 120
MAX_SPEED = 1000
yet = False
Time = pygame.time.Clock()


while(1):

	#set fps
	Time.tick(fps)
	#process events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == KEYDOWN and event.key == K_F4:
			exit()
		if event.type == KEYDOWN and event.key == K_SPACE:
			Bullet_list.add(Fish1.Fire(bg))
	#bullet on screen
	

	#update
	bg.update(Fish1)

	#bullet hit fish
	hits = pygame.sprite.groupcollide(mobs, Bullet_list, True, True, pygame.sprite.collide_mask)
	for hit in hits:
		hit.kill()
		hit.reborn()
		mobs.add(hit)
	# hits = pygame.sprite.groupcollide(Bullet_list, mobs, True, True)
	# for hit in hits:
	# 	print(hit)
	
	"""
	#hit fish
	for Fish2 in Fish:
		if Fish1.hit(Fish2):
			Fish2.health -= 1
			if Fish2.health == 0:
				Fish2.kill()
	#hit bullet
	for Fish2 in Fish:
		for Bullet in Fish1.bullet:
			if Bullet.name != "" and Fish2.hit(Bullet):
				Bullet.kill()
				Fish2.health -= 1
				if Fish2.health == 0:
					Fish2.kill()
	"""
	#update sprites
	mobs.update(bg, Fish1)

	#mc update
	Main_Fish.update(bg)

	Bullet_list.update(bg)

	# for Fish2 in Fish:
	# 	Fish2.run()
	# 	Fish2.update(bg, Fish1)


	#draw
	bg.draw(Game.screen)
	mobs.draw(Game.screen)
	Bullet_list.draw(Game.screen)
	Main_Fish.draw(Game.screen)
	# for Fish2 in Fish:
	# 	Fish2.draw()
	# Fish1.draw()
	# Fish1.hitbox.draw(Game.screen)
	# Fish2.hitbox.draw(Game.screen)
	pygame.display.flip()	

