#__author__ = 'James'
#-*-coding:utf-8-*-

from PIL import Image
import os

pil_im = Image.open('python.jpg')   # 新建PIL图像对象
pil_im_gray = pil_im.convert('L')    # 将其转化为灰度图像

filelist = []
#从列表中读取所有的图像文件并转换为jpeg格式
for infile in filelist:
    outfile = os.path.splitext(infile)[0]+'.jpg'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)    #save（文件保存路径）：保存图像
        except IOError:
            print "cannot convert",infile