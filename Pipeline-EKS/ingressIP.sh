#!/bin/bash

# Get the Ingress IPs
ingress_ips=($(kubectl describe service | grep Ingress | awk '{print $3}'))

# Update the Jenkinsfile with the Ingress IPs
sed -i "s/IPflask1 = '.*/IPflask1 = '${ingress_ips[0]}'/" Jenkinsfile
sed -i "s/IPflask2 = '.*/IPflask2 = '${ingress_ips[1]}'/" Jenkinsfile
sed -i "s/IPflask3 = '.*/IPflask3 = '${ingress_ips[2]}'/" Jenkinsfile
sed -i "s/IPprod = '.*/IPprod = '${ingress_ips[3]}'/" Jenkinsfile

echo "Jenkinsfile updated successfully."
