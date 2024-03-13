# -*- coding: utf-8 -*-
"""IOSC WORKSHOP 2.0 DAY-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zpEaVFHqp3OSfy5pJ80MsY05k3G3lCaP

#IMPORTING LIBRARIES
"""

import numpy as np
import pandas as pd

"""#LOADING DATASET"""

df = pd.read_csv("/content/loan_approval_dataset.csv")

"""#DATA PREPROCESSING"""

df.head()

df.info()

df.isnull().sum()

df.describe()

df.columns

df.drop(['loan_id'],axis=1,inplace=True) #Not required attribute

"""#ENCODING"""

df = pd.get_dummies(df,columns = [" education"," self_employed"])

"""#DATA VISUALISATION"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr())

"""#TRAIN TEST SPLIT"""

from sklearn.model_selection import train_test_split
X = df.drop([' loan_status'],axis=1)
y = df[' loan_status']
X.shape,y.shape

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=1)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

"""#ACCURACY CHECK"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
model = RandomForestClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("ACCURACY OF RANDOM FOREST CLASSIFIER: ",accuracy_score(y_test,y_pred))

"""#Predicting on new Data"""

df

new_X_data = np.array([2, 7200000, 25000000, 10, 480, 2000000, 10000000, 12000000, 4000000, 1, 0, 0, 1])

# Reshape the 1D array to 2D array
new_X_data = new_X_data.reshape(1, -1)

# Use the reshaped array for prediction
prediction = model.predict(new_X_data)

print("Prediction for the new data:", prediction)