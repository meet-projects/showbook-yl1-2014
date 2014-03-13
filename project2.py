import pygame
import class.py

if __name__=="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600,600))
	main_screen.fill((255,255,255))
	button_rec = pygame.Rect(135,345,350,70)
	button_sq = pygame.Surface([350,70])
	button_sq.fill((50,40,85))
	main_screen.blit(button_sq, button_rec)

	


	while True:
		ev = pygame.event.poll()
		button(100,100,50,50)
		pygame.display.flip()

