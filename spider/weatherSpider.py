#__author__ = 'JamesPei'
#-*-coding:utf-8-*-

import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")

from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector, Selector


class WeatherSpider(BaseSpider):
    name = "weather"
    allowed_domains = ["www.weather.com.cn"]
    start_urls = ['http://www.weather.com.cn/static/html/weather.shtml']

    def parse(self, response):

        cityurls = Selector(response=response).xpath('//div[contains(@id,"maptabbox")]/ul/li/a/@href').extract()

        for link in cityurls:
            yield Request(link, callback=self.parse_item)

    def parse_item(self, response):
        times = Selector(response=response).xpath('//div/ul[@id="someDayNav"]/li[contains(@class,"hover")]/a/@href').extract()
        for time in times:
            yield Request("http://www.weather.com.cn"+time, callback=self.parse_weather)

    def parse_weather(self, response):
        weather = Selector(response=response).xpath('//div[@id="7d"]/ul/li[@class="sky skyid lv2 on"]/p').extract()
        for p in weather:
            p = str(p)
            detail = Selector(text=p)
            max = detail.re(r'<span>(.*?)')
            min = detail.re(r'<i>(.*?)')
            print u'最高:'+str(max), u'最低:'+str(min)
