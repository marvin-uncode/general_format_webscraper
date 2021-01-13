# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Webscraper1Item(scrapy.Item):
    phone_number = scrapy.Field()
    pass