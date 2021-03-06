#!/usr/bin/python3

import sqlite3
import pandas as pd

DB_FILE = "player_stats.sqlite"
TABLE_NAME = "stats"

class DataStore:
	def __init__(self, reset=False):
		self.conn = sqlite3.connect(DB_FILE)
		self.c = self.conn.cursor()
		# Delete old records
		if reset:
			self.c.execute("DROP TABLE IF EXISTS stats;")
			self.c.execute("CREATE TABLE {tbl} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, team TEXT NOT NULL, games_played INTEGER, position TEXT, goals INTEGER, assists INTEGER, points INTEGER, plus_minus INTEGER, pim INTEGER, hits INTEGER, bks INTEGER, fw INTEGER, fl INTEGER, fop DECIMAL, ppg INTEGER, ppa INTEGER, shg INTEGER, sha INTEGER, gw INTEGER, sog INTEGER, pct DECIMAL);".format(tbl=TABLE_NAME))
			self.conn.commit()	

	def save_value(self, item):
		if '\'' in item["name"]:
			item["name"] = item["name"].replace('\'', "")

		for key in item:
			if item[key] == 'N/A':
				item[key] = -99999
			
		self.c.execute("INSERT INTO {tbl} (name, team, games_played, position, goals, assists, points, plus_minus, pim, hits, bks, fw, fl, fop, ppg, ppa, shg, sha, gw, sog, pct ) VALUES ( '{name}', '{team}', '{games_played}', '{position}', '{goals}', '{assists}', '{points}', '{plus_minus}', '{pim}', '{hits}', '{bks}', '{fw}', '{fl}', '{fop}', '{ppg}', '{ppa}', '{shg}', '{sha}', '{gw}', '{sog}', '{pct}' );".format(tbl=TABLE_NAME, name=str(item["name"]), team=item["team"], games_played=int(item["games_played"]), position=item["position"], goals=int(item["goals"]), assists=int(item["assists"]), points=int(item["points"]), plus_minus=int(item["plus_minus"]), pim=int(item["pim"]), hits=int(item["hits"]), bks=int(item["bks"]), fw=int(item["fw"]), fl=int(item["fl"]), fop=float(item["fop"]), ppg=int(item["ppg"]), ppa=int(item["ppa"]), shg=int(item["shg"]), sha=int(item["sha"]), gw=int(item["gw"]), sog=int(item["sog"]), pct=float(item["pct"])))
		self.conn.commit()

	def fetch_all(self):
		query = "SELECT * FROM {tbl}".format(tbl=TABLE_NAME)
		df = pd.read_sql_query(query, self.conn)
		return df
		
	def close(self):
		self.conn.close()