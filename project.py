import pygame
import classes
import time

def home():
	scr.fill((255,255,255))
	square = classes.square(440, 80, 255, 0, 0)
	square2 = classes.square(440, 80, 255, 0, 0)
	square3 = classes.square(440, 80, 255, 0, 0)
	
	myfont = pygame.font.SysFont("Comic Sans MS", 50)

	label = classes.label(70, "Last Minute Show")
	label2 = classes.label(50, "Comedy Shows")
	label3 = classes.label(50, "Band Shows")
	label4 = classes.label(50, "Dancing Shows")

	label.draw(scr,100, 100)

	scr.blit(square.square, (100, 250))
	scr.blit(square2.square, (100, 350))
	scr.blit(square3.square, (100, 450))

	label2.draw(scr, 200, 270)
	label3.draw(scr, 230, 370)
	label4.draw(scr, 200, 470)

def comedy():
	scr.fill((255,255,255))
	labelback = classes.label(30, "Back")
	squareback = classes.square(70, 40, 255, 0, 0)
	scr.blit(squareback.square, (50, 50))
	labelback.draw(scr, 60, 55)

	title = classes.label(80, "Comedy")
	title.draw(scr, 170, 100)

	name = classes.label(70, "Adi Khalifa")
	name.draw(scr, 170, 200)

	date = classes.label(70,"20/8/2014")
	date.draw(scr, 170, 300)

	Money = classes.label(70, "50$")
	Money.draw(scr, 170, 400)

def band():
	scr.fill((255,255,255))
	labelback1 = classes.label(30, "Back")
	squareback1 = classes.square(70, 40, 255, 0, 0)
	scr.blit(squareback1.square, (50, 50))
	labelback1.draw(scr, 60, 55)

	title = classes.label(80, "Band")
	title.draw(scr, 170, 100)

	name = classes.label(70, "Mettalica")
	name.draw(scr, 170, 200)

	date = classes.label(70,"13/7/2014")
	date.draw(scr, 170, 300)

	Money = classes.label(70, "70$")
	Money.draw(scr, 170, 400)

def dance():
	scr.fill((255,255,255))
	labelback1 = classes.label(30, "Back")
	squareback1 = classes.square(70, 40, 255, 0, 0)
	scr.blit(squareback1.square, (50, 50))
	labelback1.draw(scr, 60, 55)


	title = classes.label(80, "Dance")
	title.draw(scr, 170, 100)

	name = classes.label(70, "Bat-Sheva Group")
	name.draw(scr, 170, 200)

	date = classes.label(70,"5/9/2014")
	date.draw(scr, 170, 300)

	Money = classes.label(70, "40$")
	Money.draw(scr, 170, 400)


def buy():
	buybutton = classes.square(125,100,255,0,0)
	buylabel = classes.label(75,"Buy!")
	scr.blit(buybutton.square,(450,450))
	buylabel.draw(scr,460,470)

def buypress(name):
	scr.fill((255,255,255))
	thankyoulabel1 = classes.label(40,"Thank you for buying ")
	thankyoulabel2 = classes.label(40,name+" show!")
	thankyoulabel1.draw(scr,100,100)
	thankyoulabel2.draw(scr,100,150)


if __name__=="__main__":
	pygame.init()
	scr = pygame.display.set_mode((600,600))
	scr.fill((255,255,255))

	x = False
	y = False
	z = False
	x1 = 0
	y1 = 0

	while True:
		home()
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x1, y1 = ev.pos
		if x1>100 and y1>250 and x1<540 and y1<330:
			x1=0
			y1=0
			x=True
		if x1>100 and x1<540 and y1>350 and y1<430 :
			y = True
			x1=0
			y1=0
		if x1>100 and x1<540 and y1>450 and y1<530:
			z = True
			x1=0
			y1=0

		pygame.display.flip()

		while x:
			comedy()
			buy()
			ev = pygame.event.poll()
			if ev.type == pygame.QUIT:
				sys.exit()
			if ev.type == pygame.MOUSEBUTTONDOWN:
				x1, y1 = ev.pos
			if x1>50 and y1>50 and x1<120 and y1<90:
				x1=0
				y1=0
				x=False
			if x1>450 and y1>450 and x1<550 and y1<550:
				buypress("Adi Khalifa")

			pygame.display.flip()
		while y:
			band()
			buy()
			ev = pygame.event.poll()
			if ev.type == pygame.QUIT:
				sys.exit()
			if ev.type == pygame.MOUSEBUTTONDOWN:
				x1, y1 = ev.pos
			if x1>50 and y1>50 and x1<120 and y1<90:
				x1=0
				y1=0
				y=False
			if x1>450 and y1>450 and x1<550 and y1<550:
				buypress("Mettalica")


			pygame.display.flip()
		while z:
			dance()
			buy()
			ev = pygame.event.poll()
			if ev.type == pygame.QUIT:
				sys.exit()
			if ev.type == pygame.MOUSEBUTTONDOWN:
				x1, y1 = ev.pos
			if x1>50 and y1>50 and x1<120 and y1<90:
				x1=0
				y1=0
				z=False
			if x1>450 and y1>450 and x1<550 and y1<550:
				buypress("Bat-Sheva Group")


			pygame.display.flip()