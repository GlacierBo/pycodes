# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# pip3 install Mysqlclient
# ln -s /usr/local/mysql/bin/mysql_config /usr/local/bin/mysql_config
# 参考 https://www.jianshu.com/p/6411c14ce3f1

# scrapy crawl doubanSpider
# 运行爬虫的时候可能 MySQLdb 遇到个坑
# ImportError: dlopen(/Users/xxx/.local/share/virtualenvs/MyDjango-c9TXLMy3/lib/python3.6/site-packages/MySQLdb/_mysql.cpython-36m-darwin.so, 2): Library not loaded: libcrypto.1.0.0.dylib
# 参考这里 https://www.cnblogs.com/Peter2014/p/10937563.html
import MySQLdb

class DoubanPipeline:
    def __init__(self):
        self.conn = MySQLdb.connect('localhost', 'root', '123456', 'python_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 写文件
        # with open('text.txt', 'a') as f:
        #     f.write(item['id'] +","+item['rate']+","+item['title']+","+item['url'] + "\n")
        #     f.close()
        # return item

        # 入库
        insert_sql = "insert into douban(movie_id, title, rate, url)VALUES (%s, %s, %s, %s)"
        self.cursor.execute(insert_sql, (item['id'], item['rate'], item['title'], item['url']))
        self.conn.commit()
        print('正在插入数据...')
        return item

    def close_spider(self, spider):
        # 接收结束信号
        self.conn.close()
        print('完成数据插入...')
