import pygame
from random import randint as rand
from random import randrange as rabal
pygame.init()
win=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Ospon")


winsize=pygame.Surface.get_size(win)

#размеры перса
widht=winsize[0]//25
height=winsize[1]//13
Rkv=((widht/2)**2+(height/2)**2)

#классы
class bal():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.velx=rand(0,int(balspeed))*rabal(-1,2,2)
		self.vely=((int(balspeed)**2-self.velx**2)**0.5)*rabal(-1,2,2)
	def drawball(self):
		wingame.blit(ball,(self.x,self.y))
			
class ponch():
	
	def __init__(self):
		self.x=rand(wingsize[0]//34,wingsize[0]//1.07)
		self.y=rand(wingsize[1]//24,wingsize[1]//1.21)
		self.animcount3=0
		
	def drawpon(self):
		self.animcount3+=1
		if self.animcount3>=12: self.animcount3=0
		wingame.blit(pon[self.animcount3//4],(self.x,self.y))

class Menu:
	def __init__(self,punkts=[120,140,'punkts',(255,0,0),(140,0,150),0]):
		self.punkts=punkts
	def drawmenu(self,holst,font,num_punkt):
		for i in self.punkts:
			if num_punkt==i[5]:
				holst.blit(font.render(i[2],1,i[4]),(i[0],i[1]))
			else:
				holst.blit(font.render(i[2],1,i[3]),(i[0],i[1]))
	def menu(self):
		global run
		done=True
		font_menu=levels_font
		pygame.key.set_repeat(500,400)
		punkt=0
		while done:
			wingame.fill((150,200,150))
			for e in pygame.event.get():
				if e.type==pygame.QUIT: pygame.quit()
				if e.type==pygame.KEYDOWN:
					if e.key==pygame.K_ESCAPE: pygame.quit()
					if (e.key==pygame.K_UP or e.key==pygame.K_w) and punkt>0: punkt-=1
					elif (e.key==pygame.K_DOWN or e.key==pygame.K_s) and punkt<len(self.punkts)-1: punkt+=1
					if (e.key==pygame.K_SPACE):
						if punkt==0:done=False
						if punkt==1:pygame.quit()
						if punkt==2:
							done=False
							run=False
			game.drawmenu(wingame,font_menu,punkt)
			win.blit(wingame,[0,40])
			pygame.display.update()

#функции
def maxscore(score):
	global way
	f=open(way,'r')
	maxscore=int(f.read())
	if maxscore<score:
		f=open(way,'w')
		f.write(str(score))
		maxscore=score
	f.close()
	return maxscore

def drawstart():
	
	string.blit(levels_font.render('easy',1,(210,0,0)),[180,20])
	string.blit(levels_font.render('medium',1,(210,0,0)),[200,170])
	string.blit(levels_font.render('hard',1,(210,0,0)),[290,320])
	string.blit(lives_font.render('hardmod',1,(110,0,30)),[20,300])
	string.blit(lives_font.render('press  H  for fun',1,(110,50,30)),[420,250])

	win.blit(pygame.transform.rotate(fonmenu,180),(0,0))
	wingame.blit(fonmenu,(0,0))
	for balu in balls: balu.drawball()
	pygame.draw.rect(string,(0,100,200),(160,ramah*150+10,260,50),10)
	if tmam==1: pygame.draw.rect(string,(0,250,0),(5,295,160,50),10)
	win.blit(wingame,(0,sizestroki))
	win.blit(string,(wingsize[0]/3.9,wingsize[1]/7.68))
	
	string.fill((94,176,108))
	

	
	pygame.display.update() #обновление экрана

def draw():
	global animcount
	wingame.blit(fon,(0,0))
	
	p.drawpon()
	if animcount+1>=16: 
		animcount=0
	wingame.blit(ospon[animcount//4],(x,y)) #рисуем
	animcount+=1
	
	
	for balu in balls: balu.drawball()

	if tmam==1: wingame.blit(tma,(x-wingsize[0]-15,y-wingsize[1]+30))

	wingame.blit(score_font.render('time: '+ str(time//30),1,(210,100,0),(221,171,0)),[wingsize[0]*0.5,wingsize[1]/1.05])
	wingame.blit(lives_font.render('fps: '+ str(int(clock.get_fps())),1,(210,100,0),(221,171,0)),[wingsize[0]*0.1,wingsize[1]/1.06])
	
	win.blit(wingame,(0,sizestroki))
	pygame.display.update()

def inter(x1,x2,y1,y2):
	if ((x1-x2)**2+((y1-y2)*0.99)**2<Rkv): return 1
	else: return 0

def otskok():
		if balu.x>wingsize[0]/1.03-widht/2 or balu.x<wingsize[0]/45.5: balu.velx*=(-1)
		if balu.y>wingsize[1]/1.1044-widht/2 or balu.y<wingsize[1]/72.7: balu.vely*=(-1)

def stolknovenie(x1,y1):
	global lives
	if inter(x,x1,y,y1) and pygame.mixer.Channel(1).get_busy()==0 and pygame.mixer.Channel(2).get_busy()==0:
			lives-=1
			drawstring()
			pygame.mixer.Channel(1).play(damag)
		
def drawstring():
	info_string.fill((221,171,0))
	info_string.blit(score_font.render('score: '+ str(score),1,(210,0,0),(221,171,0)),[110,10])
	info_string.blit(lives_font.render('lives: '+str(lives),1,(210,0,0),(221,171,0)),[1090,8])
	win.blit(info_string,(0,0))
	info_string.fill((221,171,0))
	pygame.display.update()

info_string=pygame.Surface((winsize[0],winsize[1]/19.2))
sizestroki=pygame.Surface.get_size(info_string)[1]
string=pygame.Surface((winsize[0]/2,winsize[1]/2))
wingame=pygame.Surface((winsize[0],winsize[1]-sizestroki))
pygame.mouse.set_visible(False)

wingsize=pygame.Surface.get_size(wingame)

pygame.font.init() #инициализируем шрифты
levels_font=pygame.font.Font('fonts/ravie.ttf',32)
score_font=pygame.font.Font('fonts/ravie.ttf',32)
lives_font=pygame.font.Font('fonts/bradhitc.ttf',32)
zanovo_font=lives_font

win.blit(levels_font.render('Hello!!! downloading...',1,(210,0,0)),[450,250])
pygame.display.update()

startfon=pygame.mixer.Sound('sounds/guitar.ogg')
gamefon=[pygame.mixer.Sound('sounds/eao.ogg'),
	pygame.mixer.Sound('sounds/fon.ogg'),
	pygame.mixer.Sound('sounds/fon1.ogg'),
	pygame.mixer.Sound('sounds/fon2.ogg'),
	pygame.mixer.Sound('sounds/fon3.ogg'),
	pygame.mixer.Sound('sounds/fon4.ogg')]

poncheat=pygame.mixer.Sound('sounds/cannibal.ogg')
damag=pygame.mixer.Sound('sounds/damage.ogg')

ospon=[
	pygame.transform.scale(pygame.image.load('picture/osm1.jpg'),(widht,height)).convert(),
	pygame.transform.scale(pygame.image.load('picture/osm2.jpg'),(widht,height)).convert(), 
	pygame.transform.scale(pygame.image.load('picture/osm3.jpg'),(widht,height)).convert(), 
	pygame.transform.scale(pygame.image.load('picture/osm4.jpg'),(widht,height)).convert()]

ball=pygame.transform.scale(pygame.image.load('picture/ball.png'),(widht//2, widht//2))
pon=[
	pygame.transform.scale(pygame.image.load('picture/pon1.png'),(widht, widht)).convert(), 
	pygame.transform.scale(pygame.image.load('picture/pon2.png'),(widht, widht)).convert(),
	pygame.transform.scale(pygame.image.load('picture/pon3.png'),(widht, widht)).convert()]

fon=pygame.transform.scale(pygame.image.load('picture/fon.png'),(winsize[0],winsize[1]-40)).convert()
fonmenu=pygame.transform.scale(pygame.image.load('picture/pixelfon.jpg'),winsize).convert()
tma=pygame.transform.scale(pygame.image.load('picture/tma.png'),(wingsize[0]*2,wingsize[1]*2))

clock=pygame.time.Clock()
game=True
tmam=-1
ramah=0
while game:

	
	#вводим переменные
	
	#расположение перса
	x=250
	y=220
	

	animcount=0
	score=0
	lives=0
	balspeed=10
	run=True
	balls=[]
	time=0
	
	#фоновая музыка
	pygame.mixer.Channel(0).play(startfon,-1)
	pygame.mixer.Channel(0).set_volume(0.3)

	#щщщщщщщщщщщщщщщщщщщщ

	pygame.key.set_repeat(100,200)

	for i in range(10):
		balls.append(bal(500, 300))

	#start меню
	while run:
		clock.tick(45/(3-ramah)-5)
		for event in pygame.event.get():
			if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE): #проверка выхода
				pygame.quit()
			if event.type==pygame.KEYDOWN:
				if (event.key==pygame.K_UP or event.key==pygame.K_w) and ramah>0: ramah-=1
				elif (event.key==pygame.K_DOWN or event.key==pygame.K_s) and ramah<2: ramah+=1
				elif (event.key==pygame.K_SPACE): run=False
				if event.key==pygame.K_h: tmam*=-1

		for balu in balls:
			otskok()
			balu.x+=balu.velx
			balu.y+=balu.vely		
		drawstart()

	if ramah==0: way='scors/easy.txt'
	elif ramah==1: way='scors/medium.txt'
	else: way='scors/hard.txt'
	
	balspeed=(ramah*20+10)//2 #скорость шаров
	
	speed=10-ramah*2 #скорость перса
	
	pygame.key.set_repeat(1,1)
	lives=5
	p=ponch()#пончики
	balls=[] #массив с шарами

	run=True



#меню
	punkts=[(500,200,"play",(255,0,255),(255,0,0),0),
		(500,300,"QUIT=escape",(255,0,255),(255,0,0),1),
		(500,400,"complete the game",(255,0,255),(255,0,0),2)]

	game=Menu(punkts)


	pygame.mixer.Channel(0).play(gamefon[rand(0,5)],-1)
	pygame.mixer.Channel(0).set_volume(0.5)

	drawstring()
	
	
	
	#игра
	while run and lives>0:
		clock.tick(30)
		time+=1
		for event in pygame.event.get():
			if event.type==pygame.QUIT: run=False
			if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE: 
				game.menu()
				pygame.key.set_repeat(1,1)

						
		if inter(x,p.x,y,p.y): 
			balls.append(bal(p.x, p.y))
			balspeed+=0.5*ramah
			p=ponch()
			score+=1
			drawstring()
			pygame.mixer.Channel(2).play(poncheat,0)
		
		for balu in balls:
			otskok()
			stolknovenie(balu.x,balu.y)
			balu.x+=balu.velx
			balu.y+=balu.vely
		
		
		key=pygame.key.get_pressed()
		if (key[pygame.K_LEFT] or key[pygame.K_a]) and x>wingsize[0]/45.5: x-=speed
		elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and x<wingsize[0]/1.03-widht: x+=speed
		if (key[pygame.K_UP] or key[pygame.K_w]) and y>wingsize[1]/72.7: y-=speed
		elif (key[pygame.K_DOWN] or key[pygame.K_s]) and y<wingsize[1]/1.1044-height: y+=speed

		draw()
	
	run=True
	win.blit(fon,(0,sizestroki))
	string.fill((181,225,45))
	
	string.blit(zanovo_font.render('your score: '+ str(score),1,(210,0,0)),[250,20])
	string.blit(zanovo_font.render('max score on this difficulty: '+str(maxscore(score)),1,(210,0,0)),[150,160])
	string.blit(zanovo_font.render('for exit press ""escape""',1,(210,0,0)),[250,240])
	string.blit(zanovo_font.render('for playing press "space"',1,(210,0,0)),[50,330])
	
	win.blit(string,(wingsize[0]/3.9,wingsize[1]/7.68))
	
	pygame.display.update()
	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT: #проверка выхода
				run=False
				game=False
			if event.type==pygame.KEYDOWN:
				if (event.key==pygame.K_ESCAPE):
					run=False
					game=False
				elif (event.key==pygame.K_SPACE): run=False


pygame.quit()