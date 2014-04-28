import pygame, sys, math

from Player import Player

class HealthBar():
	def __init__(self, owner, pos = (250, 250), path = "rsc/Health Bar/p1/"):
		self.path = path
		self.owner = owner
		life = int(math.ceil(self.owner.health/10.0)*10)
		self.image = pygame.image.load("rsc/Health Bar/p1/10.png")
		self.rect = self.image.get_rect()
		self.place(pos)
		
		
	def place(self, pos):
		self.rect.center = pos
		
		
	def update(self):
		life = int(math.ceil(self.owner.health/10.0)*10)
		if life <= 0:
			life = 0
		elif life >= 100:
			life = 100
		self.image = pygame.image.load(self.path + str(life) + ".png")
		#self.rect = self.image.get_rect()
		
		

		


