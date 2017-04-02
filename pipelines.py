# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
import MySQLdb


class HomeworkPipeline(object):
	def process_item(self, item, spider):
		print "---------------------------------------------------------------------------"
		conn=MySQLdb.connect("localhost",'root','411995202','for_spider')
		cur=conn.cursor()
		sql="insert into news (url,title,content)values(\"%s\", \"%s\", \"%s\")"
		try:
			title=item['news_title']
			url=item['news_url']
			text=str(item['news_body'])
			print sql%(url,title,text)
			cur.execute(sql%(url,title,text))
			conn.commit()
			line = str(dict(item))+'\n'
			self.f.write(line)
		except:
			raise
			pass
	def open_spider(self,spider):
		self.f = open('a.txt','wb')
	def close_spiser(self,spider):
		self.f.close()

class JsonWriterPipeline(object):
	def __init__(self):
		self.file = codecs.open('items.jl','wb','utf-8')

	def process_item(self,item,spider):
		line = json.dumps(dict(item))+"\n"
		self.file.write(line)
		return item
