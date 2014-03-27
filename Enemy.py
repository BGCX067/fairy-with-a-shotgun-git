import pygame, sys, math, random

from Block import Block

class Enemy(Block):
    def __init__(self, image, pos = (0,0), blocksize = [50,50]):
        Block.__init__(self, image, pos, blocksize)
        self.maxSpeed = blocksize[0]/14.0
        self.living = True
        self.detectRange = 100
        self.seePlayer = False
        self.headingx = "right"
        self.headingy = "up"
        self.directionCount = 0
        self.realx = pos[0]
        self.realy = pos[1]
        self.x = pos[0]
        self.y = pos[1]
        self.offsetx = 0
        self.offsety = 0
        
    def fixLocation(self, x, y):
        self.offsetx += x
        self.offsety += y
        
    def update(*args):
        self = args[0]
        self.playerspeedx = args[2]
        self.playerspeedy = args[3]
        self.scrollingx = args[4]
        self.scrollingy = args[5]
        playerx = args[6]
        playery = args[7]
        print "enemy:", self.realx, self.realy, "player:", playerx, playery
        self.move()
        self.detectPlayer(playerx, playery)
        if not self.seePlayer:
            self.ai()
        
        
    def detectPlayer(self, playerx, playery):
        if self.distanceToPoint([playerx, playery]) < self.detectRange:
            print "I seeeee you!!!"
            self.seePlayer = True
            self.speedx = self.maxSpeed
            self.speedy = self.maxSpeed
            #print playerx, self.realx, playery, self.realy
            if playerx > self.realx:
                self.headingx = "right"
            elif playerx < self.realx:
                self.headingx = "left"
            if playery > self.realy:
                self.headingy = "down"
            elif playery < self.realy:
                self.headingy = "up"
        else:
            self.seePlayer = False
            print "Where are you?"
            
    def move(self):
        #print "enemy", self.realx, self.speedx
        if self.headingx == "right":
            self.realx += self.speedx
        else:
            self.realx -= self.speedx
        if self.headingy == "down":
            self.realy += self.speedy
        else:
            self.realy -= self.speedy
            
        if self.scrollingx:
            self.offsetx -= self.playerspeedx
        if self.scrollingy:
            self.offsety -=  self.playerspeedy
        
        self.x = self.realx + self.offsetx
        self.y = self.realy + self.offsety
            
        self.rect.center = (round(self.x), round(self.y))
            
    def ai(self):
        if self.directionCount > 0:
            self.directionCount -= 1
        else:
            self.directionCount = random.randint(10,100)
            dir = random.randint(0,3);
            if dir == 0:
                self.headingx = "right"
                self.headingy = "up"
            if dir == 1:
                self.headingx = "right"
                self.headingy = "down"
            if dir == 2:
                self.headingx = "left"
                self.headingy = "down"
            if dir == 3:
                self.headingx = "left"
                self.headingy = "up"
            self.speedx = random.randint(0, int(self.maxSpeed))
            self.speedy = random.randint(0, int(self.maxSpeed))
      
    def collideBlock(self, block):
        #print self.rect, self.headingx, self.headingy
        if self.realx < block.realx and self.headingx == "right":
            self.speedx = 0
            self.realx -= 1
            self.x -= 1
            print "hit right"
            self.directionCount = 0
        if self.realx > block.realx and self.headingx == "left":
            self.speedx = 0
            self.realx += 1
            self.x += 1
            print "hit left"
            self.directionCount = 0
        if self.realy > block.realy and self.headingy == "up":
            self.speedy = 0
            self.realy += 1
            self.y += 1
            print "hit up"
            self.directionCount = 0
        if self.realy < block.realy and self.headingy == "down":
            self.speedy = 0
            self.realy -= 1
            self.y -= 1
            print "hit down"
            self.directionCount = 0
            
            
    def distanceToPoint(self, pt):
        x1 = self.realx
        y1 = self.realy
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
