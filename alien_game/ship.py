import pygame

class Ship():
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#飞船初始位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.moving_right = False
		self.moving_left = False
		
		#移动速度，中心位置
		self.ship_speed_factor = 1.5
		self.center = float(self.rect.centerx)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		if self.moving_right == True:
			if self.rect.centerx < self.screen_rect.width:
				self.center += self.ship_speed_factor
		if self.moving_left == True:
			if self.rect.centerx > 0:
				self.center -= self.ship_speed_factor
				
		self.rect.centerx = self.center
		
