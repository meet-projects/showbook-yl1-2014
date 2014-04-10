import pygame
import classes

if __name__=="__main__":
	pygame.init()
	scr = pygame.display.set_mode((600,600))
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
	x = True
	y = False
	z = False

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x1, y = ev.pos
			print x1, y
		pygame.display.flip()

		while x:
			scr.fill((255,255,255))

			pygame.display.flip()
		while y:
			scr.fill((255,255,255))

			pygame.display.flip()
		while z:
			scr.fill((255,255,255))

			pygame.display.flip()