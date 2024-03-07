# example of using mnist set for classification
from sklearn.base import BaseEstimator
from sklearn.model_selection import cross_val_score
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import f1_score

from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score


class Stupid_Classifier(BaseEstimator):

    def fit(self, X, y=None):
        pass

    def predict(self, X):
        return np.zeros((len(X),1), dtype=bool) #returns an array with only false


print("MNIST example")
print("fetching data.....can take some time....")
#note fetching can take 1-2 minutes if not cached before
#mnist = fetch_openml("mnist_784", version = 1, cache=True)


from mlxtend.data import loadlocal_mnist

X_train, y_train = loadlocal_mnist(
            images_path='train-images.idx3-ubyte',
            labels_path='train-labels.idx1-ubyte')

X_test, y_test = loadlocal_mnist(
            images_path='t10k-images.idx3-ubyte',
            labels_path='t10k-labels.idx1-ubyte')


print(X_train.shape)
print(y_train.shape)

print("have data now")

#The following is only used if data is from openML online
"""
mnist = fetch_openml("mnist_784", version = 1, cache=True)
mnist.keys()
X, y = mnist["data"], mnist["target"]
print(X.shape)
print(y.shape)
#convert the string array to int array

y = y.astype(np.uint8)
"""

some_digit = X_train[0]
print("label : "+str(y_train[0]))


some_digit_image = some_digit.reshape(28,28)
plt.figure(0)

plt.imshow(some_digit_image, cmap = "binary")
plt.axis("off")
plt.figure(1)
plt.axis("on")

#The following is only used if data is from openML online
""" 
X_train = X[:60000]
X_test = X[60000:]
y_train = y[:60000]
y_test = y[60000:]
"""

# visualize the distributions
plt.hist(y_train,bins=10)

#convert this into a binary classification problem
y_train_5 = (y_train ==5) # creates an array of true if 5, false otherwise
y_test_5 = (y_test == 5) # creates an array of true if 5, false otherwise

sgd_clf = SGDClassifier(random_state=42)
print("Training the model... please wait..")
sgd_clf.fit(X_train, y_train_5)
print("Model is trained")
predictions = sgd_clf.predict(X_test)


print("digit is five : "+str(sgd_clf.predict([some_digit])))

# looking at how good our predictor is.
print("Evaluating performance: Cross validation ")

scores = cross_val_score(sgd_clf,X_train,y_train_5,cv=3,scoring="accuracy")
print(scores)

print("Evaluating performance: Cross validation on stupid predictor ")

stupid_clf = Stupid_Classifier()
predictions_stupid = stupid_clf.predict(X_test)
scores_stupid = cross_val_score(stupid_clf,X_train,y_train_5,cv=3,scoring="accuracy")
print(scores_stupid)

print("Evaluating performance: Confusion matrix")
matrix = confusion_matrix(y_test_5,predictions)
print(matrix)
#output is the confusion matrix

tn, fp, fn, tp = matrix.ravel()
print("(TN,FP,FN,TP)",(tn, fp, fn, tp))
print("precision: "+ str(precision_score(y_test_5,predictions)))
print("recall: "+ str(recall_score(y_test_5,predictions)))

print("F1 score: "+str(f1_score(y_test_5,predictions)))

print(classification_report(y_test_5,predictions))


plt.show()
print("end of program")