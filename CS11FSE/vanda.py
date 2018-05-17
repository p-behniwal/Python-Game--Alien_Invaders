from pygame import *

init()
running = True
width, height = size = 800,600
screen = display.set_mode(size)
myClock = time.Clock()

class Player(sprite.Sprite):
	def __init__(self):
		sprite.Sprite.__init__(self)
		self.image = Surface((100,100))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect()

		self.acc = [0,0]
		self.vel = [0,0]
		self.pos = [width/2,0]

	def move(self):
		self.acc = [0, 0.6]

		kp = key.get_pressed()
		SPEED = 2
		if kp[K_d]:
			self.acc[0] = SPEED
		if kp[K_a]:
			self.acc[0] = -SPEED

		self.acc[0] -= self.vel[0] * 0.1
		self.vel[0] += self.acc[0]
		self.vel[1] += self.acc[1]
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]

		if self.pos[1] > height:
			self.pos[1] = height
			self.acc[1] = 0
			self.vel[1] = 0
		self.rect.midbottom = self.pos[0], self.pos[1]
		print(self.pos)

all_sprites = sprite.Group()
player = Player()
all_sprites.add(player)
while running:
	for evt in event.get():
		if evt.type == QUIT:
			running = False
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:
				running = False
	screen.fill((255,255,255))
	player.move()
	all_sprites.draw(screen)

	display.flip()
	myClock.tick(60)
quit()