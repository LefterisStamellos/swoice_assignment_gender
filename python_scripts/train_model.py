####### reads csv with extracted features, does feature selection
#### (k=15 Best using ANOVA F-value score function) #########
### trains and dumps model into pkl 
# classification algorithm: k = 1 NN, manhattan distance

import os
import numpy as np

#http://pandas.pydata.org/
import pandas as pd

#http://scikit-learn.org/
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.cross_validation import cross_val_score
from sklearn.externals import joblib
from sklearn.feature_selection import SelectKBest,f_classif

def train_model(feats_csv):

	df = pd.DataFrame()
	df = pd.read_csv(feats_csv).iloc[:,1:]

	y = np.ravel(df.iloc[:,-1:])
	X = np.array(df.iloc[:,:-1])

	############ 15 Best selected features using ANOVA F-value score function ###############
	X_new = SelectKBest(f_classif, k=15).fit_transform(X, y)
	selected_features = SelectKBest(f_classif, k=15).fit(X, y).get_support(indices = True)

	############ KNN manhattan ###############
	##### preprocessing: data scaling######## 
	min_max_scaler = MinMaxScaler()
	X_new = min_max_scaler.fit_transform(X_new)

	model = KNeighborsClassifier(n_neighbors = 1,algorithm = 'brute',metric = 'manhattan',weights = 'uniform')
	model.fit(X_new,y)

	newdir = '../kNN_clfr'
	os.mkdir(newdir)

	joblib.dump(model, os.path.join(newdir,'kNN.pkl')) 

	return