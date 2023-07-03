#!/bin/bash

# Define the Flask application URL
FLASK_URL="http://${env.test1}:5000"

# Make a GET request to the Flask application
response=$(curl -s -o /dev/null -w "%{http_code}" "http://${env.test1}:5000")

# Check the HTTP response code
if [ "$response" == "200" ]; then
    echo "Flask application is running successfully."
else
    echo "Flask application is not running. HTTP response code: $response"
    exit 1

    # Check if the address is already in use
    if [ "$response" == "7" ]; then
        echo "Address already in use. Another process is using the specified host and port."
        exit 1
    fi
fi
