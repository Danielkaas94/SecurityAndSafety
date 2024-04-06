import pandas as pd
import numpy
from sklearn.metrics import confusion_matrix, zero_one_loss, accuracy_score
from sklearn.model_selection import train_test_split

# Must declare data_dir as the directory of training and test files
#data_dir="./datasets/KDD-CUP-99/"
# get file from http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data.gz 
data_dir="./"
raw_data_filename = data_dir + "kddcup.data.corrected"

print ("Loading raw data")

raw_data = pd.read_csv(raw_data_filename, header=None)

print ("Transforming data")
# Categorize columns: "protocol", "service", "flag", "attack_type"
raw_data[1], protocols= pd.factorize(raw_data[1])
raw_data[2], services = pd.factorize(raw_data[2])
raw_data[3], flags    = pd.factorize(raw_data[3])
raw_data[41], attacks = pd.factorize(raw_data[41])

print(attacks)

# separate features (columns 1..40) and label (column 41)
features= raw_data.iloc[:,:raw_data.shape[1]-1]
labels= raw_data.iloc[:,raw_data.shape[1]-1:]

# convert them into numpy arrays
#features= numpy.array(features)
#labels= numpy.array(labels).ravel() # this becomes an 'horizontal' array
labels= labels.values.ravel() # this becomes a 'horizontal' array
print(labels)

# Separate data in train set and test set
df= pd.DataFrame(features)

# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df, labels, train_size=0.8, test_size=0.2)
print ("X_train, y_train:", X_train.shape, y_train.shape)
print ("X_test, y_test:", X_test.shape, y_test.shape)


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

