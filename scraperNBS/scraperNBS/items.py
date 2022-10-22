# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapernbsItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()
    date = scrapy.Field()
    links = scrapy.Field()
    labels = scrapy.Field()
    url = scrapy.Field()