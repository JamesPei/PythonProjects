#__author__ = 'James'
#-*- coding:utf-8 -*-

from nntplib import NNTP
from time import strftime,time,localtime
from email import message_from_string
from urllib import urlopen
from codeTransfer import *
import textwrap
import re

# print strftime('%y%m%d')
# start = localtime(time()-60*60*24*365)
# print strftime('%y%m%d',start)

class SimpleWebSource:

    def __init__(self, url, titlePattern, bodyPattern):
        self.url = url
        self.titlePattern = re.compile(titlePattern)
        self.bodyPattern = re.compile(bodyPattern)

    def getItems(self):
        text = urlopen(self.url).read()
        titles = self.titlePattern.findall(text)
        bodies = self.bodyPattern.findall(text)
        for title in titles:
            print title[1].decode('utf-8')
        print bodies

bbc_url = 'http://news.sina.com.cn'
bbc_title = r'<a target="_blank" href="(.*?)">(.*?)</a>'
bbc_body = r'(?s)</a>\s*<br />\s*(.*?)\s*<'
# bbc = SimpleWebSource(bbc_url,bbc_title,bbc_body)
# bbc.getItems()

server = NNTP('129.69.1.59')
server.group('camp.lang.python')[0]