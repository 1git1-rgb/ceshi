# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemo04Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书本的名字
    name = scrapy.Field()
    # 图片的地址
    src = scrapy.Field()
    pass
