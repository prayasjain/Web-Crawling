# -*- coding: utf-8 -*-
import scrapy


class FlashdealsSpider(scrapy.Spider):
  name = 'flashdeals'
  allowed_domains = ['www.geekbuying.com']
  start_urls = ['https://www.geekbuying.com/deals/categorydeals']

  def parse(self, response):
    for product in response.xpath('//div[@class="flash_li"]'):
      name = product.xpath('.//a[@class="flash_li_link"]/text()').get()
      url = product.xpath('.//a[@class="flash_li_link"]/@href').get()
      price = product.xpath('.//div[@class="flash_li_price"]/span/text()').get()
      discount = product.xpath('.//div[@class="category_li_off"]/text()').get()
      
      yield {
        'product_name': name,
        'product_url': url,
        'product_price': price,
        'discount': discount
      }
    
    next_page = response.xpath('//a[@class="next"]/@href').get()
    if next_page:
      yield response.follow(url=next_page, callback=self.parse)
