# -*- coding: utf-8 -*-
import scrapy
from meizi.items import MeiziItem

class MeizispiderSpider(scrapy.Spider):
    name = 'meiziSpider'
    allowed_domains = ['www.mzitu.com']
    # 循环
    start_urls = ['http://www.mzitu.com/xinggan/page/' + str(x) for x in range(1, 172, 1)]

    def parse(self, response):
        urls = response.xpath("//ul[@id='pins']/li/a/@href").extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.mei_zi_urls)

    def mei_zi_urls(self, response):
        # 最后一个页面
        last_url = response.xpath("//div[@class='pagenavi']/a/@href").extract()[-2]
        # 根据最后一个页面拼接 需要爬取的链接
        last_num = last_url.split('/')[-1]
        mei_zi_num = str(last_url.split('/')[-2])
        # print(last_url, ' , 最后一页页码：', last_num, ' , 妹子ID:', mei_zi_num)
        for pageNum in range(1, int(last_num), 1):
            yield scrapy.Request('https://www.mzitu.com/' + mei_zi_num + '/' + str(pageNum), callback=self.mei_zi_image)

    def mei_zi_image(self, response):
        item = MeiziItem()
        image_url = response.xpath("//div[@class='main-image']/p/a/img/@src").extract()
        item['image_urls'] = image_url
        referer = response.url
        item['referer'] = response.url
        print(image_url, referer)
        yield item
