import pygame, sys, math

class Blast(pygame.sprite.Sprite):
    def __init__(self, direction = "right", pos = (0,0)):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.baseImage = pygame.image.load("rsc/Projectiles/Blast.png")
        self.speedx = 30
        self.speedy = 0
        self.size = [5,10]
        self.sizeGrowth = 1.1
        self.damage = 100
        self.damageDrain = 5
        self.headingx = direction
        self.realx = pos[0]
        self.realy = pos[1]
        if self.headingx == "left":
            self.baseImage = pygame.transform.flip(self.baseImage, 1, 0)
            self.realx -= 21
            self.realy -= 9
        else:
            self.realx += 21
            self.realy -= 9
        self.image = pygame.transform.scale(self.baseImage, self.size)
        self.rect = self.image.get_rect()
        self.place([self.realx, self.realy])
        self.offsetx = 0
        self.offsety = 0
        
        
    def place(self, pos):
        self.rect.center = pos    
        
    def update(*args):
        self = args[0]
        self.playerspeedx = args[2]
        self.playerspeedy = args[3]
        self.scrollingx = args[4]
        self.scrollingy = args[5]
        self.move()
        self.damage -= self.damageDrain
        self.size = [self.size[0]*self.sizeGrowth, self.size[1]*self.sizeGrowth]
        self.image = pygame.transform.scale(self.baseImage, [int(self.size[0]), int(self.size[1])])
        self.rect = self.image.get_rect(center = self.rect.center)
        if self.damage <= 0:
            self.kill()
        
        
    def move(self):
        #print "enemy", self.realx, self.speedx
        if self.headingx == "right":
            self.realx += self.speedx
        else:
            self.realx -= self.speedx
       
            
        if self.scrollingx:
            self.offsetx -= self.playerspeedx
        if self.scrollingy:
            self.offsety -=  self.playerspeedy
        
        self.x = self.realx + self.offsetx
        self.y = self.realy + self.offsety
        
        print self.x, self.y
            
        self.rect.center = (round(self.x), round(self.y))