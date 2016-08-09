#http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html

import pandas as pd, numpy as np
from sklearn.feature_selection import SelectKBest,f_classif

df = pd.DataFrame()
# csv containing all feature values
df = pd.read_csv('str_mfcc_and_gfcc_and_pitch_gender.csv').iloc[:,1:]

X = np.array(df.iloc[:,:-1])
y = np.ravel(df.iloc[:,-1:])

############ 15 Best selected features using ANOVA F-value score function ###############

X_new = SelectKBest(f_classif, k=15).fit_transform(X, y)
selected_features = SelectKBest(f_classif, k=15).fit(X, y).get_support(indices = True)

