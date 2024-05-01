from pathlib import Path
import scrapy as s
from scrapy_playwright.page import PageMethod

# Run virtual\Scripts\activate to activate virtual env.
# Run the command scrapy crawl screenshot to execute the Spider.
class ScreenshotsSpider(s.Spider):
    name = "screenshot"
    
    def start_requests(self):
        yield s.Request(
            url='https://quotes.toscrape.com/',
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("screenshot", path="screenshots/home.png", full_page=True),
                ],
            },
        )

    def parse(self, response):
        url = response.url
        screenshot = response.meta["playwright_page_methods"][0]
        screenshot_path = screenshot.kwargs['path']
        
        # for url in response.css('a::attr(href)').extract():
        #     # yield {'link': url}
        #     yield Request(url=url, callback=self.parse, meta={
        #         "playwright": True,
        #         "playwright_page_methods": [
        #             PageMethod("screenshot", path="example.png", full_page=True),
        #         ],
        #     },)
