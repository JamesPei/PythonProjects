#__author__='James'
#-*-coding:utf8-*-

from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector, Selector


class StackOverFlowSpider(BaseSpider):

    condition = ''
    name = "stackoverflow"
    allowed_domains = ["stackoverflow.com"]

    def __init__(self, condition):
        self.condition = '/questions/tagged/'+condition

    start_urls = ['http://stackoverflow.com'+condition]


    def parse(self, response):
        Selector(response = response).xpath()



