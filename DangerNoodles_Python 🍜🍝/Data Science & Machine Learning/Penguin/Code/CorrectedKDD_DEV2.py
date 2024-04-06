import os
from collections import defaultdict
import pandas as pd
import numpy as np


from sklearn.metrics import confusion_matrix, zero_one_loss, accuracy_score
from sklearn.model_selection import train_test_split

from colorama import Fore
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, LinearSVC
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
header_names = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'attack_type', 'success_pred']
column_names = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
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
    
    "connection_type", # attack_type/connection_type
]


# col_names = np.array(header_names)
col_names = np.array(column_names)

nominal_idx = [1, 2, 3]
binary_idx = [6, 11, 13, 14, 20, 21]
numeric_idx = list(set(range(41)).difference(nominal_idx).difference(binary_idx))

nominal_cols = col_names[nominal_idx].tolist()
binary_cols = col_names[binary_idx].tolist()
numeric_cols = col_names[numeric_idx].tolist()

category = defaultdict(list)
category['benign'].append('normal')

with open('datasets/training_attack_types.txt', 'r') as f:
    for line in f.readlines():
        attack, cat = line.strip().split(' ')
        category[cat].append(attack)

attack_mapping = dict((v,k) for k in category for v in category[k])
print(Fore.BLACK,attack_mapping)







print ("Loading raw data")
# KeyError: 'normal.' giver fejl omkring attack_mapping[x], WHY??? Det er jo ren copy paste fra kapitel 5
raw_data_df = pd.read_csv(raw_data_filename, names=column_names)
"""
raw_data_df['attack_category'] = raw_data_df['connection_type'] \
                                .map(lambda x: attack_mapping[x]) 
# train_df.drop(['success_pred'], axis=1, inplace=True)
"""


# raw_data = pd.read_csv(raw_data_filename, header=None, names=column_names)
raw_data = pd.read_csv(raw_data_filename, header=None) # Original 🥇
# raw_data = pd.read_csv(raw_data_filename, names=header_names)
# raw_data = pd.read_csv(raw_data_filename,header=None, names=header_names)
# raw_data = pd.read_csv(raw_data_filename, names=header_names)
# raw_data = pd.read_csv(raw_data_filename, names=column_names)
# raw_data.columns = col_names # Fejl - KeyError: 1
print(Fore.LIGHTWHITE_EX, raw_data.head())



# Can we check for nulls?
print(Fore.YELLOW ,raw_data.isnull().sum())
# Handle missing values by dropping rows with any missing values
# raw_data.dropna(inplace=True)

# Some kind of Data analysis
print (Fore.GREEN, "### Data analysis ###")
print (Fore.LIGHTGREEN_EX, raw_data.info())
print (Fore.LIGHTGREEN_EX, raw_data.describe())
# raw_data_connection_type = raw_data['connection_type'].value_counts()
# raw_data_connection_type = raw_data[41].value_counts()

# raw_data_protocol_type = raw_data[1].value_counts()

# TODO Lav en grænse, for hvornår vi fravælger resultater, fordi de er for sjældne.
raw_data_connection_type = raw_data_df['connection_type'].value_counts()
grænse = 520 # 10
sjældne_værdier = raw_data_connection_type[raw_data_connection_type < grænse].index
# sjældne_værdier = sjældne_værdier['connection_type'].value_counts() # IndexError: only integers
"""
I Python er ~ en bitwise negation operator, der bruges til at invertere (flip) bits i et tal eller et binært tal. 
Men når det bruges i forbindelse med Pandas, ændrer det sin betydning lidt. 
I Pandas bruges ~ som en logisk negation operator, der inverterer en boolesk Serie (en kolonne i et DataFrame).
"""
filter_df_grænse = raw_data_df[~raw_data_df['connection_type'].isin(sjældne_værdier)]
filter_df_grænse = filter_df_grænse['connection_type'].value_counts()
print(filter_df_grænse)


# TODO Alternativt, lav en top 10
top_10_values = raw_data_connection_type.head(10).index
filter_df_top10 = raw_data_df[~raw_data_df['connection_type'].isin(top_10_values)]
filter_df_top10 = filter_df_top10['connection_type'].value_counts()
print(filter_df_top10)






raw_data_attack_types = raw_data_df['connection_type'].value_counts()
# raw_data_attack_cats = raw_data_df['attack_category'].value_counts()

raw_data_service = raw_data[2].value_counts()
sorted_src_bytes = raw_data.sort_values(by=4, ascending=False) # src_bytes
sorted_dst_bytes = raw_data.sort_values(by=5, ascending=False) # dst_bytes
print(Fore.WHITE, sorted_src_bytes)
print(Fore.BLACK, sorted_dst_bytes)



# raw_data_protocol_type.plot(kind='barh', figsize=(20,10), fontsize=20) # Hvorfor kommer der ikke noget frem?
# raw_data_service.plot(kind='barh', figsize=(20,10), fontsize=20) # Hvorfor kommer der ikke noget frem?
# raw_data_connection_type.plot(kind='barh', figsize=(20,10), fontsize=20) # Fin, men mange kolonner med næsten ingen data.
# filter_df_top10.plot(kind='barh', figsize=(20,10), fontsize=20) # mit plot ligner ikke som jeg havde forventet. Har jeg glemt en variabel/beregning? Nu ser den bedre ud! (Challenge2_DataAnalysis_Filter.png)
filter_df_grænse.plot(kind='barh', figsize=(20,10), fontsize=20)  # Hvis den overhovedet virker, så er den utrolig langsom om at komme frem.... Der er nok mindst gået 20 minutter. Nu virker den hurtig! (Challenge2_DataAnalysis_FilterGrænse.png)
plt.show() # Disse plot er upålidelige, de vises kun frem alt efter hvad humør de er i?...

# raw_data_attack_cats.plot(kind='barh', figsize=(20,10), fontsize=20)
# raw_data_attack_types.plot(kind='barh', figsize=(20,10), fontsize=20)
# raw_data.hist(bins=50, figsize=(20,15)) # Jeg ved ikke hvad det ligner....

print (Fore.GREEN, "### Data analysis ###")


print(raw_data.iloc[:,3]) # Viser Flag
# print(raw_data.iloc[:,'attack_type'])

# input()
# Check for missing values
# print(Fore.YELLOW ,raw_data.isnull().sum())




print(Fore.BLUE ,"Transforming data")
# Categorize columns: "protocol", "service", "flag", "attack_type"
# Factorize convert categorical data into numerical representations.
# print(Fore.RED ,raw_data['protocol_type'])

"""
# Alternativ løsning, hvis man bruger raw_data.columns = col_names
raw_data[1], protocols= pd.factorize(raw_data['protocol_type'])
raw_data[2], services = pd.factorize(raw_data['service'])
raw_data[3], flags    = pd.factorize(raw_data['flag'])
raw_data[41], attacks = pd.factorize(raw_data['connection_type'])
print(attacks)
"""
raw_data[1], protocols= pd.factorize(raw_data[1])
raw_data[2], services = pd.factorize(raw_data[2])
raw_data[3], flags    = pd.factorize(raw_data[3])
raw_data[41], attacks = pd.factorize(raw_data[41])
print(attacks)


# separate features (columns 1..40) and label (column 41)
features= raw_data.iloc[:,:raw_data.shape[1]-1]
labels= raw_data.iloc[:,raw_data.shape[1]-1:] # Connection Type # Select only the last column of the DataFrame

# convert them into numpy arrays
# features= numpy.array(features) # Just Testing
#labels= numpy.array(labels).ravel() # this becomes an 'horizontal' array
print(Fore.RED, "\n",labels,"\n")
labels= labels.values.ravel() # this becomes a 'horizontal' array
print(Fore.GREEN, "\n",labels,"\n")

# Separate data in train set and test set
df= pd.DataFrame(features)
print(Fore.MAGENTA, df.head())

# create training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.8, test_size=0.2)
# X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.3, test_size=0.7)
# X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.2, test_size=0.8)
X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=0.7)
print ("X_train, y_train:", X_train.shape, y_train.shape)
print ("X_test, y_test:", X_test.shape, y_test.shape)

### Test SelectFromModel ###
# from sklearn.feature_selection import SelectFromModel
# sfn = SelectFromModel(log_reg_model, prefit=True)
# Generate new training set, keeping only the selected features
# X_train_new = sfn.transform(X_train)
# print("Original nun features: {}, selected nun features: {}".format(X_train.shape[1], X_train_new.shape[1]))
# print(X_train_new)


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
Dette gav dette problem/Crash/Warning:
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
# knn = KNeighborsClassifier(n_neighbors=7)
knn = KNeighborsClassifier(n_neighbors=1, n_jobs=1)
logreg = LogisticRegression(max_iter=1000, random_state=52)
dtree = DecisionTreeClassifier()
# lsvm = LinearSVC() # TOO SLOW!
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


print(Fore.BLUE, "## Using Attribute Ratio (AR) feature selection ##")


averages = train_df.loc[:, numeric_cols].mean()
averages_per_class = train_df[numeric_cols+['attack_category']].groupby('attack_category').mean()

AR = {}
for col in numeric_cols:
    AR[col] = max(averages_per_class[col])/averages[col]

AR

def binary_AR(df, col):
    series_zero = train_df[train_df[col] == 0].groupby('attack_category').size()
    series_one = train_df[train_df[col] == 1].groupby('attack_category').size()
    return max(series_one/series_zero)

# Recreating dataframes with 2-class and 5-class labels

labels2 = ['normal', 'attack']
labels5 = ['normal', 'dos', 'probe', 'r2l', 'u2r']

train_df = pd.read_csv(train_file, names=header_names)
train_df['attack_category'] = train_df['attack_type'] \
                                .map(lambda x: attack_mapping[x])
train_df.drop(['success_pred'], axis=1, inplace=True)
    
test_df = pd.read_csv(test_file, names=header_names)
test_df['attack_category'] = test_df['attack_type'] \
                                .map(lambda x: attack_mapping[x])
test_df.drop(['success_pred'], axis=1, inplace=True)

train_attack_types = train_df['attack_type'].value_counts()
train_attack_cats = train_df['attack_category'].value_counts()
test_attack_types = test_df['attack_type'].value_counts()
test_attack_cats = test_df['attack_category'].value_counts()

train_df['su_attempted'].replace(2, 0, inplace=True)
test_df['su_attempted'].replace(2, 0, inplace=True)
train_df.drop('num_outbound_cmds', axis = 1, inplace=True)
test_df.drop('num_outbound_cmds', axis = 1, inplace=True)

train_df['labels2'] = train_df.apply(lambda x: 'normal' if 'normal' in x['attack_type'] else 'attack', axis=1)
test_df['labels2'] = test_df.apply(lambda x: 'normal' if 'normal' in x['attack_type'] else 'attack', axis=1)

combined_df = pd.concat([train_df, test_df])
original_cols = combined_df.columns

combined_df = pd.get_dummies(combined_df, columns=nominal_cols, drop_first=True)

added_cols = set(combined_df.columns) - set(original_cols)
added_cols= list(added_cols)

combined_df.attack_category = pd.Categorical(combined_df.attack_category)
combined_df.labels2 = pd.Categorical(combined_df.labels2)

combined_df['labels5'] = combined_df['attack_category'].cat.codes
combined_df['labels2'] = combined_df['labels2'].cat.codes

train_df = combined_df[:len(train_df)]
test_df = combined_df[len(train_df):]


for col in binary_cols+dummy_variables:
    cur_AR = binary_AR(train_df, col)
    if cur_AR:
        AR[col] = cur_AR



train_df[train_df.service_Z39_50 == 1].groupby('attack_category').size()


import operator
AR = dict((k, v) for k,v in AR.items() if not np.isnan(v))
sorted_AR = sorted(AR.items(), key=lambda x:x[1], reverse=True)

sorted_AR






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

