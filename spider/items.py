# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class rocheItem(scrapy.Item):
    name = scrapy.Field()
    generic = scrapy.Field()
    compound = scrapy.Field()
    indication = scrapy.Field()
    expectedFiling = scrapy.Field()
    pass
