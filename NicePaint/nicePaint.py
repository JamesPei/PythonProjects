#__author__ = 'James'
# -*- coding:utf_8 -*-

from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = ''
COMMENT_CHARS = '#:'


