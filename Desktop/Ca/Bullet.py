import pygame
from Game import *
from bg import *
from setting import *
from math import *
class bullet(pygame.sprite.Sprite):
	pos = (0, 0)
	rpos = (0, 0)
	name = ""
	image = ""
	Game = 0
	bg = 0
	w = 40
	h = 0
	bgx = 0
	bgy = 0
	v = 50
	life = 0
	direction = 0
	angle = 0
	def __init__(self, pos = 0, Game = 0, bg = 0, name = "", vx = 0, vy = 0):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.rpos = pos
		self.Game = Game
		self.bg = bg
		self.name = name
		self.vx = vx
		self.vy = vy
		self.life = BULLET_LIFE_TIME
		if(self.name == ""):
			return

		self.image = pygame.image.load(name)
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * 50 //100, h *50//100))
		self.w = self.image.get_width()
		self.h = self.image.get_height()

		self.bgx = self.bg.x
		self.bgy = self.bg.y

		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

	def update(self, bg, type, mc):
		if self.name == "":
			return
		
		self.life -= 1
		if self.life == 0:
			self.kill()
		if type == "MAIN":
			x = self.rpos[0] + bg.x - self.bgx
			y = self.rpos[1] + bg.y - self.bgy
			self.pos = (x, y)
			self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		# if self.pos[0] < self.bg.x or self.pos[0] + self.w - bg.x > self.bg.w or self.pos[1] < bg.y or self.pos[1] + self.h - bg.y > self.bg.h:
		# 	self.kill()
			self.run()
		else:
			
			x = self.rpos[0] - self.bgx + bg.x
			y = self.rpos[1] - self.bgy + bg.y
			self.pos = (x, y)
			self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
			if type == "mobs_0" and self.angle == 0:
				mcx = mc.pos[0] - self.rpos[0]
				mcy = mc.pos[1] - self.rpos[1]
				self.angle = atan2(-mcy,mcx)
				self.angle %= 2*pi
				self.angle = degrees(self.angle)

				self.image = pygame.transform.rotate(self.image, self.angle)
			self.run()

	def run(self):
		self.rpos = (self.rpos[0] + self.vx, self.rpos[1] + self.vy)