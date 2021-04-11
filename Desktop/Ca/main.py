from Game import *
from entity import *
from bg import *
from MC import *
from setting import *
from Mob1 import *

import pygame
from pygame.locals import *
from random import *
import time


Game = game()#1366, 768)

st = (Game.width/2, Game.height/2)	

mobs = pygame.sprite.Group()
Bullet_Main = pygame.sprite.Group()
Bullet_Mobs = pygame.sprite.Group()
Main_Fish = pygame.sprite.GroupSingle()


Fish1 = mc(st, "ca2", Game, bg, 100)
Fish = [mob1((randint(0, Game.width * 6 // 8), randint(0, Game.height * 6 // 8)), "ca3", Game, bg, 100)  for i in range(number_of_fish)]

for fish in Fish:
	mobs.add(fish)
	
Main_Fish.add(Fish1)
bg = bg(-500, -500, Game)


Time = pygame.time.Clock()


def health_bar(fish):
	x = fish.Game.width * 70 // 100
	y = HEALTH_HEIGHT
	COLOR = (111, 116, 111)


	w1 = image1.get_width()
	w2 = image2.get_width()
	w3 = image3.get_width()
	w4 = image4.get_width()
	h = image3.get_height()
	fish.health = max(fish.health, 0)

	mw = fish.Game.width - 30  - x
	health_len = mw/100
	nw = fish.health * health_len
	#health bg
	Game.screen.blit(image1, (x + w2, y))
	Game.screen.blit(image1, (x + w2 + w1, y))
	Game.screen.blit(image1, (x + w2 + w1 + w2, y))
	Game.screen.blit(image2, (x, y))
	#curr_health
	
	Game.screen.blit(image6, (x + 15, y + 10))

	if(fish.health == fish.maxhealth):Game.screen.blit(image4, (x + 15, y + 10))
	Game.screen.blit(image3, (x + w4 + 15, y + 10))
	Game.screen.blit(image3, (x + w4 + w1 + 15, y + 10))
	pygame.draw.rect(Game.screen, COLOR, (x + w4 + 15, y + 10, mw - nw, h))



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
			Bullet_Main.add(Fish1.Fire(bg))
			for fish in Fish:
				Bullet_Mobs.add(fish.Fire(Fish1, bg))
	

	#update
	bg.update(Fish1)

	#bullet hit fish
	hits = pygame.sprite.groupcollide(mobs, Bullet_Main, True, True, pygame.sprite.collide_mask)
	for hit in hits:
		hit.health -= BULLET_DAMAGE
		if hit.health == 0:
			hit.kill()
			hit.reborn()
		mobs.add(hit)


	#update mobs
	mobs.update(bg, Fish1)
	Bullet_Mobs.update(bg,"MOBS")

	#mc update
	Main_Fish.update(bg)
	Bullet_Main.update(bg, "MAIN")
	

	#draw
	bg.draw(Game.screen)
	mobs.draw(Game.screen)
	Bullet_Main.draw(Game.screen)
	Bullet_Mobs.draw(Game.screen)
	Main_Fish.draw(Game.screen)

	#draw health
	for fish in mobs:
		fish.draw_health()
	health_bar(Fish1)	
	
	#update display
	pygame.display.flip()
	pygame.display.update()	

