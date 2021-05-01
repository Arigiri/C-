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
		self.begin = pos
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
		self.delay = 0
	def update(self, bg, type, mc):
		if self.name == "":
			return
		a = (self.rpos[0] - self.begin[0])
		b = (self.rpos[1] - self.begin[1])
		a *= a
		b *= b

		dist = (a + b) ** (1/2)
		if dist > BULLET_DISTANCE:
			self.kill()

		if type == "MAIN":
			x = self.rpos[0] + bg.x - self.bgx
			y = self.rpos[1] + bg.y - self.bgy
			self.pos = (x, y)
			self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
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
			if type == "boss":
				self.name = "bosss1_animation" + "\\" + "\\" + "bullet" + str(self.delay % 4 + 1) + ".png"
				self.image = pygame.image.load(self.name)
				self.w = self.image.get_width()
				self.h = self.image.get_height()
				self.delay += 1
			self.run()

	def run(self):
		self.rpos = (self.rpos[0] + self.vx, self.rpos[1] + self.vy)
	def __str__(self):
		return self.name + '\n' + str(int(self.pos[0])) + '\n' + str(int(self.pos[1])) + '\n' + str(int(self.rpos[0])) + '\n' + str(int(self.rpos[1])) + '\n' + str(int(self.vx)) + '\n' + str(int(self.vy))
	def write(self, num, type):
		print(1)
		f = open("saves\\bullet" + type + str(num) + ".txt", "w")
		f.write(str(self))
		f.close()
	def read(self, num, type):
		f = open("saves\\bullet" + type + str(num) + ".txt", "r")
		read = f.readlines()
		self.name = read[0][0:len(read[0])- 1]
		self.pos = int(read[1]), int(read[2])
		self.rpos = int(read[3]), int(read[4])
		self.vx = int(read[5])
		self.vy = int(read[6])
		
		f.close()