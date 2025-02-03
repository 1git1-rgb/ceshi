import scrapy


class ScrapyLogSpider(scrapy.Spider):
    name = "Scrapy_Log"
    allowed_domains = ["www.baidu.com"]
    start_urls = ["https://www.baidu.com"]

    def parse(self, response):

        pass
