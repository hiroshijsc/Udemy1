from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn
import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston

boston = load_boston()
boston_df = DataFrame(boston.data)
boston_df.columns = boston.feature_names
boston_df['Price'] = boston.target

X_multi = boston_df.drop('Price', axis=1)
X_train, X_test, Y_train, Y_test = train_test_split(X_multi, boston_df.Price)
lreg = LinearRegression()
pred_train = lreg.predict(X_train)
pred_test = lreg.predict(X_test)

train = plt.scatter(pred_train, (pred_train - Y_train), c='b', alpha=0.5)
test = plt.scatter(pred_test, (pred_test - Y_test), c='r', alpha=0.5)
plt.hlines(y=0, xmin=1.0, xmax=50)
