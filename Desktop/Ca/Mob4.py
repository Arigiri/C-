from Game import *
from color import *
from bg import *
from random import *
from MC import *
from Bullet import *
from entity import *
from setting import *
import pygame
class mob4(fish):
	"""docstring for mob1"""
	Del = 0
	Slash_Wait = 100
	nm = "1"
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob4, self).__init__(pos, name, Game, bg, maxhealth, 4)
	def name_detect(self):
		if self.direction == "LEFT":
			self.name = "ca" + str(self.mob) + self.nm + ".png"
		else:
			self.name = "cas" + str(self.mob) + self.nm + ".png"
	old_time = 0
	def Slash(self, fish):
		self.Slash_Wait -= 1
		curr_time = pygame.time.get_ticks()
		if curr_time - self.old_time >= SPLASH_TIME * 100:
			self.yet = True
		else:
			self.yet = False
		if self.yet:
			self.nm = "1"
		else:
			self.nm = "2"
		if self.Slash_Wait != 0:
			return
		else: 
			self.yet = False
			self.Slash_Wait = 100
		x = fish.pos[0] + fish.w/2
		y = fish.pos[1] + fish.h/2
		x1 = self.pos[0] + self.w/2
		y1 = self.pos[1] + self.h/2
		vx = x - x1
		vy = y - y1
		p1 = fish.rect.center
		p2 = self.rect.center
		p = (p1[0] - p2[0], p1[1] - p1[1])
		dist = (p[1] * p[1] + p[0] * p[0]) ** (1/2)
		if dist <= BULLET_SPEED * 100:
			vx *= 3
			vy *= 3
		self.vx = vx//MOBS_SPEED
		self.vy = vy//MOBS_SPEED
		self.old_time = curr_time
