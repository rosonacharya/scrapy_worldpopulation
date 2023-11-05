import scrapy
from pathlib import Path
class ScrpSpider(scrapy.Spider):
    name = "scrp"
    start_urls = [
         "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    ]

    def parse(self, response):
        for book in response.css("div.product_pod"):
            yield {
                "text": book.css("h3> a::attr(title)").extract_first(),
                "price": book.css(".price_color::text").get(),
               # "tags": quote.css("div.tags a.tag::text").getall(),
            }
        #page = response.url.split("/")[-2]
        #filename = f"quotes-{page}.html"
        #Path(filename).write_bytes(response.body)
        #self.log(f"Saved file {filename}")