# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



from .models.mongo_db import (TeamRating, AVGSimulatedSeason, 
	EndSeasonProbabilities, ClubSoccerPredictions)


class Scrapy538Pipeline:
	def process_item(self, item, spider):
		

		team_rating = TeamRating(
			
			spi = item['spi'],
			offense = item['offense'],
			defense = item['defense']
		)


		avg_season = AVGSimulatedSeason(
			
			pts = item['pts'],
			goal_diff = item['goal_diff']
		)


		end_season = EndSeasonProbabilities(

			win_league = item['win_league'],
			qualify_ucl = item['qualify_ucl']
		)

		club_soccer = ClubSoccerPredictions(

			league_name = item['league_name'],
			league_date = item['league_date'],

			timestamp = item['timestamp'],
			league_country = item['league_country'],

			team_name = item['team_name'],
			team_pts =  item['team_points'],

			team_rating = team_rating,
			avg_simulated_season = avg_season,
			end_season_probabilities = end_season

		)

		club_soccer.save()
		return item
