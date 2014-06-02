import pygame, sys, math, random

pygame.init()

from Block import Block
from Player import Player
from HardBlock import HardBlock
from Enemy import Enemy
from Background import Background
from Money import Money
from HUD import CounterDisplay
from Blast import Blast
from HealthBar import *


clock = pygame.time.Clock()
width = 800
height = 600
size = width, height
fullscreen = 0

blocksize = [75,75]
playersize = [77,90]

screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0,0,0

blocks = pygame.sprite.Group()
hardBlocks = pygame.sprite.Group()
enemies = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()
moneys = pygame.sprite.Group()
HUDs = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

Player.containers = (all, players)
Block.containers = (all, blocks)
HardBlock.containers = (all, hardBlocks, blocks)
Enemy.containers = (all, enemies)
Background.containers = (all, blocks)
Money.containers = (all, moneys)
CounterDisplay.containers = (all, HUDs)
Blast.containers = (all, projectiles)
HealthBar.containers = (all, HUDs)


#CURSOR = pygame.cursor.load_xbm("rsc/CURSORS/CursorM1.xbm")

#cursor = pygame.cursors.compile(CURSOR)
#pygame.mouse.set_cursor((24,24),(12,12),cursor[0],cursor[1])


bg = Background("rsc/bg/mainbg.png", size)

def loadLevel(level):
    f = open(level+".lvl", 'r')
    lines = f.readlines()
    f.close()
    
    newlines = []
    
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newlines += [newline]
        
    for line in newlines:
        print line
    
    playerpos = [0,0]
    for y, line in enumerate(newlines):
        for x, c in enumerate(line):
            if c == "@":
                playerpos = [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2]
            if c == "#":
                HardBlock("rsc/blocks/black.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "$":
                Money(5, 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            elif c == "=":
                HardBlock("rsc/blocks/blue.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
    
            elif c == "w":
                Block("rsc/blocks/wood.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
                      
            elif c == "-":
                HardBlock("rsc/blocks/grass.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
                      
            elif c == "l":
                Block("rsc/blocks/Leaf.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      blocksize)
            
    
    
    
    #f = open(level+".tng", 'r')
    #lines = f.readlines()
    #f.close()
    
    newlines = []
    
    for line in lines:
        newline = ""
        for c in line:
            if c != "\n":
                newline += c
        newlines += [newline]
        
    for line in newlines:
        print line
    
    for y, line in enumerate(newlines):
        for x, c in enumerate(line):
            if c == "@":
                player = Player([(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2],
                     playersize,
                     size)
            elif c == "e":
                Enemy("rsc/enemy/slime 1.png", 
                      [(x*blocksize[0])+blocksize[0]/2, (y*blocksize[1])+blocksize[1]/2], 
                      playersize)
    for each in all.sprites():
        each.fixLocation(player.offsetx, player.offsety)
     
    

    
    
levels = ["rsc/levels/level1",
          "rsc/levels/level2"]
level = 0
loadLevel(levels[level])
player1 = players.sprites()[0]
moneycounter = CounterDisplay(player1.money, (20,height - 10))
healthbar = HealthBar(player1, (50,50))
player1.living = False

while True:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                if (event.key == pygame.K_RSHIFT or event.key == pygame.K_LSHIFT):
                    if fullscreen == 0:
                        fullscreen = pygame.FULLSCREEN
                    else:
                        fullscreen = 0
                    screen = pygame.display.set_mode((width,height),fullscreen)
                    pygame.display.flip()
                if event.key == pygame.K_RETURN:
                    player.living = True
                    if level < len(levels)-1:
                        level += 1
                    else:
                        level = 0  
                    pm = player1.money
                        
                    for each in all.sprites():
                        each.kill()
                    bg = Background("rsc/bg/mainbg.png", size)
                    screen.blit(bg.image, bg.rect)
                    loadLevel(levels[level])
                    player1 = players.sprites()[0]
                    player1.money = pm
                    moneycounter = CounterDisplay(player1.money, (20,height - 10))
                    healthbar = HealthBar(player1, (50,50))

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.direction("right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.direction("left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.jump()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player1.direction("down")
                if event.key == pygame.K_SPACE:
                    Blast(player1.headingx, player1.rect.center)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player1.direction("stop right")
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player1.direction("stop left")
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player1.stop_jump()
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player1.direction("stop down")
                    
        playersHitBlocks = pygame.sprite.groupcollide(players, hardBlocks, False, False)
        enemiesHitBlocks = pygame.sprite.groupcollide(enemies, hardBlocks, False, False)
        enemiesHitEnemies = pygame.sprite.groupcollide(enemies, enemies, False, False)
        playersHitMoney = pygame.sprite.groupcollide(players, moneys, False, True)
        
        for player in playersHitBlocks:
            for block in playersHitBlocks[player]:
                player.collideBlock(block)
                
        for enemy in enemiesHitBlocks:
            for block in enemiesHitBlocks[enemy]:
                enemy.collideBlock(block)
                
        #for enemy in enemiesHitEnemies:
            #for otherEnemy in enemiesHitEnemies[enemy]:
                #enemy.collideBlock(otherEnemy)
        
        for player in playersHitMoney:
            for money in playersHitMoney[player]:
                player.collideMoney(money)
                moneycounter.updateValue(player.money)
        
        
        all.update(size,
                   player1.speedx, 
                   player1.speedy, 
                   player1.scrollingx, 
                   player1.scrollingy,
                   player1.realx,
                   player1.realy)
        
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(30)
    














