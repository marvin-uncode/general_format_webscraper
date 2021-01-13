from webscraper_1 import rank_items
import scrapy


class RanktribeSpider(scrapy.Spider):
    name = 'ranktribe'
    start_urls = ['https://www.ranktribe.com/alabama']

    def parse(self, response):
        items = rank_items.Webscraper1Item()

        phone_number = response.css('.summary-phone').extract()
        items['phone_number'] = phone_number
        print(phone_number)

        yield items
