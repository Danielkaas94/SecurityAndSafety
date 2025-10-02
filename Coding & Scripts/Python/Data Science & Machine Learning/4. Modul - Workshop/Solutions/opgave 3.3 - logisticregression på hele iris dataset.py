from sklearn.metrics import classification_report, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

from sklearn.linear_model import LogisticRegression
import numpy as np


iris = load_iris()  # load iris sample dataset
print(iris)
X = iris.data
y = iris.target
# check how many samples we have
print("Number of samples: " +str(len(y)))

log_reg = LogisticRegression()

#so our y will be 1, if it is verginica (label is 2 of that flower), or 0 otherwise
y = (y==2).astype(np.int32)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = 17)
print("samples in X training set: "+str(len(X_train)))
print("sammples in test set: "+str(len(X_test)))

log_reg.fit(X_train,y_train)

predictions = log_reg.predict(X_test)

print("predictions : "+str(predictions))
print("actual      : "+str(y_test))

print("Evaluating performance: Confusion matrix")
matrix = confusion_matrix(y_test,predictions) #compare
print(matrix)
tn, fp, fn, tp = matrix.ravel()
print("(TN,FP,FN,TP)",(tn, fp, fn, tp))

print("classification report")
print(classification_report(y_test,predictions))

print("precision: "+ str(precision_score(y_test,predictions,average='weighted')))
print("recall: "+ str(recall_score(y_test,predictions,average='weighted')))

print("f1 score "+ str(f1_score(y_test,predictions,average='weighted')))
