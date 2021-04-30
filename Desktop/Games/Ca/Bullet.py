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
	def find_ab(self, mc):
		x0 = self.pos[0]
		y0 = self.pos[1]
		x1 = mc.pos[0]
		y1 = mc.pos[1]
		D = x0 - x1
		Dx = y0 - y1
		Dy = y1 * x0 - x1 * y0
		if D == 0:
			return BULLET_SPEED, 0
		x = Dx/D
		y = Dy/D
		return x, y
	def distance(self,A, B):
		x1 = A[0]
		y1 = A[1]
		x2 = B[0]
		y2 = B[1]
		x = x2 - x1
		y = y2 - y1
		return (x * x + y * y) ** 1/2
	def find_v(self, mc):
		x0 = self.pos[0]
		y0 = self.pos[1]
		a = self.a
		b = self.b
		delta = (-2 * x0 + 2 * a * b - 2 * a * y0) * (-2 * x0 + 2 * a * b - 2 * a * y0) - 4 * (1 + a * a)* (x0 * x0 + (b - y0) * (b - y0) - BULLET_SPEED * BULLET_SPEED)
		delta **= (1/2)
		x1 = (2 * x0 - 2 * a * (b - y0))
		x2 = x1 + delta
		x1 -= delta
		y1 = x1 * a + b
		y2 = x2 * a + b
		A = self.distance((x1, y1), self.pos)
		B = self.distance((x1, y1), mc.pos)
		C = self.distance(self.pos, mc.pos)
		if A + B == C:
			return (x1, y1)
		return (x2, y2)
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
				# self.a,self.b= self.find_ab(mc)
				# vx, vy = self.find_v(mc)
				# self.vx = vx - self.pos[0]
				# self.vy = vy - self.pos[1]
			if type == "boss":
				self.name = "bosss1_animation" + "\\" + "\\" + "bullet" + str(self.delay % 4 + 1) + ".png"
				self.image = pygame.image.load(self.name)
				self.w = self.image.get_width()
				self.h = self.image.get_height()
				self.delay += 1
			self.run()

	def run(self):
		self.rpos = (self.rpos[0] + self.vx, self.rpos[1] + self.vy)