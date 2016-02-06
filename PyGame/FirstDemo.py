#__author__ = 'James'
#-*-coding:utf-8-*-

#指定图像文件名称
background_image_filename = '3.jpg'
mouse_image_filename = '1.png'

import pygame   #导入pygame库
from pygame.locals import *     #导入一些常用的函数和常量
from sys import exit        #向sys模块借一个exit函数用来退出程序

pygame.init()   #初始化pygame,为使用硬件做准备

#set_mode会返回一个Surface对象，代表了在桌面上出现的那个窗口，三个参数第一个为元祖，代表分 辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深
screen = pygame.display.set_mode((480, 640), 0, 32)     #创建了一个窗口
pygame.display.set_caption("Hello, World!")     #设置窗口标题

#加载并转换图像
#convert函数是将图像数据都转化为Surface对象，每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）；
# convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

#游戏的主循环是一个无限循环，直到用户跳出。在这个主循环里做的事情就是不停地画背景和更新光标位置，虽然背景是不动的，我们还是需要每次都画它， 否则鼠标覆盖过的位置就不能恢复正常了。
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()

    #blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。
    screen.blit(background, (0,0))      #将背景图画上去

    x, y = pygame.mouse.get_pos()       #获得鼠标位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2       #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))       #把光标画上去

    pygame.display.update()     #刷新一下画面