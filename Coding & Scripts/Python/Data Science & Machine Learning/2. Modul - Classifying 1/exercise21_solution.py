# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 22:06:11 2018

@author: Bruger
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

# Array of points with a classification
X = np.array(np.matrix('6,350; 2.5, 400;4.5,500; 3.5,350; 2,300;4,600;7,300;5,500;5,400;6,400;3,400;4,500;1,200;3,400;7,700;3,550;2.5,650'))
y = np.array(np.matrix('0;0;1;0;0;1;1;1;0;1;0;0;0;0;1;1;0'))[:,0]

#X = np.array(np.matrix('4,450;5,600;6,700;4.5,550;4.9,500;5,650;5.5,500; 5.25,525; 4.25,625; 4.75, 575'))
#y = np.array(np.matrix('0;1;1;0;0;1;0;1;1;1'))[:,0]

pos=np.where(y==1)
neg=np.where(y==0)

plt.plot(X[pos[0],0], X[pos[0],1], 'ro')
plt.plot(X[neg[0],0], X[neg[0],1], 'bo')
#directly setting limits
plt.xlim(0,7)
plt.ylim(200, 900)

# use max/min values to set limits
#plt.xlim([min(X[:,0]),max(X[:,0])])
#plt.ylim([min(X[:,1]),max(X[:,1])])

logreg = linear_model.LogisticRegression(C=100)

model = logreg.fit(X, y)

#compare predictions to ground truths
print(logreg.predict(X))
print(y)

#create new data point
X_2 = np.array(np.matrix('4,550'))

#plot it
plt.plot(X_2[0][0], X_2[0][1], 'gx')

#predict class probabilities
ynew = logreg.predict_proba(X_2)
print('X=%s, Predicted=%s' % (X_2, ynew))
print('Class 0 probability: %06.6f' % ynew[0][0])
print('Class 1 probability: %06.6f' % ynew[0][1])

#directly predict point
print("Predict: " + str(logreg.predict(X_2)))

#params and score
print("Coef: " + str(model.coef_))
print("Intercept: " + str(model.intercept_))
print("Score: " + str(model.score(X, y)))

# calculations on equation (no need to fully understand this)
# model.coef_[0,0]*x + model.coef_[0,1]*y + model.intercept_[0] = 0
# y = - ( model.coef_[0,0]*x +  model.intercept_[0]) / model.coef_[0,1]

xx = np.linspace(0, 7)
yy = -  (model.coef_[0,0] / model.coef_[0,1]) * xx - ( model.intercept_[0]  /  model.coef_[0,1])

#print line parameters
print('A: %06.6f' % -(model.coef_[0,0] / model.coef_[0,1]))
print('b: %06.6f' % - ( model.intercept_[0]  /  model.coef_[0,1]))

plt.plot(xx, yy, 'k-')

plt.plot
plt.show()



