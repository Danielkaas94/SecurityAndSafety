#!/bin/bash
if [ "$1" == "" ]
then
    echo "Usage: ./pingsweep.sh <IP address prefix>"
    echo "Example: ./pingsweep.sh 192.168.2"
else
    echo "Scanning IP addresses in the range $1.1 to $1.254..."
    
    for ip in $(seq 1 254); do
        ping -c 1 "$1.$ip" | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
    
    echo "Ping sweep initiated. Results will be displayed as they arrive."
    echo "Please wait..."
fi