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
	immune = True
	health = 0
	maxhealth = 0
	bullet = [bullet()]
	direction = "LEFT"
	direction1 = "UP"
	Slow = False
	dash = False
	mousepos = 0
	list_names = 16
	move = 1
	
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0): #khai báo
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		if name == "":
			return
		self.name = name + ".png"
		self.image = pygame.image.load(self.name)
		self.stamia_image = pygame.image.load("stamia.png")
		sw = self.stamia_image.get_width()
		sh = self.stamia_image.get_height()
		
		self.stamia = FULL_STAMIA
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * Game.RATIO //100, h * Game.RATIO//100))
		self.Game = Game

		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.bg = bg
		rate = sw/sh
		self.stamia_image = pygame.transform.scale(self.stamia_image, (int(rate * self.h) , self.h ))
		self.sw = self.stamia_image.get_width()
		self.sh = self.stamia_image.get_height()

		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

		self.maxhealth = maxhealth
		self.health = self.maxhealth
		self.lives = MC_LIVES
		self.mousepos = pos
		self.mousepos = (self.Game.width/2, self.Game.height/2)

		self.name_listc = []
		for i in range(0, self.list_names):
			self.name_listc.append("mc_animation\\mc" + str(i))
		self.name_lists = []
		for i in range(0, self.list_names):
			self.name_lists.append("mc_animation\\mcs" + str(i))
		pygame.mouse.set_pos(self.mousepos)

		

		 
	
	old_time = 0
	image1 = ""
	Slow_Time = SLOW_TIME
	def draw_blade(self, game):
		if self.image1 != "":
			if self.direction == "RIGHT":
				game.screen.blit(self.image1, (self.pos[0] + self.w, self.pos[1] + self.h//3))
			else:
				game.screen.blit(self.image1, (self.pos[0] - self.w, self.pos[1] + self.h//3))
	

	def update(self, bg, Game): #update nhân vật chính
		self.Game = Game
		if self.move == 0:
			self.move = 1
			pygame.mouse.set_pos((self.Game.width/2, self.Game.height/2))
			return
		global BG_SPEED
		self.vx, self.vy = 0, 0
		mousepos = pygame.mouse.get_pos()
		self.vx = (mousepos[0] -self.mousepos[0]) * MAIN_SPEED
		self.vy = (mousepos[1] - self.mousepos[1]) * MAIN_SPEED
		BG_SPEED = self.vx
		BG_SPEED = self.vy
		if self.Slow > 0 and self.Slow_Time > 0:
			self.vx *= SLOW
			self.vy *= SLOW
			self.Slow_Time -= 1
		elif self.Slow_Time <= 0:

			self.Slow = False
		if self.mousepos[0] > mousepos[0]:
			self.direction = "LEFT"
		elif self.mousepos[0] < mousepos[0]:
			self.direction = "RIGHT"
		else:
			self.direction1 = ""	
		if self.mousepos[1] > mousepos[0]:
			self.direction1 = "UP"
		elif self.mousepos[1] < mousepos[1]:
			self.direction1 = "DOWN"
		else: self.direction1 = ""
		self.bg = bg
		if self.bg.x >= 0:
			cl = 0
		else:
			cl = self.w
		if -self.bg.x + self.Game.width + self.w >= self.bg.w:
			cr = Game.width - self.w
		else:
			cr = self.Game.width - 2 * self.w
		if self.bg.y >= 0:
			cu = 0
		else:
			cu = self.h
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
			name = "mc_animation\\mc"
		else:
			name = "mc_animation\\mcs"

		self.name = name + str(self.img % self.list_names) + ".png"
		
		self.image = pygame.image.load(self.name)
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * Game.RATIO //100, h * Game.RATIO//100))
		self.img += 1
		self.stamia += STAMIA_RESTORE
		self.stamia = min(self.stamia, FULL_STAMIA)
		pygame.mouse.set_pos((self.Game.width/2, self.Game.height/2))


	

		
	def Fire(self, bg):
		if self.stamia < FIRE_STAMIA:
			return bullet()
		self.stamia -= FIRE_STAMIA
		if self.direction == "LEFT":
			Bullet = bullet((self.pos[0] - self.bullet[0].w , self.pos[1] + self.h/2), self.Game, bg, "bullet1.png")
			Bullet.type = "MAIN"
			Bullet.vx = -MC_BULLET_SPEED 
			Bullet.vy = 0
		else:
			Bullet = bullet((self.pos[0]  + self.w, self.pos[1] + self.h/2), self.Game, bg, "bullet2.png")
			Bullet.type = "MAIN"
			Bullet.vx = MC_BULLET_SPEED 
			Bullet.vy = 0
		return Bullet
	def __str__(self):
		return self.name + '\n' + str(int(self.pos[0])) + '\n' + str(int(self.pos[1])) + '\n' + str(self.stamia) + '\n' + str(int(self.health)) + '\n' + str(int(self.lives)) + '\n' + str(int(self.mousepos[0])) + '\n' + str(int(self.mousepos[1]))
	def read(self, Game):
		f = open("saves\\mc_save.txt", "r")
		read = f.readlines()
		self.name = read[0][0:len(read[0]) - 1]
		self.pos = int(read[1]), int(read[2])
		self.stamia = int(read[3])
		self.health = int(read[4])
		self.lives = int(read[5])
		self.mousepos = int(read[6]), int(read[7])
		self.image = pygame.image.load(self.name)
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		self.maxhealth = MC_HEALTH
		self.stamia_image = pygame.image.load("stamia.png")
		sw = self.stamia_image.get_width()
		sh = self.stamia_image.get_height()
		
		self.stamia = FULL_STAMIA
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * Game.RATIO //100, h * Game.RATIO//100))
		# self.Game = Game
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		# self.bg = bg
		rate = sw/sh
		self.stamia_image = pygame.transform.scale(self.stamia_image, (int(rate * self.h), self.h))
		self.sw = self.stamia_image.get_width()
		self.sh = self.stamia_image.get_height()
		f.close()
	def write(self):
		f = open("saves\\mc_save.txt", "w")
		f.write(str(self))
		f.close()