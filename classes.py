import pygame

def home():
	scr.fill((255,255,255))
	square = classes.square(440, 80, 255, 0, 0)
	square2 = classes.square(440, 80, 255, 0, 0)
	square3 = classes.square(440, 80, 255, 0, 0)
	
	myfont = pygame.font.SysFont("Comic Sans MS", 50)

	label = classes.label(80, "showbook")
	label2 = classes.label(50, "Comedy Shows")
	label3 = classes.label(50, "Band Shows")
	label4 = classes.label(50, "Dancing Shows")

	label.draw(scr,170, 100)

	scr.blit(square.square, (100, 250))
	scr.blit(square2.square, (100, 350))
	scr.blit(square3.square, (100, 450))

	label2.draw(scr, 200, 270)
	label3.draw(scr, 230, 370)
	label4.draw(scr, 200, 470)

class square(object):
	def __init__(self, x1, x2, r, g, b):
		self.x1 = x1
		self.x2 = x2
		self.r = r
		self.g = g
		self.b = b

		self.square = pygame.Surface([x1, x2])
		self.square.fill((r,g,b))

class label(object):
	def __init__(self, size, txt):
		self.size=size
		self.txt=txt
		orderlabel = pygame.font.Font(None, size)
		self.label = orderlabel.render(txt, 1, (0, 0, 0))
	def draw(self, scr, x, y):
		self.x = x
		self.y = y
		scr.blit(self.label, (x,y))

class event(object):
	def __init__(self, ):
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x1, y1 = ev.pos
			print x1, y1

