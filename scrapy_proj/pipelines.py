# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


def django_imitation(list_:list):
    with open('result.txt',mode='at') as f:
        print(list_,file=f)

class ScrapyProjPipeline(object):
    def __init__(self,*args, **kwargs):
        self.items = []
        super().__init__()
    
    def process_item(self, item, spider):
        self.items.append(item.values)
        if len(self.items) >= 2:
            django_imitation(self.items)
            self.items.clear()
        return item
