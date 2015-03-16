# -*- coding: utf-8 -*-

# Scrapy settings for iaviva project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'iaviva'

SPIDER_MODULES = ['iaviva.spiders']
NEWSPIDER_MODULE = 'iaviva.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'iaviva (+http://www.yourdomain.com)'

ITEM_PIPELINES={'iaviva.pipelines.IavivaPipeline': 1,}   
CONCURRENT_REQUESTS=128
CONCURRENT_REQUESTS_PER_DOMAIN=128
