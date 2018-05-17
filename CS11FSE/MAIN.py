#Prabhgun Behniwal
#Python Final Project (GAME)
#Pygame
####################################################################################################################################################
#############################    ALIEN INVADERS    ######################################
from pygame import*
from math import*
from random import*
import os
from os.path import*
from fileinput import*

#Define some colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Game Classes and Functions
def image_load(path, tscale):
	pic = transform.scale(image.load(path), tscale)
	return pic

def menu(surface, menu_pic, logo_pic, captions_list):
	myClock = time.Clock()
	buttons = [Rect(100, y*100 + 200, 400, 70) for y in range(3)]
	destinations = ["levels", "how to", "cars"] #Where the buttons will lead
	menufont = font.SysFont("Earth Orbiter", 40)

	running = True
	surface.blit(menu_pic, (0,0))
	surface.blit(logo_pic, (6.5*surface.get_width()/15, surface.get_height()/100-surface.get_height()/100))
	while running:
		for e in event.get():          
			if e.type == QUIT:
				running = False
				return "exit"

		mx,my = mouse.get_pos()
		mb = mouse.get_pressed()

		for b,d in zip(buttons,destinations):
			draw.rect(surface, (225,225,225), b)
			
			if b.collidepoint(mx,my):
				draw.rect(surface, (0,70,255), b, 3)
				if mb[0]==1:
					if buttons[0].collidepoint(mx,my):
						return "gameplay"
					if buttons[1].collidepoint(mx,my):
						return "cars"
					if buttons[2].collidepoint(mx,my):
						return "instructions"		
					
			else:
				draw.rect(surface, (131,3,3), b, 3)
					
		for t in range(3):
			text = menufont.render(captions_list[t], True, (0,0,0))
			surface.blit(text, (buttons[t][0] + (buttons[t][2] - text.get_width())//2, buttons[t][1]+(buttons[t][3]-text.get_height())//2)) 
		
		screen.blit(surface, (0,0))
		display.flip()

def instructions():
	pass
def cars():

	pass
'''
running = True
while running:
		for e in event.get():          
			if e.type == QUIT:
				running = False
				return "menu"'''	

def gameplay():
	class Player(sprite.Sprite):
		def __init__(self, my_object):
			super().__init__()
			self.speed = 0
			self.acc = 0.25
			self.x = width/2
			self.y = height/2
			self.real_image = Surface((100,100), SRCALPHA)
			self.image = self.real_image
			self.rect = self.image.get_rect()
			self.real_image.blit(my_object, (0,0))
			self.ang = -pi/2

		def update(self):
			kp = key.get_pressed()
			if kp[K_w]:
				self.x += self.speed*cos(self.ang)
				self.y += self.speed*sin(self.ang)
				while self.speed <= 5:
					self.speed += self.acc

			if kp[K_s]:
				self.x -= self.speed*cos(self.ang)
				self.y -= self.speed*sin(self.ang)
			if kp[K_w] or kp[K_s]:
				if kp[K_a]:
					self.ang -= 0.04
				if kp[K_d]:
					self.ang += 0.04

			self.image = transform.rotate(self.real_image, 360 - degrees(self.ang))
			self.rect = self.image.get_rect()
			self.rect.center = self.x, self.y
			p = (self.x + 100*cos(self.ang), self.y + 100*sin(self.ang))

	class Bullet(sprite.Sprite):
		def __init__(self, player_bullets):
			super().__init__() 
			# self.real_image = player_bullets
			self.image = player_bullets
			self.rect = self.image.get_rect()
			self.speed = 8
			self.x = player.x
			self.y = player.y
			self.ang = player.ang
			self.image = transform.rotate(self.image, 270 - degrees(self.ang))

		def update(self):
			self.x += self.speed*cos(self.ang)
			self.y += self.speed*sin(self.ang)
			self.rect.center = self.x, self.y
			if self.x < 0 or self.x > gameSurf.get_width() or self.y < 0 or self.y > gameSurf.get_height():
				bullets_list.remove(self)
				all_sprites_list.remove(self)		

	#Sprite Lists
	all_sprites_list = sprite.Group()  #contains all the game's sprites
	bullets_list = sprite.Group()  #contains only bullet sprites
	aliens_list = sprite.Group()  #contains only alien sprites 

	player = Player(image_load("images/game_vehicle.PNG", (100,100)))  #creates the user's main player using the Player() constructor (this is an instance of my Player class located in the "Game classes and functions" section)
	all_sprites_list.add(player)  #adds the player sprite to my all_sprites_list

	myClock = time.Clock()
	running = True
	key.set_repeat(250,250)
	while running:
		for e in event.get():
			if e.type == QUIT:
				running = False
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					running = False
				elif e.key == K_SPACE:
					bullet = Bullet(image_load("images/shooter_bullet.PNG", (4,14)))
					bullets_list.add(bullet)
					all_sprites_list.add(bullet)

		mb = mouse.get_pressed()
		mx,my = mouse.get_pos()			

		gameSurf.fill(WHITE)
		
		player.update()
		
		for bullet in bullets_list:
			bullet.update()
			'''if bullet.x < 0 or bullet.x > gameSurf.get_width() or bullet.y < 0 or bullet.y > gameSurf.get_height():
				bullets_list.remove(bullet)
				all_sprites_list.remove(bullet)'''
		
		all_sprites_list.draw(gameSurf)
		gameSurf.blit(player.image, player.rect)
		screen.blit(gameSurf, (0,0))
		print(bullets_list)
		display.flip()
		myClock.tick(60)

	quit()			

#Initialize pygame window and other stuff
os.environ['SDL_VIDEO_WINDOW_POS'] = '300,35' #adjusts the pygame window into place for the user 
display.set_caption("ALIEN INVADERS - ICS3U FSE") #title for the pygame window
init()  #initialize pygame
font.init()  #initialize the font
size = width, height = 1200, 800  #the main screen's width and height
screen = display.set_mode(size)  #the main screen  

#All Surfaces used in the game
gameSurf = Surface((1200,800))  #separate surface for the gameplay
menuSurf = Surface((1200,800))  #separate surface for the main menu
carsSurf = Surface((1200,800))  #separate surface for the car selection page 
instructionsSurf = Surface((1200,800))  #separate surface for the instructions page
levelsSurf = Surface((1200,800))  #separate surface for the level selections page

page = "menu"
while page != "exit":  #this while statement makes the user stay inside the game screen on different pages until he/she exits the menu
	if page == "menu":  #if the current page is the menu page, this calls the menu function
		page = menu(menuSurf, image_load("menu_screen_pics/menu_back.PNG", (1200,800)), image_load("menu_screen_pics/game_logo.PNG", (700,250)), ["PLAY", "CARS", "INSTRUCTIONS"])
	if page == "levels":
		levels()
	if page == "gameplay":
		page = gameplay()
	if page == "cars":
		cars()
	if page == "instructions":
		instructions()			



