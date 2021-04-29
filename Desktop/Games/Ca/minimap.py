import pygame
from color import *
class minimap():
	def __init__(self,pos = (0, 0), Game = 0):
		self.pos = pos
		# self.mobs = Game.mobs
		self.image = pygame.Surface(self.pos, pygame.SRCALPHA)

		self.rect = self.image.get_rect()
		self.ratio = 20
	def update(self, Game, bg, mc):
		self.mobs = Game.mobs
		self.image = pygame.Surface(self.pos, pygame.SRCALPHA)
		pygame.draw.rect(self.image, (111, 116, 111), (0, 0, bg.w//self.ratio, bg.h//self.ratio))
		for mob in self.mobs:
			x = mob.pos[0] - bg.x
			y = mob.pos[1] - bg.y
			x/=self.ratio 
			y/=self.ratio 
			pygame.draw.circle(self.image, RED, (x, y), 3)
		for boss in Game.Boss:
			x = boss.pos[0] - bg.x
			y = boss.pos[1] - bg.y
			x/=self.ratio
			y/=self.ratio
			pygame.draw.circle(self.image, RED, (x, y), 5)
		self.rect = self.image.get_rect()
		x = mc.pos[0] - bg.x
		y = mc.pos[1] - bg.y
		x/=self.ratio
		y/=self.ratio
		pygame.draw.circle(self.image, YELLOW, (x, y), 3)


	def draw(self, Game):
		pygame.draw.rect(Game.screen, BLACK, (self.pos[0], self.pos[1], Game.bg.w//self.ratio, Game.bg.h//self.ratio) , 5)
		Game.screen.blit(self.image, self.pos)

