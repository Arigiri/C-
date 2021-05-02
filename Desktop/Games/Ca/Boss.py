import pygame
from Bullet import *
from entity import *
from Mob4 import *
from Mob0 import *
from Mob1 import *
from Mob2 import *
from Mob3 import *
from entity import *
from random import *
class Laser(pygame.sprite.Sprite):
	def __init__(self, pos = (0, 0), rot = 0, Game = ""):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.rot = rot
		self.image1 = pygame.image.load("laser.png")
		w = self.image1.get_width()
		h = self.image1.get_height()
		self.image1 = pygame.transform.scale(self.image1, (w * Game.RATIO // 100, h * Game.RATIO // 100))
		# self.image = pygame.transform.rotozoom(self.image1,rot, 1)
		self.image = self.image1
		self.offset = pygame.Vector2(0, 250)
		self.rect = self.image.get_rect(center=self.pos+self.offset)
	def update(self, pos, rot):
		self.pos = pos
		self.rot = rot
		self.rotate()

		# self.image = pygame.image.load("laser.png")
	def rotate(self):
		self.image = pygame.transform.rotozoom(self.image1, -self.rot, 1)
		offset_rotated = self.offset.rotate(self.rot)
		self.rect = self.image.get_rect(center=self.pos+offset_rotated)


class Boss(fish):
	phase = 0
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(Boss, self).__init__(pos, name, Game, bg, maxhealth, 100)
		self.phase = 1
		self.health = randint(400, 1300)
		self.maxhealth = self.health
		self.shield = False

	stay_time = 500
	Bullet = pygame.sprite.Group()
	CD_S1 = 15
	old_time_S1 = 0
	old_time_S2 = 0
	old_time_CD_ATK = 0
	stay_time_s1 = 0
	stay_time_s2 = 5000
	skill_CD = 5000
	wait = 0
	done = True
	old_time_phase_2 = 0
	CD_phase_2 = 1000
	S2_ATK = False
	angle = -60
	skill_CD_S3 = 100
	Laser = pygame.sprite.Group()
	def draw_health(self, Game):
		image = pygame.image.load("boss.png")
		phs = pygame.image.load("phase.png")
		max_len = Game.width * 2 / 4
		health_percent = self.health/self.maxhealth
		x = image.get_width() + 30#(Game.width - max_len)/6
		y = image.get_height()/2#Game.height/30
		COLOR1 = (111, 116, 111)
		COLOR2 = (58, 58, 58)
		COLOR3 = (34,255,4)
		ls = x + max_len
		w = max_len * health_percent
		if self.phase == 1:
			color = GREEN
		elif self.phase == 2:
			color = YELLOW
		else:
			color = RED
		pygame.draw.rect(Game.screen, COLOR2, (x,y, max_len,25))
		pygame.draw.rect(Game.screen, color, (ls -  w + 2.5, y + 2.5, w - 5,25 - 5))
		Game.screen.blit(image, (0, 0))
		# Game.screen.blit(phs, (ls + 3, y - 15 + image.get_height()))
	def reborn(self):
		if self.phase == 2:
			self.health = 1.15 * self.maxhealth
			self.maxhealth = self.health
		else:
			self.health = (1.5/1.15) * self.maxhealth
			self.maxhealth = self.health
	def kill(self):
		if self.phase == 3:
			self.name = ""
		else: 
			self.phase += 1
			self.reborn()
	old_name = ""
	def Skill2(self, Game):
		curr_time = pygame.time.get_ticks()
		if not self.S2_ATK:
			self.angle = 0
			self.old_time_S2 = curr_time
			self.S2_ATK = True
			self.stay = True
			pos = self.pos
			K = True
			for name in self.name:
				if name == 'F': K = False
			if K:
				self.old_name = self.name
			if self.direction == "LEFT":
				pos = (self.pos[0], self.pos[1] + self.h/2)
				self.name = "mob100\\ca100F2.png"
			else:
				pos = (self.pos[0] + self.w, self.pos[1] + self.h/2)
				self.name = "mob100\\cas100F2.png"
			self.laser = Laser(pos, self.angle, Game)
			self.Laser.add(self.laser)

		elif -self.old_time_S2 + curr_time < self.stay_time_s2 * Game.RATIO/100:
			self.angle += 3.5
			pos = self.pos
			angle = self.angle
			K = True
			for name in self.name:
				if name == 'F': K = False
			if K:
				self.old_name = self.name
			if self.direction == "LEFT":
				pos = (self.pos[0], self.pos[1] + self.h/2)
				self.name = "mob100\\ca100F2.png"
			else:
				pos = (self.pos[0] + self.w, self.pos[1] + self.h/2)
				self.name = "mob100\\cas100F2.png"
				angle *= -1
			self.Laser.update(pos, angle)
		else:
			self.S2_ATK = False
			self.stay = False
			self.name = self.old_name
			for laser in self.Laser:
				laser.kill()



	def Skill1(self, Game, bg, rot):
		curr_time = pygame.time.get_ticks()
		# if self.atk == True:
		# 	if (curr_time - self.old_time_S1 < self.CD_S1 * 100 and self.old_time_S1 != 0):
		# 		return
		self.old_time_S1 = curr_time
		vx = 20
		vy = 20
		alpha = 20
		O = self.rect.center
		if curr_time - self.stay_time >= self.stay_time:
			angle = alpha
			for i in range(11):
				vx1 = vx * cos(angle + rot) - vy * sin(angle + rot) + O[0]
				vy1 = vx * sin(angle + rot) + vx * cos(angle + rot) + O[1]
				vx2 = vx1 - O[0]
				vy2 = vy1 - O[1]
				vx2/=2
				vy2/=2
				Bullet = bullet((vx1, vy1), Game, bg, "bosss1_animation\\bullet1.png",vx2, vy2)
				Bullet.type = "boss"
				self.Bullet.add(Bullet)
				angle += alpha
	def spawn(self, mob, bg ,Game):
		if mob == 1:
			fish = mob1((randint(0, bg.w), randint(0, bg.h)), "mob1\\ca11", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_1.add(fish)
		if mob == 2:
			fish = mob2((randint(0, bg.w), randint(0, bg.h)), "mob2\\ca21", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_2.add(fish)
		if mob == 3:
			fish = mob3((randint(0, bg.w), randint(0, bg.h)), "mob3\\ca31", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_3.add(fish)
			Game.mobs.add(fish)
			fish = mob3((randint(0, bg.w), randint(0, bg.h)), "mob3\\ca31", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_3.add(fish)
			Game.mobs.add(fish)
		if mob == 4:
			fish = mob4((randint(0, bg.w), randint(0, bg.h)), "mob4\\ca41", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_4.add(fish)
			Game.mobs.add(fish)
			fish = mob4((randint(0, bg.w), randint(0, bg.h)), "mob4\\ca41", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_4.add(fish)
			Game.mobs.add(fish)
		if mob == 0:
			fish = mob0((randint(0, bg.w), randint(0, bg.h)), "mob0\\ca01", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_0.add(fish)
			Game.mobs.add(fish)
			fish = mob0((randint(0, bg.w), randint(0, bg.h)), "mob0\\ca01", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_0.add(fish)
			Game.mobs.add(fish)
			fish = mob0((randint(0, bg.w), randint(0, bg.h)), "mob0\\ca01", Game, bg, MOB_MAX_HEALTH)
			Game.mobs_0.add(fish)
			Game.mobs.add(fish)


		
		return Game
	def Skill3(self, game, bg):
		if self.skill_CD_S3:
			self.skill_CD_S3 -= 1
			print(self.skill_CD_S3)
			return
		else:
			self.skill_CD_S3 = 100
		if len(game.mobs) > 8:
			return
		mobs = [0, 0, 0, 1, 2, 3, 3, 4, 4]
		mob1 = choice(mobs)
		mob2 = choice(mobs)
		while(mob2 == mob1):
			mob2 = choice(mobs)
		game = self.spawn(mob1, bg, game)
		game = self.spawn(mob2, bg, game)
	def phase1(self, Game, bg):
		atkS = randint(0, 3)
		if atkS <= 2 and not self.S2_ATK:
			self.Skill1(Game, bg, 0)
		else: self.Skill2(Game)
		# self.Skill3(Game, bg)
	def phase2(self, Game, bg):
		atkS = randint(0, 3)
		if atkS <= 2 and not self.S2_ATK or not self.done:
			if self.done == True:
				self.done = False
				self.Skill1(Game, bg, 0)
			else:
				if self.wait >= 25:
					self.done = True
					self.Skill1(Game, bg, 30)
					self.wait = 0
				else:
					self.wait += 1
		else:
			self.Skill2(Game)
	def phase3(self, Game, bg):
		atkS = randint(0, 3)
		if atkS <= 2 and not self.S2_ATK or not self.done:	
			if self.done == True:
				self.done = False
				self.Skill1(Game, bg, 0)
			else:
				if self.wait == 25:
					self.Skill1(Game, bg, 30)
					self.wait += 1
				elif self.wait >= 50:
					self.done = True
					self.Skill1(Game, bg, 0)
					self.wait = 0
				else:
					self.wait += 1
	def attack(self, bg,Game):
		curr_time = pygame.time.get_ticks()
		if self.skill_CD_S3:
			self.skill_CD_S3 -= 1
		if self.skill_CD_S3 == 0:
			if self.phase != 1:
				self.Skill3(Game, bg)
			self.skill_CD_S3 = 50
	
		if curr_time - self.old_time_CD_ATK < self.skill_CD and self.old_time_CD_ATK != 0 and self.done and not self.S2_ATK:
			return
		
		
		self.old_time_CD_ATK = curr_time
		if self.phase == 1:
			self.phase1(Game, bg)

		elif self.phase == 2:
			self.phase2(Game, bg)
		else:
			self.phase3(Game, bg)
		# self.phase3(Game, bg)

