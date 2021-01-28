from mongoengine import connect

from mongoengine import Document, EmbeddedDocument
from mongoengine import (StringField, IntField, DecimalField, 
	DateTimeField, EmbeddedDocumentField)

connect('db_538', host='mongodb://localhost/db_538')


class TeamRating(EmbeddedDocument):

	# soccer power index
	spi = DecimalField()

	offense = DecimalField()
	defense = DecimalField()


class AVGSimulatedSeason(EmbeddedDocument):

	pts = IntField()
	goal_diff = IntField()


class EndSeasonProbabilities(EmbeddedDocument):

	win_league = DecimalField()
	qualify_ucl = DecimalField()


class ClubSoccerPredictions(Document):

	league_name = StringField()
	league_date = StringField()

	timestamp = DateTimeField()
	league_country = StringField()

	team_pts = IntField()
	team_name = StringField()

	team_rating = EmbeddedDocumentField(TeamRating)
	avg_simulated_season = EmbeddedDocumentField(AVGSimulatedSeason)
	end_season_probabilities = EmbeddedDocumentField(EndSeasonProbabilities)

	meta = {
        'collection': 'club_soccer_predictions'  # 指定数据表
    }