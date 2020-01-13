import scrapy
from scrapy.http import Response, Request
from scrapy_proj.items import HabrBlog
from scrapy_redis.spiders import RedisSpider

class Habr(RedisSpider):
    name = 'habr'
    #start_urls = ['https://habr.com/ru/']

    def parse_blog(self,response:Response):
        self.log(response.meta['exe'])
        blog = HabrBlog()

        blog['title'] = response.xpath('//h1/span/text()').extract_first()
        blog['url'] = str(response.url)
        blog['body'] = ''.join(response.xpath('//div[contains(@class,"post__text")]//text()').extract()).strip().replace('\n','').replace('\r','')

        return blog

    def parse(self, response: Response):
        links = response.xpath('//a[contains(@class,"post__title_link")]/@href').extract()

        for link in links:
            yield Request(link,self.parse_blog,meta={'exe':'1'})