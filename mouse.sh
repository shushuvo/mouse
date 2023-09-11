#!/bin/bash

# Listen on a specific port and move the mouse cursor based on the received data

# Define the port to listen on
PORT=8000

# Start listening on the specified port
nc -l -k $PORT | while read -r data; do
    case $data in
        "UP")
            xdotool mousemove_relative 0 -10  # Move the cursor up by 10 pixels
            ;;
        "DOWN")
            xdotool mousemove_relative 0 10  # Move the cursor down by 10 pixels
            ;;
        "LEFT")
            xdotool mousemove_relative -- -10 0  # Move the cursor left by 10 pixels
            ;;
        "RIGHT")
            xdotool mousemove_relative 10 0  # Move the cursor right by 10 pixels
            ;;
        *)
            echo "Invalid command received: $data"
            ;;
    esac
done
