# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_excel(r'C:\Users\leicheng\Dropbox\Career\Self learning\Udemy\Machine Learning A-Z-Udemy\Machine Learning A-Z (Codes and Datasets)\Part 2 - Regression\Section 5 - Multiple Linear Regression\Python\50_Startups.xlsx')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)

# Encoding categorical data
# Edit location using onehotencoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough') # [3] is the location of column 3
X = np.array(ct.fit_transform(X))
print(X)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Training the Multiple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_hat = regressor.predict(X_test)
np.set_printoptions(precision = 2)
print(np.concatenate((y_hat.reshape(len(y_hat),1),y_test.reshape(len(y_test),1)),1))
