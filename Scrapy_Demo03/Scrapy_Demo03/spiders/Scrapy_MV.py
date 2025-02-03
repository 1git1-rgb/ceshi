import scrapy
from ..items import ScrapyDemo03Item


class ScrapyMvSpider(scrapy.Spider):
	name = "Scrapy_MV"
	allowed_domains = ["www.btwuji.com"]
	start_urls = ["https://www.btwuji.com/"]

	def parse(self, response):
		# 爬取首页的名字和第二页的地址
		li_list = response.xpath('//div/div/div/div//tr/td[@class = "inddline"]/a[2]')
		for li in li_list:
			name = li.xpath("./text()").extract_first()
			href = li.xpath("./@href").extract_first()

			# 第二页的地址需要进行拼接，获取到的第二页地址缺少了地址的前缀
			url = "https://www.btwuji.com" + href

			yield scrapy.Request(url=url, callback=self.parse_second,
			                     meta={'name': name})  # meta给parse_second函数发送name的值

	def parse_second(self, response):
		# 拿不到数据的情况下要看response.xpath中是不是有标签无法识别和语法是否正确
		src = response.xpath('//div[@id = "Zoom"]//img/@src').extract_first()

		# 接收到parse发来的name参数的值
		name = response.meta['name']
		movie = ScrapyDemo03Item(src=src, name=name)

		yield movie
		pass
