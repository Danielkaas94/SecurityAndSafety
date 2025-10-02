#Import scikit-learn dataset library
from sklearn import datasets

# Import train_test_split function
from sklearn.model_selection import train_test_split

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#Load dataset
wine = datasets.load_wine()

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=17) # 70% training and 30% test

from sklearn import linear_model
logreg = linear_model.LogisticRegression(C=100, max_iter = 10000)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Logreg Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn import tree
clf = tree.DecisionTreeClassifier().fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("DecTree Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.svm import LinearSVC
svm = LinearSVC(C=100,loss="hinge",max_iter=5000)
svm.fit(X_train,y_train)
y_pred = svm.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("SVM Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.preprocessing import StandardScaler

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Initialize the classifier and make label predictions
mnb = MultinomialNB()
mnb.fit(X_train, y_train)
y_pred = mnb.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("MNB Accuracy:",metrics.accuracy_score(y_test, y_pred))

#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("KNN Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(X_train,y_train)

y_pred = mlp.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("MLP Accuracy:",metrics.accuracy_score(y_test, y_pred))

# SCALE
print("################## SCALING ##################")
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn import linear_model
logreg = linear_model.LogisticRegression(C=100, max_iter = 10000)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Logreg Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn import tree
clf = tree.DecisionTreeClassifier().fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("DecTree Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.svm import LinearSVC
svm = LinearSVC(C=100,loss="hinge",max_iter=5000)
svm.fit(X_train,y_train)
y_pred = svm.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("SVM Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Scaling performed internally in NB
#from sklearn.naive_bayes import MultinomialNB
#from sklearn.metrics import accuracy_score

# Initialize the classifier and make label predictions
#mnb = MultinomialNB()
#mnb.fit(X_train, y_train)
#y_pred = mnb.predict(X_test)

# Model Accuracy, how often is the classifier correct?
#print("NaiveBayes Accuracy:",metrics.accuracy_score(y_test, y_pred))

#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("KNN Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)
mlp.fit(X_train,y_train)

y_pred = mlp.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("MLP Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.tree import plot_tree
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(30,10))
plot_tree(clf,  
          feature_names = wine.feature_names,
          class_names = wine.target_names,
          filled = True ) # tree_clf er så trænet model

plt.show()
