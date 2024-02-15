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

pos=np.where(y==1)
neg=np.where(y==0)

plt.plot(X[pos[0],0], X[pos[0],1], 'ro')
plt.plot(X[neg[0],0], X[neg[0],1], 'bo')
plt.xlim([min(X[:,0]),max(X[:,0])])
plt.ylim([min(X[:,1]),max(X[:,1])])

logreg = linear_model.LogisticRegression(C=1000)

model = logreg.fit(X, y)

# print the predictions on X
# print y to make comparisons
# print the parameters and the score of the model - what does the score mean?
# 0,8235 - den har taget fejl 3 gange ud af 17
# print the prediction of a 2 dimensional point within the parameter space

# model.coef_[0,0]*x + model.coef_[0,1]*y + model.intercept_[0] = 0

# y = - ( model.coef_[0,0]*x +  model.intercept_[0]) / model.coef_[0,1]

xx = np.linspace(1, 7)
yy = -  (model.coef_[0,0] / model.coef_[0,1]) * xx - ( model.intercept_[0]  /  model.coef_[0,1])


plt.plot(xx, yy, 'k-')

plt.plot
plt.show()



