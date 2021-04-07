from Game import *
from hitbox import *
from color import *
from bg import *
from random import *
import pygame

### MAIN CHARACTER ###


class mc:
	name = "" # tên ảnh
	pos = (0, 0) # tọa độ màn
	rpos = (0, 0) # tọa độ bg
	image = "" #ảnh
	Game = 0 #game
	w = 0; h = 0 #chiều rộng, chiều dài
	delay = 0 
	img = 0
	bg = 0 #background
	vx = 0 #vận tốc x
	vy = 0 # vận tốc y
	maxv = 10 #vận tốc max
	minv = 3 #vận tốc min
	hitbox = hitbox()
	health = 0
	maxhealth = 0
	

	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0): #khai báo
		self.pos = pos
		self.rpos = pos
		self.name = name + ".png"
		self.image = pygame.image.load(self.name)
		self.Game = Game
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.bg = bg
		self.hitbox = hitbox(self.pos[0], self.pos[1], self.w, self.h)
		self.vx = randint(self.minv, self.maxv)
		self.vy = randint(self.minv, self.maxv)
		self.maxhealth = maxhealth
		self.health = self.maxhealth

	def health_bar(self):
		 x = self.Game.width * 50 // 100
		 y = 50

		 mw = self.Game.width - 60  - x
		 health_len = mw/100
		 nw = self.health * health_len
		 pygame.draw.rect(self.Game.screen, BLACK, (x, y, mw, y))
		 pygame.draw.rect(self.Game.screen, GREEN, (x, y, nw, y))
		 

	def draw(self): #vẽ
		if self.name == "":
			return
		self.Game.screen.blit(self.image, self.pos)
		self.hitbox = hitbox(self.pos[0], self.pos[1], self.w, self.h)
		self.hitbox.draw(self.Game.screen)
		self.health_bar()


	def update(self): #update nhân vật chính
		pos = pygame.mouse.get_pos()
		x = pos[0]; x = min(pos[0], self.Game.width - self.w)
		y = pos[1]; y = min(pos[1], self.Game.height - self.h)
		self.pos = (x,y)
		self.hitbox = hitbox()
		self.hitbox = hitbox(self.pos[0], self.pos[1], self.pos[0] + self.h, self.pos[1] + self.w)

		self.delay += 1
		if self.delay == 5:
			self.name = "ca" + str(self.img % 2 + 1) + ".png"
			self.image = pygame.image.load(self.name)
			self.delay %= 5
			self.img += 1


	def hit(self, fishB): #va vào cá B
		pointA = [(self.hitbox.lx, self.hitbox.ly), (self.hitbox.rx, self.hitbox.ry), (self.hitbox.lx, self.hitbox.ry), (self.hitbox.rx, self.hitbox.ly)]
		pointB = [(fishB.hitbox.lx, fishB.hitbox.ly), (fishB.hitbox.rx, fishB.hitbox.ry), (fishB.hitbox.lx, fishB.hitbox.ry), (fishB.hitbox.rx, fishB.hitbox.ly)]
		for i in pointA:
			if fishB.hitbox.inside(i):
				return 1
			# pygame.draw.circle(self.Game.screen, RED, i, 3)
		for i in pointB:
			if self.hitbox.inside(i):
				return 1
			# pygame.draw.circle(self.Game.screen, BLACK, i, 1)
		return False

	def kill(self): #xóa
		self.name = ""



