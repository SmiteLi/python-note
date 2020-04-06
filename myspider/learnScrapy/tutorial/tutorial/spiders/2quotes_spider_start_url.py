import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    start_urls = [
        'http://quotes.toscrape.com/page/%s/' %i for i in range(10)
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)