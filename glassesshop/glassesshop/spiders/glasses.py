# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
  name = 'glasses'
  allowed_domains = ['www.glassesshop.com']
  start_urls = ['http://www.glassesshop.com/bestsellers']

  def parse(self, response):
    for glass in response.xpath('//div[@class="col-sm-6 col-md-4 m-p-product"]'):
      product_name = glass.xpath('.//div[@class="row"]/p[@class="pname col-sm-12"]/a/text()').get()
      product_url = glass.xpath('.//div[@class="row"]/p[@class="pname col-sm-12"]/a/@href').get()
      product_price = glass.xpath('.//div[@class="row"]/div[@class="pprice col-sm-12"]/span/text()').get()
      image_url = glass.xpath('.//div[@class="pimg default-image-front"]/a/img/@src').get()

      if product_name:
        yield {
          'glass_name': product_name,
          'glass_url': product_url,
          'glass_price': product_price,
          'glass_image_url': image_url
        }
    
    next_page = response.xpath('//a[@class="page-link" and @rel="next"]/@href').get()
    
    if next_page:
      yield scrapy.Request(url=next_page, callback=self.parse)