# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BookItem(scrapy.Item):
    name = scrapy.Field()   # 书名
    price = scrapy.Field()  # 价格
    review_rating = scrapy.Field()  # 等级
    review_num = scrapy.Field()     # 评价数量
    upc = scrapy.Field()    # 产品编码
    stock = scrapy.Field()      # 库存量

