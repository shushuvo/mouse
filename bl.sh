#!/bin/bash

# Define the server address and port
server_address="localhost"
server_port=8004

# Connect to the server
exec 3<>/dev/tcp/$server_address/$server_port

# Read the data from the server
read -r response <&3
echo "Received data: $response"

# Close the connection
exec 3<&-
exec 3>&-
