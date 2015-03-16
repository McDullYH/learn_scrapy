# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from iaviva.items import IavivaItem
from urlparse import urlparse

class IavivaPipeline(object):
    def __init__(self):
        pass
    def process_item(self, item, spider):
        #print item['url']
        up=urlparse(item['url'])
        #print up.path.split('/')[-1]
        r=requests.get(item['url'])
        with open("/home/mcdull/image/iaviva/"+up.path.split('/')[-1],'w') as f:
            f.write(r.content)
        return item
    def close_spider(self,spider):
        pass
