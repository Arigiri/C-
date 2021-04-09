import pygame
from Game import *
from bg import *
from hitbox import *
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
	direction = 0
	hitbox = hitbox()
	def __init__(self, pos = 0, Game = 0, bg = 0, name = "", direction = 0):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.rpos = pos
		self.Game = Game
		self.bg = bg
		self.name = name
		self.direction = direction
		if(self.name == ""):
			return
		self.image = pygame.image.load(name)
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.bgx = self.bg.x
		self.bgy = self.bg.y
		# self.hitbox = hitbox(self.pos[0], self.pos[1], self.w, self.h,"BULLET")
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

	def draw(self):
		self.Game.screen.blit(self.image, self.pos)

	def update(self, bg):
		x = self.rpos[0] + bg.x - self.bgx
		y = self.rpos[1] + bg.y - self.bgy
		self.pos = (x, y)
		# self.hitbox = hitbox(self.pos[0], self.pos[1], self.w, self.h, "BULLET")
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		if self.rpos[0] < 0 or self.rpos[0] + self.w > self.Game.width or self.rpos[1] < 0 or self.rpos[1] + self.h > self.Game.height:
			self.kill()
		self.run()

	def run(self):
		if self.direction == "LEFT":
			v = -self.v
		else:
			v = self.v
		self.rpos = (self.rpos[0] + v, self.rpos[1])
	
	# def kill(self):
	# 	self.name = ""

