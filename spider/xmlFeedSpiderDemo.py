#__author__ = 'James'
#-*-coding:utf-8-*-
from scrapy.contrib.spiders import XMLFeedSpider

#创建了一个spider，从给定的 start_urls 中下载feed， 并迭代feed中每个 item 标签，输出，并在 Item 中存储有些随机数据。
class MySpider(XMLFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iternodes' # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        log.msg('Hi, this is a <%s> node!: %s' % (self.itertag, ''.join(node.extract())))

        item = TestItem()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item
