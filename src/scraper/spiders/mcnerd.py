import scrapy


class McnerdSpider(scrapy.Spider):
    name = 'mcnerd'
    allowed_domains = ['mcnerd.shop']

    def start_requests(self):
        url = "https://mcnerd.shop/Warhammer-40000"
        response = scrapy.Request(url, callback=self.parse)
        self.links = response.css("div.caption a::attr(href)").getall()
        yield response

    def parse(self, response):
        for link in self.links:
            yield response.follow()

        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
