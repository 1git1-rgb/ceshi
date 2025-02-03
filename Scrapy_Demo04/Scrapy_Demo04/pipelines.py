# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDemo04Pipeline:
	# 文件执行前的函数
	def open_spider(self, spider):
		# 将数据写到文件中
		self.fp = open('book.json', 'a', encoding='utf-8')

	# 文件执行体
	def process_item(self, item, spider):
		self.fp.write(str(item))
		return item

	# 文件执行后的函数
	def close_spider(self, spider):
		# 关闭文件
		self.fp.close()
