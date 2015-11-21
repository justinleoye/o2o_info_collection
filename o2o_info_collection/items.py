# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SupplierCollectionItem(scrapy.Item):
    # define the fields for your item here like:
    contactPhone = scrapy.Field()
    distance = scrapy.Field()
    selfExpressLimit = scrapy.Field()
    delivery = scrapy.Field()
    address = scrapy.Field()
    operateEndTime = scrapy.Field()
    name = scrapy.Field()
    broadcast = scrapy.Field()
    supplierId = scrapy.Field()
    shopStatus = scrapy.Field()
    operateStartTime = scrapy.Field()
    logoImage = scrapy.Field()
    operateStatus = scrapy.Field()
    supplierName = scrapy.Field()
    dadaExpress = scrapy.Field()
    city_code = scrapy.Field()
