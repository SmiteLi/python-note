# 不涉及模块导入的话，__name__的值就是” __main__“，如果当此模块被导入引用的话，那么这个模块内的__name__值就是文件的名字（不带.py），如下test_1.py：
# https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-developer-tools
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)