#!/bin/bash

# Get the Ingress IPs
ingress_ips=($(kubectl describe service | grep 'LoadBalancer Ingress:' | awk '{print $3}'))

# Use a placeholder to represent the Flask IP in the index.html file
# The placeholder can be any unique string that doesn't appear elsewhere in the file
placeholder_1="__FLASK_IP_PLACEHOLDER_1__"
placeholder_2="__FLASK_IP_PLACEHOLDER_2__"
placeholder_3="__FLASK_IP_PLACEHOLDER_3__"

# Replace the Flask IPs in the index.html file with the Ingress IPs
sed -i "s|http://${placeholder_1}:5000|http://${ingress_ips[0]}:5000|g" httpd-deploy-prod.yml
sed -i "s|http://${placeholder_2}:5000|http://${ingress_ips[1]}:5000|g" httpd-deploy-prod.yml
sed -i "s|http://${placeholder_3}:5000|http://${ingress_ips[2]}:5000|g" httpd-deploy-prod.yml

echo "Ingress IPs inserted in index.html successfully."
