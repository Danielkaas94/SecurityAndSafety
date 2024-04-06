from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

import os
import pandas as pd

from colorama import Fore

challenge2_ascii =  r'''
   _____ _           _ _                         ___             _  __                    _          _              _____  _                                    
  / ____| |         | | |                       |__ \           | |/ /                   | |        | |            |  __ \(_)                                   
 | |    | |__   __ _| | | ___ _ __   __ _  ___     ) |  ______  | ' / _ __   _____      _| | ___  __| | __ _  ___  | |  | |_ ___  ___ _____   _____ _ __ _   _  
 | |    | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \   / /  |______| |  < | '_ \ / _ \ \ /\ / / |/ _ \/ _` |/ _` |/ _ \ | |  | | / __|/ __/ _ \ \ / / _ \ '__| | | | 
 | |____| | | | (_| | | |  __/ | | | (_| |  __/  / /_           | . \| | | | (_) \ V  V /| |  __/ (_| | (_| |  __/ | |__| | \__ \ (_| (_) \ V /  __/ |  | |_| | 
  \_____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___| |____|          |_|\_\_| |_|\___/ \_/\_/ |_|\___|\__,_|\__, |\___| |_____/|_|___/\___\___/ \_/ \___|_|   \__, | 
                                     __/ |                                                              __/ |                                             __/ | 
                                    |___/                                                              |___/                                             |___/  
'''


print(Fore.MAGENTA, challenge2_ascii)

# Step 1: Load the dataset
# Assuming your dataset is in a large text file named 'kddcup.data.txt'
# Replace 'column_names' with the actual column names of your dataset

# Define column names based on the structure of the KDD Cup 99 dataset
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

current_directory = os.getcwd() # Note: Den finder C:\Users\Daniel og ikke fra den sti jeg rent faktisk har min python fil liggende 
file_path_kddCup99 = os.path.join(current_directory,"datasets/kddcup.data.txt")

df_KDDCup99 = pd.read_csv(file_path_kddCup99, names=column_names)

print(Fore.LIGHTWHITE_EX, df_KDDCup99.head(), "\n\n")
"""
    duration protocol_type service flag  src_bytes  ...  dst_host_serror_rate  dst_host_srv_serror_rate  dst_host_rerror_rate  dst_host_srv_rerror_rate  connection_type
0         0           tcp    http   SF        215  ...                   0.0                       0.0                   0.0                       0.0          normal.
1         0           tcp    http   SF        162  ...                   0.0                       0.0                   0.0                       0.0          normal.
2         0           tcp    http   SF        236  ...                   0.0                       0.0                   0.0                       0.0          normal.
3         0           tcp    http   SF        233  ...                   0.0                       0.0                   0.0                       0.0          normal.
4         0           tcp    http   SF        239  ...                   0.0                       0.0                   0.0                       0.0          normal.
"""

