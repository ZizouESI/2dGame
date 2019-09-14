import pygame 
pygame.init()

windows = pygame.display.set_mode((500,450))

pygame.display.set_caption('my game')

#the images that we're gonna use them 
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
#y= pygame.image.load('aa.png')

#to put an object we must define the (x,y,width,height,velocity)  

clock =pygame.time.Clock()
class player(object):
	def __init__(self,x,y,width,height,velocity):
		self.x=x
		self.y=y
		self.width=width
		self.height=height
		self.velocity=velocity #for moving
		#variables for jump
		self.isJump= False
		self.jumpCount=10
		#set variable for the character 
		#the direction and how many steps ..
		self.left = False
		self.right =False
		self.walkCount=0
		self.standing =True
		self.shoot=False

	def draw(self,win): #for choosing the charImage(in the table) to appear 
		if self.walkCount +1 >=27 :
			self.walkCount=0
		if not(self.standing):
			if self.left:
				windows.blit(walkLeft[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1
			elif self.right:
				windows.blit(walkRight[self.walkCount//3],(self.x,self.y))
				self.walkCount+=1
		else:
			if self.right :
				windows.blit(walkRight[0],(self.x,self.y))
				self.shoot=True
			elif self.left:
				windows.blit(walkLeft[0],(self.x,self.y))
				self.shoot=True
			else:
				windows.blit(char,(self.x,self.y))
				self.shoot=False
class projectile(object):
	"""docstring for projectile"""
	def __init__(self,x,y,radius,color,facing):
		self.x=x
		self.y=y
		self.radius=radius
		self.color=color
		self.facing=facing
		self.velocity=8 * facing

	def draw(self,win):
		pygame.draw.circle(windows,self.color,(self.x,self.y),self.radius)
		
		
def redrawGameWindow():
	#windows.fill((0,0,0))
	windows.blit(bg,(0,0))
	pl.draw(windows)
	for bullet in bullets:
		bullet.draw(windows)

	pygame.display.update()
#creating a main loop
pl=player(300,350,64,64,5)
#the list of bullets
bullets=[]

run= True 
while run:
	clock.tick(27)
	#to check the events we must itterate in 
	#the events list given by the methods below 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
	
	for bullet in bullets:
		if bullet.x < 500 and bullet.x>0 :
			bullet.x += bullet.velocity
		else:
			bullets.pop(bullets.index(bullet))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_s] and pl.shoot:
		if pl.left:
			facing=-1
		else:
			facing=1

		if len(bullets)< 10:
			bullets.append(projectile(round(pl.x+pl.width //2),round(pl.y+pl.height//2),6,(255,255,0),facing))


	if keys[pygame.K_LEFT] and pl.x>pl.velocity:
		pl.x-=pl.velocity
		pl.left=True
		pl.right=False
		pl.standing=False
	elif keys[pygame.K_RIGHT] and pl.x<500 -pl.width -pl.velocity :
		pl.x+=pl.velocity
		pl.right=True
		pl.left=False
		pl.standing=False
	else :
		pl.standing=True
		pl.walkCount=0

	if not(pl.isJump):	
		if keys[pygame.K_SPACE]:
			pl.isJump=True
			pl.right=False
			pl.left=False
			pl.walkCount=0
	else:
		if pl.jumpCount >= -10 :
			neg=1
			if pl.jumpCount<0:
				neg=-1

			pl.y-= (pl.jumpCount ** 2) * 0.5 * neg
			pl.jumpCount-=1
		else:
			pl.isJump=False
			pl.jumpCount=10
	redrawGameWindow()


pygame.quit()
