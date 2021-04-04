import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        film_ids = [
            326,
        ]
        urls = [f'https://www.kinopoisk.ru/film/{id}/reviews/ord/rating/status/all/perpage/10/' for id in film_ids]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        film_name = response.xpath('//*/a[@class="breadcrumbs__link"]/text()').get()
        reviews = response.xpath('//*/span[@class="_reachbanner_"]/text()').getall()

        print("!!!!!!!!!!!!!! ")
        print(len(reviews))
        for review in reviews:
            item = {}
            item["film_name"] = film_name
            item["review"] = review
            yield item
