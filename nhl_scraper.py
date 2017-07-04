#!/usr/bin/python3

import pandas as pd
from scrapy import Spider
from player import Player
from urllib.parse import urlparse
from urllib.parse import parse_qs

CENTER = "center"
LEFT_WING = "left_wing"
RIGHT_WING = "right_wing"
DEFENSEMAN = "defenseman"

DATASET = {
	CENTER : "https://ca.sports.yahoo.com/nhl/stats/byposition?pos=C&conference=NHL&year=season_2016&qualified=1",
	LEFT_WING : "https://ca.sports.yahoo.com/nhl/stats/byposition?pos=LW&conference=NHL&year=season_2016&qualified=1",
	RIGHT_WING : "https://ca.sports.yahoo.com/nhl/stats/byposition?pos=RW&conference=NHL&year=season_2016&qualified=1",
	DEFENSEMAN : "https://ca.sports.yahoo.com/nhl/stats/byposition?pos=D&conference=NHL&year=season_2016&qualified=1"
}

class NHLScraper(Spider):
	name = "stats"
	start_urls = [DATASET[CENTER]]

	def parse(self, response):
		rows = response.xpath("//table[3]/tr[starts-with(@class, 'ysprow')]")
		parsed_url = urlparse(response.url)
		parsed_query = parse_qs(parsed_url.query)
		current_position = parsed_query['pos'][0]
		for row in rows:
			current_player = Player()
			current_player["name"] = row.xpath("td[@class='yspscores'][1]/a/text()")[0].extract()
			current_player["team"] = row.xpath("td[@class='yspscores']/a/text()")[1].extract()
			current_player["position"] = current_position
			current_player["games_played"] = row.xpath("td[@class='yspscores'][3]/text()")[0].extract()
			current_player["goals"] = row.xpath("td[@class='yspscores'][5]/text()")[0].extract()
			current_player["assists"] = row.xpath("td[@class='yspscores'][7]/text()")[0].extract()
			current_player["points"] = row.xpath("td[@class='ysptblclbg6']/span/text()")[0].extract()
			current_player["plus_minus"] = row.xpath("td[@class='yspscores'][10]/text()")[0].extract()
			current_player["pim"] = row.xpath("td[@class='yspscores'][12]/text()")[0].extract()
			current_player["hits"] = row.xpath("td[@class='yspscores'][14]/text()")[0].extract()
			current_player["bks"] = row.xpath("td[@class='yspscores'][16]/text()")[0].extract()
			current_player["fw"] = row.xpath("td[@class='yspscores'][18]/text()")[0].extract()
			current_player["fl"] = row.xpath("td[@class='yspscores'][20]/text()")[0].extract()
			current_player["fop"] = row.xpath("td[@class='yspscores'][22]/text()")[0].extract()
			current_player["ppg"] = row.xpath("td[@class='yspscores'][24]/text()")[0].extract()
			current_player["ppa"] = row.xpath("td[@class='yspscores'][26]/text()")[0].extract()
			current_player["shg"] = row.xpath("td[@class='yspscores'][28]/text()")[0].extract()
			current_player["sha"] = row.xpath("td[@class='yspscores'][30]/text()")[0].extract()
			current_player["gw"] = row.xpath("td[@class='yspscores'][32]/text()")[0].extract()
			current_player["sog"] = row.xpath("td[@class='yspscores'][34]/text()")[0].extract()
			current_player["pct"] = row.xpath("td[@class='yspscores'][36]/text()")[0].extract()
			yield current_player