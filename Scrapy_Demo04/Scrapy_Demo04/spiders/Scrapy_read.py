import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ScrapyDemo04Item


class ScrapyReadSpider(CrawlSpider):
	name = "Scrapy_read"
	allowed_domains = ["www.dushu.com"]
	start_urls = ["https://www.dushu.com/book/1188_1.html"]

	# CrawlSpider主要用于从网站中抓取数据，并且它通过规则（Rule）来定义链接提取和跟进的规则
	rules = (Rule(LinkExtractor(allow=r"/book/1188_\d+.html"),
	              callback="parse_item",
	              follow=False),)

	def parse_item(self, response):
		# 创建xpath的公共方法
		img_list = response.xpath("//div[@class = 'bookslist']/ul//img")

		# 循环获取数据
		for img in img_list:
			# 获取图片名字
			name = img.xpath("./@alt").extract_first()
			# 获取图片地址
			src = img.xpath("./@src").extract_first()
			# 将参数传给参数体(items)
			book = ScrapyDemo04Item(name=name, src=src)
			# 将参数传给管道
			yield book
