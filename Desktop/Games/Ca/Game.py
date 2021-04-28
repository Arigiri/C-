import pygame
from setting import *
from setting_menu import *
from Mob4 import *
from Mob0 import *
from Mob1 import *
from Mob2 import *
from Mob3 import *
from entity import *
from Blade import *
from Boss import *
class game():
	screen = 0
	width = 0
	height = 0
	stage = 1
	Pause = False

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.width, self.height = pygame.display.get_surface().get_size()
		self.font = pygame.font.SysFont(None, 72)
		self.menu = setting_menu(self)
	
		# self.rect.lefttop = (0, 0)
		# self.rect.rightbottom = (self.width, self.height)

		self.Buttons = pygame.sprite.Group()
		self.Buttons.add(self.menu.button)
	def spawn(self, bg, mc, fish):
		x = randint(0, bg.w * 6 // 8)
		y = randint(0, bg.h * 6 // 8)
		while (x >= mc.pos[0] - fish.w and x <= mc.pos[0] + mc.w - fish.w and y >= mc.pos[1] - fish.h and y <= mc.pos[1] + mc.h - fish.h):
			x = randint(0, bg.w * 6 // 8)
			y = randint(0, bg.h * 6 // 8)
		return (x, y)

	def setup(self, bg, mc):
		#sprite group
		self.mobs = pygame.sprite.Group()
		self.mobs_0 = pygame.sprite.Group()
		self.mobs_4 = pygame.sprite.Group()
		self.mobs_1 = pygame.sprite.Group()
		self.mobs_2 = pygame.sprite.Group()
		self.mobs_3 = pygame.sprite.Group()
		self.Bullet_Main = pygame.sprite.Group()
		self.Bullet_Mobs = pygame.sprite.Group()
		self.Blade_mc = pygame.sprite.Group()
		self.Boss = pygame.sprite.Group()
		#mobs spawn
		tmp = mob0()
		Fish0 = []
		for i in range(number_of_mob_0):
			Fish0.append(mob0(self.spawn(bg, mc, tmp), "mob0\\ca01", self, bg, 100))
		tmp = mob1()
		Fish1 = []
		for i in range(number_of_mob_1):
			Fish1.append(mob1(self.spawn(bg, mc, tmp), "mob1\\ca12", self, bg, 100))
		tmp = mob2()
		Fish2 = []
		for i in range(number_of_mob_2):
			Fish2.append(mob2(self.spawn(bg, mc, tmp), "mob2\\ca21", self, bg, 100))
		tmp = mob3()
		Fish3 = []
		for i in range(number_of_mob_3):
			Fish3.append(mob3(self.spawn(bg, mc, tmp), "mob3\\cas31", self, bg, 100))
		tmp = mob4()
		Fish4 = []
		for i in range(number_of_mob_4):
			Fish4.append(mob4(self.spawn(bg, mc, tmp), "mob4\\ca41", self, bg, 100))
		tmp = Boss()
		BOSS = []
		for i in range(number_of_boss_1):
			BOSS.append(Boss(self.spawn(bg, mc, tmp), "boss\\ca100", self, bg, 100))
		for fish in Fish0:
			self.mobs_0.add(fish)
			self.mobs.add(fish)
		for fish in Fish1:
			self.mobs_1.add(fish)
			self.mobs.add(fish)
		for fish in Fish2:
			self.mobs_2.add(fish)
			self.mobs.add(fish)
		for fish in Fish3:
			self.mobs_3.add(fish)
			self.mobs.add(fish)
		for fish in Fish4:
			self.mobs_4.add(fish)
			self.mobs.add(fish)
		for fish in BOSS:
			self.Boss.add(fish)
			self.mobs.add(fish)
	def load(self, bg, mc):
		fade = 100
		
		f = open("stage" + str(self.stage) + ".txt", "r")
		kt = f.readlines()
		# kt = kt.split()
		tme = 100

		f.close()
		global number_of_mob_0
		number_of_mob_0 = int(kt[0])
		self.setup(bg, mc)
		self.stage += 1