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