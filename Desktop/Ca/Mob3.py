from Mob4 import *
from entity import *

class mob3(fish):
	def __init__(self, pos = (0,0), name = "", Game = 0, bg = 0, maxhealth = 0):
		super(mob3, self).__init__(pos, name, Game, bg, maxhealth, 2)
	def freeze(self):
		