import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'letterboxd'
    start_urls = ['https://letterboxd.com/andrewcult/list/im-just-a-girl-in-the-world/detail/']

    def parse(self, response):
        for filmes in response.xpath('//h2//a/text()'):
            yield{
                'filmes': response.xpath('//h2//a[contains(@href, "/film/")]/text()'),
                'ano': response.xpath('//h2//a[contains(@href, "/films/")]/text()')
            }

