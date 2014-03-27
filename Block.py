import pygame, sys, math

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos = (0,0), blocksize = [50,50]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, blocksize)
        self.rect = self.image.get_rect()
        self.realx = pos[0]
        self.realy = pos[1]
        self.x = pos[0]
        self.y = pos[1]
        self.place(pos)
        self.speedx = 0
        self.speedy = 0
        self.scrollingx = False
        self.scrollingy = False
        
    def place(self, pos):
        self.rect.center = pos
        
    def fixLocation(self, x, y):
        self.x += x
        self.y += y
        
    def update(*args):
        self = args[0]
        self.speedx = args[2]
        self.speedy = args[3]
        self.scrollingx = args[4]
        self.scrollingy = args[5]
        self.move()
        
    def move(self):
        if self.scrollingx:
            self.x -= self.speedx
        if self.scrollingy:
            self.y -= self.speedy
            
        self.rect.center = (round(self.x), round(self.y))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

