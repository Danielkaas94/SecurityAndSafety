import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.cluster import KMeans
from colorama import Fore
import os

ascii_art = '''
      _____                       _           
     |  __ \                     (_)          
     | |__) |__ _ __   __ _ _   _ _ _ __  ___ 
     |  ___/ _ \ '_ \ / _` | | | | | '_ \/ __|
     | |  |  __/ | | | (_| | |_| | | | | \__ \\
     |_|   \___|_| |_|\__, |\__,_|_|_| |_|___/
                       __/ |                  
                      |___/                   
'''

print(Fore.LIGHTWHITE_EX + ascii_art)

print(Fore.RED + "\n\n### LET'S GO!! ###")
print(Fore.LIGHTRED_EX + "### LET'S GO!! ###")
print(Fore.BLACK + "### LET'S GO!! ###")
print(Fore.LIGHTBLACK_EX + "### LET'S GO!! ###")
print(Fore.BLUE + "### LET'S GO!! ###")
print(Fore.LIGHTBLUE_EX + "### LET'S GO!! ###")
print(Fore.CYAN + "### LET'S GO!! ###")
print(Fore.LIGHTCYAN_EX + "### LET'S GO!! ###")
print(Fore.YELLOW + "### LET'S GO!! ###")
print(Fore.LIGHTYELLOW_EX + "### LET'S GO!! ###")
print(Fore.WHITE + "### LET'S GO!! ###")
print(Fore.LIGHTWHITE_EX + "### LET'S GO!! ###")
print(Fore.MAGENTA + "### LET'S GO!! ###")
print(Fore.LIGHTMAGENTA_EX + "### LET'S GO!! ###\n\n")

# Read the penguins.csv file
# penguins = pd.read_csv("penguins.csv")

# Get the current working directory
current_directory = os.getcwd() # Note: Den finder C:\Users\Daniel og ikke fra den sti jeg rent faktisk har min python fil liggende 

file_path_penguins = os.path.join(current_directory,"datasets/penguins.csv")
penguins = pd.read_csv(file_path_penguins)


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
sns.boxplot(data=penguins.drop(columns=['species']))
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



'''
       _____                             _              _   _                       _             
      / ____|                           (_)            | | | |                     (_)            
     | (___  _   _ _ __   ___ _ ____   ___ ___  ___  __| | | | ___  __ _ _ __ _ __  _ _ __   __ _ 
      \___ \| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \/ _` | | |/ _ \/ _` | '__| '_ \| | '_ \ / _` |
      ____) | |_| | |_) |  __/ |   \ V /| \__ \  __/ (_| | | |  __/ (_| | |  | | | | | | | | (_| |
     |_____/ \__,_| .__/ \___|_|    \_/ |_|___/\___|\__,_| |_|\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                  | |                                                                        __/ |
                  |_|                                                                       |___/ 

'''
# Split the data into features and target variable
X = penguins.drop(columns=['species'])
y = penguins['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Logistic Regression model
log_reg_model = LogisticRegression(max_iter=1000)
log_reg_model.fit(X_train, y_train) # ValueError: could not convert string to float: 'Biscoe'. Fordi nogle features er tekstbaseret (String)

# Train Decision Tree model
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

# Train Random Forest model
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Evaluate models
models = {'Logistic Regression': log_reg_model, 'Decision Tree': dt_model, 'Random Forest': rf_model}
for name, model in models.items():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))

'''
      _    _                                       _              _   _                       _             
     | |  | |                                     (_)            | | | |                     (_)            
     | |  | |_ __  ___ _   _ _ __   ___ _ ____   ___ ___  ___  __| | | | ___  __ _ _ __ _ __  _ _ __   __ _ 
     | |  | | '_ \/ __| | | | '_ \ / _ \ '__\ \ / / / __|/ _ \/ _` | | |/ _ \/ _` | '__| '_ \| | '_ \ / _` |
     | |__| | | | \__ \ |_| | |_) |  __/ |   \ V /| \__ \  __/ (_| | | |  __/ (_| | |  | | | | | | | | (_| |
      \____/|_| |_|___/\__,_| .__/ \___|_|    \_/ |_|___/\___|\__,_| |_|\___|\__,_|_|  |_| |_|_|_| |_|\__, |
                            | |                                                                        __/ |
                            |_|                                                                       |___/ 

'''


# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Add cluster labels to the dataset
penguins['cluster'] = kmeans.labels_

# Visualize clustering results
plt.figure(figsize=(10, 6))
sns.scatterplot(data=penguins, x='flipper_length_mm', y='bill_length_mm', hue='cluster', palette='Set1', legend='full')
plt.title("K-means Clustering of Penguins")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Bill Length (mm)")
plt.show()


'''
         _____            ____                          _       _       _   _____  _       _   
        / ____|          |  _ \                        | |     (_)     | | |  __ \| |     | |  
       | (___   ___  __ _| |_) | ___  _ __ _ __        | | ___  _ _ __ | |_| |__) | | ___ | |_ 
        \___ \ / _ \/ _` |  _ < / _ \| '__| '_ \   _   | |/ _ \| | '_ \| __|  ___/| |/ _ \| __|
        ____) |  __/ (_| | |_) | (_) | |  | | | | | |__| | (_) | | | | | |_| |    | | (_) | |_ 
       |_____/ \___|\__,_|____/ \___/|_|  |_| |_|  \____/ \___/|_|_| |_|\__|_|    |_|\___/ \__|
                                                                                         
'''

# Pairplot for visualizing relationships between features
sns.pairplot(penguins, hue='species', palette='Set1')
plt.suptitle("Pairplot of Penguin Features", y=1.02)
plt.show()
