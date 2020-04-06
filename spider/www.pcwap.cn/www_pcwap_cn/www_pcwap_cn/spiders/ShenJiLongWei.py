import scrapy, os, pymongo, urllib, datetime

class ShenJiLongWeiSpider(scrapy.Spider):
    name = "ShenJiLongWei"
    start_urls = [
        'https://www.pcwap.cn/show/7570238.html',
    ]

    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('ADMIN123.com')
    print('mongodb://%s:%s@55.qiweioa.cn:8089/?authSource=admin' % (username, password))
    client = pymongo.MongoClient('mongodb://%s:%s@55.qiweioa.cn:8089/?authSource=admin' % (username, password))
    db = client.ShenJiLongWei
    chapters = db.chapters

    def parse(self, response):
        chapter = {
                'chapter_name': response.css('#title_show::text').get(),
                'chapter_content': response.css('div #content_show::text').getall(),
                'url': response.url,
                "date": datetime.datetime.utcnow(),
            }

        self.chapters.insert_one(chapter)

        print(chapter)
 
        next_page = response.css('div.am-btn-group a::attr(href)').getall()[-1]
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


        

        # filename = './ShenJiLongWei/ShenJiLongWei-%s.html' % page

        # if not os.path.exists(os.path.split(filename)[0]):
        #     os.makedirs(os.path.split(filename)[0])

        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)