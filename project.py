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
	# label = myfont.render("Comedy Shows", 1, (0,0,0))
	# label2 = myfont.render("Band Shows", 1, (0,0,0))
	# label3 = myfont.render("Dancing Shows", 1, (0,0,0))


	# orderlabel = pygame.font.Font(None, 80)
	# label = orderlabel.render("showbook", 1, (0, 0, 0), (255, 255, 255))

	label = classes.label(80, "showbook", (255,255,0))
	label.draw(scr,170, 100)

	scr.blit(square.square, (100, 250))
	scr.blit(square2.square, (100, 350))
	scr.blit(square3.square, (100, 450))
	# scr.blit(label, (200, 270))
	# scr.blit(label2, (230, 370))
	# scr.blit(label3, (200, 470))

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if square.get_bounding_rect().collidepoint(x, y ):
				print "clicked"
		# scr.blit(label,(170,100))
		pygame.display.flip()