#!/bin/bash

# Define the Flask application URLs
IPflask1='http://FLASK_IP_PLACEHOLDER_1:5000'
IPflask2='http://FLASK_IP_PLACEHOLDER_2:5000'
IPflask3='http://FLASK_IP_PLACEHOLDER_3:5000'
IPprod='http://FLASK_IP_PLACEHOLDER_PROD'


# Define the Flask application URL
FLASK_URL="http://${IPprod}"
sleep 10
# Make a GET request to the Flask application
response=$(curl -s -o /dev/null -w "%{http_code}" "http://${IPprod}")

# Check the HTTP response code
if [ "$response" == "200" ]; then
    echo "Flask application is running successfully."
else
    echo "Flask application is not running. HTTP response code: $response"
    exit 1
fi

FLASK_URL="http://${IPflask1}"
sleep 10
# Make a GET request to the Flask application
response=$(curl -s -o /dev/null -w "%{http_code}" "http://${IPflask1}")

# Check the HTTP response code
if [ "$response" == "200" ]; then
    echo "Flask application is running successfully."
else
    echo "Flask application is not running. HTTP response code: $response"
    exit 1
fi

FLASK_URL="http://${IPflask2}"
sleep 10
# Make a GET request to the Flask application
response=$(curl -s -o /dev/null -w "%{http_code}" "http://${IPflask2}")

# Check the HTTP response code
if [ "$response" == "200" ]; then
    echo "Flask application is running successfully."
else
    echo "Flask application is not running. HTTP response code: $response"
    exit 1
fi

FLASK_URL="http://${IPflask3}"
sleep 10
# Make a GET request to the Flask application
response=$(curl -s -o /dev/null -w "%{http_code}" "http://${IPflask3}")

# Check the HTTP response code
if [ "$response" == "200" ]; then
    echo "Flask application is running successfully."
else
    echo "Flask application is not running. HTTP response code: $response"
    exit 1
fi