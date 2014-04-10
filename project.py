import pygame
import classes

if __name__=="__main__":
	pygame.init()
	# pygame.set_caption("showbook")
	scr = pygame.display.set_mode((600,600))
	scr.fill((255,255,255))
	square = pygame.Surface([440, 80])
	square2 = pygame.Surface([440, 80])
	square3 = pygame.Surface([440, 80])
	square.fill((255,0,0))
	square2.fill((255,0,0))
	square3.fill((255,0,0))

	# orderlabel = pygame.font.Font(None, 80)
	# label = orderlabel.render("showbook", 1, (0, 0, 0), (255, 255, 255))

	label = classes.label(80, "showbook", (255,255,0))
	label.draw(scr,170, 100)

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if square.get_bounding_rect().collidepoint(x, y ):
				print "clicked"
		scr.blit(square, (100, 250))
		scr.blit(square2, (100, 350))
		scr.blit(square3, (100, 450))
		# scr.blit(label,(170,100))
		pygame.display.flip()
