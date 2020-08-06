# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Selector
from scrapy.selector import Selector
from DZspider import items
# from ..items import DzspiderItem


class DzdpSpider1Spider(scrapy.Spider):
    name = 'dzdp_spider1'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/jiazhuang/shop/ajax/designreviewlist?_nr_force=1594719433708&act=getreviewlist&shopid=H105G4DfcfUPizLC&tab=all&order=&page=1']
    comment_id = 0
    # start_urls = ['http://www.dianping.com/shop/H105G4DfcfUPizLC/review_all/p3']
    def parse(self, response):
        # print(response.body)
        data = json.loads(response.body)
        # with open('a.html', 'wb') as f:
        #     f.write(response.body)
        # print(data)
        searches = Selector(text=data['msg']).xpath('//div[@class="comment-list"]/ul/li')
        for search in searches:
            # print(search)
            item = items.DzspiderItem()
            comments = search.xpath('.//div[@class="comment-rst"]/span/text()').extract()
            construction = comments[0].split('：')[-1]
            service = comments[1].split('：')[-1]
            design = comments[2].split('：')[-1]
            item['username'] = search.xpath('.//div[@class="user-name"]/p/a/text()').extract_first()
            item['construction'] = construction
            item['service'] = service
            item['design'] = design
            content = search.xpath('.//div[@class="desc J_brief-cont"]/text()').extract()[0]
            item['content'] = content.strip() + ";"
            item['style'] = search.xpath('.//ul[@class="cmt-order-info"]/li/text()').extract()[0]
            item['area'] = search.xpath('.//ul[@class="cmt-order-info"]/li/text()').extract()[1]
            item['cost'] = search.xpath('.//ul[@class="cmt-order-info"]/li/text()').extract()[2]
            item['designer'] = search.xpath('.//ul[@class="cmt-order-info"]/li/text()').extract()[3]
            item['leader'] = search.xpath('.//ul[@class="cmt-order-info"]/li/text()').extract()[4]
            item['contract'] = search.xpath('.//ul[@class="cmt-order-info"]/li/text()').extract()[5]
            imgURLs = search.xpath('.//div[@class="shop-photo"]//ul//a/img/@src').extract()
            item['imgURLs'] = ';\n'.join(imgURLs)
            item['time'] = search.xpath('.//div[@class="misc-info"]/span/text()').extract_first().replace(u'\xa0', u' ')
            # print('^' * 30,  item['imgURLs'])
            yield item

        pageNum = 3
        for page in range(2, pageNum):
            url = 'http://www.dianping.com/jiazhuang/shop/ajax/designreviewlist?_nr_force=1594719433708&act=getreviewlist&shopid=H105G4DfcfUPizLC&tab=all&order=&page={}'.format(page)
            yield scrapy.Request(url, callback=self.parse)






        '''
        r = response.xpath('//div[@class="review-words"]/text()').extract()
        print('&'*30, r)

        # print('*' * 30)
        data = json.loads(response.body)
        # with open('dadp.html',  'wb') as f:
        #     f.write(data['msg'].encode())
      
        results = Selector(text=data['msg']).xpath("//div[@class='comment-list']/ul/li")
        print(len(results))
        for result in results:
            name = result.xpath('.//p[@class="name"]//text()').extract()
            name = ''.join(name).strip().replace('\n', ';').replace('\r', ';')

            score = result.xpath('.//div[@class="comment-rst"]//text()').extract()
            score = ''.join(score).strip().replace('\n', ';').replace('\r', ';')

            content =  result.xpath('.//div[@class="comment-txt"]//text()').extract()
            content = ''.join(content).strip().replace('\n', ';').replace('\r', ';')

            order_info = result.xpath('.//ul[@class="cmt-order-info"]//text()').extract()
            order_info = ''.join(order_info).strip().replace('\n', ';').replace('\r', ';')

            date = result.xpath('.//span[@class="time"]/text()').get()
            
            '''

