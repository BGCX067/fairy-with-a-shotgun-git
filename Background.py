import pygame, sys, math

class Background(pygame.sprite.Sprite):
    def __init__(self, image, size):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        
    def update(*args):
		pass
        
    def fixLocation(self, x, y):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

