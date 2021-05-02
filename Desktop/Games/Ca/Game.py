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
from minimap import *
class game():
	screen = 0
	width = 0
	height = 0
	stage = 1
	Pause = False
	RATIO = 70
	updated = False
	Fire_delay = 0
	load_success = 0
	save_success = 0
	restart = False
	Pause_delay = 0
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		pygame.init()
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.width, self.height = pygame.display.get_surface().get_size()
		self.font = pygame.font.SysFont(None, 72)
		self.menu = setting_menu(self)
		self.stop = 0
		rate = 3
		self.MAIN_SPEED, self.MOB_SPEED, self.BULLET_SPEED, self.BIG_BULLET_SPEED, self.SPLASH_SPEED, self.DASH_SPEED, self.MC_BULLET_SPEED = MAIN_SPEED, MOB_SPEED, BULLET_SPEED, BIG_BULLET_SPEED, SPLASH_SPEED, DASH_SPEED, MC_BULLET_SPEED
		if not (self.width == 1366 and self.height == 768):
			self.MAIN_SPEED *= rate
			self.MOB_SPEED *= rate
			self.BULLET_SPEED *= rate
			self.BIG_BULLET_SPEED *= rate
			self.SPLASH_SPEED *= rate
			self.DASH_SPEED *= rate
			self.MC_BULLET_SPEED *= rate
		# self.rect.lefttop = (0, 0)
		# self.rect.rightbottom = (self.width, self.height)

		self.Buttons = pygame.sprite.Group()
		self.Buttons = self.menu.Buttons
		# self.Buttons.add(self.menu.button)
	def spawn(self, bg, mc, fish):
		x = randint(0, bg.w * 6 // 8)
		y = randint(0, bg.h * 6 // 8)
		while (x >= mc.pos[0] - fish.w and x <= mc.pos[0] + mc.w - fish.w and y >= mc.pos[1] - fish.h and y <= mc.pos[1] + mc.h - fish.h):
			x = randint(0, bg.w * 6 // 8)
			y = randint(0, bg.h * 6 // 8)
		return (x, y)

	def setup(self, bg, mc):
		self.bg = bg
		# self.RATIO = self.Min_ratio + 5
		if not self.restart:
			self.minimap = minimap((0, 0), self)
			self.minimap = minimap((self.width - self.bg.w/self.minimap.ratio*self.RATIO/100 - 5, self.height - self.bg.h/self.minimap.ratio*self.RATIO/100 - 5), self)
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
			Fish0.append(mob0(self.spawn(bg, mc, tmp), "mob0\\ca01", self, bg, MOB_MAX_HEALTH))
		tmp = mob1()
		Fish1 = []
		for i in range(number_of_mob_1):
			Fish1.append(mob1(self.spawn(bg, mc, tmp), "mob1\\ca12", self, bg, MOB_MAX_HEALTH))
		tmp = mob2()
		Fish2 = []
		for i in range(number_of_mob_2):
			Fish2.append(mob2(self.spawn(bg, mc, tmp), "mob2\\ca21", self, bg, MOB_MAX_HEALTH))
		tmp = mob3()
		Fish3 = []
		for i in range(number_of_mob_3):
			Fish3.append(mob3(self.spawn(bg, mc, tmp), "mob3\\cas31", self, bg, MOB_MAX_HEALTH))
		tmp = mob4()
		Fish4 = []
		for i in range(number_of_mob_4):
			Fish4.append(mob4(self.spawn(bg, mc, tmp), "mob4\\ca41", self, bg, MOB_MAX_HEALTH))
		tmp = Boss()
		BOSS = []
		for i in range(number_of_boss_1):
			BOSS.append(Boss(self.spawn(bg, mc, tmp), "boss\\ca100", self, bg, MOB_MAX_HEALTH))
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
		
		f = open("stages\\stage" + str(self.stage) + ".txt", "r")
		kt = f.readlines()
		# kt = kt.split()
		tme = 100

		f.close()
		global number_of_mob_0, number_of_mob_1,number_of_mob_2,number_of_mob_3,number_of_mob_4,number_of_boss_1
		number_of_mob_0 = int(kt[0])
		number_of_mob_1 = int(kt[1])
		number_of_mob_2 = int(kt[2])
		number_of_mob_3 = int(kt[3])
		number_of_mob_4 = int(kt[4])
		number_of_boss_1 = int(kt[5])
		self.setup(bg, mc)
		self.stage += 1
	def __str__(self):
		paper = str(self.stage) + '\n' + str(self.RATIO) + '\n'
		return paper
	def write(self, mc):
		count1 = 0
		for mob in self.mobs:
			mob.write(count1)
			count1 += 1
		self.bg.write()
		count2 = 0
		for bullet in self.Bullet_Mobs:
			bullet.write(count2, "mob")
			count2 += 1
		count3 = 0
		for bullet in self.Bullet_Main:
			bullet.write(count3, "main")
			count3 += 1
		f = open("saves\\game_save.txt", "w")
		f.write(str(count1) + '\n' + str(count2) + '\n' + str(count3) + '\n')
		f.write(str(self))
		mc.write()
	def read(self, mc, bg):	
		bg.read()
		self.bg = bg
		f = open("saves\\game_save.txt", "r")
		read = f.readlines()
		count1 = int(read[0])
		count2 = int(read[1])
		count3 = int(read[2])
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
		for i in range(count1):
			Fish = fish()
			Fish.read(i)
			if Fish.mob == 0:
				tmp = Fish.rpos
				Fish = mob0(Fish.pos, Fish.name, self, bg, Fish.health)
				Fish.rpos = tmp
				self.mobs_0.add(Fish)
				self.mobs.add(Fish)
			if Fish.mob == 1:
				tmp = Fish.rpos
				Fish = mob1(Fish.pos, Fish.name, self, bg, Fish.health)
				Fish.rpos = tmp
				self.mobs_1.add(Fish)
				self.mobs.add(Fish)
			if Fish.mob == 2:
				tmp = Fish.rpos
				Fish = mob2(Fish.pos, Fish.name, self, bg, Fish.health)
				Fish.rpos = tmp
				self.mobs_2.add(Fish)
				self.mobs.add(Fish)
			if Fish.mob == 3:
				tmp = Fish.rpos
				Fish = mob3(Fish.pos, Fish.name, self, bg, Fish.health)
				Fish.rpos = tmp
				self.mobs_3.add(Fish)
				self.mobs.add(Fish)
			if Fish.mob == 4:
				tmp = Fish.rpos
				Fish = mob4(Fish.pos, Fish.name, self, bg, Fish.health)
				Fish.rpos = tmp
				self.mobs_4.add(Fish)
				self.mobs.add(Fish)
			if Fish.mob == 100:
				tmp = Fish.rpos
				Fish = Boss(Fish.pos, Fish.name, self, bg, Fish.health)
				Fish.rpos = tmp
				self.Boss.add(Fish)
				self.mobs.add(Fish)
		for i in range(count2):
			Bullet = bullet()
			Bullet.read(i, "mob")
			Bullet = bullet(Bullet.pos, self, bg, Bullet.name, Bullet.vx, Bullet.vy)
			self.Bullet_Mobs.add(Bullet)

		for i in range(count3):
			Bullet = bullet()
			Bullet.read(i, "main")
			Bullet = bullet(Bullet.pos, self, bg, Bullet.name, Bullet.vx, Bullet.vy)
			self.Bullet_Main.add(Bullet)
		self.stage = int(read[3])
		self.RATIO = int(read[4])
		mc.read(self)
		self.updated = True
		self.minimap = minimap((0, 0), self)
		self.minimap = minimap((self.width - self.bg.w/self.minimap.ratio*self.RATIO/100 - 5, self.height - self.bg.h/self.minimap.ratio*self.RATIO/100 - 5), self)

			

		
