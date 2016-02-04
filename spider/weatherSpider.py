#__author__ = 'JamesPei'
#-*-coding:utf-8-*-

import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")

from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
import re

class WeatherSpider(BaseSpider):
    name = "weather"
    allowed_domains = ["www.weather.com.cn"]
    start_urls = ['http://www.weather.com.cn/static/html/weather.shtml']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        cityurl = hxs.select('//div[id="maptabbox01"]/ul/li/a/text()').extract()
        print '*******************************8:', repr(cityurl)