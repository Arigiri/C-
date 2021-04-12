import pygame
from pygame.locals import *
from Game import *
class start_button():
	def __init__(self, x, y):
		self.name = "st.png"
		self.image = pygame.image.load(self.name)
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.x = x - self.w/2 - 60
		self.y = y		
	def draw(self):
		self.game.screen.blit(self.image, (self.x, self.y))
	def get_hit(self):
		pos = pygame.mouse.get_pos()
		return pos[0] >= self.x and pos[0] <= self.x + self.w and pos[1] >= self.y and pos[1] <= self.y + self.h
class menu(start_button):
	def __init__(self, game):
		super(menu, self).__init__(game.width/2, game.height * 2 / 3)
		self.game = game
	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == KEYDOWN and event.key == K_F4:
				exit()
			if event.type == MOUSEBUTTONDOWN:
				if self.get_hit():
					print(1)
					pygame.mouse.set_visible(False)
					return False
		image = pygame.image.load("bg2.png")
		self.game.screen.blit(image, (0, 0))
		self.draw()
		pygame.display.flip()
		return True