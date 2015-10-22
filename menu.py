from init import *
from VadickFantasyXVI import *
import webbrowser

select_sound = pygame.mixer.Sound('sound/select.ogg')
select_sound.set_volume(0.3)
selected_sound = pygame.mixer.Sound('sound/selected.ogg')

loading_screen = pygame.image.load('images/loading.png').convert()
loading_bar_empty = pygame.image.load('images/loading_bar/empty.png').convert_alpha()
loading_bar_filled = pygame.image.load('images/loading_bar/filled.png').convert_alpha()

dlcshit = pygame.image.load('images/dlcshit.png').convert_alpha()

class Menu(object):
	def __init__(self):
		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()
		self.bg = pygame.image.load('images/menu/bg.png').convert()
		self.buttons = pygame.image.load('images/menu/buttons.png').convert_alpha()
		self.buttons_selected = pygame.image.load('images/menu/buttons_selected.png').convert_alpha()
		self.selected = 0
		self.buttons_list = ['start', 'quit']

	def render(self):
		self.screen.blit(self.bg, (0, 0))
		self.screen.blit(self.buttons, (0, 0))
		if self.buttons_list[self.selected] == 'start':
			self.screen.blit(self.buttons_selected, (0, 0), (0,0, 800, 500))
		if self.buttons_list[self.selected] == 'quit':
			self.screen.blit(self.buttons_selected, (0, 500), (0, 500, 800, 100))
			
	def gamelol(self):
		while True:
			screen.blit(dlcshit, (0, 0))
			pygame.display.update()
			for event in pygame.event.get():
				if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
					selected_sound.play()
					
					webbrowser.open('http://vadickproduction.ru/dlc', new = 2)
					
					screen.blit(loading_screen, (0, 0))
					screen.blit(loading_bar_empty, (103, 508))
					loading = 0
					while loading < SCREEN_SIZE[0]:
						screen.blit(loading_bar_filled, (103, 508), Rect(0, 0, loading, SCREEN_SIZE[1]))
						loading += randint(1, 100)
						pygame.display.update()
						pygame.time.wait(randint(200, 300))
					pygame.time.wait(300)
					return
				if (event.type == QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
					exit()
			
	def run(self):
		pygame.mixer.music.load('music/menu.ogg')
		pygame.mixer.music.play(-1)

		while True:
			self.render()

			for event in pygame.event.get():
				if (event.type == QUIT):
					exit()
			
			pressed_keys = pygame.key.get_pressed()

			if pygame.key.get_pressed():
				if pressed_keys[K_s] or pressed_keys[K_DOWN]:
					#select_sound.play()

					self.selected += 1
					if self.selected >= len( self.buttons_list):
						self.selected = 0

				if pressed_keys[K_w] or pressed_keys[K_UP]:
					#select_sound.play()

					self.selected -= 1
					if self.selected <= -1:
						self.selected = len( self.buttons_list) - 1

				if pressed_keys[K_SPACE] or pressed_keys[K_RETURN] or pressed_keys[K_z]:
					selected_sound.play()

					if self.buttons_list[self.selected] == 'start':
						screen.blit(loading_screen, (0, 0))
						screen.blit(loading_bar_empty, (103, 508))
						loading = 0
						while loading < SCREEN_SIZE[0]:
							screen.blit(loading_bar_filled, (103, 508), Rect(0, 0, loading, SCREEN_SIZE[1]))
							loading += randint(1, 100)
							pygame.display.update()
							pygame.time.wait(randint(200, 300))
						pygame.time.wait(300)

						self.gamelol()

					if self.buttons_list[self.selected] == 'quit':
						screen.blit(loading_screen, (0, 0))
						screen.blit(loading_bar_empty, (103, 508))
						loading = 0
						while loading < SCREEN_SIZE[0]:
							screen.blit(loading_bar_filled, (103, 508), Rect(0, 0, loading, SCREEN_SIZE[1]))
							loading += randint(1, 100)
							pygame.display.update()
							pygame.time.wait(randint(200, 300))
						pygame.time.wait(300)

						self.gamelol()


			pygame.display.update()