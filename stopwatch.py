#  Copyright 2022 Mashiur Rahman Mahid
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY
import time
import pygame,sys
from pygame.locals import*
pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,600),RESIZABLE)
pygame.display.set_caption("") 
icon=pygame.image.load('stopwatch.png')
pygame.display.set_icon(icon)

color="#FF55C3"
font=pygame.font.Font('NeoEuler.otf', 140)
font1=pygame.font.Font('Genos-Bold.ttf', 20)




class Label():
	def __init__(self,label_txt,x,y,x1,y1,font=font):
		self.label_txt=label_txt
		self.x=x
		self.y=y
		self.x1=x1
		self.y1=y1
		self.label_font=font
		self.color0="#3F008C"
		self.label_position=pygame.Rect(self.x,self.y,self.x1,self.y1)
		self.label_txt=self.label_font.render(self.label_txt,True,self.color0)
		self.mouse_position=pygame.mouse.get_pos()
		txt_rect=self.label_txt.get_rect()
		txt_rect.center=self.label_position.center
		screen.blit(self.label_txt,txt_rect)



img=pygame.image.load('background.png')
count=False
d=0
then=time.time()
game_running=True
while game_running:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button==1:
				if count:
					count=False
				elif not count:
					count=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RETURN:
				then=time.time()
				d=0
				count=False
	
	if count:
		now=time.time()
		d=(now-then)

	total_second=round(d,4)
	milliseconds= round((total_second-int(total_second))*1000)
	minutes,seconds=divmod(total_second,60)
	hours,minutes=divmod(minutes,60)
	seconds=int(seconds)
	minutes=int(minutes)
	hours=int(hours)
	
	l=[hours,minutes,seconds,milliseconds]
	ln=['HOURS','MINUTES','SECONDS','MILLISECONDS']
	
	screen.fill(color)
	screen.blit(img,(45,70))
	for i in range(4):
		Label(ln[i],(i+.1)*250,200,240,150,font=font1)
		Label(str(l[i]),(i+.1)*250,100,240,150)	
	
	pygame.display.update()
