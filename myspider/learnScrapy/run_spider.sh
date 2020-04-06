#!/bin/bash
scrapy runspider quotes_spider.py -o quotes.json

scrapy startproject tutorial
scrapy genspider example example.com

tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

To put our spider to work, go to the project’s top level directory and run:
scrapy crawl quotes
scrapy crawl quotes -o quotes.jl

scrapy shell "http://quotes.toscrape.com/page/1/"
response.css('title')
response.css('title').getall()
response.css('title::text').getall() # list
response.css('title::text').get() # the 1st element
response.css('title::text')[0].get() # the same as above

>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']

# open the websiet in browser
view(response)

# 开发者模式，找到xpath
https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-developer-tools

# we’ll simply select all span tags with the class="text" by using the has-class-extension:
response.xpath('//span[has-class("text")]/text()').getall()

response.xpath('//title')

# Following links
response.css('li.next a').get()
response.css('li.next a::attr(href)').get()
response.css('li.next a').attrib['href']

scrapy crawl quotes -o quotes-humor.json -a tag=humor