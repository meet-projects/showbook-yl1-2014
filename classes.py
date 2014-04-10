import pygame

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
