import pygame
from color import *
class hitbox:
	lx = 0; ly = 0; rx = 0; ry = 0; w = 0; h = 0

	more = 30
	def __init__(self, x = 0, y = 0, w = 0, h = 0, type = ""):
		if type == "FISH":
			self.lx = x + self.more - self.more/2
			self.ly = y + self.more
			self.w = w - 2 * self.more
			self.h = h - 2 * self.more
			self.rx = self.lx + self.w
			self.ry = self.ly + self.h
		elif type == "BULLET":
			self.lx = x
			self.ly = y
			self.w = w
			self.h = h
			self.rx = self.lx + self.w
			self.ry = self.ly + self.h	
	def inside(self, pos):
		return self.lx <= pos[0] and self.rx >= pos[0] and self.ly <= pos[1] and self.ry >= pos[1]
	def __str__(self):
		return "{0},{1},{2},{3}".format(self.lx, self.ly, self.rx, self.ry)
	def draw(self, screen):
		pygame.draw.rect(screen, BLACK, (self.lx, self.ly, self.w, self.h), 1)