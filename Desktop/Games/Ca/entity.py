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
	maxv = 3 #vận tốc max
	minv = -3 #vận tốc min
	shield = False
	health = 0
	maxhealth = 0
	health_len = 100
	stay = False
	bullet = [bullet()]
	direction = "LEFT"
	number_of_animation = 2
	fire = False
	delay = 0
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, health = 0, mob = ""): #khai báo
		pygame.sprite.Sprite.__init__(self)

		self.pos = pos
		self.rpos = pos
		self.name = name
		if name == "":
			return
		if self.name[len(self.name) - 1] != 'g':
			self.name += '.png'
		# print(self.name)
		self.image = pygame.image.load(self.name)
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * Game.RATIO //100, h *Game.RATIO//100))
		self.Game = Game
		self.bg = bg
		self.mob = mob
		self.change = 0
		self.mouth = 1
		# if self.mob == 0:
		# 	self.mouth = ""
		self.yet = 1
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		

		self.rect = self.image.get_rect()
		self.rect.center = (self.w/2 + self.pos[0], self.h/2 + self.pos[1])
		
		self.maxhealth = MOB_MAX_HEALTH
		self.health = health

		self.vx = randint(self.minv, self.maxv)
		self.vy = randint(self.minv, self.maxv)
		if self.mob == "100":
			self.number_of_animation = 4
		self.health_len = self.w / MOB_MAX_HEALTH
		self.cot = 0

	def draw_health(self):
		if self.mob == 100:
			return
		y = self.pos[1] - 10
		x = self.pos[0]

		mw = self.health_len * self.maxhealth
		nw = self.health_len * self.health

		h = 10

		pygame.draw.rect(self.Game.screen, BLACK, (x, y, mw, h))
		pygame.draw.rect(self.Game.screen, GREEN, (x + 1, y + 1, nw, h))
	# def draw_health(self, Game):
	# 	max_len = Game.width * 2 / 3
	# 	health_percent = self.health/self.maxhealth
	# 	x = (Game.width - max_len)/2
	# 	y = Game.height/6
	# 	COLOR1 = (111, 116, 111)
	# 	COLOR2 = (58, 58, 58)
	# 	COLOR3 = (34,255,4)
	# 	ls = x + max_len
	# 	w = max_len * health_percent

	# 	pygame.draw.rect(Game.screen, COLOR2, (x,y, max_len,25))
	# 	pygame.draw.rect(Game.screen, RED, (ls -  w + 2.5, y + 2.5, w - 5,25 - 5))
		
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

	def name_detect(self):
		if  self.fire:
			return
		if self.mob == 100:
			for char in self.name:
				if char == 'F':
					return
	
		if self.direction == "LEFT":
			self.name = "ca" + str(self.mob) 
		else:
			self.name = "cas" + str(self.mob) 
		
		self.name = "mob" + str(self.mob) + "\\" + self.name + str(self.cot % self.number_of_animation + 1)
		self.cot += 1
		self.name = self.name +".png"
	def update(self, bg, mc, game): #update bot
		self.bg = bg
		if self.name == "":
			self.kill()
			return

		if (self.delay == 100 or self.rpos[0] <= 0 or self.rpos[1] <= 0 or self.rpos[0] + self.w >= self.bg.w or self.rpos[1] + self.h >= self.bg.w) and self.yet:
			self.vx = randint(self.minv, self.maxv) 
			self.vy = randint(self.minv, self.maxv) 
			if self.mob == 1:
				self.vx *= 3
				self.vy *= 3
			self.delay = 0
		if self.change == 10 and self.mob != 4 and self.mob != 1:
			self.change = 0
			if self.mouth == 1:
				self.mouth = 2
			elif self.mouth != "": self.mouth = 1
		if self.mob == 100:
			self.mouth = ""
		if not self.stay:
			if self.vx > 0:
				self.direction = "RIGHT"
			else:
				self.direction = "LEFT"
		self.name_detect()

		self.image = pygame.image.load(self.name).convert_alpha()

		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * game.RATIO //100, h *game.RATIO//100))

		x = self.rpos[0] + bg.x
		y = self.rpos[1] + bg.y
		x = min(x, bg.w - self.w)
		y = min(y, bg.h - self.h)

		self.pos = (x, y)
		self.rect.center = (self.w/2 + self.pos[0], self.h/2 + self.pos[1])
		self.mask = pygame.mask.from_surface(self.image)
		self.dead(mc)
		if self.stay == False:
			self.run(bg)

	def run(self, bg):
		self.rpos = (self.rpos[0] + self.vx, self.rpos[1] + self.vy)
		x = self.rpos[0]
		y = self.rpos[1]
		x = max(x, 0)
		y = max(y, 0)
		x = min(x, bg.w - self.w)
		y = min(y, bg.h - self.h)
		self.rpos = (x, y)
	def __str__(self):
		return self.name + '\n' + str(int(self.pos[0])) + '\n' + str(int(self.pos[1])) + '\n' + str(int(self.rpos[0])) + '\n' + str(int(self.rpos[1]))+ '\n' + str(self.mob) + '\n' + str(int(self.vx)) + '\n' + str(int(self.vy)) + '\n' + str(self.cot) + '\n' + str(self.health)
	def write(self, num):
		f = open("saves\\" + "entity" + str(num) + ".txt", "w")
		f.write(str(self))
		f.close()
	def read(self, num):
		f = open("saves\\" + "entity" + str(num) + ".txt", "r")
		read = f.readlines()

		self.name = read[0][0:len(read[0]) - 1]
		self.pos = int(read[1]), int(read[2])
		self.rpos = int(read[3]), int(read[4])
		self.mob = int(read[5])
		self.vx = int(read[6])
		self.vy = int(read[7])
		self.cot = int(read[8])
		self.health = int(read[9])
		f.close()



