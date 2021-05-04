from Mob4 import *
from entity import *
class Freeze(pygame.sprite.Sprite):
	image = ""
	name = ""
	fish = ""
	def __init__(self, pos = (0, 0), name = "", fish = "", Game = ""):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.name = name
		if self.name == "":
			return
		self.image = pygame.image.load(self.name)
		self.image = pygame.transform.scale(self.image, (self.image.get_width() * Game.RATIO // 100, self.image.get_height() * Game.RATIO // 100))
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.rect = self.image.get_rect()
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		self.fish = fish
	def draw(self,Surface):
		Surface.blit(self.image,self.rect)

	def update(self, fish, Game):
		if self.name == "":
			return
		name = "mob3\\freeze"
		if fish.direction == "LEFT":
			x = fish.pos[0] - self.w
			y = fish.pos[1] - fish.h/2 - fish.h/4
			name += "1"
		else:
			x = fish.pos[0] + fish.w 
			y = fish.pos[1] - fish.h/2 - self.h/4
			name += "2"
		self.image = pygame.image.load(name + ".png")
		self.image = pygame.transform.scale(self.image, (self.image.get_width() * Game.RATIO // 100, self.image.get_height() * Game.RATIO // 100))
		self.w = self.image.get_width()
		self.h = self.image.get_height()
		self.pos = (x, y)
		self.rect.center = (self.pos[0] + self.w/2, self.pos[1] + self.h/2)
		
	
class mob3(fish):
	def __init__(self, pos = (0,0), name = "mob3\\ca31", Game = 0, bg = 0, maxhealth = 0):
		super(mob3, self).__init__(pos, name, Game, bg, maxhealth, 3)
		self.Game = Game
	freeze = Freeze()
	old_time = 0
	freeze_delay = 0
	def find_ab(self, mc, bg):
		x0 = self.pos[0]
		y0 = self.pos[1]
		x1 = mc.pos[0]
		y1 = mc.pos[1]
		D = x0 - x1
		Dx = y0 - y1
		Dy = y1 * x0 - x1 * y0
		if D == 0:
			return bg.Game.BULLET_SPEED, 0
		x = Dx/D
		y = Dy/D
		return x, y
	def distance(self,A, B):
		x1 = A[0]
		y1 = A[1]
		x2 = B[0]
		y2 = B[1]
		x = x2 - x1
		y = y2 - y1
		return (x * x + y * y) ** 1/2
	def find_v(self, mc, bg):
		x0 = self.pos[0]
		y0 = self.pos[1]
		a = self.a
		b = self.b
		delta = (-2 * x0 + 2 * a * b - 2 * a * y0) * (-2 * x0 + 2 * a * b - 2 * a * y0) - 4 * (1 + a * a) * (x0 * x0 + (b - y0) * (b - y0) - bg.Game.BULLET_SPEED * bg.Game.BULLET_SPEED)
		delta **= (1/2)
		x1 = ((2 * x0 - 2 * a * (b - y0)) - delta)/(2 * (1 + a * a))
		x2 = ((2 * x0 - 2 * a * (b - y0)) + delta)/(2 * (1 + a * a))
		y1 = x1 * a + b
		y2 = x2 * a + b
		A = self.distance((x1, y1), self.pos)
		B = self.distance((x1, y1), mc.pos)
		C = self.distance(self.pos, mc.pos)
		if A + B == C:
			return (x1, y1)
		return (x2, y2)

	def LIGHT(self, mc, bg, game):
		curr_time = pygame.time.get_ticks()
		
		if self.freeze_delay == 0 and curr_time - self.old_time >= FREEZE_DELAY * 100 :

			self.freeze_delay = 1
			self.old_time = curr_time
			self.freeze = Freeze((0,0), "mob3\\freeze1.png", self, self.Game)
			name = "mob3\\freeze"
			tt = "ca31"
			if self.direction == "LEFT":
				x = self.pos[0]  - self.freeze.w
				y = self.pos[1] - self.h/2 - self.h/4 
				name += "1"
			else:
				x = self.pos[0] + self.w# + self.freeze.w
				y = self.pos[1] - self.h/2 - self.h/4
				name += "2"
				tt = "cas31"
			self.a,self.b = self.find_ab(mc, bg)
			vx,vy = self.find_v(mc, bg)
			vx = abs(vx - self.pos[0])
			vy = abs(vy - self.pos[1])
			if mc.pos[0] < self.pos[0]:
				vx *= -1
			if mc.pos[1] < self.pos[1]:
				vy *= -1
			name += '.png'
			angle = -1
			Bullet = bullet((x,y), game, bg, name, vx, vy)
			Bullet.type = "mobs_3"
			self.name = "mob3\\" + tt + ".png"
			game.Bullet_Mobs.add(Bullet)
			self.fire = True
		elif curr_time - self.old_time > FREEZE_TIME * 100 and self.freeze_delay != 0:
			self.freeze.kill()
			self.old_time = curr_time
			self.freeze_delay = 0
			self.fire = False
			return False


