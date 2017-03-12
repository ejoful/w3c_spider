# -*- coding: utf-8 -*-
import scrapy


class W3cschoolSpider(scrapy.Spider):
    name = "w3cschool"
    allowed_domains = ["w3cschool.cn"]
    start_urls = (
        'http://www.w3cschool.cn/',
    )

    def parse(self, response):
        pass
