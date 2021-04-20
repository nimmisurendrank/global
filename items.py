# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GlobaltradeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    logo_url = scrapy.Field()
    title = scrapy.Field()
    sub_title = scrapy.Field()
    primary_location = scrapy.Field()
    area_of_expertise = scrapy.Field()
    about = scrapy.Field()
    pass
