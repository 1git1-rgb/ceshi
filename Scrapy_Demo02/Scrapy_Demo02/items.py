# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemo02Item(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	# 图片路径
	src = scrapy.Field()
	# 图片名称
	name = scrapy.Field()
	# 书籍价格
	price = scrapy.Field()
	pass
