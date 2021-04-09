from Game import *
from hitbox import *
from color import *
from bg import *
from random import *
from Bullet import *
from time import *
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
	hitbox = hitbox()
	health = 0
	maxhealth = 0
	bullet = [bullet()]
	direction = "LEFT"
	O = (0,0)
	mousepos = 0
	speed = 5
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
		self.rect = self.image.get_rect()#hitbox(self.pos[0], self.pos[1], self.w, self.h, "FISH")
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		# self.vx = randint(self.minv, self.maxv)
		# self.vy = randint(self.minv, self.maxv)
		self.maxhealth = maxhealth
		self.health = self.maxhealth
		self.mousepos = pos
		self.mousepos = (self.Game.width/2, self.Game.height/2)

		pygame.mouse.set_pos(self.mousepos)
		
	def health_bar(self):
		x = self.Game.width * 70 // 100
		y = 25
		self.health = max(self.health, 0)

		mw = self.Game.width - 30  - x
		health_len = mw/100
		nw = self.health * health_len
		pygame.draw.rect(self.Game.screen, BLACK, (x, y, mw, y))
		if self.health == 0:
			return 
		pygame.draw.rect(self.Game.screen, GREEN, (x + mw - nw, y, nw, y))
		 

	# def draw(self): #vẽ
	# 	if self.name == "":
	# 		return
	# 	self.Game.screen.blit(self.image, self.pos)
	# 	self.hitbox = hitbox(self.pos[0], self.pos[1], self.w, self.h, "FISH")
	# 	self.hitbox.draw(self.Game.screen)
	# 	self.health_bar()
	# 	for Bullet in self.bullet:
	# 		if Bullet.name != "":
	# 			Bullet.draw()


	def update(self, bg): #update nhân vật chính
		mousepos = pygame.mouse.get_pos()
		self.vx = -(self.mousepos[0] - mousepos[0]) * self.speed
		self.vy = -(self.mousepos[1] - mousepos[1]) * self.speed
		if self.mousepos[0] > mousepos[0]:
			self.direction = "LEFT"
		elif self.mousepos[0] < mousepos[0]:
			self.direction = "RIGHT"	
		
		x = self.pos[0] + self.vx; x = max(x, 0); x = min(x, self.Game.width - self.w)
		y = self.pos[1] + self.vy; y = max(y, 0); y = min(y, self.Game.height - self.h)
		self.pos = (x,y)
		# print(self.pos)

		# self.hitbox = hitbox()
		# self.hitbox = hitbox(self.pos[0], self.pos[1], self.pos[0] + self.h, self.pos[1] + self.w)
		self.rect = self.image.get_rect()#hitbox(self.pos[0], self.pos[1], self.w, self.h, "FISH")
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
		# for Bullet in self.bullet:
		# 	if Bullet.name != "":
		# 		Bullet.update(bg)
		# 		Bullet.run()
		sleep(0.01)

	# def hit(self, fishB): #va vào cá B
	# 	pointA = [(self.hitbox.lx, self.hitbox.ly), (self.hitbox.rx, self.hitbox.ry), (self.hitbox.lx, self.hitbox.ry), (self.hitbox.rx, self.hitbox.ly)]
	# 	pointB = [(fishB.hitbox.lx, fishB.hitbox.ly), (fishB.hitbox.rx, fishB.hitbox.ry), (fishB.hitbox.lx, fishB.hitbox.ry), (fishB.hitbox.rx, fishB.hitbox.ly)]
	# 	for i in pointA:
	# 		if fishB.hitbox.inside(i):
	# 			return 1
	# 		# pygame.draw.circle(self.Game.screen, RED, i, 3)
	# 	for i in pointB:
	# 		if self.hitbox.inside(i):
	# 			return 1
	# 		# pygame.draw.circle(self.Game.screen, BLACK, i, 1)
	# 	return False

	def kill(self): #xóa
		self.name = ""

	def Fire(self, bg):
		Bullet = 0
		if self.direction == "LEFT":
			Bullet = bullet((self.pos[0] - self.bullet[0].w , self.pos[1] + self.h/2), self.Game, bg, "dan.png", self.direction)
			self.bullet.append(Bullet)
		else:
			Bullet = bullet((self.pos[0]  + self.w, self.pos[1] + self.h/2), self.Game, bg, "dan.png", self.direction)
			self.bullet.append(Bullet)
		return Bullet