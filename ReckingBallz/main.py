import pygame
import random
from pygame import mixer

class Ball(pygame.sprite.Sprite):
	def __init__(self,xpos,ypos):
		super().__init__()
		self.x = xpos
		self.y = ypos
		self.img = pygame.image.load("ball.png")
		self.rect = self.img.get_rect()
		self.rect.center = [self.x,self.y]

	def update(self,v):
		self.y += v
		self.rect.center = [self.x,self.y]


def new_brick():
	x = 532
	y = random.randrange(0,500)
	rect = img.get_rect()
	rect.center = [x,y]
	return rect

def move(bricks):
	for b in bricks:
		b.centerx -= 0.2
		return bricks

def show(bricks):
	for b in bricks:
		screen.blit(img,b)

def crash(a,b):  #Function to detect collision between bird and pipes
	if(a.colliderect(b)):
		return True 
	else:
		return False


pygame.init()
mixer.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("ReckingBallz")
clock = pygame.time.Clock()
v = 0
vel = 5

mixer.music.load('blast.wav')
mixer.music.set_volume(0.7)

icon = pygame.image.load('effect.png')
pygame.display.set_icon(icon)

ball = Ball(218,218)
img = pygame.image.load('bricks.png')
boom = pygame.image.load('boom.png')
boom = pygame.transform.smoothscale(boom,(64,64))
bricks = []

NEWBRICK = pygame.USEREVENT
pygame.time.set_timer(NEWBRICK, 1500)

score = 0
font = pygame.font.Font("freesansbold.ttf",32)

running = True 
while running : 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				v = -5

			if event.key == pygame.K_DOWN:
				v = 5


		if event.type == pygame.KEYUP:
			v = 0

		if event.type == NEWBRICK:
			bricks.append(new_brick())

	
	ball.update(v)
	screen.fill((0,0,0))
	screen.blit(ball.img,ball.rect)
	print(len(bricks))
	
	for b in bricks:
		b.centerx -= vel
		screen.blit(img,b)
		

		if b.centerx < 10 :
			bricks.remove(b)



	for b in bricks:
		if crash(ball.rect,b) or crash(ball.rect,b):
			bricks.remove(b)
			screen.blit(boom,b)
			score += 10
			mixer.music.play()


	text =  font.render(str(score),False,(255,255,255))
	screen.blit(text,(5,5))
	
	pygame.display.update()
	clock.tick(60)
