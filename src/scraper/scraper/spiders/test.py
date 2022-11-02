import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['https://quotes.toscrape.com/page/1/']
    def start_requests(self):

        urls = ['https://quotes.toscrape.com/page/1/']
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

