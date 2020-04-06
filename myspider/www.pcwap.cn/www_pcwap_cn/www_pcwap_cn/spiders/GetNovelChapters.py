import scrapy, os, pymongo, urllib, datetime

class SiteIndexGetAllNovel(scrapy.Spider):
    name = "GetNovelChapters"
    
    # start_urls = [
    #     'https://www.pcwap.cn/novel/114974.html',
    # ]
    # scrapy shell 'https://www.pcwap.cn/'
    username = urllib.parse.quote_plus('admin')
    password = urllib.parse.quote_plus('ADMIN123.com')
    client = pymongo.MongoClient('mongodb://%s:%s@55.qiweioa.cn:8089/?authSource=admin' % (username, password))
    db = client.www_pcwap_cn
    novel_list = db.novel_list.find_one()['1']
    start_urls = novel_list
    novel_chapters = db.novel_chapters

    def parse(self, response):
        first_chapter = response.css('ul.am-list a::attr(href)').get()
        yield scrapy.Request(first_chapter, callback=self.deal_chapters)

    def deal_chapters(self, response):
        chapter = {
            'chapter_name': response.css('#title_show::text').get(),
            'chapter_content': response.css('div #content_show::text').getall(),
            'url': response.url,
            "date": datetime.datetime.utcnow(),
        }
        self.novel_chapters.insert_one(chapter)      
        next_page = response.css('div.am-btn-group a::attr(href)').getall()[-1]
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback=self.deal_chapters)



        
        

        # novel_list = response.css('span.am-u-sm-8 a::attr(href)').getall()

        # for novel in response.css('span.am-u-sm-8'):
        #     print(novel)
        #     novel_list = novel.css('a::attr(href)').get()
        #     print(novel_list)
        # for novel in response.css('div.am-u-sm-12 *'):
        #     print(novel)
        #     novel_list = novel.css('a::attr(href)').getall()
        #     print(list(set(novel_list)))
        

 
        # next_page = response.css('div.am-btn-group a::attr(href)').getall()[-1]
        # print(next_page)
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)