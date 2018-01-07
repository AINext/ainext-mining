# -*- coding: utf-8 -*-
import scrapy


class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['infoq.com']
    start_urls = ['http://infoq.com/']

    def parse(self, response):
        pass
