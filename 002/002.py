import scrapy

# This code extract quotes from http://quotes.toscrape.com/
# You can run the spider using following command
# scrapy runspider filename.py -o filename.json

class QuotesCrawler(scrapy.Spider):
    name = 'quote_crawler'
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self, response):
        quotes = response.css('div.quote')
        for quote_box in quotes:
            yield {
                    'text': quote_box.css('span.text::text').get(),
                    'author': quote_box.css('span small.author::text').get(),
                    'tags': quote_box.css('div.tags a::text').getall()
                    }

        next_page = response.css('nav ul li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
