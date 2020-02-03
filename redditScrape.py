#import libraries
import scrapy

class QuoteSpider(scrapy.Spider):
    name = "reddit_user"
    allowed_domains = ["reddit.com"]
    start_urls = ['https://www.reddit.com/user/sharpShootr']
    

    def parse(self, response):
        self.log('I just visited: '+ response.url)
        for comment in response.css('div.quote'):
            item = {
                'sub_reddit': comment.css('a._2mHuuvyV9doV3zwbZPtIPG::text').extract_first(),
                'comment': comment.css('p._1qeIAgB0cPwnLhDF9XSiJM::text').extract_first(),
            } 
            yield item
