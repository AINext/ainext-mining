# -*- coding: utf-8 -*-
import scrapy
import time

class InfoqSpider(scrapy.Spider):
    name = 'infoq'
    allowed_domains = ['infoq.com']
    start_urls = ['http://infoq.com/cn/AI/articles']


    def parse(self, response):
        articles = response.xpath("//ul[@class='l l_large']/li")
        links = articles.xpath("./a[@class='lt']/@href").extract()

        for link in links:
            yield response.follow(link.strip(), self.parse_article)

        next_page = response.css("a.btn_next::attr('href')").extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        def extract_with_xpath(query):
            return response.xpath(query).extract_first().strip()

        def extract_with_xpath_idx(query, idx):
            return response.xpath(query).extract()[idx].strip()

        def extract_with_css(query):
           return response.css(query).extract_first().strip()

        def extract_date():
           s = response.xpath("//span[@class='heading_author']/text()").extract()
           dateStr = s[len(s)-2]
           d = dateStr.split()[1]
           timeArray = time.strptime(d, "%Y年%m月%d日")
           dd = time.strftime("%Y/%m/%d", timeArray)
           return dd

        yield {
            'url' : response.url,
            'title' : extract_with_xpath_idx("//section[@class='heading']/h1/text()", 1),
            'author' : extract_with_xpath("//span[@class='authors-list']/span[@class='followable']/a/text()"),
            'date' : extract_date(),
            'content'  : extract_with_xpath("//div[@class='article_content']")
        }
