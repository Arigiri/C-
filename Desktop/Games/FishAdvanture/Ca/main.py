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
	image2 = pygame.image.load("HP\\HP2.png")
	image4 = pygame.image.load("HP\\HP4.png")
	image6 = pygame.image.load("HP\\HP4s.png")
	w2 = image2.get_width()	
	w4 = image6.get_width()
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
			#lose game
			pygame.mixer.Channel(0).play(pygame.mixer.Sound("music\\lose.wav"))
			pygame.mouse.set_visible(True)
			Game.menu.restart_button = restart_button((Game.width * 9 / 10, Game.height * 9 / 10))
			Game.menu.restart_button = restart_button((Game.width - Game.menu.restart_button.w - 30, Game.height - Game.menu.restart_button.h - 30))
			Game.menu.quit_button = quit_button((Game.width * 1 / 10, Game.height * 9 / 10))
			Game.menu.quit_button = quit_button((30, Game.height - Game.menu.restart_button.h - 30))
			while 1:
				Game.screen.fill(BLACK)
				pygame.mixer.Channel(1).pause()
				img = pygame.image.load("lose\\t1.png")
				img = pygame.transform.scale(img, (Game.width, Game.height))
				rect = img.get_rect(center = (Game.width/2, Game.height/2))
				img1 = pygame.image.load("lose\\t0.png")
				rect1 = img1.get_rect(center = (Game.width/2, Game.height/2))
				Game.screen.blit(img, rect)
				Game.screen.blit(img1, rect1)
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						exit()
					if event.type == MOUSEBUTTONDOWN:
						if Game.menu.restart_button.get_clicked():
							pygame.mouse.set_visible(False)
							Game.restart = True
							return
						if Game.menu.quit_button.get_clicked():
							pygame.quit()
							exit()
				Game.menu.restart_button.draw(Game.screen)
				Game.menu.quit_button.draw(Game.screen)
				pygame.display.update()
			pygame.mixer.Channel(1).play()

def draw_stamia(fish):
	rx = fish.pos[0] + fish.w +fish.sw
	ry = fish.pos[1] + fish.sh
	h = (fish.sh/FULL_STAMIA * fish.stamia) 
	lx = rx - fish.sw 
	ly = ry - h
	pygame.draw.rect(Game.screen, YELLOW,  (lx, ly, fish.sw, h))
	Game.screen.blit(fish.stamia_image, (fish.pos[0] + fish.w, fish.pos[1]))
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def end_stage():
	if Game.restart == True:
		Game.stage = 1
		Fish1.health = MC_HEALTH
		Fish1.lives = MC_LIVES
		global Main_Fish
		Main_Fish = pygame.sprite.GroupSingle()
		Game.load(bg, Fish1)
		Game.Pause = False
		Game.restart = False
		
		Main_Fish.add(Fish1)
		return
	
	if len(Game.mobs)== 0:
		Game.angle = 0

		
		if Game.stage > 7:
			#win game
			i = 1
			while(i <= 4):
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						exit()
				if not Game.Played:
					pygame.mixer.Channel(0).play(pygame.mixer.Sound("music\\Win_game.wav"))
					Game.Played = True
				if Game.win_delay == 0:
					Game.screen.fill(BLACK)
					img = pygame.image.load("win\\t" + str(i) + ".png")
					rect = img.get_rect(center = (Game.width/2, Game.height/2))
					if i == 4:
						img1 = pygame.image.load("win\\t5.png")
						img1 = pygame.transform.scale(img1, (Game.width, Game.height))
						rect1 = img1.get_rect(center = (Game.width/2, Game.height/2))
						Game.screen.blit(img1, (0,0))
					Game.screen.blit(img, rect)
					i += 1
					Game.win_delay += 300
				else:
					Game.win_delay -= 1
				pygame.display.update()
			Game.menu.restart_button = restart_button((Game.width * 9 / 10, Game.height * 9 / 10))
			Game.menu.restart_button = restart_button((Game.width - Game.menu.restart_button.w - 30, Game.height - Game.menu.restart_button.h - 30))
			Game.menu.quit_button = quit_button((Game.width * 1 / 10, Game.height * 9 / 10))
			Game.menu.quit_button = quit_button((30, Game.height - Game.menu.restart_button.h - 30))
			while(1):
				pygame.mouse.set_visible(True)
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						exit()
					if event.type == MOUSEBUTTONDOWN:
						if Game.menu.restart_button.get_clicked():
							pygame.mouse.set_visible(False)
							Game.restart = True
							return
						if Game.menu.quit_button.get_clicked():
							pygame.quit()
							exit()
				Game.menu.restart_button.draw(Game.screen)
				Game.menu.quit_button.draw(Game.screen)
				pygame.display.update()
		else:
			if not Game.Played:
				
				pygame.mixer.Channel(0).play(pygame.mixer.Sound("music\\Level_Complete.wav"))
				
				
				Game.Played = True
			img = pygame.image.load("setting\\clear_stage.png")
			rect = img.get_rect(center = (Game.width/2, Game.height/2))
			Game.screen.blit(img, rect)
			pygame.display.update()

	if Game.stop == True:
		pygame.mixer.Channel(0).stop()
		Game.stop = False
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
	# Game.stage = 8
	end_stage()
	#check pause
	d = pygame.key.get_pressed()
	if d[K_ESCAPE] and not Game.Pause_delay:
		if Game.Pause == False:
			Game.Pause = True
			pygame.mouse.set_visible(True)
		else:
			Game.Pause = False
			pygame.mouse.set_visible(False)
		Game.Pause_delay = 5
	if Game.Pause_delay:
		Game.Pause_delay -= 1
	#if pause
	if Game.Pause == True:
		for fish in Main_Fish:
			fish.move = 0
		Game.menu.draw(Game.screen)
		Game.Buttons.draw(Game.screen)
		Game.menu.update(Game, Fish1, bg)
		if Game.save_success:
			img = pygame.image.load("setting\\save_success.png")
			rect = img.get_rect(center = (Game.width/2, Game.height/2))
			Game.screen.blit(img, rect)
			Game.save_success -= 1
		else:
			bg.draw(Game.screen)
			for fish in Game.mobs:
				if fish.mob != 100:
					fish.draw_health()
				else:
					fish.draw_health(Game)

			health_bar(Fish1)
			draw_stamia(Fish1)
			Game.minimap.draw(Game)
			Game.mobs.draw(Game.screen)
			Main_Fish.draw(Game.screen)
			Game.menu.draw(Game.screen)
			Game.Buttons.draw(Game.screen)
			Game.menu.update(Game, Fish1, bg)


		pygame.display.update()
		return
	else:
		pygame.mouse.set_visible(False)
	end_stage() 
	#event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
		
		if event.type == KEYDOWN:
			if len(Game.mobs) == 0:
				Game.stop = True
				# end_stage() 
				return
		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1 and len(Game.mobs) != 0:
				blade = Blade(Fish1)
				if blade.blade != "":
					
					pygame.mixer.Channel(0).play(pygame.mixer.Sound("music\\Splash.wav"))
					
					Game.Blade_mc.add(blade) 
		if event.type == KEYDOWN and event.key == K_SPACE and Game.Fire_delay == 0 and len(Game.mobs) != 0:
			bullet = Fish1.Fire(bg)
			if bullet.name != "":
				
				pygame.mixer.Channel(0).play(pygame.mixer.Sound("music\\main_shoot.wav"))
				
				Game.Bullet_Main.add(bullet)
			Game.Fire_delay = 5
	if len(Game.mobs) == 0:
		return
	if Game.Fire_delay:Game.Fire_delay -= 1
	#update
	bg.update(Fish1)

	#check fish in current screen
	mobs = pygame.sprite.Group()
	mobs = get_mobs_on_screen(Game, bg)
	
	#enermy bullet hit main_fish
	hits = pygame.sprite.groupcollide(mobs, Game.Bullet_Main, False, True, pygame.sprite.collide_mask)
	
	for hit in hits:	
		if not hit.shield:
			hit.health -= MAIN_DAMAGE
			if hit.health <= 0:
				if hit.mob == 100:hit.destroy()
				else:hit.kill()
	hits = pygame.sprite.groupcollide(Game.Bullet_Mobs, Main_Fish, False, False, pygame.sprite.collide_rect)
	for hit in hits:
		if hit.type == "mobs_3":
			for fish in Main_Fish:
				fish.Slow = True
	hits = pygame.sprite.groupcollide(Main_Fish, Game.Bullet_Mobs, False, True, pygame.sprite.collide_rect)
	for hit in hits:
		hit.health -= BULLET_DAMAGE	
	#enermy fish crash main fish
	hits = pygame.sprite.groupcollide(mobs, Main_Fish, False, False, pygame.sprite.collide_rect)
	for hit in hits:
		if hit.mob == 4 or hit.mob == 1:
			for fish in Main_Fish:
				fish.health -= SPLASH_DAMAGE
	#Boss attack main fish
	for fish in Game.Boss:
		hits = pygame.sprite.groupcollide(Main_Fish, fish.Bullet, False, True, pygame.sprite.collide_rect)
		for hit in hits:
			hit.health -= BULLET_DAMAGE
		hits = pygame.sprite.groupcollide(Main_Fish, fish.Laser, False, False, pygame.sprite.collide_mask)
		for hit in hits:
			hit.health -= LASER_DAMAGE
	#Blade process
	if len(Game.Blade_mc) >= 1:
		hits = pygame.sprite.groupcollide(mobs, Game.Blade_mc, False, False, pygame.sprite.collide_rect)
		for hit in hits:  
			if hit.shield:
				hit.health -= BLADE_DAMAGE//3
			else:
				hit.health -= BLADE_DAMAGE
			if hit.health <= 0:
					hit.kill()

	#update mobs_3
	for fish in mobs:
		if fish.mob == 3:
			fish.LIGHT(Fish1, bg, Game)
	#update all mobs
	Game.mobs.update(bg, Fish1, Game) 

	#mobs attack
	for fish in mobs:
		if fish.mob == 0 or fish.mob == 2:
			bullet = fish.Fire(Fish1, bg, Game)
			if bullet.name != "":
				Game.Bullet_Mobs.add(bullet)
	#boss attack
	for boss in Game.Boss:
		boss.attack(bg, Game)
	#mob4 attack
	for fish in Game.mobs_4:
		fish.Slash(Fish1, Game)
	#mob1 attack
	for fish in Game.mobs_1:
		fish.Roar()
	#update main blade
	for blade in Game.Blade_mc:
		if blade.update(Fish1, Game):
			blade.kill()
	#update enermy's bullet
	Game.Bullet_Mobs.update(bg, Fish1, Game)
	#updatee boss's bullet
	for boss in Game.Boss:
		boss.Bullet.update(bg,  Fish1, Game)
	

	#mc update
	Main_Fish.update(bg, Game)
	#update main bullet
	Game.Bullet_Main.update(bg, Fish1, Game)
	#minimap update
	Game.minimap.update(Game,bg, Fish1)
	#draw
	bg.draw(Game.screen)	
	Game.mobs.draw(Game.screen)
	Game.Bullet_Main.draw(Game.screen)
	Game.Bullet_Mobs.draw(Game.screen)
	Main_Fish.draw(Game.screen)

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
	
	#draw minimap
	Game.minimap.draw(Game)
	#update display
	pygame.display.update()	


if __name__ == '__main__':
	Game = game()

	bg = bg(0, 0, Game)
	
	Menu = menu(Game)
	Time = pygame.time.Clock()
	Fish1 = mc()
	
	Menu.update(Fish1, bg)
	pygame.display.flip()
	pygame.mixer.Channel(1).play(pygame.mixer.Sound("music\\bg.mp3"))
	while(Menu.update(Fish1, bg)):
		if pygame.mixer.Channel(1).get_busy() == False:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("music\\bg.mp3"))
		if Game.load_success: 
			img = pygame.image.load("setting\\load_success.png")
			rect = img.get_rect(center = (Game.width/2, Game.height/2))
			Game.screen.blit(img, rect)
			Game.load_success -= 1
		pygame.display.update()		
		Time.tick(fps)

	
	if Fish1.name == "":
		Fish1 = mc((Game.width/2, Game.height/2), "mc_animation\\mc0", Game, bg, MC_HEALTH)	
	if not Game.updated:
		Game.load(bg, Fish1)
		Game.setup(bg, Fish1)
	bg.image = pygame.transform.scale(bg.image, (bg.w * Game.RATIO // 100, bg.h * Game.RATIO // 100))
	bg.w = bg.image.get_width()
	bg.h = bg.image.get_height()
	global MAIN_SPEED
	MAIN_SPEED = MAIN_SPEED * Game.RATIO/100
	Main_Fish = pygame.sprite.GroupSingle()
	
	Main_Fish.add(Fish1)

	curr_time = pygame.time.get_ticks()
	while(1):
		if pygame.mixer.Channel(1).get_busy() == False:
			pygame.mixer.Channel(1).play(pygame.mixer.Sound("music\\bg.mp3"))
		process()