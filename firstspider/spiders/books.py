# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import BookItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//article[@class="product_pod"]//h3')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)

        le = LinkExtractor(restrict_xpaths='//ul[@class="pager"]//li[@class="next"]')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_book(self, response):

        book = BookItem()
        sel = response.xpath('//div[@class="col-sm-6 product_main"]')

        book['name'] = sel.xpath('./h1/text()').extract_first()
        book['stock'] = sel.xpath('.//p[@class="instock availability"]/text()').extract()[1].split('\n')[2].split()[2][1:]
        book['price'] = sel.xpath('.//p[@class="price_color"]/text()').extract_first()
        book['review_rating'] = sel.xpath('//p[3]/@class').re_first('star-rating ([A-Za-z]+)')
        book['upc'] = sel.xpath('//tr[1]/td/text()').extract_first()
        book['review_num'] = sel.xpath('//tr[last()]//td/text()').extract_first()

        yield book


