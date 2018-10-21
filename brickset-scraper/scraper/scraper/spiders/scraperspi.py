# -*- coding: utf-8 -*-
import scrapy


class ScraperspiSpider(scrapy.Spider):
    name = 'scraperspi'
    allowed_domains = ['scraperspi.com']
    start_urls = ['http://scraperspi.com/']

    def parse(self, response):
        pass
