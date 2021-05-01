import pygame
from MC import *
from setting import *
class bg:
	x = 0; y = 0; w = 0; h = 0
	Game = 0
	name = "bg.jpg"
	image = 0
	image = pygame.image.load(name)
	
	def __init__(self, x, y, Game):
		self.x = x
		self.y = y
		self.w = pygame.Surface.get_width(self.image)
		self.h = pygame.Surface.get_height(self.image)
		self.Game = Game
		Ratio1 = int(Game.width / self.w* 100) + 1
		Ratio2 = int(Game.height / self.h * 100) + 1
		Game.Min_ratio = max(Ratio1, Ratio2)

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self, mc):
		x = mc.pos[0]
		y = mc.pos[1]
		tmpx = self.x 
		tmpy = self.y
		ratio = 7/8
		rate = 8
		if x >= self.Game.width - 2 * mc.w and mc.vx != 0:
			tmpx -= BG_SPEED
		if x <=  mc.w and mc.vx != 0:
			tmpx += BG_SPEED
		if y >= self.Game.height - 2 * mc.h and mc.vy != 0:
			tmpy -= BG_SPEED
		if y <= mc.h and mc.vy != 0:
			tmpy += BG_SPEED
		tmpx = min(tmpx, 0)
		tmpy = min(tmpy, 0)
		if not(tmpx > 0 or tmpy > 0 or -tmpx + self.Game.width > self.w):
			if self.x != tmpx:
				self.x = tmpx
		if not(-tmpy + self.Game.height > self.h):
			if self.y != tmpy:
				self.y = tmpy
			
	def __str__(self):
		return	str(self.x) + '\n' + str(self.y)
	def write(self):
		f = open("saves\\bg_save.txt", "w")
		f.write(str(self))
		f.close()
	def read(self):
		f = open("saves\\bg_save.txt", "r")
		read = f.readlines()
		self.x = int(read[0])
		self.y = int(read[1])
		f.close()

			
