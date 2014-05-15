import pygame, sys, math, random, time

from Block import Block

class Enemy(Block):
    def __init__(self, image, pos = (0,0), blocksize = [50,50], screensize = [800,600]):
        Block.__init__(self, image, pos, blocksize)
        self.maxSpeed = blocksize[0]/14.0
        self.screensize = screensize
        self.living = True
        self.detectRange = 100
        self.seePlayer = False
        self.headingx = "right"
        self.headingy = "none"
        self.directionCount = 0
        self.realx = pos[0]
        self.realy = pos[1]
        self.x = screensize[0]/2
        self.y = screensize[1]/2
        self.x = pos[0]
        self.y = pos[1]
        self.g = blocksize[0]/10
        self.offsetx = 0
        self.offsety = 0
        self.jumpSpeed = 0
        self.jumpSpeedMax = 50
        self.fallSpeedMax = int(blocksize[0]/2) -2
        self.onfloor = False
        self.floor = screensize[1]
        self.touchFloor = False
        self.turn = 0
        
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
        self.move()
        self.detectPlayer(playerx, playery)
        self.collideWall(self.screensize)
        
        if (self.rect.bottom < self.floor) and self.headingy == "none":
            self.headingy = "down"
        self.headingChanged = False
        self.touchFloor = False
        if not self.seePlayer:
            self.ai()
        self.turn += 1
        
        
    def detectPlayer(self, playerx, playery):
        if self.distanceToPoint([playerx, playery]) < self.detectRange:
            #print "I seeeee you!!!"
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
            #print "Where are you?"
            
    def move(self):
        #print "enemy", self.realx, self.speedx
        self.realx += self.speedx
        self.realy += self.speedy
        
        if not self.touchFloor:
            self.headingy = "down"
        if self.headingy == "down":
            if self.speedy < self.fallSpeedMax:
                self.speedy += self.g
            else:
                self.speedy = self.fallSpeedMax
                
        self.realx += self.speedx
        self.realy += self.speedy
        
        
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
        
    def collideWall(self, size):
        if self.rect.left < 0 and self.headingx == "left":
            self.speedx = 0
        elif self.rect.right > size[0] and self.headingx == "right":
            self.speedx = 0
        if self.rect.top < 0 and self.headingy == "up":
            self.speedy = 0
        elif self.rect.bottom > size[1] and self.headingy == "down":
            self.speedy = 0
            
    def ai(self):
        if self.directionCount > 0:
            self.directionCount -= 1
        else:
            self.directionCount = random.randint(10,100)
            dir = random.randint(0,3)
            if dir == 0:  
                self.direction("right")
            if dir == 1:
                self.direction("stop right")
            if dir == 2:
                self.direction("left")
            if dir == 3:
                self.direction("stop left")
            if dir == 4:
                self.direction("jump")
            self.speedx = random.randint(0, int(self.maxSpeed))
            self.speedy = random.randint(0, int(self.maxSpeed))
            
            
    def direction(self, dir):
        if dir == "right":
            self.headingx = "right"
            self.speedx = self.maxSpeed
            self.lastHeading = "right"
            self.headingChanged = True
        if dir == "stop right":
            self.headingx = "right"
            self.speedx = 0
        if dir == "left":
            self.headingx = "left"
            self.speedx = -self.maxSpeed
            self.lastHeading = "left"
            self.headingChanged = True
        if dir == "stop left":
            self.headingx = "left"
            self.speedx = 0
        if dir == "jump":
            if not self.jumping:
                self.jumping = True
                self.headingy = "up"
                self.jumpSpeed = self.jumpSpeedMax
                self.speedy = -self.jumpSpeed
                self.headingChanged = True
                self.touchingFloor = False
        if dir == "up":
            self.headingy = "up"
            self.speedy = -self.maxSpeed
            self.lastHeading = "up"
            self.headingChanged = True
        if dir == "stop up":
            self.headingy = "up"
            self.speedy = 0
        if dir == "down":
            self.headingy = "down"
            self.speedy = self.maxSpeed
            self.lastHeading = "down"
            self.headingChanged = True
        if dir == "stop down":
            self.headingy = "down"
            self.speedy = 0
      
    def collideBlock(self, block):
        #time.sleep(.5)
        print self.rect, self.headingx, self.headingy, block.rect, block.realx, block.realy
        if self.floor == block.rect.top + 2 and self.headingy == "none":
            self.touchFloor = True
            self.jumping = False
        else:
            if self.realx < block.realx and self.headingx == "right":
                self.speedx = 0
                self.realx -= 1
                self.x -= 1
                print "hit right"
            if self.realx > block.realx and self.headingx == "left":
                self.speedx = 0
                self.realx += 1
                self.x += 1
                print "hit left"
            if self.realy > block.realy and self.headingy == "up":
                self.speedy = 0
                self.realy += 1
                self.y += 1
                print "hit up"
            print "\n",self.turn, self.realy, block.realy, self.realy > block.realy, self.headingy, self.headingy == "down","\n"
            if self.realy < block.realy and self.headingy == "down":
                self.touchFloor = True
                self.speedy = 0
                self.realy -= self.g + 2
                self.headingy = "none"
                self.floor = block.rect.top+2
                self.y = self.floor - self.rect.height/2
                print "///////////////////////hit down"
            
            
    
            
            
    def distanceToPoint(self, pt):
        x1 = self.realx
        y1 = self.realy
        x2 = pt[0]
        y2 = pt[1]
        
        return math.sqrt(((x2-x1)**2)+((y2-y1)**2))
        
