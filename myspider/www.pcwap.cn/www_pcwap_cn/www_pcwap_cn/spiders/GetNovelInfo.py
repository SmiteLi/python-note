import scrapy, os, pymongo, urllib, datetime

class SiteIndexGetAllNovel(scrapy.Spider):
    name = "GetNovelInfo"
    
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
    novel_info = db.novel_info

    def parse(self, response):
        key = response.css('meta::attr(property)').getall()
        value = response.css('meta::attr(content)').getall()
        value.pop(0)
        value.pop(0)
        d_novel_info = dict(zip(key, value))
        print(d_novel_info)
        self.novel_info.insert_one(d_novel_info)
        

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