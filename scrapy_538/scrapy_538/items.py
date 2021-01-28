# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import numpy as np
from datetime import datetime
from scrapy.loader import ItemLoader
from itemloaders.processors import Join, MapCompose, TakeFirst


class Scrapy538Item(scrapy.Item):

	i = lambda v: int(v)
	f = lambda v: float(v)
	t = lambda v: datetime.strptime(v, 'Updated %b. %d, %Y, at %I:%M %p')

	league_name = scrapy.Field()
	league_date = scrapy.Field()
	
	timestamp = scrapy.Field(input_processor = MapCompose(t))
	league_country = scrapy.Field()
	
	team_name = scrapy.Field()
	team_points = scrapy.Field(input_processor = MapCompose(lambda v: int(v.split(' ')[0])))
	
	
	spi = scrapy.Field(input_processor = MapCompose(f))
	offense = scrapy.Field(input_processor = MapCompose(f))
	defense = scrapy.Field(input_processor = MapCompose(f))

	goal_diff = scrapy.Field(input_processor = MapCompose(i))
	pts = scrapy.Field(input_processor = MapCompose(f))

	qualify_ucl = scrapy.Field(input_processor = MapCompose(f))
	win_league = scrapy.Field(input_processor = MapCompose(f))


class Scrapy538Loader(ItemLoader):

	default_item_class = Scrapy538Item
	default_output_processor = TakeFirst()