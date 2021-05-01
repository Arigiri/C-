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
class load_button(button):
	def __init__(self, pos = (0, 0)):
		super(load_button, self).__init__(pos, "load")
	def draw(self, surface):
		surface.blit(self.image, self.pos)
class Zoom_button(button):
	def __init__(self, pos = (0, 0), Game = ""):
		super(button, self).__init__()
		self.pos = pos
		self.name = "zoom"
		self.image = pygame.image.load("setting\\" + self.name + ".png").convert_alpha()
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		self.bar1 = button((10, Game.height / 2), "bar1")
		self.bar2 = button((10, Game.height / 2), "bar2")
		self.bar2 = button((10 , Game.height / 2 + self.bar2.h/2),"bar2")
		self.bar1 = button((10 + self.bar2.w * RATIO / 100, Game.height / 2), "bar1")
		
		self.Bar = pygame.sprite.Group()
		self.Bar.add(self.bar2)
		self.Bar.add(self.bar1)

	Show = False

	def update(self, game):
		# for event in pygame.event.get():
		# 	if event.type == QUIT:
		# 		exit()
		# 	if event.type == MOUSEBUTTONUP:
		# 		if self.get_clicked():	self.Show = not self.Show
		# 		pos = pygame.mouse.get_pos()
		# 		self.clicked_buttons = [s for s in game.Buttons if s.rect.collidepoint(pos)]
		# 		for button in self.clicked_buttons:
		# 			if button.name == "exit":
		# 				game.Pause = False
		# 			if button.name == "load":
		# 				game.read(mc)
		if self.bar1.hold():
			pos = pygame.mouse.get_pos()
			if pos[0] >= self.bar2.pos[0] and pos[0]<= self.bar2.w + self.bar2.pos[0]:
				game.RATIO = max(int(pos[0]/self.bar2.w * 100), game.Min_ratio)
				self.bar1.pos = (10 + self.bar2.w * game.RATIO / 100, game.height / 2)
				self.bar1.rect.center = (self.bar1.pos[0] + self.bar1.w/2, self.bar1.rect.center[1])
				
		if self.Show: 
			self.Bar.draw(game.screen)
			# pygame.display.flip()
		return True

class exit_button(button):
	def __init__(self, pos = (0, 0)):
		super(button, self).__init__()
		self.pos = pos
		self.name = "exit"
		self.image = pygame.image.load("setting\\" + self.name + ".png").convert_alpha()
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)

	# def update(self, game, mc):
	# 	for event in pygame.event.get():
	# 		if event.type == QUIT:
	# 			exit()
	# 		if event.type == MOUSEBUTTONDOWN:
	# 			if self.get_clicked():	return False
	# 	return True
class save_button(button):
	def __init__(self, pos = (0, 0)):
		super(button, self).__init__()
		self.pos = pos
		self.name = "save"
		self.image = pygame.image.load("setting\\" + self.name + ".png")
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
class setting_menu(pygame.sprite.Sprite):
	def __init__(self, Game):
		pygame.sprite.Sprite.__init__(self)
		self.game = Game
		self.image = pygame.image.load("setting\\menu.png")
		self.image = pygame.transform.scale(self.image, (self.game.width, self.game.height))
		self.rect = self.image.get_rect()
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.pos = ((Game.width - self.w)/2, 15)
		tmp = pygame.image.load("setting\\save.png")
		self.save_button = save_button((Game.width - tmp.get_width() - 30, Game.height * 1 / 10))
		self.Buttons = pygame.sprite.Group()
		tmp = pygame.image.load("setting\\zoom.png")
		self.exit_button = button((0, 0), "exit")
		self.exit_button = exit_button((Game.width - self.exit_button.w - 30, self.exit_button.h))
		self.zoom_button = Zoom_button((Game.width - tmp.get_width() - 30, Game.height * 1 / 10), Game)
		self.load_button = load_button((Game.width /2, Game.height * 1 / 4))
		self.Buttons.add(self.save_button)
		self.Buttons.add(self.exit_button)
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		# self.Buttons.add(self.zoom_button)
		# self.Buttons.add(self.exit_button)
	def update(self, game, mc, bg):
		for event in pygame.event.get():
			if event.type == QUIT:
				exit()
			if event.type == MOUSEBUTTONDOWN:
				for button in self.Buttons:
					if button.get_clicked():
						if button.name == "exit":
							game.Pause = False
						if button.name == "save":
							game.write(mc)
						if button.name == "zoom":
							button.Show = not button.Show
						if button.name == "load":
							game.read(mc, bg)

		pygame.draw.rect(game.screen, RED, self.load_button.rect, 1)
	def draw(self, surface):
		surface.blit(self.image, self.pos)
		image = pygame.image.load("setting\\tt.png")
		w = image.get_width()
		h = image.get_height()
		surface.blit(image, (self.pos[0] + self.w/2 - w/2, self.pos[1] - h/4))
