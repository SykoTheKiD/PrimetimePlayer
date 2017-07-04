#!/usr/bin/python3

from data_store import DataStore

db_data = DataStore()

df = db_data.fetch_all()
df.drop(['id'], 1, inplace=True)
df.drop(['name'], 1, inplace=True)
df.drop(['team'], 1, inplace=True)
print(df)

db_data.close()