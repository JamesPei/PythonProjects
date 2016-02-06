#__author__ = 'James'
#-*-coding:utf-8-*-

import sys,pygame
from pygame.locals import *
from random import randrange

class Weight(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #在画sprite时使用的图像和矩形
        self.image = Weight_image
        self.rect = self.image.get_rect()
        self.reset()

    #将图像移动到屏幕顶端的随机位置
    def reset(self):
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    #更新图片，显示下一帧
    def update(self):
        self.rect.top += 1
        if self.rect.top > screen_size[1]:
            self.reset()

#初始化
pygame.init()
screen_size = 800,600
# pygame.display.set_mode(screen_size,FULLSCREEN)
pygame.display.set_mode(screen_size)
pygame.mouse.set_visible(1)

#载入图片
Weight_image = pygame.image.load('1.png').convert_alpha()

#创建一个子图形组（sprite group），增加Weight
sprites = pygame.sprite.RenderUpdates()     #Group sub-class that tracks dirty updates
sprites.add(Weight())

#获取屏幕表面并填充
screen = pygame.display.get_surface()
bg = (255,255,255)  #白
screen.fill(bg)
pygame.display.flip()       #Update the full display Surface to the screen

#用于清除子图形
def clear_callback(surf, rect):
    surf.fill(bg, rect)


#检查退出事件
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    #清除前面的位置
    #Erases the Sprites used in the last Group.draw() call. The destination Surface is cleared by filling the drawn Sprite positions with the background.
    #The background is usually a Surface image the same dimensions as the destination Surface. However, it can also be a callback function that takes two arguments;
    # the destination Surface and an area to clear. The background callback function will be called several times each clear.
    sprites.clear(screen, clear_callback)       #draw a background over the Sprites
    #更新所有子图形
    sprites.update()
    #绘制所有子图形
    updates = sprites.draw(screen)      #blit the Sprite images and track changed areas
    #更新所需的显示部分
    pygame.display.update(updates)








