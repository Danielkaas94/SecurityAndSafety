from matplotlib.lines import Line2D
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LogisticRegression
import numpy as np

def format_float(num):
    return np.format_float_positional(num, trim='-')

iris = load_iris()  # load iris sample dataset
print(iris)
X = iris.data[:,2:] # petal length and width, so 2D information
y = iris.target
# check how many samples we have
print("Number of samples: " +str(len(y)))
#visulize the dataset
plt.figure()
#define colors - red, green, blue
colormap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
# pplot labxel
plt.xlabel(iris.feature_names[2]) # just using feature nr 2 and 3
plt.ylabel(iris.feature_names[3])
# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=colormap,edgecolor='black', s=50)
print(iris.target_names)

lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='--') for c in colormap.colors]
plt.legend(lines, iris.target_names)

log_reg = LogisticRegression()
model = log_reg.fit(X,y)

print(X)
print('Labels: ', y)
print('Predictions: ', model.predict(X))
print('\nNumber of wrong predictions: ', ((model.predict(X) != y) == True).sum())

test = (model.predict(X) != y) == True

for i in range(len(test)):
    if(test[i] == True):
        print('\nindex', i)
        print('X: ', X[i])
        print('Label: ', y[i])
        print('Predicted: ', model.predict(X[[i]]))
        print('proba: ', model.predict_proba([X[i]]))

# Create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
 
# Predict the function value for the whole grid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
 
# Plot the contour and training examples
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=colormap, edgecolors='k', s=50)
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])
plt.title('Decision Boundary of Logistic Regression on 2D Iris Dataset')
plt.show()
