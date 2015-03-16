#!/usr/bin/python
#-*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from iaviva.items import IavivaItem
import re
from scrapy.http import Request
from scrapy.selector import Selector



class IavivaSpider(CrawlSpider):
    name = "iaviva"
    allowed_domains = ["iaviva.com"]
    #start_urls=["http://www.iaviva.com/loveshow/"]
    start_urls=["http://www.iaviva.com/"]
    #rules = (Rule(SgmlLinkExtractor(allow=('/lovecase/\d+/')),  callback = 'parse_img_url', follow=True),)
    rules = (Rule(SgmlLinkExtractor(allow=('/\w+/')),  callback = 'parse_img_url', follow=True),)
    def parse_img_url(self, response):
        urlItem = IavivaItem()
        sel = Selector(response)
        #for divs in sel.xpath('//div[@class="pbsShowcase"]'):
        for div in sel.xpath('//div[@id="innerShowcase2"]'):
            img_url=div.xpath('.//a/@href').extract()[0]
            #img_url=div.xpath('.//img/@src2').extract()[0]
            urlItem['url'] = img_url
            yield urlItem
