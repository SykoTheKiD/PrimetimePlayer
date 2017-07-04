#!/usr/bin/python3

from scrapy.item import Item, Field

class Player(Item):
	name = Field()
	team = Field()
	games_played = Field()
	position = Field()
	goals = Field()
	assists = Field()
	points = Field() 
	plus_minus = Field() 
	pim = Field() 
	hits = Field()
	bks = Field()
	fw = Field() 
	fl = Field()
	fop = Field()
	ppg = Field()
	ppa = Field()
	shg = Field()
	sha = Field()
	gw = Field()
	sog = Field()
	pct = Field()