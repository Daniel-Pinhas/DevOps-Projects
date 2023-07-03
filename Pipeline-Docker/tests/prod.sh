#!/bin/bash

# Define the Flask application URL
FLASK_URL="http://${IPprod}:5000"
sleep 10
# Make a GET request to the Flask application
response=$(curl -s -o /dev/null -w "%{http_code}" "http://${IPprod}:5000")

# Check the HTTP response code
if [ "$response" == "200" ]; then
    echo "Flask application is running successfully."
else
    echo "Flask application is not running. HTTP response code: $response"
    exit 1
fi
