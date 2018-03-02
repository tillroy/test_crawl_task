# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from test_spider.db_client import Connector


class SpiderPipeline(object):
    def open_spider(self, spider):
        self.conn = Connector()

    def process_item(self, item, spider):
        value = item.get("value")
        corr_id = item.get("corr_id")

        self.conn.write_record(corr_id, value)

        return item
