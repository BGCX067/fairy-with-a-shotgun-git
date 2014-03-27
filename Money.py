import pygame, sys, math

from Block import Block

class Money(Block):
    def __init__(self, value, pos = (0,0), blocksize = [50,50]):
        self.value = value
        image = "rsc/blocks/money.png"
        Block.__init__(self, image, pos, blocksize)
