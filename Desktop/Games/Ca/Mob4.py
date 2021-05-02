from Game import *
from color import *
from bg import *
from random import *
from MC import *
from Bullet import *
from entity import *
from setting import *
import pygame
class mob4(fish):
	"""docstring for mob1"""
	Del = 0
	Slash_Wait = 100
	nm = "1"
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob4, self).__init__(pos, name, Game, bg, maxhealth, 4)
	def name_detect(self):
		if self.direction == "LEFT":
			self.name = "mob4\\ca" + str(self.mob) + self.nm + ".png"
		else:
			self.name = "mob4\\cas" + str(self.mob) + self.nm + ".png"
	old_time = 0
	def find_ab(self, mc):
		x0 = self.pos[0]
		y0 = self.pos[1]
		x1 = mc.pos[0]
		y1 = mc.pos[1]
		D = x0 - x1
		Dx = y0 - y1
		Dy = y1 * x0 - x1 * y0
		if D == 0:
			return SPLASH_SPEED, 0
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
		delta = (-2 * x0 + 2 * a * b - 2 * a * y0) * (-2 * x0 + 2 * a * b - 2 * a * y0) - 4 * (1 + a * a) * (x0 * x0 + (b - y0) * (b - y0) - SPLASH_SPEED * SPLASH_SPEED)
		delta **= (1/2)
		x1 = ((2 * x0 - 2 * a * (b - y0)) - delta)/(2 * (1 + a * a))
		x2 = ((2 * x0 - 2 * a * (b - y0)) + delta)/(2 * (1 + a * a))
		# x1 -= delta
		y1 = x1 * a + b
		y2 = x2 * a + b
		A = self.distance((x1, y1), self.pos)
		B = self.distance((x1, y1), mc.pos)
		C = self.distance(self.pos, mc.pos)
		if A + B == C:
			return (x1, y1)
		return (x2, y2)

	def Slash(self, fish, Game):
		self.Slash_Wait -= 1
		curr_time = pygame.time.get_ticks()
		if curr_time - self.old_time >= SPLASH_TIME * 100:
			self.yet = True
		else:
			self.yet = False
		if self.yet:
			self.nm = "1"
		else:
			self.nm = "2"
		if self.Slash_Wait != 0:
			self.fire = False
			return
		else: 
			self.yet = False
			self.Slash_Wait = 100

		self.a, self.b = self.find_ab(fish)
		self.vx, self.vy = self.find_v(fish)
		self.vx = abs(self.vx - self.pos[0])
		self.vy = abs(self.vy - self.pos[1])
		if fish.pos[0] < self.pos[0]:

			self.vx *= -1
		if fish.pos[1] < self.pos[1]:
			self.vy *= -1
			self.old_time = curr_time
			self.fire = True
