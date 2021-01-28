import scrapy
from ..items import Scrapy538Loader

class SoccerSpider(scrapy.Spider):

	name = 'soccer_spider'
	start_urls = [
		'https://projects.fivethirtyeight.com/soccer-predictions/premier-league/',
		'https://projects.fivethirtyeight.com/soccer-predictions/bundesliga/',
		'https://projects.fivethirtyeight.com/soccer-predictions/la-liga/',
		'https://projects.fivethirtyeight.com/soccer-predictions/serie-a/',
		'https://projects.fivethirtyeight.com/soccer-predictions/ligue-1/'
	]


	def parse(self, response):


		league_name = response.css('.leagueName::text').get()
		league_date = response.css('.leagueDate::text').get(),
		
		timestamp = response.css('.timestamp::text').get()
		league_country = response.css('.leagueCountry::text').get(),
		
		for team_row in response.xpath("//tr[@class = 'team-row']"):
			loader = Scrapy538Loader(selector = team_row)

			loader.add_value('league_name', league_name)
			loader.add_value('league_date', league_date)
			
			loader.add_value('timestamp', timestamp)
			loader.add_value('league_country', league_country)
				
			loader.add_xpath('team_name', '@data-str')
			loader.add_css('team_points', 'span.record::text')
				
			loader.add_css('spi', '.drop-6::attr(data-val)')
			loader.add_xpath('offense', "./td[@class = 'num rating offense drop-1']/@data-val")
			loader.add_xpath('defense', "./td[@class = 'num rating defense drop-1']/@data-val")

			loader.add_xpath('goal_diff', "./td[@class = 'num record goaldiff drop-2']/text()")
			loader.add_xpath('pts', "./td[@class = 'num record drop-2 border-right']/@data-val")

			loader.add_xpath('qualify_ucl', "./td[@class = 'pct'][1]/@data-val")
			loader.add_xpath('win_league',  "./td[@class = 'pct'][2]/@data-val")
			
			yield loader.load_item()
		
