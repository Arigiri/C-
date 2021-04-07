import pygame

class game:
	screen = 0
	width = 0
	height = 0
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.width, self.height = pygame.display.get_surface().get_size()
		# pygame.mouse.set_visible(False)
