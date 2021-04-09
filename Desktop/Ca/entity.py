from Game import *
from hitbox import *
from color import *
from bg import *
from random import *
from MC import *
from Bullet import *

import pygame
vec = pygame.math.Vector2 
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
	maxv = 10 #vận tốc max
	minv = -10 #vận tốc min
	hitbox = hitbox()

	health = 0
	maxhealth = 0
	health_len = 100

	bullet = [bullet()]
	direction = "LEFT"

	delay = 0
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0): #khai báo
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.rpos = pos
		self.name = name + ".png"
		self.image = pygame.image.load(self.name)
		self.Game = Game
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.bg = bg
		self.rect = self.image.get_rect()#hitbox(self.pos[0], self.pos[1], self.w, self.h)
		self.rect.center = (self.w/2 + self.pos[0], self.h/2 + self.pos[1])
		
		self.maxhealth = maxhealth
		self.health = self.maxhealth
		self.vx = randint(self.minv, self.maxv)
		self.vy = randint(self.minv, self.maxv)
		if self.vy <= 3:
			self.vy = 0
		
		self.health_len = self.w // maxhealth

		
	# def draw(self): #vẽ
	# 	if self.name == "":
	# 		return
	# 	# self.Game.screen.blit(self.image, self.pos)

	# 	self.hitbox = hitbox(self.pos[0], self.pos[1], self.w, self.h, "FISH")
	# 	self.hitbox.draw(self.Game.screen)

	# 	y = self.pos[1] - 10
	# 	x = self.pos[0]
	# 	mw = self.health_len * self.maxhealth
	# 	h = 10
	# 	nw = self.health_len * self.health

	# 	pygame.draw.rect(self.Game.screen, BLACK, (x, y, mw, h))
	# 	pygame.draw.rect(self.Game.screen, GREEN, (x + 1, y + 1, nw, h))

	# def kill(self): #xóa
	# 	self.name = ""
	# 	self.reborn()
		
	def reborn(self):

		self.name = "ca3.png"
		x = 100#randint(self.w, self.Game.width - self.w)
		y = 100#randint(self.h, self.Game.height - self.h)
		# self.pos = (x, y)
		self.rpos = (x, y)
		self.image = pygame.image.load(self.name)
		self.health = self.maxhealth
		self.vx = randint(self.minv, self.maxv)
		self.vy = randint(self.minv, self.maxv)


	def dead(self, fish):
		if self.pos[1] - self.bg.y + self.h >= self.bg.h or self.pos[0] - self.bg.x + self.w >= self.bg.w:
			self.vx = randint(self.minv, self.maxv)
			self.vy = randint(self.minv, 0)
		if self.pos[1] - self.bg.y <= 0 or self.pos[0] - bg.x <= 0:
			self.vx = randint(1, self.maxv)
			self.vy = randint(1, self.maxv)
		# x = self.pos[0] - fish.pos[0]
		# y = self.pos[1] - fish.pos[1]
		# x *= x
		# y *= y
		# if (x + y)  ** (1/2) >= self.Game.height * 2:
		# 	self.kill()
		# 	self.reborn()

	def update(self, bg, mc): #update bot
		self.bg = bg

		if self.delay == 100 or self.rpos[0] < 0 or self.rpos[1] < 0 or self.rpos[0] + self.w > self.bg.w or self.rpos[1] + self.h > self.bg.w:
			self.vx = randint(self.minv, self.maxv)
			self.vy = randint(self.minv, self.maxv)
			self.delay = 0
		if self.vx > 0:
			self.direction = "RIGHT"
		else:
			self.direction = "LEFT"
		if self.direction == "LEFT":
			self.name = "ca3.png"
		else:
			self.name = "cas3.png"
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


	# def hit(self, fishB): #va vào cá B
	# 	pointA = [(self.hitbox.lx, self.hitbox.ly), (self.hitbox.rx, self.hitbox.ry), (self.hitbox.lx, self.hitbox.ry), (self.hitbox.rx, self.hitbox.ly)]
	# 	pointB = [(fishB.hitbox.lx, fishB.hitbox.ly), (fishB.hitbox.rx, fishB.hitbox.ry), (fishB.hitbox.lx, fishB.hitbox.ry), (fishB.hitbox.rx, fishB.hitbox.ly)]
	# 	for i in pointA:
	# 		if fishB.hitbox.inside(i):
	# 			return 1
	# 	for i in pointB:
	# 		if self.hitbox.inside(i):
	# 			return 1
	# 	return False

	def Fire(self, bg):
		if self.direction == "LEFT":
			self.bullet.append(bullet((self.pos[0] - self.bullet[0].w , self.pos[1] + self.h/2), self.Game, bg, "dan.png", self.direction))
		else:
			self.bullet.append(bullet((self.pos[0]  + self.w, self.pos[1] + self.h/2), self.Game, bg, "dan.png", self.direction))

	


