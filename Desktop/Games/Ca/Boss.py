import pygame
from Bullet import *
from entity import *
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
	old_time_CD_ATK = 0
	stay_time_s1 = 0
	skill_CD = 5000
	wait = 0
	done = True
	old_time_phase_2 = 0
	CD_phase_2 = 1000
	def draw_health(self, Game):
		max_len = Game.width * 2 / 4
		health_percent = self.health/self.maxhealth
		x = (Game.width - max_len)/6
		y = Game.height/30
		COLOR1 = (111, 116, 111)
		COLOR2 = (58, 58, 58)
		COLOR3 = (34,255,4)
		ls = x + max_len
		w = max_len * health_percent

		pygame.draw.rect(Game.screen, COLOR2, (x,y, max_len,25))
		pygame.draw.rect(Game.screen, RED, (ls -  w + 2.5, y + 2.5, w - 5,25 - 5))
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
	def Skill1(self, Game, bg, rot):
		curr_time = pygame.time.get_ticks()
		# if self.atk == True:
		# 	if (curr_time - self.old_time_S1 < self.CD_S1 * 100 and self.old_time_S1 != 0):
		# 		return

		self.stay = False
		self.old_time_S1 = curr_time
		self.stay = False
		vx = 20
		vy = 20
		alpha = 20
		O = self.rect.center
		if curr_time - self.stay_time >= self.stay_time:
			angle = alpha
			for i in range(10):
				vx1 = vx * cos(angle + rot) - vy * sin(angle + rot) + O[0]
				vy1 = vx * sin(angle + rot) + vx * cos(angle + rot) + O[1]
				vx2 = vx1 - O[0]
				vy2 = vy1 - O[1]
				vx2/=2
				vy2/=2
				self.Bullet.add(bullet((vx1, vy1), Game, bg, "BOSS_BULLET.png",vx2, vy2))
				angle += alpha
	def phase1(self, Game, bg):
		self.Skill1(Game, bg, 0)
	
	def phase2(self, Game, bg):
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
	def phase3(self, Game, bg):

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
		if curr_time - self.old_time_CD_ATK < self.skill_CD and self.old_time_CD_ATK != 0 and self.done:
			return
		
		
		self.old_time_CD_ATK = curr_time
		if self.phase == 1:
			self.phase1(Game, bg)
		elif self.phase == 2:
			self.phase2(Game, bg)
		else:
			self.phase3(Game, bg)
		# self.phase3(Game, bg)

