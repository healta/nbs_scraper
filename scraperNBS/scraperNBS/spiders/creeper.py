import scrapy
from ..items import ScrapernbsItem

class CreeperSpider(scrapy.Spider):
    name = 'creeper'
    
    #I couldn't figure out how to bypass the javascript on the page
    #with just scrapy, so I used Selenium to get all the /news/ links
    #on the page, and then run them with scrapy
    with open ("/home/healta/Documents/Programming/articles.txt", "r") as f:
        links = f.readlines()

    start_urls = [i for i in links]

    def parse(self, response):
        article_text = ""

        items = ScrapernbsItem()
        
        #just using the css.selectors here, they all worked out fine
        #with some minor formatting
        title = str(response.css(".headline::text").extract())
        text = response.css("#main p::text").extract()
        date = str(response.css(".nbs-post__date::text").extract())
        labels = response.css(".label--sm::text").extract()
        links = response.css("p a::attr('href')").extract()
        url = str(response)[5:-1]

        for i in text:
            article_text+=i
        
        items["title"] = title[2:-2]
        items["text"] = article_text
        items["date"] = date[2:-2]
        items["labels"] = labels
        items["links"] = links
        items["url"] = url

        yield items