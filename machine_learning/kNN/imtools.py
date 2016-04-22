#__author__ = 'James'
#-*-coding:utf-8
from numpy import arange, meshgrid, array

from matplotlib.pyplot import contour, plot, axis


def plot_2D_boundary(plot_range, points, decisionfcn, labels, values=[0]):
    '''plot_range 为　(xmin,xmax,ymin,ymax), points是类数据点列表，decisionfcn是评估函数,
    labels是函数decidionfcn关于每个类返回的标记列表'''

    clist = ['b','r','g','k','m','y']   #不同的类用不同的颜色标识

    #在一个网格上进行评估,并画出决策函数的边界
    x = arange(plot_range[0],plot_range[1],.1)
    y = arange(plot_range[2],plot_range[3],.1)
    xx,yy = meshgrid(x,y)
    xxx,yyy = xx.flatten(), yy.flatten()    #网格中的x,y坐标点列表
    zz = array(decisionfcn(xxx,yyy))
    zz = zz.reshape(xx.shape)

    #以values画出边界
    contour(xx,yy,zz,values)

    #对于每类,用*画出分类正确的点,用o画出分类不正确的点
    for i in range(len(points)):
        d = decisionfcn(points[i][:,0], points[i][:,1])
        correct_ndx = labels[i]==d
        incorrect_ndx = labels[i]!=d
        plot(points[i][correct_ndx,0],points[i][correct_ndx, 1],'*', color=clist[i])
        plot(points[i][incorrect_ndx,0],points[i][incorrect_ndx, 1],'o', color=clist[i])

    axis('equal')
