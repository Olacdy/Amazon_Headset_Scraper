import scrapy


class AmazonHeadsetScrapingItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    reviews_num = scrapy.Field()
    score_review = scrapy.Field()
