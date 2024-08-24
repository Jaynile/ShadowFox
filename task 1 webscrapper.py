import requests
from bs4 import BeautifulSoup
import scrapy
from scrapy.crawler import CrawlerProcess
def scrape_with_beautiful_soup(url):# Beautiful Soup Scraping
    
    response = requests.get(url)# Send a GET request to fetch the raw HTML content
    
    
    soup = BeautifulSoup(response.text, 'html.parser')# Parse the HTML content with BeautifulSoup
    
    titles = soup.find_all('h2')# Extract titles (or any other data)
    
   
    print("Beautiful Soup Scraping Results:")
    for title in titles:
        print(title.get_text())
beautiful_soup_url = 'https://example.com/news'  # Replace with the URL you want to scrape


scrape_with_beautiful_soup(beautiful_soup_url)# Scrape using BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

def run_scrapy_spider():
    process = CrawlerProcess(settings={
        'FEEDS': {
            'quotes.json': {
                'format': 'json',
                'overwrite': True
            },
        },
    })
    process.crawl(QuotesSpider)
    process.start()

print("\nRunning Scrapy Spider...")
run_scrapy_spider()
