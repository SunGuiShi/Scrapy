# -*- coding: utf-8 -*-
import scrapy


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.biquge.cm']
    start_urls = ['http://www.biquge.cm/']

    def parse(self, response):
        pass
