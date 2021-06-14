import scrapy
from scrapy import signals
from urllib.parse import urljoin
from scrapy.selector import Selector
import sys
from ..items import AmazonHeadsetScrapingItem


class HeadsetSpider(scrapy.Spider):
    name = 'headset_spider'
    page_num = 0
    start_urls = ['https://www.amazon.com/s?k=gaming+headsets']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            self.parent = kwargs['parent']
            self.page_limit = kwargs['page_lim']
        except:
            self.page_limit = 1

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(HeadsetSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        self.parent.is_closed = True

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response, **kwargs):
        self.page_num += 1
        products = response.css('.s-latency-cf-section').extract()

        print(response.status, flush=True)

        for product in products:

            item = AmazonHeadsetScrapingItem()

            response_product = Selector(text=product)
            name = response_product.css('.a-size-medium.a-text-normal::text').extract_first()
            price = response_product.css('.sg-col-12-of-20 .a-price-whole::text').extract_first()
            price_fraction = response_product.css('.sg-col-12-of-20 .a-price-fraction::text').extract_first()
            reviews_num = response_product.css('.sg-col-12-of-20 .a-link-normal .a-size-base::text').extract_first()
            score_review = response_product.css('.sg-col-12-of-20 .aok-align-bottom > span::text').extract_first()

            item['name'] = name
            if price:
                item['price'] = price + "." + price_fraction
            if reviews_num:
                item['reviews_num'] = reviews_num
            if score_review:
                item['score_review'] = score_review

            if name:
                yield item

        next_page = response.css('.a-last a::attr(href)').extract_first()
        if next_page and self.page_num <= self.page_limit:
            url = urljoin('https://www.amazon.com', next_page)
            yield scrapy.Request(url=url, callback=self.parse)
