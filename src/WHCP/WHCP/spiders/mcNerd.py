import scrapy
import scrapy

class McnerdSpider(scrapy.Spider):
    name = 'mcnerd'
    allowed_domains = ['mcnerd.shop']

    def start_requests(self):
        url = "https://mcnerd.shop/Warhammer-40000"
        response = scrapy.Request(url, callback=self.parse)
        
        yield response

    
    def parse(self, response):
        links = response.css("div.caption a::attr(href)").getall()

        for link in links:
            
            
            match response.url.split("/")[-1]:
                case "Regelbuecher-und-Codices":
                    pass
                case "Weitere_Sets_1":
                    pass
                case "Kampfpatrouille":
                    pass
                case "Start-Collecting_4":
                    pass
                case _:
                    pass

            
            page = "McNerd_" + response.url.split("/")[-1]
            filename = f'{page}.txt'
            with open(filename, 'w') as f:
                for item in links:
                    f.write("%s\n" % item)
            self.log(f'Saved file {filename}')