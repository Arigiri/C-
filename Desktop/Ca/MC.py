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
	immune = True
	health = 0
	maxhealth = 0
	bullet = [bullet()]
	direction = "LEFT"
	direction1 = "UP"
	dash = False
	mousepos = 0
	
	move = 1
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0): #khai báo
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.rpos = pos
		self.name = name + ".png"
		self.image = pygame.image.load(self.name)
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * RATIO //100, h *RATIO//100))
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
		

		 
	# blade = ""
	old_time = 0
	image1 = ""
	def draw_blade(self, game):
		if self.image1 != "":
			if self.direction == "RIGHT":
				game.screen.blit(self.image1, (self.pos[0] + self.w, self.pos[1] + self.h//3))
			else:
				game.screen.blit(self.image1, (self.pos[0] - self.w, self.pos[1] + self.h//3))

	def update(self, bg): #update nhân vật chính
		if self.move == 0:
			self.move = 1
			pygame.mouse.set_pos((self.Game.width/2, self.Game.height/2))
			return
		mousepos = pygame.mouse.get_pos()
		self.vx = -(self.mousepos[0] - mousepos[0]) * MAIN_SPEED
		self.vy = -(self.mousepos[1] - mousepos[1]) * MAIN_SPEED
		if self.dash:
			self.Dash()
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
			cr = self.Game.width - self.w
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
			name = "ca2"
		else:
			name = "cas2"
		if self.delay == 5:
			self.name = name + str(self.img % 2 + 1) + ".png"
			self.image = pygame.image.load(self.name)
			w = self.image.get_width()
			h = self.image.get_height()
			self.image = pygame.transform.scale(self.image, (w * RATIO //100, h *RATIO//100))
			self.delay %= 5
			self.img += 1
		pygame.mouse.set_pos((self.Game.width/2, self.Game.height/2))

	old_dash = 0
	def Dash(self):
		curr_time = pygame.time.get_ticks()
		
		if curr_time - self.old_dash>= DASH_TIME * 100 and self.old_dash != 0:
			self.old_dash = 0
			self.dash = False
			return
		if self.old_dash == 0:
				self.old_dash = curr_time
		if self.vx == 0 and self.vy == 0:
			if self.direction == "LEFT":
				self.vx = -DASH_SPEED
			elif self.direction == "RIGHT":
				self.vx =  DASH_SPEED
		else:
			self.vx *= DASH_RATIO
			self.vy *= DASH_RATIO
			# self.dash = False

		
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