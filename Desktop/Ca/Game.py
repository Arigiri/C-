import pygame
from setting import *
from Mob4 import *
from Mob0 import *
from Mob1 import *
from Mob2 import *
from entity import *
from Blade import *
class game:
	screen = 0
	width = 0
	height = 0
	stage = 1
	Pause = False
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.width, self.height = pygame.display.get_surface().get_size()
		self.font = pygame.font.SysFont(None, 72)
	def setup(self, bg):
		self.mobs = pygame.sprite.Group()
		self.mobs_0 = pygame.sprite.Group()
		self.mobs_4 = pygame.sprite.Group()
		self.mobs_1 = pygame.sprite.Group()
		self.mobs_2 = pygame.sprite.Group()
		self.Bullet_Main = pygame.sprite.Group()
		self.Bullet_Mobs = pygame.sprite.Group()
		self.Blade_mc = pygame.sprite.Group()
		Fish = [mob0((randint(0, bg.w * 6 // 8), randint(0, bg.h * 6 // 8)), "ca3", self, bg, 100)  for i in range(number_of_mob_0)]
		Fish0 = [mob4((randint(0, bg.w * 6 // 8), randint(0, bg.h * 6 // 8)), "ca41", self, bg, 100) for i in range(number_of_mob_4)]
		Fish1 = [mob1((randint(0, bg.w * 6 // 8), randint(0, bg.h * 6 // 8)), "ca12", self, bg, 100) for i in range(number_of_mob_1)]
		Fish2 = [mob2((randint(0, bg.w * 6 // 8), randint(0, bg.h * 6 // 8)), "ca12", self, bg, 100) for i in range(number_of_mob_2)]
		for fish in Fish:
			self.mobs_0.add(fish)
			self.mobs.add(fish)
		for fish in Fish0:
			self.mobs_4.add(fish)
			self.mobs.add(fish)
		for fish in Fish1:
			self.mobs_1.add(fish)
			self.mobs.add(fish)
		for fish in Fish2:
			self.mobs_2.add(fish)
			self.mobs.add(fish)
	def load(self, bg):
		fade = 100
		
		f = open("stage" + str(self.stage) + ".txt", "r")
		kt = f.readlines()
		# kt = kt.split()
		tme = 100

		f.close()
		global number_of_mob_0
		number_of_mob_0 = int(kt[0])
		self.setup(bg)
		# x = self.width/2
		# y = self.height/2
		while(tme):
			bg.draw(self.screen)
			tme -= 1
			img = self.font.render('Stage ' + str(self.stage), True, (255, 255, fade))
			self.screen.blit(img, (self.width/2 - img.get_width()/2, self.height/2 - img.get_height()/2))
			fade -= 1
			pygame.display.update()
			sleep(0.0005)
		self.stage += 1
