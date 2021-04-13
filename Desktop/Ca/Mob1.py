from Mob4 import *
from entity import *

import pygame
class mob1(fish):
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob1, self).__init__(pos, name, Game, bg, maxhealth, 1)

	old_time = 0
	count_down = 1
	mouth = 2
	shield = False
	def name_detect(self):
		if self.direction == "LEFT":
			self.name = "ca" + str(self.mob) + str(self.mouth) + ".png"
		else:
			self.name = "cas" + str(self.mob) + str(self.mouth) + ".png" 
	def Roar(self):
		curr_time = pygame.time.get_ticks()
		if curr_time - self.old_time >= ROAR_TIME * 100:
			self.mouth = 2
			self.shield = False
		self.count_down -= 1
		if self.count_down == 0:
			self.count_down = 250
		else:
			return
		self.mouth = 1
		self.shield = True
		self.old_time = curr_time
