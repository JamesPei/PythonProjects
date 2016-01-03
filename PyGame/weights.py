#__author__ = 'James'
#-*-coding:utf-8-*-

import sys,pygame
from pygame.locals import *
from random import randrange

#初始化
pygame.init()
screen_size = 800,600
pygame.display.set_mode(screen_size,FULLSCREEN)
pygame.mouse.set_visible(0)

#载入图片
Weight_image = pygame.image.load('1.png')
Weight_image = Weight_image.convert()

class Weight(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #在画sprite时使用的图像和矩形
        self.image = Weight_image




