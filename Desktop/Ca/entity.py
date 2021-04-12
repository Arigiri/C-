from Game import *
from color import *
from bg import *
from random import *
from MC import *
from Bullet import *
from setting import *

import pygame

class fish(pygame.sprite.Sprite):

	name = "" # tên ảnh
	pos = (0, 0) # tọa độ màn
	rpos = (0, 0) # tọa độ bg
	image = "" #ảnh
	Game = 0 #game
	w = 0; h = 0 #chiều rộng, chiều dài
	bg = 0 #background
	vx = 0 #vận tốc x
	vy = 0 # vận tốc y
	maxv = 5 #vận tốc max
	minv = -5 #vận tốc min

	health = 0
	maxhealth = 0
	health_len = 100

	bullet = [bullet()]
	direction = "LEFT"

	delay = 0
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0, mob = ""): #khai báo
		pygame.sprite.Sprite.__init__(self)

		self.pos = pos
		self.rpos = pos
		self.name = name + ".png"
		self.image = pygame.image.load(self.name)
		self.Game = Game
		self.bg = bg
		self.mob = mob
		self.change = 0
		self.mouth = 1
		if self.mob == 3:
			self.mouth = ""
		self.yet = 1
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		

		self.rect = self.image.get_rect()
		self.rect.center = (self.w/2 + self.pos[0], self.h/2 + self.pos[1])
		
		self.maxhealth = maxhealth
		self.health = self.maxhealth

		self.vx = randint(self.minv, self.maxv)
		self.vy = randint(self.minv, self.maxv)

		self.health_len = self.w / maxhealth

	def draw_health(self):
		
		y = self.pos[1] - 10
		x = self.pos[0]

		mw = self.health_len * self.maxhealth
		nw = self.health_len * self.health

		h = 10

		pygame.draw.rect(self.Game.screen, BLACK, (x, y, mw, h))
		pygame.draw.rect(self.Game.screen, GREEN, (x + 1, y + 1, nw, h))
	def reborn(self):

		self.name = "ca" + str(self.mob) + ".png"
		x = randint(self.w, self.Game.width - self.w)
		y = randint(self.h, self.Game.height - self.h)

		self.rpos = (x, y)
		self.image = pygame.image.load(self.name)
		self.health = self.maxhealth

		self.vx = randint(self.minv, self.maxv)
		self.vy = randint(self.minv, self.maxv)


	def dead(self, fish):
		if self.pos[1] - self.bg.y + self.h >= self.bg.h:
			self.vx = randint(self.minv, self.maxv)
			self.vy = randint(self.minv, 0)
		if self.pos[0] - self.bg.x + self.w >= self.bg.w:
			self.vx = randint(self.minv, -1)
			self.vy = randint(self.minv, self.maxv)
		if self.pos[1] - self.bg.y <= 0:
			self.vx = randint(self.minv, self.maxv)
			self.vy = randint(1, self.maxv)
		if self.pos[0] - bg.x <= 0:
			self.vx = randint(1, self.maxv)
			self.vy = randint(self.minv, self.maxv)
		# x = self.pos[0] - fish.pos[0]
		# y = self.pos[1] - fish.pos[1]
		# x *= x
		# y *= y
		# if (x + y)  ** (1/2) >= self.Game.height * 2:
		# 	self.kill()
		# 	self.reborn()

	def update(self, bg, mc, game): #update bot
		self.bg = bg
		if self.name == "":
			self.kill()
			return
		if (self.delay == 100 or self.rpos[0] < 0 or self.rpos[1] < 0 or self.rpos[0] + self.w > self.bg.w or self.rpos[1] + self.h > self.bg.w) and self.yet:
			self.vx = randint(self.minv, self.maxv)
			self.vy = randint(self.minv, self.maxv)
			self.delay = 0
		if self.change == 5:
			self.change = 0
			if self.mouth == 1:
				self.mouth = 2
			elif self.mouth != "": self.mouth = 1
		if self.vx > 0:
			self.direction = "RIGHT"
		else:
			self.direction = "LEFT"
		if self.direction == "LEFT":
			self.name = "ca" + str(self.mob) + str(self.mouth) + ".png"
		else:
			self.name = "cas" + str(self.mob) + str(self.mouth) + ".png"
		self.delay += 1
		self.image = pygame.image.load(self.name)
		x = self.rpos[0] + bg.x
		y = self.rpos[1] + bg.y
		self.pos = (x, y)
		self.rect.center = (self.w/2 + self.pos[0], self.h/2 + self.pos[1])
		self.mask = pygame.mask.from_surface(self.image)
		self.dead(mc)
		self.run()

	def run(self):
		self.rpos = (self.rpos[0] + self.vx, self.rpos[1] + self.vy)

	


