import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_setting,screen):
		super(Alien,self).__init__()
		self.screen=screen
		self.ai_setting=ai_setting

		#load alien image and set attributes
		self.image=pygame.image.load('image/alien.bmp') #load imgae of alien
		self.rect=self.image.get_rect()

		#start the each alien at top left of screen
		self.rect.x=self.rect.width
		self.rect.y=self.rect.height

		# Store the alien's exact position.
		self.x=float(self.rect.x)
	def update(self):
		"""Move the alien right or left."""
		self.x += (self.ai_setting.alien_speed *self.ai_setting.fleet_direction)
		self.rect.x = self.x     
	def check_edge(self):
		"""Return True if alien is at edge of screen."""
		screen_rect=self.screen.get_rect()
		if self.rect.right>=screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	def blitme(self):
		self.screen.blit(self.image,self.rect)

