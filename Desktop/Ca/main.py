from Game import *
from entity import *
from bg import *
from MC import *
from setting import *

import pygame
from pygame.locals import *
from random import *
import time


Game = game()#1366, 768)

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


Time = pygame.time.Clock()

def health_bar(fish):
	x = fish.Game.width * 70 // 100
	y = HEALTH_HEIGHT
	fish.health = max(fish.health, 0)

	mw = fish.Game.width - 30  - x
	health_len = mw/100
	nw = fish.health * health_len
	pygame.draw.rect(fish.Game.screen, BLACK, (x, y, mw, y))
	if fish.health == 0:
		return 
	pygame.draw.rect(fish.Game.screen, GREEN, (x + mw - nw, y, nw, y))

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
	

	#update
	bg.update(Fish1)

	#bullet hit fish
	hits = pygame.sprite.groupcollide(mobs, Bullet_list, True, True, pygame.sprite.collide_mask)
	for hit in hits:
		hit.health -= BULLET_DAMAGE
		if hit.health == 0:
			hit.kill()
			hit.reborn()
		mobs.add(hit)
	
	#update sprites
	mobs.update(bg, Fish1)

	#mc update
	Main_Fish.update(bg)
	Bullet_list.update(bg)


	#draw
	bg.draw(Game.screen)
	mobs.draw(Game.screen)
	Bullet_list.draw(Game.screen)
	Main_Fish.draw(Game.screen)

	#draw health
	for fish in mobs:
		fish.draw_health()
	health_bar(Fish1)	

	#update display
	pygame.display.flip()
	pygame.display.update()	

