import pygame
class label(object):
	def __init__(self, size, txt, col):
		self.size=size
		self.txt=txt
		self.col=col
		orderlabel = pygame.font.Font(None, size)
		self.label = orderlabel.render(txt, 1, (0, 0, 0), (col))
	def draw(self, scr, x, y):
		self.x = x
		self.y = y
		scr.blit(self.label, (x,y))