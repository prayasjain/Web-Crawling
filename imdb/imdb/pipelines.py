# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo

class MongoDbPipeline(object):
    collection_name = "best_movies"

    #@classmethod
    #def from_crawler(cls, crawler):
    #    pass

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://prayas:<password>@cluster0-jy27y.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]
    
    def close_spider(self, spider):
        self.client.close()


    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        logging.info("here")
        return item
