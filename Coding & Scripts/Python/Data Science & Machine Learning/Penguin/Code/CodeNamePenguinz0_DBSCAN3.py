# Import Important Stuff
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree # 🌲🌳🌲🌳 Yes I am a proud tree hugger IRL 🌳🌲🌳🌲
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, zero_one_loss, silhouette_score
from colorama import Fore
import os



ascii_art_penguin = r'''
 _______
< Hello >
 -------
        \
         \
          \   
              .--.
             |o_o |
             |:_/ |
            //   \ \
           (|     | )
          /'\_   _/`\
          \___)=(___/
'''
ascii_art_penguin_text = r'''
      _____                       _           
     |  __ \                     (_)          
     | |__) |__ _ __   __ _ _   _ _ _ __  ___ 
     |  ___/ _ \ '_ \ / _` | | | | | '_ \/ __|
     | |  |  __/ | | | (_| | |_| | | | | \__ \
     |_|   \___|_| |_|\__, |\__,_|_|_| |_|___/
                       __/ |                  
                      |___/                   
'''

print(Fore.BLACK + ascii_art_penguin)
print(Fore.LIGHTWHITE_EX + ascii_art_penguin_text)

print(Fore.RED + "\n\n### LET'S GO!! ###")
print(Fore.RED + "### LET'S GO!! ###")
print(Fore.BLACK + "### LET'S GO!! ###")
print(Fore.BLACK + "### LET'S GO!! ###")
print(Fore.BLUE + "### LET'S GO!! ###")
print(Fore.BLUE + "### LET'S GO!! ###")
print(Fore.CYAN + "### LET'S GO!! ###")
print(Fore.CYAN + "### LET'S GO!! ###")
print(Fore.YELLOW + "### LET'S GO!! ###")
print(Fore.YELLOW + "### LET'S GO!! ###")
print(Fore.WHITE + "### LET'S GO!! ###")
print(Fore.WHITE + "### LET'S GO!! ###")
print(Fore.MAGENTA + "### LET'S GO!! ###")
print(Fore.MAGENTA + "### LET'S GO!! ###\n\n")

# Read the penguins.csv file
# Get the current working directory
current_directory = os.getcwd() # Note: Den finder C:\Users\Daniel og ikke fra den sti jeg rent faktisk har min python fil liggende 
file_path_penguins = os.path.join(current_directory,"datasets/penguins.csv")
penguins = pd.read_csv(file_path_penguins)
print(penguins.columns)

# Noget Data analysis ligesom fra kapitel 5
print(Fore.BLACK, penguins)
print(Fore.CYAN, penguins.info())
print(Fore.YELLOW, penguins.describe())

penguins_NoGentoo = penguins[penguins['species'] != "Gentoo"]

penguins_island = penguins['island'].value_counts()
penguins_island_NoGentoo = penguins_NoGentoo['island'].value_counts()
penguins_species = penguins['species'].value_counts()
penguins_species_NoGentoo = penguins_NoGentoo['species'].value_counts()
penguins_sex = penguins['sex'].value_counts()
penguins_sex_NoGentoo = penguins['sex'].value_counts()


# penguins_island.plot(kind='barh', figsize=(20,10), fontsize=20)
penguins_species.plot(kind='barh', figsize=(20,10), fontsize=20)
# penguins_sex.plot(kind='barh', figsize=(20,10), fontsize=20) # Rimelig 50/50
# penguins_island_NoGentoo.plot(kind='barh', figsize=(20,10), fontsize=20)
# penguins_species_NoGentoo.plot(kind='barh', figsize=(20,10), fontsize=20)
# penguins_sex_NoGentoo.plot(kind='barh', figsize=(20,10), fontsize=20)

# penguins.plot(kind='barh', figsize=(20,10), fontsize=20) # This is nuts

sorted_penguins_body_mass_g = penguins.sort_values(by='body_mass_g', ascending=False)
print(Fore.WHITE, sorted_penguins_body_mass_g)

print(Fore.BLACK, penguins_species)
# Til venstre for pilen =>, er antallet, fra før fjernelse af Null rækker, til højre for pilen viser det nye antal mu det renset data (penguins.dropna(inplace=True))
"""
Adelie       152 => 146
Gentoo       124 => 119
Chinstrap     68 => 68
"""

print(Fore.CYAN, penguins_island)
"""
Biscoe       168 => 163
Dream        124 => 123
Torgersen     52 => 47
"""

print(Fore.GREEN, penguins_sex)
"""
MALE      168
FEMALE    165
"""

# Vi kan konkludere, at Gentoo pingvinen primært opholder sig på øen Biscoe 
print(Fore.RED, penguins_island_NoGentoo)
"""
Dream        124 => 123 
Torgersen     52 => 47
Biscoe        44 => 44
"""



# Display the first few rows of the dataset
print(Fore.LIGHTWHITE_EX, penguins.head(), "\n\n")

'''
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    MALE
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  FEMALE
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  FEMALE
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  FEMALE
'''


# Check for missing values
print(Fore.YELLOW ,penguins.isnull().sum())

# Handle missing values by dropping rows with any missing values
penguins.dropna(inplace=True)

# Check for outliers using box plots
plt.figure(figsize=(10, 6))
sns.boxplot(data=penguins)
# sns.boxplot(data=penguins_NoGentoo.drop(columns=['species']))
plt.title("Box plot of numerical features")
plt.xticks(rotation=45)
plt.show()
print("\n\n" + Fore.WHITE, penguins.head(), "\n\n")
'''
   species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    MALE
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  FEMALE
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  FEMALE
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  FEMALE
5  Adelie  Torgersen            39.3           20.6              190.0       3650.0    MALE
'''



ascii_art_super = r'''
       _____                             _              _   _                       _             
      / ____|                           (_)            | | | |                     (_)            
     | (___  _   _ _ __   ___ _ ____   ___ ___  ___  __| | | | ___  __ _ _ __ _ __  _ _ __   __ _ 
      \___ \| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \/ _` | | |/ _ \/ _` | '__| '_ \| | '_ \ / _` |
      ____) | |_| | |_) |  __/ |   \ V /| \__ \  __/ (_| | | |  __/ (_| | |  | | | | | | | | (_| |
     |_____/ \__,_| .__/ \___|_|    \_/ |_|___/\___|\__,_| |_|\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                  | |                                                                        __/ |
                  |_|                                                                       |___/ 

'''
print(ascii_art_super)

# Split the data into features and target variable

# TODO Hvis der er mere tid, find en løsning, så det er muligt at have 'island' og 'sex' med. ✅
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encoder_sex = LabelEncoder()
label_encoder_island = LabelEncoder()
label_encoder_species = LabelEncoder()

### Convert to numeric data types ###
print(Fore.RED, penguins['sex']) # MALE/FEMALE
penguins['sex'] = label_encoder_sex.fit_transform(penguins['sex'])
print(penguins['sex']) # 1/0

print(Fore.GREEN, penguins['island']) # Torgersen/Dream/Biscoe
penguins['island'] = label_encoder_island.fit_transform(penguins['island'])
print(penguins['island']) # 2/1/0

print(Fore.BLUE, penguins['species']) # Adelie/Chinstrap/Gentoo
penguins['species'] = label_encoder_species.fit_transform(penguins['species'])
print(penguins['species']) # 0/1/2

# X = penguins.drop(columns=['species']) # ValueError: could not convert string to float: 'Biscoe'
# X = penguins.drop(columns=['species','island','sex'])
X = penguins
print(Fore.MAGENTA, X.head())
y = penguins['species']
# y = penguins[penguins.drop(columns=['species','island','sex'])]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) # Hvis test_size=0.2, så har LogisticRegression ingen fejl.


# Train Logistic Regression model
log_reg_model = LogisticRegression(max_iter=1600, random_state=42) # Increase the number of iterations (max_iter) or scale the data as shown in:
log_reg_model.fit(X_train, y_train) # ValueError: could not convert string to float: 'Biscoe'. Fordi nogle features er tekstbaseret (String)

# Train Decision Tree model
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Train Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)


# Test SelectFromModel - Feature Selection
from sklearn.feature_selection import SelectFromModel

sfn = SelectFromModel(log_reg_model, prefit=True)

# Generate new training set, keeping only the selected features
X_train_new = sfn.transform(X_train)
print("Original nun features: {}, selected nun features: {}".format(X_train.shape[1], X_train_new.shape[1]))
# print(X_train_new)
# Original nun features: 4, selected nun features: 2 # Dette er når X = penguins.drop(columns=['species','island','sex'])
    # Hvis jeg ikke tager fejl, så vælger den bill_length_mm og Bill_depth_mm
# Original nun features: 7, selected nun features: 3 # Når X = penguins
    # Vælger sikkert bill_length_mm og Bill_depth_mm, så enten island eller species, så vi kan konkludere, at body_mass_g ikke er så vigtigt?

ascii_art_logRes = r'''
      _                 _     _   _        _____                              _             
     | |               (_)   | | (_)      |  __ \                            (_)            
     | |     ___   __ _ _ ___| |_ _  ___  | |__) |___  __ _ _ __ ___  ___ ___ _  ___  _ __  
     | |    / _ \ / _` | / __| __| |/ __| |  _  // _ \/ _` | '__/ _ \/ __/ __| |/ _ \| '_ \ 
     | |___| (_) | (_| | \__ \ |_| | (__  | | \ \  __/ (_| | | |  __/\__ \__ \ | (_) | | | |
     |______\___/ \__, |_|___/\__|_|\___| |_|  \_\___|\__, |_|  \___||___/___/_|\___/|_| |_|
                   __/ |                               __/ |                                
                  |___/                               |___/                                 
'''
"""
                Predicted Class
            |  Class 1  |  Class 2  |  Class 3  |
-------------------------------------------------
Actual   |            |            |            |
Class    |   TP (1,1) |   FP (1,2) |   FP (1,3) |
-------------------------------------------------
         |            |            |            |
         |   FN (2,1) |   TP (2,2) |   FP (2,3) |
Actual   |            |            |            |
Class    ----------------------------------------
         |            |            |            |
         |   FN (3,1) |   FN (3,2) |   TP (3,3) |
-------------------------------------------------
"""
print(Fore.YELLOW, ascii_art_logRes)

# Evaluate models
models = {'Logistic Regression': log_reg_model, 'Decision Tree': dt_model, 'Random Forest': rf_model}
for name, model in models.items():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    c_matrix = confusion_matrix(y_test, y_pred)
    error = zero_one_loss(y_test, y_pred)

    print(c_matrix)
    print(error)
    print(Fore.WHITE, f"{name} accuracy: {accuracy:.2f}")
    print(Fore.WHITE, classification_report(y_test, y_pred))

ascii_art_unsuper = r'''
      _    _                                       _              _   _                       _             
     | |  | |                                     (_)            | | | |                     (_)            
     | |  | |_ __  ___ _   _ _ __   ___ _ ____   ___ ___  ___  __| | | | ___  __ _ _ __ _ __  _ _ __   __ _ 
     | |  | | '_ \/ __| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \/ _` | | |/ _ \/ _` | '__| '_ \| | '_ \ / _` |
     | |__| | | | \__ \ |_| | |_) |  __/ |   \ V /| \__ \  __/ (_| | | |  __/ (_| | |  | | | | | | | | (_| |
      \____/|_| |_|___/\__,_| .__/ \___|_|    \_/ |_|___/\___|\__,_| |_|\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                            | |                                                                        __/ |
                            |_|                                                                       |___/ 

'''
print(ascii_art_unsuper)

##############
### KMeans ###
##############
# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=160) # 3 fine clusters!
# kmeans = KMeans(n_clusters=4, random_state=1250) # 4 næsten lige store clusters!
# kmeans = KMeans(n_clusters=6, random_state=43) # Bare grimt
# kmeans = KMeans(n_clusters=5, random_state=43, max_iter=100)

X = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']] # Faktisk pænere clusters uden sortering af features
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# kmeans.fit(X)
kmeans.fit(X_scaled) # Meget bedre!

# Add cluster labels to the dataset
penguins['cluster'] = kmeans.labels_


## KMeans Statistics ##
# Get cluster labels
labels = kmeans.labels_
# Inertia
inertia = kmeans.inertia_
# Silhouette score
silhouette_avg = silhouette_score(X_scaled, labels)
# Cluster sizes
unique, counts = np.unique(labels, return_counts=True)
cluster_sizes = dict(zip(unique, counts))
# Print statistics
print(Fore.YELLOW, "Inertia:", inertia)
print("Silhouette score:", silhouette_avg)
print("Cluster sizes:", cluster_sizes)
"""
Inertia: 893.9643961664724              # Relatively high, suggest some spread or overlap within clusters.
Silhouette score: 0.3638172524295727    # Reasonable clustering quality.
Cluster sizes: {0: 119, 1: 146, 2: 68}

Inertia: 293.9088557186051              # Mindre spread eller overlap
Silhouette score: 0.3989037703465259    # Bedre kvalitet i forhold til 3 clusters
Cluster sizes: {0: 84, 1: 130, 2: 57, 3: 62}
"""


# Visualize KMeans clustering results 1
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='bill_length_mm', hue='cluster', palette='Set1', legend='full')
plt.title("K-means Clustering of Penguins")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Bill Length (mm)")
plt.show()

# Visualize KMeans clustering results 2
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='cluster', palette='Set1', legend='full')
plt.title("K-means Clustering of Penguins")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

### 3D Plot Test ### (Virker)
# kmeansfig = plt.figure(figsize=(10, 6))
# ax1 = kmeansfig.add_subplot(121, projection='3d')
# ax1.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 3], c=kmeans.labels_, cmap='viridis')
# ax1.set_title('KMeans Clustering')
# ax1.set_xlabel('bill_length_mm')
# ax1.set_ylabel('bill_depth_mm')
# ax1.set_zlabel('body_mass_g')



# Jeg kan godt lide DBSCAN, så den skal også i brug udover KMeans og sådan er det!
##############
### DBSCAN ###
##############
# Select numerical features for clustering
print(X)
X = penguins[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']] # Uden sortering, så vil der være 7 grupper med masser af noise.
print(X)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5) # Initial version 1️⃣
# dbscan.fit(X) # Alt vil blive til noise -1 Rød - Scaling er nødvendigt!
dbscan.fit(X_scaled)

# Add cluster labels to the dataset
penguins['cluster'] = dbscan.labels_


## DBSCAN Statistics ##
# Get cluster labels
labels = dbscan.labels_
# Number of clusters
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
# Number of noise points
n_noise = list(labels).count(-1)
# Sizes of clusters
cluster_sizes = [list(labels).count(label) for label in set(labels) - {-1}]
# Print statistics
print("Number of clusters:", n_clusters)
print("Number of noise points:", n_noise)
print("Sizes of clusters:", cluster_sizes)
"""
Number of clusters: 4
Number of noise points: 66
Sizes of clusters: [115, 16, 27, 109]
"""


# Visualize DBSCAN clustering results 1
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='bill_length_mm', hue='cluster', palette='Set1', legend='full')
plt.title("DBSCAN Clustering of Penguins")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Bill Length (mm)")
plt.show()

# Visualize DBSCAN clustering results 2
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='bill_length_mm', y='body_mass_g', hue='cluster', palette='Set1', legend='full')
plt.title("DBSCAN Clustering of Penguins")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Body Mass (g)")
plt.show()

### 3D Plot Test ### (Virker)
# dbscanfig = plt.figure(figsize=(10, 6))
# ax2 = dbscanfig.add_subplot(122, projection='3d')
# ax2.scatter(X_scaled[:, 0], X_scaled[:, 1], X_scaled[:, 3], c=dbscan.labels_, cmap='viridis')
# ax2.set_title('DBSCAN Clustering')
# ax2.set_xlabel('bill_length_mm')
# ax2.set_ylabel('bill_depth_mm')
# ax2.set_zlabel('body_mass_g')
# plt.tight_layout()
# plt.show()

ascii_art_sea = r'''
       _____            _                        _____      _            _       _   
      / ____|          | |                      |  __ \    (_)          | |     | |  
     | (___   ___  __ _| |__   ___  _ __ _ __   | |__) |_ _ _ _ __ _ __ | | ___ | |_ 
      \___ \ / _ \/ _` | '_ \ / _ \| '__| '_ \  |  ___/ _` | | '__| '_ \| |/ _ \| __|
      ____) |  __/ (_| | |_) | (_) | |  | | | | | |  | (_| | | |  | |_) | | (_) | |_ 
     |_____/ \___|\__,_|_.__/ \___/|_|  |_| |_| |_|   \__,_|_|_|  | .__/|_|\___/ \__|
                                                                  | |                
                                                                  |_|                                                                                                 
'''
print(Fore.RED, ascii_art_sea)
print(Fore.GREEN, ascii_art_sea)
print(Fore.BLUE, ascii_art_sea)

# Fjern "Cluster fra Penguin", da det var en column fra DBSCAN - Less is more - Keep it simple
penguins = penguins.drop(columns=['cluster'])

penguins_pairplot_default = penguins

print(Fore.MAGENTA, "### label_encoder.inverse_transform ###")
# penguins['species'] = label_encoder_species.fit_transform(penguins['species'])

print(penguins['species']) # 0/2
penguins['species'] = label_encoder_species.inverse_transform(penguins['species']) # Så Rød/Grøn/Blå hue har navnet på species og ikke bare 0, 1, 2 
print(penguins['species']) # Adelie/Gentoo

# Seaborn Pairplot for visualizing relationships between features
# sns.pairplot(penguins_NoGentoo, hue='species', palette='Set1')
sns.pairplot(penguins, hue='species', palette='Set1')
plt.suptitle("Pairplot of Penguin Features", y=1.02)
plt.show()


penguins = penguins_pairplot_default
penguins['sex'] = label_encoder_sex.inverse_transform(penguins['sex'])

sns.pairplot(penguins, hue='sex', palette='Set1')
plt.suptitle("Pairplot of Penguin Features", y=1.02)
plt.show()


penguins = penguins_pairplot_default
penguins['island'] = label_encoder_island.inverse_transform(penguins['island'])

sns.pairplot(penguins, hue='island', palette='Set1')
plt.suptitle("Pairplot of Penguin Features", y=1.02)
plt.show()