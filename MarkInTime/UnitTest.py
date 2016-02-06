# __author__ = 'James'
# -*- coding:utf-8 -*-

from util import *
from handlers import *
import re

# for line in lines(open(u'G:\线程教程.txt')):
#     print line

# for block in blocks(open(u'G:\线程教程.txt')):
#     print block

handler = HTMLRenderer()
# handler.start('document')
print re.sub(r'\*(.+?)\*',handler.sub('emphasis'),'this *is* a test')

