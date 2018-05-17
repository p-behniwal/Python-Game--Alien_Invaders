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

#initialize pygame window
os.environ['SDL_VIDEO_WINDOW_POS'] = '25,25' #adjusts the pygame window into place for the user 
init()
size = width, height = 1500, 830 #the main screen with its respective width and height
screen = display.set_mode(size)
display.set_caption("ALIEN INVADERS - ICS3U FSE") #title for the pygame window
myClock = time.Clock()

#Game Classes and Functions
def image_load(path, tscale):
	pic = transform.scale(image.load(path), tscale)
	return pic

class Player(sprite.Sprite):
	def __init__(self, my_object):
		self.vel = [0,0]
		self.acc = 0.25
		self.x = width/2
		self.y = height/2
		self.real_image = Surface((100,100), SRCALPHA)
		self.image = self.real_image
		self.rect = self.image.get_rect()
		self.real_image.blit(my_object, (0,0))
		self.ang = -pi/2
		self.speed = 5

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
		self.real_image = Surface((4,14), SRCALPHA)
		self.image = self.real_image
		self.rect = self.image.get_rect()
		self.real_image.blit(player_bullets, (0,0))
		self.speed = 0
		self.ang = -pi/2

	def update(self):
		kp = key.get_pressed()
		self.x += self.speed*cos(self.ang)
		self.y += self.speed*sin(self.ang)
		# if kp[K_SPACE]:




'''class Bullet(sprite.Sprite):
	def __init__(self, player_bullets):
		self.speed = 15
		self.x = player.x
		self.y = player.y
		self.real_image = Surface((4,14), SRCALPHA)
		self.image = self.real_image
		self.rect = self.image.get_rect()
		self.real_image.blit(player_bullets, (0,0))
		self.ang = player.ang

	def update(self):
		kp = key.get_pressed()
		if kp[K_SPACE]: 
			for i in range(10):
				self.x = self.x + 15*cos(radians(self.ang))
				self.y = self.y - 15*sin(radians(self.ang))
				print("wow")
				# time.wait(500)'''
		 
# class road
##Image loads##

player = Player(image_load("images/game_vehicle.PNG", (100,100)))
bullets = []
running = True
while running:
	for e in event.get():
		if e.type == QUIT:
			running = False
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				running = False
			elif e.key == K_SPACE:
				
				bullet = Bullet(image_load("images/shooter_bullet.PNG", (4,14)))
				bullet.x = player.x
				bullet.y = player.y
				bullet.update()
				screen 	
 

	mb = mouse.get_pressed()
	mx,my = mouse.get_pos()		
	screen.fill(WHITE)		
	player.update()
	# bullet.update()
	screen.blit(player.image,player.rect)

	display.flip()
	myClock.tick(60)
quit()