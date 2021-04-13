import pygame
from MC import *
class Blade(pygame.sprite.Sprite):
	blade = ""
	image = ""
	rect = ""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
	old_time = 0
	K = True
	def update(self, mc):

		curr_time = pygame.time.get_ticks()

		if self.blade == "":
			self.old_time = curr_time
			self.blade = "slash"
		

		if mc.direction == "LEFT":
			self.pos = (mc.pos[0] - mc.w/2, mc.pos[1] + mc.h//3)
		else:
			self.pos = (mc.pos[0] + mc.w/2, mc.pos[1] + mc.h//3)
		if mc.direction == "RIGHT" and self.blade != "":
			blade = self.blade + "1"
		elif self.blade != "":
			blade = self.blade + "2"
		if self.blade != "":
			self.image = pygame.image.load(blade + ".png").convert_alpha()
			self.w = self.image.get_width()
			self.h = self.image.get_height()
			self.rect = self.image.get_rect()
			self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
			self.rect.topleft = self.pos

		if curr_time - self.old_time >= MAIN_BLADE * 100:
			self.blade = ""
			self.K = False