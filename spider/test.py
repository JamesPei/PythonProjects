#__author__ = 'JamesPei'
#-*-coding:utf-8-*-

import sys, types
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.selector import HtmlXPathSelector, Selector

html = '''
<div id="maptabbox01" style="display: none;" class="maptabboxin">
		<ul>
			<li><a href="http://www.weather.com.cn/weather1d/101010100.shtml" target="_blank">北京</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101030100.shtml" target="_blank">天津</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101090101.shtml" target="_blank">石家庄</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101100101.shtml" target="_blank">太原</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101080101.shtml" target="_blank">呼和浩特</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101090201.shtml" target="_blank">保定</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101100201.shtml" target="_blank">大同</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101080201.shtml" target="_blank">包头</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101090402.shtml" target="_blank">承德市</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101100401.shtml" target="_blank">晋中</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101080501.shtml" target="_blank">通辽</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101091101.shtml" target="_blank">秦皇岛</a></li>
		</ul>
	</div>
	<div id="maptabbox02" style="display: none;" class="maptabboxin">
		<ul>
			<li><a href="http://www.weather.com.cn/weather1d/101010100.shtml" target="_blank">北京1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101030100.shtml" target="_blank">天津1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101090101.shtml" target="_blank">石家庄1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101100101.shtml" target="_blank">太原1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101080101.shtml" target="_blank">呼和浩特1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101090201.shtml" target="_blank">保定1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101100201.shtml" target="_blank">大同1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101080201.shtml" target="_blank">包头1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101090402.shtml" target="_blank">承德市1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101100401.shtml" target="_blank">晋中1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101080501.shtml" target="_blank">通辽1</a></li>
			<li><a href="http://www.weather.com.cn/weather1d/101091101.shtml" target="_blank">秦皇岛1</a></li>
		</ul>
	</div>
'''

detail='''<p title="多云" class="wea">多云</p>
<p class="tem">
<span>4</span>/<i>-4℃</i>
</p>
<p class="win">
<em>
<span title="北风" class="N"></span>
<span title="西风" class="W"></span>
</em>
<i>4-5级转微风</i>
</p>
'''

# list1 = Selector(text=html).xpath('//div[@id="maptabbox01"]/ul/li/a/text()').extract()
# list1 = Selector(text=html).xpath('//div[@id="maptabbox01"]/ul/li/a/@href').extract()
# print list1
# for str in list1:
#     print type(str)
#     print str.decode('utf-8')

max = Selector(text=detail).xpath('//p[@class="tem"]/span/text()').extract_first()
min = Selector(text=detail).xpath('//p[@class="tem"]/i/text()').extract_first()
print max, min

