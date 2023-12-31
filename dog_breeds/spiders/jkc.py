import scrapy
from scrapy.linkextractors import LinkExtractor



class JkcSpider(scrapy.Spider):
    name = "jkc"
    allowed_domains = ["www.jkc.or.jp"]
    start_urls = ["https://www.jkc.or.jp/archives/enrollment"]

    def parse(self, response):
        le = LinkExtractor(
            allow_domains=self.allowed_domains,
            restrict_css=[
                'section#main div.anchor_link2 ul li a'
            ]
        )
        for link in le.extract_links(response):
            print(response)

    def close(self, reason):
        start_time = self.crawler.stats.get_value('start_time')
        finish_time = self.crawler.stats.get_value('finish_time')
        print('\n\n\tTotal run time: ', finish_time - start_time)