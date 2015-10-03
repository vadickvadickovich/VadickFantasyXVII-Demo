from const import *
from menu import *
from init import *
from random import randint, choice

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption('VadickFantasyXVI')
pygame.display.set_icon(pygame.image.load('images/icon.png'))

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

font = pygame.font.SysFont('arial', 16)

#pygame.mixer.quit()
movie = pygame.movie.Movie('video/intro.mpg')

loading_screen = pygame.image.load('images/loading.png').convert()
loading_bar_empty = pygame.image.load('images/loading_bar/empty.png').convert_alpha()
loading_bar_filled = pygame.image.load('images/loading_bar/filled.png').convert_alpha()

if __name__ == '__main__':
	movie.play()
	while movie.get_busy():
		event = pygame.event.wait()
		if event.type == QUIT:
			break
		if event.type == KEYDOWN:
			break
	if movie.get_busy():
		movie.stop()

	screen.blit(loading_screen, (0, 0))
	screen.blit(loading_bar_empty, (103, 508))
	loading = 0
	while loading < SCREEN_SIZE[0]:
		screen.blit(loading_bar_filled, (103, 508), Rect(0, 0, loading, SCREEN_SIZE[1]))
		loading += randint(1, 100)
		pygame.display.update()
		pygame.time.wait(randint(200, 500))
	pygame.time.wait(500)

	MainMenu = Menu()
	MainMenu.run()
	