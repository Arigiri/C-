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
			self.name = "mob4\\ca" + str(self.mob) + self.nm + ".png"
		else:
			self.name = "mob4\\cas" + str(self.mob) + self.nm + ".png"
	old_time = 0
	def Slash(self, fish, Game):
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
			self.fire = False
			return
		else: 
			self.yet = False
			self.Slash_Wait = 100

		p1 = fish.rect.center
		p2 = self.rect.center
		p = (p1[0] - p2[0], p1[1] - p2[1])
		if p[1] == 0:
			if self.vx > 0:self.vx = BULLET_SPEED 
			else: self.vx = -BULLET_SPEED
			self.vy = 0
		else:
			ratio = p[0]/p[1]
			if abs(self.vx) > abs(self.vy) and ratio > 1:
				if self.vx > 0:
					self.vx = MOB_SPEED
				else:
					self.vx = -MOB_SPEED
				self.vy = self.vx/ratio
			else:
				if self.vy > 0:
					self.vy = MOB_SPEED
				else:
					self.vy = -MOB_SPEED
				self.vx = self.vy*ratio
			self.old_time = curr_time
			self.fire = True
