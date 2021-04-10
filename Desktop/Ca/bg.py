  
import pygame
from MC import *
class bg:
	x = 0; y = 0; w = 0; h = 0
	Game = 0
	name = "bg.jpg"
	image = 0
	image = pygame.image.load(name)
	v = 50
	def __init__(self, x, y, Game):
		self.x = x
		self.y = y
		self.w = pygame.Surface.get_width(self.image)
		self.h = pygame.Surface.get_height(self.image)
		self.Game = Game

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self, mc):
		x = mc.pos[0]
		y = mc.pos[1]
		tmpx = self.x 
		tmpy = self.y
		ratio = 7/8
		rate = 8
		# print(mc.pos)
		# print(self.Game.height * ratio)
		# print(self.Game.height // rate)
		if x >= self.Game.width - 2 * mc.w and mc.vx != 0:
			tmpx -= self.v
		if x <=  mc.w and mc.vx != 0:
			tmpx += self.v
		if y >= self.Game.height - 2 * mc.h and mc.vy != 0:
			tmpy -= self.v
		if y <= mc.h and mc.vy != 0:
			tmpy += self.v
		# print(tmpx, tmpy)
		tmpx = min(tmpx, 0)
		tmpy = min(tmpy, 0)
		if not(tmpx > 0 or tmpy > 0 or -tmpx + self.Game.width > self.w):
			# print(self.x, tmpx)
			if self.x != tmpx:
				# mc.move = 0
				# mc.undo(self)
				self.x = tmpx
		if not(-tmpy + self.Game.height > self.h):
			# print(self.y, tmpy)
			if self.y != tmpy:
				# mc.move = 0
				# mc.undo(self)
				self.y = tmpy
			
	def __str__(self):
		return "{0},{1}".format(self.x, self.y)
			
