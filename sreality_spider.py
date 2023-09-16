import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from dao import insert



class SrealityScrapper(scrapy.Spider):
    name = "sreality"

    def start_requests(self):
        URL = "https://ondrejbruha.com/astrofotografie-2023"
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css("img"):
            yield {
                "src": selector.css("img::attr(src)").extract_first(),
                "title": selector.css("img::attr(alt)").extract_first(),
            }
            next_page_link = response.css('img.next img::attr(src)').extract_first()
            if next_page_link:
                yield response.follow(next_page_link, callback=self.parse_parser)


def result():
    results = []

    def crawler_result(item):
        results.append(item)

    dispatcher.connect(crawler_result, signal=signals.item_scraped)
    process = CrawlerProcess()
    process.crawl(SrealityScrapper)
    process.start()
    return results


if __name__ == "__main__":
    result = result()
    for item in result:
        insert(item["src"], item["title"])
