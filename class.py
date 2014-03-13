import pygame
class Button(object):
	def __init__(self, x1, y1, x2, y2, r, g, b):
		self.x1= x1
		self.y1= y1
		self.x2= x2
		self.y2= y2
		self.r= r
		self.g= g
		self.b= b
	
		s=pygame.Rect(x1,y1,x2,y2)
		a=pygame.Surface([x2,y2])
		a.fill((r, g, b))
		main_screen.blit(a,s) 

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,255,255))
	button_rec = pygame.Rect(135,345,350,70)
	button_sq = pygame.Surface([350,70])
	button_sq.fill((50,40,85))
	main_screen.blit(button_sq, button_rec)
	Button(100,100,50,50, 50, 40, 85)
	


	while True:
		ev = pygame.event.poll()
		pygame.display.flip()

