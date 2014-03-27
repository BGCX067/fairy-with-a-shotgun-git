import pygame, sys, math

class CounterDisplay(pygame.sprite.Sprite):
    def __init__(self, startValue, pos = (0,0)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.value = startValue
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(str(self.value), 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.place(pos)
        
    def place(self, pos):
        self.rect.center = pos
        
    def update(self, size):
        self.image = self.font.render(str(self.value), 1, (255, 255, 255))
        self.rect = self.image.get_rect(center = self.rect.center)
    
    def updateValue(self, value):
        self.value = value
        