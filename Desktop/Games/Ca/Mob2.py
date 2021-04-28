from Mob4 import *
from entity import *

class mob2(fish):
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob2, self).__init__(pos, name, Game, bg, maxhealth, 2)
	Del = 0
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
		pygame.transform.scale(image, (w * RATIO//100, h *RATIO//100))
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
		self.fire = True
		vx = x - (x1 + w/2)
		vy = y - (y1 + h/2)
		p1 = mc.rect.center
		p2 = self.rect.center
		p = (p1[0] - p2[0], p1[1] - p1[1])
		dist = (p[1] * p[1] + p[0] * p[0]) ** (1/2)
		# if dist <= BIG_BULLET_SPEED * 10:
		# 	vx *= 3
		# 	vy *= 3
		pygame.display.update()
		Bullet = bullet((x1, y1), self.Game, bg, "mob2\\big_bullet.png", vx//BIG_BULLET_SPEED, vy//BIG_BULLET_SPEED)
		return Bullet
