import pygame
from pygame.locals import *
class button(pygame.sprite.Sprite):
	def __init__(self, pos = (0, 0)):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.image = pygame.image.load("setting.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

	def get_clicked(self):
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		return x >= self.pos[0] and x <= self.pos[0] + self.w and y >= self.pos[1] and y <= self.pos[1] + self.h

class setting_menu(pygame.sprite.Sprite):
	def __init__(self, Game):
		pygame.sprite.Sprite.__init__(self)
		self.game = Game
		self.image = pygame.image.load("menu.png")
		self.image = pygame.transform.scale(self.image, (self.game.width, self.game.height))
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.pos = ((Game.width - self.w)/2, 15)
		self.button = button((30, 30))

		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		
	def draw(self, surface):
		surface.blit(self.image, self.pos)
		image = pygame.image.load("tt.png")
		
		w = image.get_width()
		h = image.get_height()
		surface.blit(image, (self.pos[0] + self.w/2 - w/2, self.pos[1] - h/4))