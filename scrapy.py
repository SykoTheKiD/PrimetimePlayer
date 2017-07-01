#!/usr/bin/python3

import scrapy
import pandas as pd

CENTER = "center"
DEFENSEMAN = "defenseman"
LEFT_WINGER = "left_winger"
RIGHT_WINGER = "right_winger"

DATASET = {
	LEFT_WINGER : "http://www.nhl.com/stats/player?aggregate=0&gameType=2&report=skatersummary&pos=L&reportType=season&seasonFrom=20162017&seasonTo=20162017&filter=gamesPlayed,gte,1&sort=playerPositionCode",
	RIGHT_WINGER : "http://www.nhl.com/stats/player?aggregate=0&gameType=2&report=skatersummary&pos=R&reportType=season&seasonFrom=20162017&seasonTo=20162017&filter=gamesPlayed,gte,1&sort=playerPositionCode",
	CENTER : "http://www.nhl.com/stats/player?aggregate=0&gameType=2&report=skatersummary&pos=C&reportType=season&seasonFrom=20162017&seasonTo=20162017&filter=gamesPlayed,gte,1&sort=playerPositionCode",
	DEFENSEMAN : "http://www.nhl.com/stats/player?aggregate=0&gameType=2&report=skatersummary&pos=D&reportType=season&seasonFrom=20162017&seasonTo=20162017&filter=gamesPlayed,gte,&sort=points,goals,assists"
}

class NHLScraper(scrapy.Spider):
	name = "stats"
	

def scrape():
	pass

if __name__ == "__main__":
	scrape()