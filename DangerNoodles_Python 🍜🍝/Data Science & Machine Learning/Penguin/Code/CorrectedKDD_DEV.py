import pandas as pd
import numpy
from sklearn.metrics import confusion_matrix, zero_one_loss, accuracy_score
from sklearn.model_selection import train_test_split

from colorama import Fore
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.tree import plot_tree
from matplotlib import pyplot as plt
import seaborn as sns
# Med de uhyre lange ventetider, så overvejer jeg at der skal afspiles en lyd, når en classifier/element er færdig med sin kørsel
# import simpleaudio as sa
# import pygame

# Define function for confusion matrix plot
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
    plt.xlabel('Predicted labels')
    plt.ylabel('True labels')
    plt.title(title)
    plt.show()




# Must declare data_dir as the directory of training and test files
#data_dir="./datasets/KDD-CUP-99/"
# get file from http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz 
data_dir="./"
data_dir="datasets/"
# raw_data_filename = data_dir + "kddcup.data.corrected"
raw_data_filename = data_dir + "kddcup.data.corrected"
print(Fore.MAGENTA, raw_data_filename)
# input()


# Define column names based on the structure of the KDD Cup 99 dataset - Not implemented
column_names = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "land",
    "wrong_fragment",
    "urgent",
    "hot", # 10 - Number of 'hot' indicators (bro-ids feature)
    "num_failed_logins",
    "logged_in",
    "num_compromised",
    "root_shell",
    "su_attempted",
    "num_root",
    "num_file_creations",
    "num_shells",
    "num_access_files",
    "num_outbound_cmds",
    "is_host_login",
    "is_guest_login",
    "count",

    "srv_count", # 24 - Number of connection to same service as current connection in past two seconds
    
    "serror_rate",
    "srv_serror_rate",
    "rerror_rate",
    "srv_rerror_rate",
    "same_srv_rate",
    "diff_srv_rate",
    "srv_diff_host_rate",
    "dst_host_count",
    "dst_host_srv_count",

    "dst_host_same_srv_rate",

    "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate",
    "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate",
    "dst_host_srv_serror_rate",

    "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate",
    
    "connection_type"
]



print ("Loading raw data")
# raw_data = pd.read_csv(raw_data_filename, header=None, names=column_names)
raw_data = pd.read_csv(raw_data_filename, header=None)
print(Fore.LIGHTWHITE_EX, raw_data.head())



print ("Transforming data")
# Categorize columns: "protocol", "service", "flag", "attack_type"
# Factorize convert categorical data into numerical representations.
raw_data[1], protocols= pd.factorize(raw_data[1])
raw_data[2], services = pd.factorize(raw_data[2])
raw_data[3], flags    = pd.factorize(raw_data[3])
raw_data[41], attacks = pd.factorize(raw_data[41])
print(attacks)


# separate features (columns 1..40) and label (column 41)
features= raw_data.iloc[:,:raw_data.shape[1]-1]
labels= raw_data.iloc[:,raw_data.shape[1]-1:] # Connection Type

# convert them into numpy arrays
# features= numpy.array(features) # Just Testing
#labels= numpy.array(labels).ravel() # this becomes an 'horizontal' array
print(Fore.RED, "\n",labels,"\n")
labels= labels.values.ravel() # this becomes a 'horizontal' array
print(Fore.GREEN, "\n",labels,"\n")

# Separate data in train set and test set
df= pd.DataFrame(features)

# create training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.8, test_size=0.2)
# X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.3, test_size=0.7)
X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.2, test_size=0.8)
print ("X_train, y_train:", X_train.shape, y_train.shape)
print ("X_test, y_test:", X_test.shape, y_test.shape)



print(Fore.WHITE, "\n### Standard Scaler ###\n")
# Scaling & Support Vector Classifier (SVC)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Pairplot for visualizing relationships between features # Does not work
# sns.pairplot(df, hue='connection_type', palette='Set1')
# plt.suptitle("Pairplot of Challenge 2", y=1.02)
# plt.show()

# TODO Det her tager for langtid om at gennemfører
# Initialize and train a Support Vector Classifier (SVC)
# print(Fore.WHITE, "\n### SVC Fit ###\n")
# svm_model = SVC()
# svm_model.fit(X_train_scaled, y_train)

# # Predictions on the testing set
# print(Fore.WHITE, "\n### SVC Predict ###\n")
# y_pred = svm_model.predict(X_test_scaled)
# # Evaluate the model
# print(Fore.WHITE, "\n### Classification Report ###\n")
# print(classification_report(y_test, y_pred))


# Copy/Inspire from the wine_multi.py
"""
Dette gav dette problem/Crash:
ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Det viser sig, at datasættet er alt for stort, 
men skal vi bare tage en fraktion af datasættet, 
eller udvælge nogle algoritmer/classifers som bedre kan tåle mængden af data.

Good Classifiers:
    • Logistic Regression
    • Linear Support Vector Machines
    • Gradient Boosting Machines
        • XGBoost & LightGBM
    • Random Forest
    • Neural Networks

Classifiers to be Cautious with:
    • k-Nearest Neighbors
    • Decision Trees and Rule-Based Models
    • Naive Bayes
    • Non-linear SVMs
        • Gaussian Radial Basis Function (RBF)
    • AdaBoost
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier # Multi-Layer Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
# Creating instances of classifiers
# Create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)
logreg = LogisticRegression(max_iter=1000, random_state=52)
dtree = DecisionTreeClassifier()
svm = SVC()
nb = GaussianNB()
ann = MLPClassifier(hidden_layer_sizes=(100, 50), alpha=0.0001, batch_size=256, max_iter=500, solver='adam', activation='relu')

# Training and testing each classifier
# classifiers = [logreg, dtree, svm, nb, knn, ann]
# classifiers = [logreg, svm, ann]

print(Fore.BLUE, "#### Just Testing classifier ####" , "\n\n")
# Training and testing each classifier
classifiers = [svm, logreg, ann]
classifiers = [logreg]
# classifiers = [ann, logreg]
for clf in classifiers:
    print(Fore.YELLOW, f"Fit for {clf.__class__.__name__}: Please wait")
    # clf.fit(X_train, y_train)
    clf.fit(X_train_scaled, y_train)
    print(Fore.YELLOW, f"Predict for {clf.__class__.__name__}: Please wait")
    # y_pred = clf.predict(X_test)
    y_pred = clf.predict(X_test_scaled)
    #confusion_matrix
    # plot_confusion_matrix_LogisticRegression
    # plot_confusion_matrix(y_test, clf.predict(X_test_scaled), f'Confusion Matrix ({clf.__class__.__name__})')
    # plot_confusion_matrix(y_test, y_pred, f'Confusion Matrix ({clf.__class__.__name__})')
    results = confusion_matrix(y_test, y_pred)
    error = zero_one_loss(y_test, y_pred)

    print (Fore.WHITE, "Confusion matrix:\n", results)
    print (Fore.RED, "Error: ", error)
    print(Fore.LIGHTWHITE_EX, f"Accuracy for {clf.__class__.__name__}: {metrics.accuracy_score(y_test, y_pred)}")
    # print ("Score: ", trained_model.score(X_train, y_train))



print(Fore.MAGENTA ,"Ready?", "\n")
# input()

# dtree = DecisionTreeClassifier().fit(X_train, y_train)
dtree = DecisionTreeClassifier().fit(X_train_scaled, y_train)
# y_pred = dtree.predict(X_test)
y_pred = dtree.predict(X_test_scaled)
# Model Accuracy, how often is the classifier correct?
print("DecTree Accuracy:",metrics.accuracy_score(y_test, y_pred))


feature_names = list(features.columns)
print(Fore.RED,feature_names)

# fig = plt.figure(figsize=(16,7))
# plot_tree(dtree,  
#         #   feature_names = wine.feature_names,
#           feature_names=feature_names,
#           class_names=labels,
#         #   class_names = wine.target_names,
#           filled = True,
#           impurity = True,
#           rounded = True) # tree_clf er så trænet model
# plt.show()


print(Fore.MAGENTA ,"Ready?", "\n")
input()


# Training
print ("Training model")

#TODO create model (clf)
trained_model = clf.fit(X_train, y_train)
print ("Score: ", trained_model.score(X_train, y_train))

# Predicting
print ("Predicting")
y_pred = clf.predict(X_test)

print ("Computing performance metrics")

# Note you may want to print the confusion matrix to a file, e.g. using numpy.array_str
results = confusion_matrix(y_test, y_pred)
error = zero_one_loss(y_test, y_pred)

print ("Confusion matrix:\n", results)
print ("Error: ", error)
print("Accuracy:", accuracy_score(y_test, y_pred))

