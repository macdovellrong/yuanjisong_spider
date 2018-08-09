# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YuanjisongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    idjob = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    cooperation = scrapy.Field()
    day_rate = scrapy.Field()
    total_rate = scrapy.Field()
    task_time = scrapy.Field()
    area1 = scrapy.Field()
    area2 = scrapy.Field()
    area3 = scrapy.Field()
    requirement = scrapy.Field()
    status = scrapy.Field()
    participants = scrapy.Field()
