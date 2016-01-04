#__author__ = 'James'
#-*-coding:utf8-*-

import pygame,config,os
from random import randrange

#所有子图形的泛型超类。构造函数负责载入图像，设置子图形的rect和area属性，并且允许它在指定区域内进行移动。area由屏幕的大小和留白决定
class SquishSprite(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink, shrink)

class Weight(SquishSprite):
    def __init__(self, speed):
        SquishSprite.__init__(self, config.weight_image)
        self.speed = speed
        self.reset()

    #将秤砣移动到屏幕顶端（视线外），放置在任意水平位置上
    def reset(self):
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x,0

    #根据它的速度将秤砣垂直移动一段距离。并且根据它是否触及屏幕底端来设置landed属性
    def update(self):
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom

class Banana(SquishSprite):
    def __init__(self):
        SquishSprite.__init__(self, config.banana_image)
        self.rect.bottom = self.area.bottom
        #在没有香蕉的部分进行填充
        #如果秤砣移动到了这些区域，它不会被判定为碰撞
        self.pad_top = config.banana_pad_top
        self.pad_side = config.banana_pad_side

    #将banana中心点的横坐标设定为当前鼠标指针的横坐标，并且使用rect的clamp方法确保banana停留在所允许的范围内
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)

    #确定香蕉是否触碰到了另外的子图形。除了使用rect的colliderect方法外首先要计算一个不包括香蕉图像顶端和侧边的“空区域”的新矩形（使用inflate对顶端和侧边填充）
    def touches(self,other):
        #使用适当的填充缩小边界
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        #移动边界，将它们放置到banana的底部
        bounds.bottom = self.rect.bottom
        #检查边界是否和其它对象的rect交叉
        return bounds.colliderect(other.rect)




