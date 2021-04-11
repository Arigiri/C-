from Game import *
from color import *
from bg import *
from random import *
from MC import *
from Bullet import *
from entity import *
from setting import *
import pygame
vec = pygame.math.Vector2 
class mob1(fish):
	"""docstring for mob1"""
	delay = 599
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob1, self).__init__(pos, name, Game, bg, maxhealth)
		# self.fish = fish(pos, name, Game, bg, maxhealth)

	def Fire(self, mc, bg):
		# self.delay += 1
		# if self.delay == 600:
		# 	self.delay = 0
		# else:
		# 	return bullet()
		x = mc.pos[0] + mc.w/2
		y = mc.pos[1] + mc.h/2
		if self.direction == "LEFT":
			x1 = self.pos[0] - self.bullet[0].w
		else:
			x1  = self.pos[0] + self.w
		y1 = self.pos[1] + self.h/2
		
		vx = x - x1
		vy = y - y1

		# pygame.draw.circle(Game.screen, RED, (x, y), 5)
		# pygame.draw.circle(Game.screen, RED, (x1, y1), 5)
		pygame.display.update()
		# sleep(1)
		Bullet = bullet((x1, y1), self.Game, bg, "dan.png", vx//BULLET_SPEED, vy//BULLET_SPEED)
		# Bullet.update(self.bg, "MOBS")
		return Bullet

