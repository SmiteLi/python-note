import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes4"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # Note that response.follow just returns a Request instance; you still have to yield this Request.
            yield response.follow(next_page, callback=self.parse)

# https://docs.scrapy.org/en/latest/intro/tutorial.html#following-links
# for href in response.css('ul.pager a::attr(href)'):
#     yield response.follow(href, callback=self.parse)

# for a in response.css('ul.pager a'):
#     yield response.follow(a, callback=self.parse)

# anchors = response.css('ul.pager a')
# yield from response.follow_all(anchors, callback=self.parse)

# yield from response.follow_all(css='ul.pager a', callback=self.parse)