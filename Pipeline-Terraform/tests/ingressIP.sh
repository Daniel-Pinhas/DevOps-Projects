#!/bin/bash

# Get the Ingress IPs
ingress_ips=($(kubectl describe service | grep Ingress | awk '{print $3}'))

# Define the Flask application URLs with placeholders
IPflask1='http://FLASK_IP_PLACEHOLDER_1:5000'
IPflask2='http://FLASK_IP_PLACEHOLDER_2:5000'
IPflask3='http://FLASK_IP_PLACEHOLDER_3:5000'
IPprod='http://FLASK_IP_PLACEHOLDER_PROD'

# Replace the placeholders with the corresponding Ingress IPs
sed -i "s|http://FLASK_IP_PLACEHOLDER_1:5000|${ingress_ips[0]}:5000|g" prod.sh
sed -i "s|http://FLASK_IP_PLACEHOLDER_2:5000|${ingress_ips[1]}:5000|g" prod.sh
sed -i "s|http://FLASK_IP_PLACEHOLDER_3:5000|${ingress_ips[2]}:5000|g" prod.sh
sed -i "s|http://FLASK_IP_PLACEHOLDER_PROD|${ingress_ips[3]}|g" prod.sh

echo "Flask application URLs updated successfully."
