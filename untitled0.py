# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:46:51 2019

@author: sridhar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading the Data

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#Feature Scaling in Pythom

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(-1,1))

#Fitting the Data Set to SVR

from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X, y)

#Fit and Ploting the Graph

y_pred = regressor.predict([[6.5]])
y_pred = sc_y.inverse_transform(y_pred)

#Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualising the SVR results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01) # choice of 0.01 instead of 0.1 step because the data is feature scaled
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


