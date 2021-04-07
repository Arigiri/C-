import pygame

class bg:
	x = 0; y = 0; w = 0; h = 0
	Game = 0
	name = "bg.jpg"
	image = 0
	image = pygame.image.load(name)
	v = 50
	def __init__(self, x, y, Game):
		self.x = x
		self.y = y
		self.w = pygame.Surface.get_width(self.image)
		self.h = pygame.Surface.get_height(self.image)
		self.Game = Game
		print(self.w, self.h)
		print(self.Game.width, self.Game.height)

	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self):
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		tmpx = self.x 
		tmpy = self.y
		if x >= 1000:
			tmpx -= self.v
		if x <= 100:
			tmpx += self.v
		if y >= 600:
			tmpy -= self.v
		if y <= 100:
			tmpy += self.v
		# print(tmpx, tmpy)
		tmpx = min(tmpx, 0)
		tmpy = min(tmpy, 0)
		if not(tmpx > 0 or tmpy > 0 or -tmpx + self.Game.width > self.w):
			self.x = tmpx
		if not(-tmpy + self.Game.height > self.h):
			self.y = tmpy
			
			



