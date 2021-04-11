from Game import *
from color import *
from bg import *
from random import *
from Bullet import *
from time import *
from setting import *
import pygame

### MAIN CHARACTER ###


class mc(pygame.sprite.Sprite):
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

	health = 0
	maxhealth = 0
	bullet = [bullet()]
	direction = "LEFT"

	mousepos = 0
	
	move = 1
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
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

		self.maxhealth = maxhealth
		self.health = self.maxhealth
		self.mousepos = pos
		self.mousepos = (self.Game.width/2, self.Game.height/2)

		pygame.mouse.set_pos(self.mousepos)
		

		 


	def update(self, bg): #update nhân vật chính
		if self.move == 0:
			self.move = 1
			pygame.mouse.set_pos((self.Game.width/2, self.Game.height/2))
			return
		mousepos = pygame.mouse.get_pos()
		self.vx = -(self.mousepos[0] - mousepos[0]) * MAIN_SPEED
		self.vy = -(self.mousepos[1] - mousepos[1]) * MAIN_SPEED
		if self.mousepos[0] > mousepos[0]:
			self.direction = "LEFT"
		elif self.mousepos[0] < mousepos[0]:
			self.direction = "RIGHT"	
		self.bg = bg
		if self.bg.x >= 0:
			cl = 0
		else:
			cl = self.w
		if -self.bg.x + self.Game.width + self.w >= self.bg.w:
			cr = self.Game.width - self.w
		else:
			cr = self.Game.width - 2 * self.w
		if self.bg.y >= 0:
			cu = 0
		else:
			cu = self.Game.height/8
		if -self.bg.y + self.Game.height + self.h >= self.bg.h:
			cd = self.Game.height - self.h
		else:

			cd = self.Game.height - 2 * self.h


		x = self.pos[0] + self.vx; x = max(x, cl); x = min(x, cr)
		y = self.pos[1] + self.vy; y = max(y, cu); y = min(y, cd)
		self.pos = (x,y)

		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		self.delay += 1

		if self.direction == "LEFT":
			name = "ca"
		else:
			name = "cas"
		if self.delay == 5:
			self.name = name + str(self.img % 2 + 1) + ".png"
			self.image = pygame.image.load(self.name)
			self.delay %= 5
			self.img += 1
		pygame.mouse.set_pos((self.Game.width/2, self.Game.height/2))





	def kill(self): #xóa
		self.name = ""

	def Fire(self, bg):
		if self.direction == "LEFT":
			Bullet = bullet((self.pos[0] - self.bullet[0].w , self.pos[1] + self.h/2), self.Game, bg, "dan.png")
			Bullet.vx = -BULLET_SPEED
			Bullet.vy = 0
		else:
			Bullet = bullet((self.pos[0]  + self.w, self.pos[1] + self.h/2), self.Game, bg, "dan.png")
			Bullet.vx = BULLET_SPEED
			Bullet.vy = 0
		return Bullet