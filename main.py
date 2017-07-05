#!/usr/bin/python3

# Main.py
# 
# Main driver that runs the program
# @author Jay Syko
# 

import numpy as np
from data_store import DataStore
from sklearn import preprocessing, model_selection, neighbors

def main():

	db_data = DataStore()

	df = db_data.fetch_all()
	df.drop(['id'], 1, inplace=True)
	df.drop(['name'], 1, inplace=True)
	df.drop(['team'], 1, inplace=True)
	db_data.close()

	X = np.array(df.drop(['position'], 1))
	y = np.array(df['position'])
	X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3)

	clf = neighbors.KNeighborsClassifier()
	clf.fit(X_train, y_train)

	accuracy = clf.score(X_test, y_test)
	print("Accuracy: ", accuracy * 100, "%")

	# Prediction Test
	
	# Predict Auston Matthews
	eg = np.array([82, 40, 29, 69, 2, 14, 21, 61, 530, 602, 0.468, 8, 13, 0, 0, 8, 279, 0.143])
	eg = eg.reshape(1, -1)

	prediction = clf.predict(eg)[0]

	if prediction == 'C':
		print("Prediction:", "Center")
	elif prediction == 'LW':
		print("Prediction:", "Left Wing")
	elif prediction == 'RW':
		print("Prediction:", "Right Wing")
	else:
		print("Prediction:", "Defenseman")

if __name__ == "__main__":
	main()