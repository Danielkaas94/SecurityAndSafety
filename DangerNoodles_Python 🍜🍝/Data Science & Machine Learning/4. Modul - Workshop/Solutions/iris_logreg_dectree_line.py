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
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=colormap,edgecolor='black', s=500)
print(iris.target_names)

lines = [Line2D([0], [0], color=c, linewidth=3, linestyle='--') for c in colormap.colors]
plt.legend(lines, iris.target_names)

log_reg = LogisticRegression()
#so our y will be 1, if it is verginica (label is 2 of that flower), or 0 otherwise
y = (y==2).astype(np.int32)
model = log_reg.fit(X,y)

print('\nX[70]: ', X[[70]])
print('Label: ', y[70])
print('Predicted: ', model.predict(X[[70]]))

p1 = [2,1]
p2 = [4,1.5]
p3 = [4.8,1.6]
p4 = [6,2]
point_size = 11
plt.plot(p1[0],p1[1],'ys',markersize=point_size)
plt.plot(p2[0],p2[1],'ys',markersize=point_size)
plt.plot(p3[0],p3[1],'ys',markersize=point_size)
plt.plot(p4[0],p4[1],'ys',markersize=point_size)
plt.annotate("P1",p1)
plt.annotate("P2",p2)
plt.annotate("P3",p3)
plt.annotate("P4",p4)

pred1 = log_reg.predict_proba([p1])
pred2 = log_reg.predict_proba([p2])
pred3 = log_reg.predict_proba([p3])
pred4 = log_reg.predict_proba([p4])
print("probability p1" +str(pred1))
print("probability p2" +str(pred2))
print("probability p3" +str(pred3))
print("probability p4" +str(pred4))

c1 = log_reg.predict([p1])
c2 = log_reg.predict([p2])
c3 = log_reg.predict([p3])
c4 = log_reg.predict([p4])
print("class p1 : "+str(c1))
print("class p2 : "+str(c2))
print("class p3 : "+str(c3))
print("class p4 : "+str(c4))

xx = np.linspace(0, 7)
yy = -  (model.coef_[0,0] / model.coef_[0,1]) * xx - ( model.intercept_[0]  /  model.coef_[0,1])

plt.plot(xx, yy, 'k-')

plt.axvline(x=2.45)

plt.axvline(x=4.75)

plt.axhline(y=1.75)

plt.plot

plt.show()
