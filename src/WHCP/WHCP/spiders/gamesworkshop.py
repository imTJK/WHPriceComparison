import scrapy


class GamesWorkshop(scrapy.Spider):
    name = 'GamesWorkshop'
    allowed_domains = ['www.games-workshop.com']
    start_urls = ['https://www.games-workshop.com/de-DE/Warhammer-40-000']

    def start_requests(self):
        urls = [
            'https://www.games-workshop.com/de-DE/Warhammer-40-000?N=3562378816+3694373482+49637768+3984380624+1320453649+1176910732+2317334297+3927560896+1915851837+2509539302+1252943013+1953378169+2160870842+1504000890&Nr=AND%28sku.siteId%3ADE_gw%2Cproduct.locale%3Ade_DE_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1667415120000+and+product.endDate+%3E%3D+1667415120000%5D&view=all',
            'https://www.games-workshop.com/de-DE/Warhammer-40-000?N=3562378816+1465328448&Nr=AND%28sku.siteId%3ADE_gw%2Cproduct.locale%3Ade_DE_gw%29&Nrs=collection%28%29%2Frecord%5Bproduct.startDate+%3C%3D+1667415180000+and+product.endDate+%3E%3D+1667415180000%5D&view=all',
            'https://www.games-workshop.com//Tervigon-der-Tyraniden',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
