from Mob4 import *
from entity import *
class Freeze(pygame.sprite.Sprite):
	image = ""
	name = ""
	def __init__(self, pos = (0, 0), name = ""):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.name = name
		if self.name == "":
			return
		self.image = pygame.image.load(self.name)
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
	def draw(self,Surface):
		Surface.blit(self.image,self.pos)
	def update(self, Fish):
		if fish.direction == "LEFT":
			x = fish.pos[0] - self.w
			y = fish.pos[1] - fish.h - 100 * self.h/2
		else:
			x = fish.pos[0] + fish.w 
			y = fish.pos[1] - fish.h - self.h/2
		self.pos = (x, y)
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		
	
class mob3(fish):
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob3, self).__init__(pos, name, Game, bg, maxhealth, 3)
	freeze = Freeze()
	old_time = 0
	def LIGHT(self):
		curr_time = pygame.time.get_ticks()
		if curr_time - self.old_time > FREEZE_TIME * 100000 and self.old_time != 0:
			self.freeze = Freeze()
			return
			pass
		else:
			self.old_time = curr_time
		self.freeze = Freeze((0,0), "freeze1.png")
		name = "freeze"
		if self.direction == "LEFT":
			x = self.pos[0]  - self.freeze.w
			y = self.pos[1] - self.h/2 - self.h/4 #+ self.freeze.h/2
			name += "1"
		else:
			x = self.pos[0] + self.w# + self.freeze.w
			y = self.pos[1] - self.h/2 - self.h/4
			name += "2"
		self.freeze = Freeze((x,y), name + ".png")

		

