#!/usr/bin/python3

import pandas as pd
from scrapy import Spider
from player import Player

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
	start_urls = [DATASET[key] for key in DATASET]

	def parse(self, response):
		rows = response.xpath("//table[3]/tr[starts-with(@class, 'ysprow')]")
		for row in rows:
			plyer = Player()
			plyer["player_name"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][1]/a/text()")[0].extract()
			plyer["team"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores']/a/text()")[1].extract()
			plyer["position"] = current_position
			plyer["games_played"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][5]/text()").extract()
			plyer["goals"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][7]/text()").extract()
			plyer["assists"] = titles["player" + str(i)] = row.xpath("td[@class='ysptblclbg6']/span/text()").extract()
			plyer["points"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][10]/text()").extract()
			plyer["plus_minus"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][12]/text()").extract()
			plyer["pim"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][14]/text()").extract()
			plyer["hits"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][16]/text()").extract()
			plyer["bks"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][18]/text()").extract()
			plyer["fw"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][20]/text()").extract()
			plyer["fl"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][22]/text()").extract()
			plyer["fop"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][24]/text()").extract()
			plyer["ppg"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][26]/text()").extract()
			plyer["shg"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][28]/text()").extract()
			plyer["sha"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][30]/text()").extract()
			plyer["gw"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][32]/text()").extract()
			plyer["sog"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][34]/text()").extract()
			plyer["pct"] = titles["player" + str(i)] = row.xpath("td[@class='yspscores'][36]/text()").extract()
			yield plyer

def scrape():
	x = NHLScraper()

if __name__ == "__main__":
	scrape()