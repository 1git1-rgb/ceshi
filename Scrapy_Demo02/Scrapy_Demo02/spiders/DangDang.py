import scrapy
from ..items import ScrapyDemo02Item


class DangdangSpider(scrapy.Spider):
	name = "DangDang"
	allowed_domains = ["bang.dangdang.com"]
	start_urls = ["http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-recent7-0-0-1-1"]

	base_url = "http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-recent7-0-0-1-"
	page = 1

	def parse(self, response):
		# 创建xpath的公共方法
		li_list = response.xpath("//div/ul[@class = 'bang_list clearfix bang_list_mode']/li")
		# 遍历循环查询到的数据
		for li in li_list:
			# 获取书籍图片地址
			src = li.xpath(".//img/@src").extract_first()
			if src:
				src = src
			else:
				src = li.xpath(".//img/@data-original").extract_first()
			# 获取书名
			name = li.xpath(".//img/@alt").extract_first()
			# 获取图书价格
			price = li.xpath(".//p/span[@class = 'price_n']/text()").get()

			# 将获取到数据传给itme 定义数据结构
			book = ScrapyDemo02Item(src=src, name=name, price=price)
			# 将获取到的内容信息传给管道进行下载
			yield book

		# 爬取多页的图片信息
		if self.page < 25:
			self.page = self.page + 1
			url = self.base_url + str(self.page)
			# 怎么调用parse方法
			# scrapy.Request就是scrpay的get请求
			# url 就是请求地址  callback就是要执行的那个函数 不允许要加圆括号
			yield scrapy.Request(url=url, callback=self.parse)

		pass
