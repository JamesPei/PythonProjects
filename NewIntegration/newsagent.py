#__author__ = 'James'
#-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from nntplib import NNTP
from time import strftime,time,localtime
from email import message_from_string
from urllib import urlopen
import textwrap
import re

day = 24*60*60 #一天的秒数

def wrap(string, max = 70):
    #将字符串调整为最大行宽
    return '\n'.join(textwrap.wrap(string))+'\n'

#包括标题和主体文本的简单新闻项目
class NewsItem:

    def __init__(self,title,body):
        self.title = title
        self.body = body

#从新闻来源获取新闻项目并发布到新闻目标的对象
class NewsAgent:

    def __init__(self):
        self.sources = []
        self.destinations = []

    def addSource(self,source):
        self.sources.append(source)

    def addDestination(self,dest):
        self.destinations.append(dest)

    #从所有来源获取所有新闻项目并发布到所有目标
    def distribute(self):
        items = []
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.receiveItems(items)

#从NNTP组中获取新闻项目的新闻来源
class NNTPSource:

    def __init__(self, servername, group, window):
        self.servername = servername
        self.group = group
        self.window = window

    def getItems(self):
        start = localtime(time() - self.window*day)
        date = strftime('%y%m%d',start)
        hour = strftime('%H%M%S',start)

        server = NNTP(self.servername)

        ids = server.newnews(self.group, date, hour)[1]

        for id in ids:
            lines = server.article(id)[3]
            message = message_from_string('\n'.join(lines))

            title = message['subject']
            body = message.get_payload()
            if message.is_multipart():
                body = body[0]

            yield NewsItem(title, body)

        server.quit()

#使用正则表达式从网页中提取新闻项目的新闻来源
class SimpleWebSource:

    def __init__(self, url, titlePattern, bodyPattern):
        self.url = url
        self.titlePattern = re.compile(titlePattern)
        self.bodyPattern = re.compile(bodyPattern)

    def getItems(self):
        text = urlopen(self.url).read()
        titles = self.titlePattern.findall(text)
        # for title in titles:
        #     print title[0]
        # bodies = self.bodyPattern.findall(text)
        for title in titles:
            yield NewsItem(title[0],title[1].decode('utf-8'))

#将所有新闻项目格式化为纯文本的新闻目标类
class PlainDestination:

    def receiveItems(self, items):
        for item in items:
            print item.title
            print '_'*len(item.title)
            print item.body

#将所有新闻项目格式化为HTML的目标类
class HTMLDestination:

    def __init__(self,filename):
        self.filename = filename

    def receiveItems(self, items):
        out = open(self.filename,'w')
        print >> out,"""
        <html >
            <head>
            <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                <title>Today's News</title>
            </head>
            <body>
                <h1>Today's News</h1>
        """

        print >> out,'<ul>'

        id = 0
        for item in items:
            id += 1
            print >> out,'<li><a href="%s">%s</a></li>'%(item.title,item.body)
        print >> out,'</ul>'

        # id = 0
        # for item in items:
        #     id+=1
        #     print >> out,'<h2><a name="%i">%s</a></h2>'%(id,item.title)
        #     print >> out,'<pre>%s</pre>'%item.body

        print >> out,"""
            </body>
        </html>
        """

#来源和目标的默认设置。可以自己修改
def runDefaultSetup():

    agent = NewsAgent()

    #从BBC新闻站获取新闻的NNTPSource：
    bbc_url = 'http://news.sina.com.cn'
    bbc_title = r'<a target="_blank" href="(.*?)">(.*?)</a>'
    bbc_body = r'(?s)</a>\s*<br />\s*(.*?)\s*<'
    bbc = SimpleWebSource(bbc_url,bbc_title,bbc_body)

    agent.addSource(bbc)

    #从comp.lang.python.annouce获取新闻的NNTPSource:
    clpa_server = 'news.newsfan.net' # Insert real server name
    clpa_group = 'comp.lang.python.announce'
    clpa_window = 1
    clpa = NNTPSource(clpa_server,clpa_group,clpa_window)

    agent.addSource(clpa)

    #增加纯文本目标和HTML目标:
    agent.addDestination(PlainDestination())
    agent.addDestination(HTMLDestination('news.html'))

    #发布新闻项目
    agent.distribute()

if __name__ == '__main__':runDefaultSetup()#用if __name__ == '__main__'来判断是否是在直接运行该.py文件,详见http://www.cnblogs.com/xuxm2007/archive/2010/08/04/1792463.html




