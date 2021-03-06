import pygame
from MC import *
class Blade(pygame.sprite.Sprite):
	blade = ""
	old_time = 0
	K = True
	blade = ""
	def __init__(self, mc):
		if mc.stamia < BLADE_STAMIA:
			return
		mc.stamia -= BLADE_STAMIA
		pygame.sprite.Sprite.__init__(self)
		curr_time = pygame.time.get_ticks()
		self.old_time = curr_time
		self.blade = "slash"
		if mc.direction == "LEFT":
			self.pos = (mc.pos[0] - mc.w/2, mc.pos[1] )
		else:
			self.pos = (mc.pos[0] + mc.w/1.33, mc.pos[1] )
		if mc.direction == "RIGHT" and self.blade != "":
			blade = self.blade + "1"
		elif self.blade != "":
			blade = self.blade + "2"
		self.image = pygame.image.load(blade + ".png").convert_alpha()
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * RATIO //100, h *RATIO//100))
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		self.rect.topleft = self.pos

	
	def update(self, mc, game):
		if self.blade == "":
			return
		self.blade = "slash"
		if mc.direction == "LEFT":
			self.pos = (mc.pos[0] - mc.w/2, mc.pos[1] )
		else:
			self.pos = (mc.pos[0] + mc.w/1.33, mc.pos[1] )
		if mc.direction == "RIGHT" and self.blade != "":
			blade = self.blade + "1"
		elif self.blade != "":
			blade = self.blade + "2"
		self.image = pygame.image.load(blade + ".png").convert_alpha()
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * game.RATIO //100, h * game.RATIO//100))
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		self.rect.topleft = self.pos
		curr_time = pygame.time.get_ticks()
		return curr_time - self.old_time >= MAIN_BLADE * 100