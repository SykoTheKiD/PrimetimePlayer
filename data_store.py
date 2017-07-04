#!/usr/bin/python3

import sqlite3

DB_FILE = "player_stats.sqlite"
TABLE_NAME = "stats"

class DataStore:
	def __init__(self, reset=False):
		self.conn = sqlite3.connect(DB_FILE)
		self.c = self.conn.cursor()
		# Delete old records
		if reset:
			self.c.execute("DROP TABLE IF EXISTS stats;")
			self.c.execute("CREATE TABLE {tbl} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, team TEXT NOT NULL, games_played INTEGER, position TEXT, goals INTEGER, assists INTEGER, points INTEGER, plus_minus INTEGER, pim INTEGER, hits INTEGER, bks INTEGER, fw INTEGER, fl INTEGER, fop INTEGER, ppg INTEGER, shg INTEGER, sha INTEGER, gw INTEGER, sog INTEGER, pct DECIMAL);".format(tbl=TABLE_NAME))
			self.conn.commit()	

	def save_value(self, item):
		self.c.execute("INSERT INTO {tbl} (name, team, games_played, position, goals, assists, points, plus_minus, pim, hits, bks, fw, fl, fop, ppg, shg, sha, gw, sog, pct ) VALUES ( '{name}', '{team}', '{games_played}', '{position}', '{goals}', '{assists}', '{points}', '{plus_minus}', '{pim}', '{hits}', '{bks}', '{fw}', '{fl}', '{fop}', '{ppg}', '{shg}', '{sha}', '{gw}', '{sog}', '{pct}' );".format(tbl=TABLE_NAME, name=str(item["name"]), team=item["team"], games_played=item["games_played"], position=item["position"], goals=item["goals"], assists=item["assists"], points=item["points"], plus_minus=item["plus_minus"], pim=item["pim"], hits=item["hits"], bks=item["bks"], fw=item["fw"], fl=item["fl"], fop=item["fop"], ppg=item["ppg"], shg=item["shg"], sha=item["sha"], gw=item["gw"], sog=item["sog"], pct=item["pct"]))
		self.conn.commit()

	def get_all(self, item):
		self.c.execute("SELECT * FROM {tbl}".format(tbl=TABLE_NAME))
		return self.c.fetchall()

	def close(self):
		self.conn.close()