import pygame
from pygame.locals import *
from Game import *
from setting_menu import *
import setting
class start_button():
	def __init__(self, x, y):
		self.name = "st.png"
		self.image = pygame.image.load(self.name)
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.x = x - self.w/2 - 60
		self.y = y		

	def get_hit(self):
		pos = pygame.mouse.get_pos()
		return pos[0] >= self.x and pos[0] <= self.x + self.w and pos[1] >= self.y and pos[1] <= self.y + self.h

class setting(button):
	def __init__(self, pos = (0, 0)):
		super(setting, self).__init__(pos, "setting")
	def draw(self, surface):
		surface.blit( self.image,self.pos)

class menu(button):
	def __init__(self, game):
		super(menu, self).__init__((game.width/2, game.height * 2 / 3), "st")
		self.game = game
		self.game.Pause = False
		self.setting_menu = setting_menu(self.game)
		self.settingMenu = setting((self.pos[0], self.pos[1] + self.h))

	def draw(self):
		self.game.screen.blit(self.image, (self.pos[0], self.pos[1]))
	def update(self):
		if not self.game.Pause:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				elif event.type == KEYDOWN and event.key == K_F4:
					exit()
				if event.type == MOUSEBUTTONDOWN:
					if self.get_clicked():
						pygame.mouse.set_visible(False)
						return False
					if self.settingMenu.get_clicked():
						self.game.Pause = True

		image = pygame.image.load("bg2.png")
		image = pygame.transform.scale(image, (self.game.width, self.game.height))
		self.game.screen.blit(image, (0, 0))
		self.draw()
		self.settingMenu.draw(self.game.screen)
		if self.game.Pause == True:
			self.setting_menu.draw(self.game.screen)
			for button in self.setting_menu.Buttons:
				button.update(self.game)
			self.setting_menu.Buttons.draw(self.game.screen)
			img = pygame.image.load("example.png")
			w = img.get_width()
			h = img.get_height()
			img = pygame.transform.scale(img, (img.get_width() * self.game.RATIO //100, img.get_height() * self.game.RATIO//100))
			pygame.draw.rect(self.game.screen, (249, 214, 210), (self.game.width * 3 / 4, self.game.height * 3 / 4, w, h))
			rect = img.get_rect(center = (self.game.width * 3 /4 + img.get_width() / 2, self.game.height * 3 / 4 + img.get_height() / 2))
			self.game.screen.blit(img, rect)
			

			
			
		pygame.display.flip()
		return True