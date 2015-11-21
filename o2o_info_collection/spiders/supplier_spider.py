import scrapy
import json
from werkzeug.urls import Href
from urlparse import urlparse, parse_qs

from o2o_info_collection.items import SupplierCollectionItem

# TODO: put geo hashs into a file,and read them from that file
geo_hashs = ['wtemjq1me', 'wtemkc33n', 'wtekg3qq9', 'wtekg0vcs', 'wtem5f0ts']

class SupplierCollectionSpider(scrapy.Spider):
    name = "supplier_collection"
    allowed_domains = ["pailequ.cn"]
    start_urls = [
        'https://pailequ.cn/ajax/place/%s?page=1' % (geo_hash+'0') for geo_hash in geo_hashs
    ]

    def parse(self, response):
        rep_json = json.loads(response.body)

        try:
            if int(rep_json['get_params']['page']) < int(rep_json['total_page']):
                parsed_url = urlparse(response.url)
                query_params = parse_qs(parsed_url.query)
                query_params['page'] = [int(query_params['page'][0]) + 1]
                base_url = response.url.split("?")[0]
                url = Href(base_url)(query_params)
                print 'url:',url
                yield scrapy.Request(url, callback=self.parse)
        except AttributeError,e:
            print e

        for supplier in rep_json['shop_list']:
            supplier['city_code'] = rep_json['city_code']
            yield SupplierCollectionItem(supplier)
