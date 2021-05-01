from Game import *
from entity import *
from bg import *
from MC import *
from setting import *
from Mob4 import *
from Menu import *
import pygame
from pygame.locals import *
from random import *
from Blade import *
from minimap import *
import time




def health_bar(fish):
	x = fish.Game.width * 70 // 100
	y = HEALTH_HEIGHT
	COLOR1 = (111, 116, 111)
	COLOR2 = (58, 58, 58)
	COLOR3 = (34,255,4)
	w1 = image1.get_width()
	w2 = image2.get_width()	
	w3 = image3.get_width()
	w4 = image6.get_width()
	h = image3.get_height()
	fish.health = max(fish.health, 0)
	health_len = (Game.width - 30 - x - 15)/fish.maxhealth
	mw = health_len * fish.maxhealth
	nw = (fish.health * health_len)
	#health bg
	pygame.draw.rect(Game.screen, COLOR2, (x + w2, y, Game.width - 30 - x - w2 + 10, image2.get_height()))
	Game.screen.blit(image2, (x, y))
	#curr_health
	
	Game.screen.blit(image6, (x + 15, y + 6))
	pygame.draw.rect(Game.screen, COLOR1, (x  + w4, y + 10, Game.width - 30 - x - w2 + 26, image4.get_height()))
	for life in range(MC_LIVES):
		img = pygame.image.load("tim2.png")
		Game.screen.blit(img, (Game.width - img.get_width() * (life + 1) - 30 * (life + 1), y + 10 + img.get_height()))
	for life in range(fish.lives):
		img = pygame.image.load("tim1.png")
		Game.screen.blit(img, (Game.width - img.get_width() * (life + 1) - 30 * (life + 1), y + 10 + img.get_height()))
	if(fish.health == fish.maxhealth):Game.screen.blit(image4, (x + 15, y + 10))
	if fish.health > 0:
		lx = x + 15 + image4.get_width() - nw + mw
		ly = y + 10
		pygame.draw.rect(Game.screen, COLOR3, (lx, ly, nw - 15, image4.get_height()))
	else:
		if fish.lives > 1:
			fish.lives -= 1
			fish.health = fish.maxhealth
		else:
			exit()

def draw_stamia(fish):
	rx = fish.pos[0] + fish.w +fish.sw
	ry = fish.pos[1] + fish.sh
	h = fish.sh/FULL_STAMIA * fish.stamia
	lx = rx - fish.sw
	ly = ry - h
	pygame.draw.rect(Game.screen, YELLOW,  (lx, ly, fish.sw, h))
	Game.screen.blit(fish.stamia_image, (fish.pos[0] + fish.w, fish.pos[1]))
def end_stage():
	if len(Game.mobs)== 0:
		global img, rect
		if Game.stop == 0:

			img = pygame.image.load("setting\\clear_stage.png")
			rect = img.get_rect(center = (Game.width/2, Game.height/2))
			Game.stop += 1 
		elif Game.stop < 50:
			Game.stop += 1
			Game.screen.blit(img, rect)
			pygame.display.update()
		else:
			Game.stop = 0
			Game.load(bg, Fish1)
		
		
		
def get_mobs_on_screen(Game, bg):
	mobs = pygame.sprite.Group()
	posl = (-bg.x, -bg.y)
	posr = (-bg.x + Game.width, -bg.y + Game.height)
	for mob in Game.mobs:
		if (mob.rpos[0] >= posl[0] and mob.rpos[0] <= posr[0] and mob.rpos[1] >= posl[1] and mob.rpos[1] <= posr[1]) or (mob.rpos[0] + mob.w >= posl[0] and mob.rpos[0] + mob.w <= posr[0] and mob.rpos[1] + mob.h >= posl[1] and mob.rpos[1] + mob.h <= posr[1]):
			mobs.add(mob)
	return mobs
def process():
	#set fps
	Time.tick(fps)
	#stage
	end_stage() 
	#process events
	
	d = pygame.key.get_pressed()
	if d[K_ESCAPE]:
		if Game.Pause == False:
			Game.Pause = True
			pygame.mouse.set_visible(True)
		else:
			Game.Pause = False
			pygame.mouse.set_visible(False)

	if d[K_F4]:
		exit()
	if Game.Pause == True:
		Game.menu.draw(Game.screen)
		Game.Buttons.draw(Game.screen)
		Game.menu.update(Game, Fish1, bg)
		pygame.display.flip()
		for fish in Main_Fish:
			fish.move = 0
		return
	else:
		pygame.mouse.set_visible(False)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		if event.type == MOUSEBUTTONDOWN:

			if event.button == 1:
				blade = Blade(Fish1)
				if blade.blade != "":
					Game.Blade_mc.add(blade) 
			else:
				for fish in Main_Fish:
					fish.dash = True
		if event.type == KEYDOWN and event.key == K_SPACE:
			bullet = Fish1.Fire(bg)
			if bullet.name != "":
				Game.Bullet_Main.add(bullet)
	if len(Game.mobs) == 0:
		return
	#update
	bg.update(Fish1)

	#check fish in current screen
	mobs = pygame.sprite.Group()
	mobs = get_mobs_on_screen(Game, bg)
	# mobs = Game.mobs
	#bullet hit fish

	hits = pygame.sprite.groupcollide(mobs, Game.Bullet_Main, False, True, pygame.sprite.collide_mask)
	
	for hit in hits:	
		if not hit.shield:
			hit.health -= MAIN_DAMAGE
			if hit.health <= 0:
				# hit.name = ""
				hit.kill()
	hits = pygame.sprite.groupcollide(Main_Fish, Game.Bullet_Mobs, False, True, pygame.sprite.collide_rect)
	for hit in hits:
		if hit.immune:
			continue
		hit.health -= BULLET_DAMAGE	
	hits = pygame.sprite.groupcollide(mobs, Main_Fish, False, False, pygame.sprite.collide_rect)
	for hit in hits:
		if hit.mob == 4 or hit.mob == 1:
			for fish in Main_Fish:
				fish.health -= SPLASH_DAMAGE
	for fish in Game.Boss:
		hits = pygame.sprite.groupcollide(Main_Fish, fish.Bullet, False, True, pygame.sprite.collide_rect)
		for hit in hits:
			hit.health -= BULLET_DAMAGE
		hits = pygame.sprite.groupcollide(Main_Fish, fish.Laser, False, False, pygame.sprite.collide_mask)
		for hit in hits:
			hit.health -= LASER_DAMAGE
	if len(Game.Blade_mc) >= 1:
		hits = pygame.sprite.groupcollide(mobs, Game.Blade_mc, False, False, pygame.sprite.collide_rect)
		for hit in hits:  
			if hit.shield:
				hit.health -= BLADE_DAMAGE//3
			else:
				hit.health -= BLADE_DAMAGE
			if hit.health <= 0:
					hit.kill()

	#update mobs_0
	sp = pygame.sprite.Group()
	for fish in mobs:
		if fish.mob == 3:
			if fish.LIGHT():
				sp.add(fish.freeze)
	hits = pygame.sprite.groupcollide(Main_Fish, sp,False, False, pygame.sprite.collide_rect)
	for hit in hits:
		hit.Slow = 1
		hit.Slow_Time = SLOW_TIME

	Game.mobs.update(bg, Fish1, Game) 

	#mobs attack
	for fish in mobs:
		if fish.mob == 0 or fish.mob == 2:
			bullet = fish.Fire(Fish1, bg, Game)
			if bullet.name != "":
				Game.Bullet_Mobs.add(bullet)
	for boss in Game.Boss:
		boss.attack(bg, Game)
	for fish in Game.mobs_4:
		fish.Slash(Fish1, Game)
	for fish in Game.mobs_1:
		fish.Roar()

	for blade in Game.Blade_mc:
		if blade.update(Fish1, Game):
			blade.kill()
	Game.Bullet_Mobs.update(bg,"mobs_0", Fish1, Game)
	for boss in Game.Boss:
		boss.Bullet.update(bg, "boss", Fish1, Game)
		# boss.Laser.update()

	#mc update
	Main_Fish.update(bg, Game)
	Game.Bullet_Main.update(bg, "MAIN", Fish1, Game)
	#minimap update
	Game.minimap.update(Game,bg, Fish1)
	#draw
	bg.draw(Game.screen)	
	Game.mobs.draw(Game.screen)
	Game.Bullet_Main.draw(Game.screen)
	Game.Bullet_Mobs.draw(Game.screen)
	# Game.Buttons.draw(Game.screen)
	Main_Fish.draw(Game.screen)
	for light in sp:
		light.draw(Game.screen)

	for blade in Game.Blade_mc:
		if blade.image != "":
			Game.Blade_mc.draw(Game.screen)
	for fish in Main_Fish: fish.draw_blade(Game)
	#draw health
	for fish in Game.mobs:
		if fish.mob != 100:
			fish.draw_health()
	health_bar(Fish1)	
	for fish in Game.Boss:
		fish.Bullet.draw(Game.screen)
		fish.Laser.draw(Game.screen)
		fish.draw_health(Game)
	#draw stamia
	for fish in Main_Fish:
		draw_stamia(fish)
	for fish in Game.mobs:
		if fish.mob == 4:
			if fish.fire:
				pygame.draw.line(Game.screen, RED, Fish1.rect.center, fish.rect.center, 5)
	#draw minimap
	Game.minimap.draw(Game)
	#update display
	pygame.display.flip()
	pygame.display.update()	


if __name__ == '__main__':
	Game = game()
	bg = bg(0, 0, Game)
	# print(Game.Min_ratio)
	Menu = menu(Game)
	Time = pygame.time.Clock()
	Fish1 = mc()
	while(Menu.update(Fish1, bg)):
		Time.tick(fps)
	
	if Fish1.name == "":
		# print(1)
		Fish1 = mc((Game.width/2, Game.height/2), "mc1", Game, bg, MC_HEALTH)
		# print(Fish1.name)
	Game.stage = 7
	if not Game.updated:
		Game.load(bg, Fish1)
		Game.setup(bg, Fish1)
	bg.image = pygame.transform.scale(bg.image, (bg.w * Game.RATIO // 100, bg.h * Game.RATIO // 100))
	bg.w = bg.image.get_width()
	bg.h = bg.image.get_height()
	global MAIN_SPEED
	MAIN_SPEED = MAIN_SPEED * Game.RATIO/100
	# print
	Main_Fish = pygame.sprite.GroupSingle()
	
	Main_Fish.add(Fish1)

	curr_time = pygame.time.get_ticks()
	while(1):
		tme = pygame.time.get_ticks()
		if tme - curr_time >= MC_IMMUNE_TIME * 100:
			for fish in Main_Fish:
				fish.immune = False
		process()