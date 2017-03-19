# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class W3CItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tutorial_category = scrapy.Field()
    tutorial_category_position = scrapy.Field()

    #教程介绍页面
    tutorial_slug = scrapy.Field()
    tutorial_name = scrapy.Field()
    tutorial_description = scrapy.Field()
    tutorial_img_path = scrapy.Field()
    tutorial_content = scrapy.Field()
    tutorial_position = scrapy.Field()

    tutorial_doc = scrapy.Field()


    # 教程文章页面
    tutorial_doc_menu_name = scrapy.Field()
    tutorial_doc_menu_position = scrapy.Field()
    tutorial_doc_menu_slug = scrapy.Field()

    # 教程文章列表
    tutorial_doc_slug = scrapy.Field()
    tutorial_doc_name = scrapy.Field()
    tutorial_doc_is_menu = scrapy.Field()
    tutorial_doc_menu_position = scrapy.Field()
    tutorial_doc_content = scrapy.Field()