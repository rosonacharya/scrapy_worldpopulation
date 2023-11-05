import scrapy
from pathlib import Path
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
        "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    ]

    def parse(self, response):
        for quote in response.css(".product_pod"):
            yield {
                "text": quote.css("h3 > a::text").get(),
                "price": quote.css(".price_color::text").get(),
                "rating": quote.css(".star-rating").attrib["class"].split(" ")[1]
            }