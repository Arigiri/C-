from Mob4 import *
from entity import *

class mob2(fish):
	def __init__(self, pos = (0,0), name = "mob2\\ca21", Game = 0, bg = 0, maxhealth = 0):
		super(mob2, self).__init__(pos, name, Game, bg, maxhealth, 2)
	Del = 0
	def find_ab(self, mc, bg):
		x0 = self.pos[0]
		y0 = self.pos[1]
		x1 = mc.pos[0]
		y1 = mc.pos[1]
		D = x0 - x1
		Dx = y0 - y1
		Dy = y1 * x0 - x1 * y0
		if D == 0:
			return BULLET_SPEED, 0
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
		delta = (-2 * x0 + 2 * a * b - 2 * a * y0) * (-2 * x0 + 2 * a * b - 2 * a * y0) - 4 * (1 + a * a) * (x0 * x0 + (b - y0) * (b - y0) - BIG_BULLET_SPEED * BIG_BULLET_SPEED)
		delta **= (1/2)
		x1 = ((2 * x0 - 2 * a * (b - y0)) - delta)/(2 * (1 + a * a))
		x2 = ((2 * x0 - 2 * a * (b - y0)) + delta)/(2 * (1 + a * a))
		# x1 -= delta
		y1 = x1 * a + b
		y2 = x2 * a + b
		A = self.distance((x1, y1), self.pos)
		B = self.distance((x1, y1), mc.pos)
		C = self.distance(self.pos, mc.pos)
		if A + B == C:
			return (x1, y1)
		return (x2, y2)

	def Fire(self, mc, bg, game):		
		if self.Del >= BIG_BULLET_WAIT:
			self.Del = 0
		else:
			self.Del += 1
			self.fire = False
			return bullet()
		
		x = mc.pos[0] + mc.w/2
		y = mc.pos[1] + mc.h/2
		image = pygame.image.load("mob2\\big_bullet.png")
		w = image.get_width()
		h = image.get_height()
		image = pygame.transform.scale(image, (w * game.RATIO//100, h *game.RATIO//100))
		w = image.get_width()
		h = image.get_height()
		self.bg = bg
		tt = "ca2"
		if self.direction == "LEFT":
			x1 = self.pos[0] - self.w
		else:
			x1  = self.pos[0]
			tt = "cas2"
		y1 = self.pos[1] + self.h/2
		self.image = pygame.image.load("mob2\\" + tt + "F.png")
		w = self.image.get_width()
		h = self.image.get_height()
		self.image = pygame.transform.scale(self.image, (w * game.RATIO//100, h *game.RATIO//100))
		self.fire = True
		self.a, self.b = self.find_ab(mc, bg)

		vx, vy = self.find_v(mc, bg)

		vx = abs(vx - self.pos[0])
		vy = abs(vy - self.pos[1])
		if mc.pos[0] < self.pos[0]:
			vx *= -1
		if mc.pos[1] < self.pos[1]:
			vy *= -1
		# pygame.display.update()
		Bullet = bullet((x1, y1), self.Game, bg, "mob2\\big_bullet.png", vx, vy)
		return Bullet
