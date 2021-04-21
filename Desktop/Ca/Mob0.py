#normal mod
from Mob4 import *
from entity import *
class mob0(fish):
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob0, self).__init__(pos, name, Game, bg, maxhealth, 0)
	Del = 0
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
		p1 = mc.rect.center
		p2 = self.rect.center
		p = (p1[0] - p2[0], p1[1] - p1[1])
		dist = (p[1] * p[1] + p[0] * p[0]) ** (1/2)
		if dist <= BULLET_SPEED * 10:
			vx *= 3
			vy *= 3
		pygame.display.update()
		Bullet = bullet((x1, y1), self.Game, bg, name + ".png", vx//BULLET_SPEED, vy//BULLET_SPEED)
		return Bullet

