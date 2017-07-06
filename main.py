#!/usr/bin/python3

# Main.py
# 
# Main driver that runs the program
# @author Jay Syko

import numpy as np
import pandas as pd
from data_store import DataStore
from sklearn import preprocessing, model_selection, neighbors

def main():
	print(" \n NHL Player Predictions\n", "="*23)
	print("Legend:", "LW = Left Wing,", "RW = Right Wing,", "C = Center,", "D = Defenseman")
	db_data = DataStore()
	df = db_data.fetch_all()
	df.drop(['id'], 1, inplace=True)
	df.drop(['team'], 1, inplace=True)

	play_sample = df.sample(7)
	df.drop(['name'], 1, inplace=True)
	df.drop(play_sample.index)

	X = np.array(df.drop(['position'], 1))
	y = np.array(df['position'])
	X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

	clf = neighbors.KNeighborsClassifier()
	clf.fit(X_train, y_train)

	accuracy = clf.score(X_test, y_test)
	print("Number of Data Points:", len(df.index), "\n")
	print("\nPredicted with Accuracy: ", accuracy * 100, "%\n")

	# Prediction Test
	names = np.array(play_sample['name'])
	positions = np.array(play_sample['position'])
	players = dict(zip(names, positions))

	play_sample.drop(['name'], 1, inplace=True)
	play_sample.drop(['position'], 1, inplace=True)

	X_play = np.array(play_sample)
	predictions = clf.predict(X_play)

	outcome = []
	for i in range(len(predictions)):
		if predictions[i] == positions[i]:
			outcome.append("PASS")
		else:
			outcome.append("FAIL")

	output = pd.DataFrame(data=np.column_stack((predictions, positions, outcome)), index=names, columns=["Predicted", "Actual", "Outcome"])
	
	print(output)

if __name__ == "__main__":
	main()