# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
  name = 'gdp_debt'
  allowed_domains = ['www.worldpopulationreview.com']
  start_urls = ['https://www.worldpopulationreview.com/countries/countries-by-national-debt/']

  def parse(self, response):
    countries = response.xpath('//table[@class="datatableStyles__StyledTable-bwtkle-1 hOnuWY table table-striped"]/tbody/tr')
    for country in countries:
      name = country.xpath('.//td[1]/a/text()').get()
      debt_ratio = country.xpath('.//td[2]/text()').get()
      yield {
        'country': name,
        'debt_ratio': debt_ratio
      }
