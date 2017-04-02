# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HomeworkItem(scrapy.Item):
	'''
	title_news = scrapy.Field()
	ori_link_news = scrapy.Field()
	content_news = scrapy.Field()
	'''
	news_title = scrapy.Field()
	news_url = scrapy.Field()
	news_body = scrapy.Field()
