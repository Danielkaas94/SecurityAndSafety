#Opgave 1.3 - plots etc

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from colorama import init, Fore, Style

# Du kan finde dokumentation for pyplot her: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.html
# Den helt præcise dokumentation er https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

X = 2 * np.random.rand(100, 1)  # hvad betyder de to parametre 100 og 1?
y = 4 + 3 * X + np.random.randn(100, 1) # så hvilke parametre ville vi forvente modellen har?
#hvad er forskellen mellem rand og randn? (du må se om du kan finde dokumentationen selv....)

# a = 3
# b = 4



print(X)
print(y)

plt.plot(X,y, "b.")  # hvad betyder "b." ? Se dokumentationen for plot i pyplot linket ovenover
                    # og prøv at skifte til noget andet.... Den laver om på farven m* bliver til MAGENTA stjerner
plt.axis([0,2,0,15])  # hvad betyder parameterne her? størrelse af grafen 📈
plt.plot()

#training the model
lin_reg = LinearRegression()
lin_reg.fit(X,y)   # train the model on the data

#calculating the score
score = lin_reg.score(X,y)  # NOTICE THAT THE CLOSER TO 1 THE BETTER.
print(Fore.BLUE + "score "+str(score))

#using the model on new data
new_x = np.array([[0],[2]])
y_predict = lin_reg.predict(new_x)

print (y_predict)
#- what is this?

# Get the value of A and b 
print(Fore.LIGHTRED_EX)
print("A: " + str(lin_reg.coef_))
print("b: " + str(lin_reg.intercept_))


#try to predict the outcome of a single x value
#read of the plot to see if it matches

#plot the new data
plt.plot(new_x,y_predict,"r")

plt.show()

#how to get a and b parameters - i.e. the trained parameters for the model...?
#see documentation for help...
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

#How does this compare to the expected values for a and b? (Hint: Look at how the test data is defined)






