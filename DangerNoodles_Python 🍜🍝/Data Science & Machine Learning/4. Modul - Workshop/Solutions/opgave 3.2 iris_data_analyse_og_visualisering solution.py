
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


data = pd.read_csv("iris.csv")

pd.set_option('display.max_columns', None)
print(data.head())
print("Basic statistics")
print(data.describe())

#boxplot to see outliers
data.boxplot(column =['sepal.width'], grid = False)

data.hist(bins=50,figsize=(20,15))

print("correlations")
corr_matrix = data.corr()
print(corr_matrix)

#scatter plot of correlations
data.plot(kind = "scatter", x = "petal.width", y = "petal.length")

#Linear regression on correlations
#Notice how to pick and transform columns
X = np.array(data["petal.width"]).reshape((-1, 1)) 
Y = data["petal.length"]

#training the model
lin_reg = LinearRegression()
lin_reg.fit(X,Y)   # train the model on the data

print("Score:" + str(lin_reg.score(X, Y)))

#using the model on new data
new_x = np.array([[0],[2.5]])
y_predict = lin_reg.predict(new_x)

print(y_predict)

#plot the new data
plt.plot(new_x,y_predict,"r")

plt.show()
