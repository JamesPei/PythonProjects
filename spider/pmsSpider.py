#__author__ = 'James'
#-*-coding:utf-8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')  #为避免'ascii' codec can't encode character异常需要设置该属性

from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector, Selector
from scrapy.http import Request
from pms.items import rocheItem

class PmsSpider(Spider):
    name = 'Roche'
    allowed_domains = ['www.roche.com']
    start_urls = ['http://www.roche.com/research_and_development/who_we_are_how_we_work/pipeline.htm']

    def parse(self, response):

        allInfos = Selector(response=response).xpath('''//div[@id="table-view"]/
                                                            div[contains(@class,"table-wrapper")]/
                                                                div[contains(@class,"tbody")]/
                                                                    div[contains(@class,"row item phase")]''').extract()

        print u'总长：',allInfos.__len__()
        total = 0

        for info in allInfos:
            total += 1
            info = str(info)
            # print '---->info:',info
            item = rocheItem()

            Name = Selector(text=info).xpath('//div/@id').extract()
            Generic = Selector(text=info).xpath('//div[contains(@class,"row item phase")]/div[contains(@class,"cell fill")]/span[contains(@class,"generic")]/text()').extract()
            Compound = Selector(text=info).xpath('//div[contains(@class,"row item phase")]/div[contains(@class,"cell fill")]/span[contains(@class,"compound")]/strong/text()').extract()
            Indication = Selector(text=info).xpath('//div[contains(@class,"row item phase")]/div[contains(@class,"cell indication")]/text()').extract()
            ExpectedFiling = Selector(text=info).xpath('//div[contains(@class,"row item phase")]/div[contains(@class,"cell filing")]/span/text()').extract()

            # print '---->name:',name,'Generic:',Generic,'Compound:',Compound,'Indication:',Indication,'ExpectedFiling:',ExpectedFiling
            item['name'] = Name
            item['generic'] = Generic
            item['compound'] = Compound
            item['indication'] = Indication
            item['expectedFiling'] = ExpectedFiling

            yield rocheItem

