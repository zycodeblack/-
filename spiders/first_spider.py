#-*-coding:UTF-8-*-
import scrapy
import re
import codecs
from homework.items import HomeworkItem
from scrapy.selector import Selector

class VoaSpider(scrapy.Spider):
	name = "voa"
	#allowed_domains = ["www.51voa.com"]
	start_urls = [
		"http://www.51voa.com"
	]

	def parse(self,response):
		x = re.findall('VOA_Special_English(.*?).html', response.body)
		for it in x:
			try:
				it = "http://www.51voa.com//VOA_Special_English" + it + ".html"
				url = it
				yield scrapy.Request(url, callback=self.parse_url)
			except:
				continue

	def parse_url(self,response):
		title = response.xpath("/html/head/title/text()").extract()
		url = response.url
		text = re.findall(r'<p>(.*?)</p>', response.body)
		item = HomeworkItem()
		item['news_title'] = title
		item['news_url'] = url
		item['news_body'] = text
		#print item
		yield item

