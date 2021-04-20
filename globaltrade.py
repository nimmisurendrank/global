import scrapy
from scrapy.http import Request
from scrapy.spiders import Spider
from t.items import GlobaltradeItem
from scrapy.loader import ItemLoader
class globaltradeSpider(scrapy.Spider):
	name = 'globaltrade'
	allowed_domains = ['globaltrade.net']


	def Start_requests(self):
		start_urls = "https://www.globaltrade.net/expert-service-provider.html"
		headers={
			'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Gecko/20100101 Firefox66.0'
			#'authority' : 'www.globaltrade.net'
			#'method' : 'GET'	
			#'scheme' : 'http'
			#'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
			#'accept-encoding' : 'gzip, deflate, br'
			#'accept-language' : 'en-US,en;q=0.5'
			#'cache-control' : 'max-age=0'
			}
		yield Request(start_urls,headers=headers,callback=self.parse)
	def parse(self,response):
		for url in response.xpath("//p[@class='sp-name']/a/@href").extract():
			headers={
			'User-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64) Gecko/20100101 Firefox66.0'
			#'authority' : 'www.globaltrade.net'
			#'method' : 'GET'	
			#'scheme' : 'http'
			#'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
			#'accept-encoding' : 'gzip, deflate, br'
			#'accept-language' : 'en-US,en;q=0.5'
			#'cache-control' : 'max-age=0'
			}
		yield Request(response.urljoin(url),callback=self.parse_result,heades=headers)
	def parse_result(self,response):
		yield GlobaltradeItem(
		logo_url=response.xpath("//div[@class='image']/img/@original").extract(),
		title=response.xpath("//h1[@class='sp-title']/span/text()").extract(),
		sub_title=response.xpath("//span[@class='sub']/text()").extract(),
		primary_location=response.xpath("//span[@itemprop='addressLocality']/text()").extract(),
		area_of_expertise=response.xpath("//a[@class='mainExp']/text()").extract(),
		about=response.xpath("//h3[@class='section-title']/table/tbody/tr/td/p/text()").extract(),
		)
		next_page= response.xpath("//div[@class='nav-page']/a/@href").extract()
		if next_page is not None:
			
			yield scrapy.Request(response.urljoin(next_page), callback=self.parse)





			
