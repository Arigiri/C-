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

	mw = fish.Game.width - 30  - x
	health_len = mw/100
	nw = fish.health * health_len
	#health bg
	pygame.draw.rect(Game.screen, COLOR2, (x + w2, y, Game.width - 30 - x - w2 + 10, image2.get_height()))
	Game.screen.blit(image2, (x, y))
	#curr_health
	
	Game.screen.blit(image6, (x + 15, y + 6))
	pygame.draw.rect(Game.screen, COLOR1, (x  + w4, y + 10, Game.width - 30 - x - w2 + 26, image4.get_height()))
	if(fish.health == fish.maxhealth):Game.screen.blit(image4, (x + 15, y + 10))
	if(fish.health > 7):pygame.draw.rect(Game.screen, COLOR3, (Game.width - nw+ 10, y + 10, nw - 30, image4.get_height() - 1))
	else:
		exit()

def end_stage():
	if len(Game.mobs)== 0:
		Game.load(bg, Fish1)
		print(1)

def process():
	#set fps
	Time.tick(fps)
	#stage
	end_stage() 
	#process events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		elif event.type == KEYDOWN and event.key == K_F4:
			exit()
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				Game.Blade_mc.add(Blade(Fish1)) 
			else:
				for fish in Main_Fish:
					fish.dash = True

		if event.type == KEYDOWN and event.key == K_SPACE:
			Game.Bullet_Main.add(Fish1.Fire(bg))
		if (event.type == KEYDOWN and event.key == K_ESCAPE) or (event.type == MOUSEBUTTONDOWN and Game.menu.button.get_clicked()) :
			if Game.Pause == False:
				Game.Pause = True
			else:
				Game.Pause = False
	if Game.Pause == True:
		pygame.mouse.set_pos(Game.width/2, Game.height/2)
		Game.menu.draw(Game.screen)
		pygame.display.flip()
		return
	#update
	bg.update(Fish1)
	
	#bullet hit fish
	hits = pygame.sprite.groupcollide(Game.mobs, Game.Bullet_Main, False, True, pygame.sprite.collide_rect)
	for hit in hits:
		if not hit.shield:
			hit.health -= MAIN_DAMAGE
			if hit.health <= 0:
				hit.name = ""
				hit.kill()
	hits = pygame.sprite.groupcollide(Main_Fish, Game.Bullet_Mobs, False, True, pygame.sprite.collide_rect)
	for hit in hits:
		if hit.immune:
			continue
		hit.health -= BULLET_DAMAGE	
	hits = pygame.sprite.groupcollide(Main_Fish, Game.mobs, False, False, pygame.sprite.collide_mask)
	for hit in hits:
		hit.health -= SPLASH_DAMAGE
	if len(Game.Blade_mc) >= 1:
		hits = pygame.sprite.groupcollide(Game.mobs, Game.Blade_mc, False, False, pygame.sprite.collide_mask)
		for hit in hits:
			if hit.shield:
				hit.health -= BLADE_DAMAGE//3
			else:
				hit.health -= BLADE_DAMAGE
			if hit.health <= 0:
					hit.kill()

	#update mobs_0
	Game.mobs.update(bg, Fish1, Game) 
	#mobs attack
	for fish in Game.mobs_0:
		bullet = fish.Fire(Fish1, bg, Game)
		if bullet.name != "":
			Game.Bullet_Mobs.add(bullet)
	for fish in Game.mobs_2:
		bullet = fish.Fire(Fish1, bg, Game)
		if bullet.name != "":
			Game.Bullet_Mobs.add(bullet)
	for fish in Game.mobs_4:
		fish.Slash(Fish1)
	for fish in Game.mobs_1:
		fish.Roar()
	for blade in Game.Blade_mc:
		if blade.update(Fish1):
			blade.kill()
	Game.Bullet_Mobs.update(bg,"mobs_0")
	

	#mc update
	Main_Fish.update(bg)
	Game.Bullet_Main.update(bg, "MAIN")

	#draw
	bg.draw(Game.screen)
	Game.mobs.draw(Game.screen)
	Game.Bullet_Main.draw(Game.screen)
	Game.Bullet_Mobs.draw(Game.screen)
	Game.Buttons.draw(Game.screen)
	Main_Fish.draw(Game.screen)
	for blade in Game.Blade_mc:
		if blade.image != "":
			Game.Blade_mc.draw(Game.screen)
	for fish in Main_Fish: fish.draw_blade(Game)
	#draw health
	for fish in Game.mobs:
		fish.draw_health()
	health_bar(Fish1)	

	#update display
	pygame.display.flip()
	pygame.display.update()	

if __name__ == '__main__':
	Game = game()
	bg = bg(-500, -500, Game)
	Menu = menu(Game)
	while(Menu.update()):
		pass
	
	Fish1 = mc((Game.width/2, Game.height/2), "ca21", Game, bg, MC_HEALTH + 1)
	Game.load(bg, Fish1)
	Game.setup(bg, Fish1)
	Main_Fish = pygame.sprite.GroupSingle()
	
	Main_Fish.add(Fish1)


	Time = pygame.time.Clock()
	curr_time = pygame.time.get_ticks()
	while(1):
		tme = pygame.time.get_ticks()
		if tme - curr_time >= MC_IMMUNE_TIME * 100:
			for fish in Main_Fish:
				fish.immune = False
		process()