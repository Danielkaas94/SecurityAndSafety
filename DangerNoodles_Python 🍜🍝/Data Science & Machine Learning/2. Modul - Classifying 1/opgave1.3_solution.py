#Opgave 1.3 - plots etc

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Du kan finde dokumentation for pyplot her: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html

X = 2 * np.random.rand(100, 1)  # hvad betyder de to parametre 100 og 1?
y = 4 + 3 * X + np.random.randn(100, 1)
# så hvilke parametre ville vi forvente modellen har?
#hvad er forskellen mellem rand og randn? (du må se om du kan finde dokumentationen selv....)

print(X)
print(y)


plt.plot(X,y, "b.")  # hvad betyder "b." ? Se dokumentationen for plot i pyplot linket ovenover
                    # og prøv at skifte til noget andet....
plt.axis([0,2,0,15])  # betyder parameterne her?
plt.plot()

#training the model
lin_reg = LinearRegression()
lin_reg.fit(X,y)   # train the model on the data

#calculating the score
score = lin_reg.score(X,y)  # NOTICE THAT THE CLOSER TO 1 THE BETTER.
print("Score: "+str(score))

# line parameters
print("A: " + str(lin_reg.coef_))
print("b: " + str(lin_reg.intercept_))

#try to predict the outcome of a single x value
new_x = np.array([[1]]) #x value
y_predict = lin_reg.predict(new_x)

print ("For x = 1\n" + str(y_predict))

#using the model on new data
new_x = np.array([[0],[2]])
y_predict = lin_reg.predict(new_x)

#print y values for endpoints x = 0, x = 2
print("For x = 0 and x = 2\n" + str(y_predict))

#plot the new data
plt.plot(new_x,y_predict,"r")

plt.show()

#how to get a and b parameters - i.e. the trained parameters for the model...?
#see documentation for help...
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

#How does this compare to the expected values for a and b? (Hint: Look at how the test data is defined)





