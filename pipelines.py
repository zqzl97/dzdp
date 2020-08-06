# -*- coding: utf-8 -*-
from openpyxl import Workbook
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DzspiderPipeline:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['username', 'construction', 'service', 'design', 'content', 'style', 'area', 'cost', 'designer', 'leader', 'contract', 'imgURLs', 'time'])


    def process_item(self, item, spider):
        data = [item['username'], item['construction'], item['service'], item['design'], item['content'], item['style'], item['area'], item['cost'], item['designer'],  item['leader'], item['contract'], item['imgURLs'],  item['time']]
        self.ws.append(data)
        self.wb.save('dzdp.xlsx')
        return item

