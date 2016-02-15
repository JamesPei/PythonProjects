#__author__ = 'JamesPei'
#-*-coding:utf-8-*-

import sys
reload(sys)
#python默认环境编码时ascii
sys.setdefaultencoding("utf-8")

from scrapy.spiders import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector, Selector
from weather.items import WeatherItem

class WeatherSpider(BaseSpider):
    name = "weather"
    allowed_domains = ["www.weather.com.cn"]
    start_urls = ['http://www.weather.com.cn/static/html/weather.shtml']

    def parse(self, response):

        cityurls = Selector(response=response).xpath('//div[contains(@id,"maptabbox")]/ul/li/a').extract()

        for link in cityurls:
            link = str(link)
            url = Selector(text=link).xpath('//a/@href').extract_first()
            yield Request(url, callback=self.parse_item)

    def parse_item(self, response):
        times = Selector(response=response).xpath('//div/ul[@id="someDayNav"]/li[contains(@class,"hover")]/a/@href').extract()

        for time in times:
            yield Request("http://www.weather.com.cn"+time, callback=self.parse_weather)

    def parse_weather(self, response):

        item = WeatherItem()

        cityname = Selector(response=response).xpath('//title/text()').extract()
        item['city_name'] = cityname

        weather = Selector(response=response).xpath('//div[@id="7d"]/ul/li[@class="sky skyid lv2 on"]/p').extract()

        if not weather:
            weather = Selector(response=response).xpath('//div[@id="7d"]/ul/li[@class="sky skyid lv3 on"]/p').extract()
            if not weather:
                weather = Selector(response=response).xpath('//div[@id="7d"]/ul/li[@class="on"]/p').extract()

        for p in weather:
            p = str(p)
            detail = Selector(text=p)
            max = detail.xpath('//p[@class="tem"]/span/text()').extract_first()
            min = detail.xpath('//p[@class="tem"]/i/text()').extract_first()

            if not max or not min:
                continue

            item['max_weather'] = max
            item['min_weather'] = min

            yield item

