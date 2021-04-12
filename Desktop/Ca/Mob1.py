from Game import *
from color import *
from bg import *
from random import *
from MC import *
from Bullet import *
from entity import *
from setting import *
import pygame
class mob1(fish):
	"""docstring for mob1"""
	Del = 0
	Slash_Wait = 100
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob1, self).__init__(pos, name, Game, bg, maxhealth, 1)
		
	def Slash(self, fish):
		self.Slash_Wait -= 1
		# print(self.Slash_Wait)
		if self.Del:
			self.Del -= 1
		else:
			self.Del = 100
			self.yet = True
		if self.Slash_Wait != 0:
			return
		else: self.Slash_Wait = 100
		print(1)
		x = fish.pos[0] + fish.w/2
		y = fish.pos[1] + fish.h/2
		x1 = self.pos[0] + self.w/2
		y1 = self.pos[1] + self.h/2
		vx = x - x1
		vy = y - y1
		self.vx = vx//MOBS_SPEED
		self.vy = vy//MOBS_SPEED
		self.yet = False
		Del = 100

