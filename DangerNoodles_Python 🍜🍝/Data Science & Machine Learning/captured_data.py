import pandas as pd
import matplotlib.pyplot as plt

# Read the captured file into a DataFrame
# Replace 'captured_data.csv' with the path to your captured file
df = pd.read_csv('captured_data.csv')

# Assuming your data has two columns: 'Timestamp' and 'Packet Length'
# Adjust column names accordingly
timestamps = df['Timestamp']
packet_lengths = df['Packet Length']

# Plotting
plt.plot(timestamps, packet_lengths)
plt.xlabel('Timestamp')
plt.ylabel('Packet Length')
plt.title('Packet Length over Time')
plt.show()
