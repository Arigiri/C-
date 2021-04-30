#normal mod
from Mob4 import *
from entity import *
class mob0(fish):
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob0, self).__init__(pos, name, Game, bg, maxhealth, 0)
	Del = 0
	ani = 0
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
		delta = (-2 * x0 + 2 * a * b - 2 * a * y0) * (-2 * x0 + 2 * a * b - 2 * a * y0) - 4 * (1 + a * a) * (x0 * x0 + (b - y0) * (b - y0) - BULLET_SPEED * BULLET_SPEED)
		delta **= (1/2)
		x1 = ((2 * x0 - 2 * a * (b - y0)) - delta)/(2 * (1 - a * a))
		x2 = ((2 * x0 - 2 * a * (b - y0)) + delta)/(2 * (1 - a * a))
		# x1 -= delta
		y1 = x1 * a + b
		y2 = x2 * a + b
		A = self.distance((x1, y1), self.pos)
		B = self.distance((x1, y1), mc.pos)
		C = self.distance(self.pos, mc.pos)
		if A + B == C:
			return (x1, y1)
		return (x2, y2)
	def find(self, mc):
		x0 = self.pos[0]
		y0 = self.pos[1]
		x1 = mc.pos[0]
		y1 = mc.pos[1]
		if y1 == y0:
			return BULLET_SPEED, 0
		a = (x1 - x0)/(y1 - y0)
		b =(x0 * x1 - x0 * x0 - y0 * y1 + y0 * y0)/(y1 - y0)
		return a, b
	def Fire(self, mc, bg, game):		
		if self.Del >= BULLET_WAIT:
			self.Del = 0
		else:
			self.Del += 1
			return bullet()
		
		x = mc.pos[0] + mc.w/2
		y = mc.pos[1] + mc.h/2
		self.bg = bg
		name = ""
		if self.direction == "LEFT":
			x1 = self.pos[0] - self.bullet[0].w
			name = "bullet2"
		else:
			x1  = self.pos[0] + self.w
			name = "bullet2"
		y1 = self.pos[1] + self.h/2
		
		vx = x - x1
		vy = y - y1
		# p1 = mc.rect.center
		# p2 = self.rect.center
		# p = (p1[0] - p2[0], p1[1] - p2[1])
		# dist = (p[1] * p[1] + p[0] * p[0]) ** (1/2)
		# if p[1] == 0:
		# 	vy = 0
		# 	if vx > 0:vx = BULLET_SPEED 
		# 	else: vx = -BULLET_SPEED
		# else:
		# 	ratio = p[0]/p[1]
		# 	if abs(vx) > abs(vy) and ratio > 1:
		# 		if vx > 0:
		# 			vx = BULLET_SPEED
		# 		else:
		# 			vx = -BULLET_SPEED
		# 		vy = vx/ratio
		# 	else:
		# 		if vy > 0:
		# 			vy = BULLET_SPEED
		# 		else:
		# 			vy = -BULLET_SPEED
		# 		vx = vy*ratio
		self.a, self.b = self.find_ab(mc, bg)
		# if self.b == 0:
		# 	vx, vy = a,b
		# else:
		vx, vy = self.find_v(mc, bg)
		# print()
		# print(vx, vy)
		vx = vx - self.pos[0]
		vy = vy - self.pos[1]
		# print((vx ** 2 + vy ** 2) ** (1/2))
		# print()
		# self.a, self.b = self.find(mc)
		# if vx > 0:
		# 	vx = BULLET_SPEED
		# else:
		# 	vx = -BULLET_SPEED
		# vy = vx * self.a + self.b
		# vx = vx - self.pos[0]
		# vy = vy - self.pos[1] 
		
		# if abs(vx) > BULLET_SPEED or abs(vy) > BULLET_SPEED:
		# 	vx /= (vx/BULLET_SPEED)
		# 	vy /= (vx/BULLET_SPEED)
		print(vx, vy)
		Bullet = bullet((x1, y1), self.Game, bg, name + ".png", vx, vy)
		return Bullet

