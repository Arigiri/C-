from Game import *
from entity import *
from bg import *
from MC import *

import pygame
from pygame.locals import *
from random import *

Game = game()#1366, 768)

Fish1 = mc((50, 100), "ca2", Game, bg)
Fish2 = fish((60, 100), "ca3", Game, bg)
bg = bg(-10, -10, Game)

MAX_SPEED = 1000
yet = False
time = pygame.time.Clock()
time.tick(60)
while(1):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == KEYDOWN and event.key == K_F4:
			exit()

		if pygame.mouse.get_pos()[0] < 0 or pygame.mouse.get_pos()[0] + Fish1.w > Game.width or pygame.mouse.get_pos()[1] > 0 or pygame.mouse.get_pos()[1] + Fish1.h < Game.height:
			x = max(pygame.mouse.get_pos()[0], 0)
			x = min(x, Game.width - Fish1.w)
			y = max(pygame.mouse.get_pos()[1], 0)
			y = min(y, Game.height - Fish1.h)
			pygame.mouse.set_pos((x, y))

	yet = True
	bg.update()
	

	bg.draw(Game.screen)
	if Fish1.hit(Fish2):
		Fish2.kill()
		x = randint(1, Game.width - Fish2.w)
		y = randint(1, Game.height - Fish2.h)
		Fish2 = fish((x, y), "ca3", Game)

	Fish1.update()
	Fish2.run()
	Fish2.update(bg)

	Fish1.draw()
	Fish2.draw()
	# Fish1.hitbox.draw(Game.screen)
	# Fish2.hitbox.draw(Game.screen)
	pygame.display.update()	

