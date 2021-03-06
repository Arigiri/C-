import pygame
from setting import *
from color import *
from pygame.locals import *

class button(pygame.sprite.Sprite):
	def __init__(self, pos = (0, 0), name = ""):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		if name == "":
			return

		self.name = name
		self.image = pygame.image.load("setting\\" + self.name + ".png")
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		if name == "st":
			self.pos = (pos[0] - self.w/2 - 60, self.pos[1])
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

	def get_clicked(self):
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		return x >= self.pos[0] and x <= self.pos[0] + self.w and y >= self.pos[1] and y <= self.pos[1] + self.h
	def hold(self):
		d = pygame.mouse.get_pressed()
		for mouse_button in d:
			if mouse_button == 1:
				return True
	def draw(self, surface):
		surface.blit(self.image, self.pos)
class load_button(button):
	def __init__(self, pos = (0, 0)):
		super(load_button, self).__init__(pos, "load")
	def draw(self, surface):
		surface.blit(self.image, self.pos)
class zoom_button(button):
	def __init__(self, pos = (0, 0), Game = ""):
		super(zoom_button, self).__init__(pos, "zoom")
		self.bar1 = button((10, Game.height / 2), "bar1")
		self.bar2 = button((10, Game.height / 2), "bar2")
		self.bar2 = button((10 , Game.height / 2 + self.bar2.h/2),"bar2")
		# print(Game.RATIO)
		self.bar1 = button((10 + self.bar2.w * Game.RATIO / 100, Game.height / 2), "bar1")
		
		self.Bar = pygame.sprite.Group()
		self.Bar.add(self.bar2)
		self.Bar.add(self.bar1)

	Show = False

	def update(self, game):

		if self.bar1.hold():
			pos = pygame.mouse.get_pos()
			if pos[0] >= self.bar2.pos[0] and pos[0]<= self.bar2.w + self.bar2.pos[0]:
				game.RATIO = max(int(pos[0]/self.bar2.w * 100), game.Min_ratio)
				self.bar1.pos = (10 + self.bar2.w * game.RATIO / 100, game.height / 2)
				self.bar1.rect.center = (self.bar1.pos[0] + self.bar1.w/2, self.bar1.rect.center[1])
				
		if self.Show: 
			self.Bar.draw(game.screen)
		return True

class exit_button(button):
	def __init__(self, pos = (0, 0)):
		super(exit_button, self).__init__(pos, "exit")
class skip_button(button):
	def __init__(self, pos = (0, 0)):
		super(skip_button, self).__init__(pos, "skip")
	Show = False
	def draw(self, surface):
		surface.blit(self.image, self.rect)

class save_button(button):
	def __init__(self, pos = (0, 0)):
		super(save_button, self).__init__(pos, "save")
class quit_button(button):
	def __init__(self, pos = (0, 0)):
		super(quit_button, self).__init__(pos, "quit")
class restart_button(button):
	def __init__(self, pos = (0, 0)):
		super(restart_button, self).__init__(pos, "restart")
class tutorial_button(button):
	def __init__(self, pos = (0, 0)):
		super(tutorial_button, self).__init__(pos, "tutorial")
class setting_menu(pygame.sprite.Sprite):
	def __init__(self, Game):
		pygame.sprite.Sprite.__init__(self)
		self.game = Game
		self.image = pygame.image.load("setting\\menu.png")

		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.pos = ((Game.width - self.w)/2, 15)
		tmp = pygame.image.load("setting\\save.png")
		
		self.Buttons = pygame.sprite.Group()
		tmp = pygame.image.load("setting\\zoom.png")
		self.exit_button = button((0, 0), "exit")
		self.exit_button = exit_button((self.pos[0] + self.w - self.exit_button.w/2, self.pos[1]))
		self.zoom_button = zoom_button((self.pos[0] + self.w/2, Game.height * 1 / 10), Game)
		self.zoom_button = zoom_button((self.pos[0] + self.w/2 - self.zoom_button.w/2, Game.height * 3 / 10), Game)
		self.load_button = load_button((Game.width /2, Game.height * 1 / 4))
		self.load_button = load_button((self.pos[0] + self.w/2 - self.zoom_button.w/2, self.zoom_button.pos[1] + self.zoom_button.h + 30))
		self.save_button = save_button((Game.width - tmp.get_width() - 30, Game.height * 2 / 10))
		self.save_button = save_button((self.pos[0] + self.w/2 - self.zoom_button.w/2, Game.height * 2 / 10))
		self.restart_button = restart_button()
		self.restart_button = restart_button((self.pos[0] + self.w/2 - self.zoom_button.w/2, self.save_button.pos[1] + self.save_button.h + 30))
		self.tutorial_button = tutorial_button()
		self.tutorial_button = tutorial_button(((self.pos[0] + self.w/2 - self.zoom_button.w/2, self.restart_button.pos[1] + self.restart_button.h + 30)))
		self.quit_button = quit_button()
		self.quit_button = quit_button((self.pos[0] + self.w/2 - self.zoom_button.w/2, self.tutorial_button.pos[1] + self.tutorial_button.h + 30))
		
		
		self.skip_button = skip_button((Game.width * 1 / 10, Game.height * 5 /6))
		self.skip_button = skip_button((self.skip_button.w/2, Game.height * 5 /6))
		self.Buttons.add(self.save_button)
		self.Buttons.add(self.exit_button)
		self.Buttons.add(self.quit_button)
		self.Buttons.add(self.restart_button)
		self.Buttons.add(self.tutorial_button)
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
	Help = 0
	def update(self, game, mc, bg):
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == MOUSEBUTTONDOWN:
				if self.Help:
					self.Help += 1
					if self.skip_button.get_clicked():
						self.Help = 11
					break
				for button in self.Buttons:
					if button.get_clicked():
						if button.name == "exit":
							game.Pause = False
						if button.name == "save":
							game.write(mc)
							game.save_success = 5
						if button.name == "zoom":
							button.Show = not button.Show
						if button.name == "load":
							game.read(mc, bg)
							game.load_success = 5
						if button.name == "quit":
							pygame.quit()
							exit()
						if button.name == "restart":
							game.restart = True
						if button.name == "tutorial":
							self.Buttons.add(self.skip_button)
							self.Help = 1
				
		if self.Help > 0:
			if self.Help > 10:
				self.Help = 0
				for button in self.Buttons:
					if button.name == "skip":
						button.kill()
			else:
				img = pygame.image.load("help\\help" + str(self.Help) + ".png")
				img = pygame.transform.scale(img, (self.game.width, self.game.height))
				self.game.screen.blit(img, (0, 0))
				self.skip_button.draw(self.game.screen)
				self.skip_button.Show = True
			
							

	def draw(self, surface):
		surface.blit(self.image, self.pos)
		image = pygame.image.load("setting\\tt.png")
		w = image.get_width()
		h = image.get_height()
		surface.blit(image, (self.pos[0] + self.w/2 - w/2, self.pos[1] + h/2 - 30))
