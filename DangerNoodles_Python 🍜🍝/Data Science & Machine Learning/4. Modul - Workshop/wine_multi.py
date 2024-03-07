#Import scikit-learn dataset library
from sklearn import datasets

# Import train_test_split function
from sklearn.model_selection import train_test_split

#Import knearest neighbors Classifier model
from sklearn.neighbors import KNeighborsClassifier

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

#Load dataset
wine = datasets.load_wine()

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=7) # 70% training and 30% test

#Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)

#Train the model using the training sets
knn.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = knn.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))



# New Stuff - Add logreg, dtree, svm, nb, knn, ann

# Importing necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from colorama import Fore

# Creating instances of classifiers
logreg = LogisticRegression()
dtree = DecisionTreeClassifier()
svm = SVC()
nb = GaussianNB()
ann = MLPClassifier()

print("\n")

# Training and testing each classifier
classifiers = [logreg, dtree, svm, nb, knn, ann]
for clf in classifiers:
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(Fore.LIGHTWHITE_EX, f"Accuracy for {clf.__class__.__name__}: {metrics.accuracy_score(y_test, y_pred)}")

print("\n")


'''
 Accuracy for LogisticRegression: 0.9814814814814815
 Accuracy for DecisionTreeClassifier: 0.8888888888888888
 Accuracy for SVC: 0.5925925925925926
 Accuracy for GaussianNB: 0.9629629629629629
 Accuracy for KNeighborsClassifier: 0.7222222222222222
 Accuracy for MLPClassifier: 0.3148148148148148
'''

# Scale 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# Training and testing each classifier again except nb
classifiers = [logreg, dtree, svm, nb, knn, ann]
for clf in classifiers:
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(Fore.LIGHTCYAN_EX, f"Accuracy for {clf.__class__.__name__}: {metrics.accuracy_score(y_test, y_pred)}")

print("\n")

'''
# Before
Accuracy for LogisticRegression: 0.9259259259259259
Accuracy for DecisionTreeClassifier: 0.9259259259259259
Accuracy for SVC: 0.6111111111111112
Accuracy for GaussianNB: 0.9814814814814815
Accuracy for KNeighborsClassifier: 0.7222222222222222

# After
Accuracy for LogisticRegression: 1.0
Accuracy for DecisionTreeClassifier: 0.9259259259259259
Accuracy for SVC: 0.9629629629629629
Accuracy for GaussianNB: 0.9814814814814815
Accuracy for KNeighborsClassifier: 0.9444444444444444
'''

# How to visualize DecisionTree

dtree = DecisionTreeClassifier().fit(X_train, y_train)

y_pred = dtree.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("DecTree Accuracy:",metrics.accuracy_score(y_test, y_pred))


from sklearn.tree import plot_tree
from matplotlib import pyplot as plt
fig = plt.figure(figsize=(16,7))
plot_tree(dtree,  
          feature_names = wine.feature_names,
          class_names = wine.target_names,
          filled = True,
          impurity = True,
          rounded = True) # tree_clf er så trænet model

plt.show()