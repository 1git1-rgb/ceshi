# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 管道下载类
class ScrapyDemo02Pipeline:
	# 爬虫文件开始之前执行的一个方法
	def open_spider(self, spider):
		self.fp = open('book.json', 'a', encoding='utf-8')

	# 执行爬虫文件
	def process_item(self, item, spider):
		self.fp.write(str(item))
		return item

	# 爬虫文件结束之后执行的一个方法
	def close_spider(self, spider):
		self.fp.close()


import urllib.request


# 多条管道同时开启下载
class DangDangDownloadPipeline:  # 定义第二个管道类 然后去settings中开启多管道"Scrapy_Demo01.pipelines.DangDangDownloadPipeline": 301,
	def process_item(self, itme, spider):
		url = itme.get('src')
		filename = './books/' + itme.get('name') + '.jpg'
		urllib.request.urlretrieve(url=url, filename=filename)

		return itme
