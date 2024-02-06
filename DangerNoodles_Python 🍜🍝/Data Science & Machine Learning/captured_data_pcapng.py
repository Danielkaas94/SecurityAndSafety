import pyshark
import pandas as pd
from colorama import init, Fore, Style
import matplotlib.pyplot as plt

# Path to your .pcapng file
# pcap_file = 'captured_data.pcapng'
pcap_file = 'captured_data.pcap'

# Use pyshark to parse the pcap file
cap = pyshark.FileCapture(pcap_file)

# Create an empty list to store the data
data = []


print(Fore.CYAN + "LET'S GO!")
# Iterate over each packet in the capture file
for packet in cap:
    # Extract relevant information from each packet
    timestamp = packet.sniff_time.timestamp()
    protocol = packet.transport_layer

    # Append the data to the list
    data.append({'Timestamp': timestamp, 'Protocol': protocol})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print(df.head())
