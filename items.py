# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DzspiderItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    construction = scrapy.Field()
    service = scrapy.Field()
    design = scrapy.Field()
    content = scrapy.Field()
    style = scrapy.Field()
    area = scrapy.Field()
    cost = scrapy.Field()
    designer = scrapy.Field()
    leader = scrapy.Field()
    contract = scrapy.Field()
    imgURLs = scrapy.Field()
    time = scrapy.Field()





