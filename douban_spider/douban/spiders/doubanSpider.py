# -*- coding: utf-8 -*-
import scrapy
import json
from douban.items import DoubanItem

# 运行这个爬虫
# scrapy crawl doubanSpider
class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['https://movie.douban.com/']
    start_urls = [
        "https://movie.douban.com/j/search_subjects?type=movie&tag=%E5%86%B7%E9%97%A8%E4%BD%B3%E7%89%87&sort=recommend&page_limit=20&page_start="
        + str(x) for x in range(1, 50, 1)]

    def parse(self, response):
        rs = json.loads(response.text)
        datas = rs.get("subjects")
        item = DoubanItem()
        for data in datas:
            item['title'] = data.get('title')
            item['rate'] = data.get('rate')
            item['url'] = data.get('url')
            item['id'] = data.get('id')
            yield item
