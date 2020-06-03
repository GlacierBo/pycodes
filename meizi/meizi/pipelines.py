# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class MeiziPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item["image_urls"]:
            yield scrapy.Request(image_url, headers={'User-Agent': 'Mozilla/5.0', 'referer': item['referer']})

    # 重命名的功能 重写此功能可以得到自己想要文件名称 否则就是uuid的随机字符串
    def file_path(self, request, response=None, info=None):
        # 图片名称
        img_name = request.url.split('/')[-1]
        file_name = request.url.split('/')[-2]
        # 分文件夹存储
        image_path = u'{0}/{1}'.format(file_name, img_name)
        print(image_path, '/', img_name)
        return image_path

