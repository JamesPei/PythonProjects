#__author__ = 'James'
# -*- coding:utf-8 -*-

import sys,re
from util import *

file = open(u'G:\Email.html','w')
# print '<html><head><title>JAVA Multiple Thread Coding</title><body>'
file.write('<html><head><title>MarkInTime Demo</title><body>')

title = True
for block in blocks(open(u'G:\Email.txt')):
    #sub（pat,repl,string[,count=0]）将字符串中的所有pat匹配项用repl代替
    block = re.sub(r'\*(.+?)\*',r'<em>\l</em>',block)
    if title:
        # print '<h1>'
        file.write('<h1>')
        # print block
        file.write(block)
        # print '</h1>'
        file.write('</h1>')
        title = False
    else:
        # print '<p>'
        file.write('<p>')
        # print block
        file.write(block)
        # print '</p>'
        file.write('</p>')


# print '</body></html>'
file.write('</body></html>')

file.flush()
file.close()
