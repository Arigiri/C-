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
		ratio = 4/5
		rate = 5
		print(mc.pos)
		print(self.Game.height * ratio)
		print(self.Game.height // rate)
		if x >= self.Game.width * ratio and mc.vx != 0:
			tmpx -= self.v
		if x <= self.Game.width // rate and mc.vx != 0:
			tmpx += self.v
		if y >= self.Game.height * ratio and mc.vy != 0:
			tmpy -= self.v
		if y <= self.Game.height // rate and mc.vy != 0:
			tmpy += self.v
		# print(tmpx, tmpy)
		tmpx = min(tmpx, 0)
		tmpy = min(tmpy, 0)
		if not(tmpx > 0 or tmpy > 0 or -tmpx + self.Game.width > self.w):
			# print(self.x, tmpx)
			self.x = tmpx
		if not(-tmpy + self.Game.height > self.h):
			# print(self.y, tmpy)
			self.y = tmpy
			
	def __str__(self):
		return "{0},{1}".format(self.x, self.y)
			



