#!/usr/bin/python3

import data_store

class SQLitePipeline(object):

	def __init__(self):
		self.store = data_store.DataStore(True)

	def process_item(self, item, spider):
		self.store.save_value(item)
		spider.log("{name} saved to DB".format(name=item["name"]))