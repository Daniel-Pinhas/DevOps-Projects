#!/bin/bash

# Get the Ingress IPs
ingress_ips=($(kubectl describe service | grep Ingress | awk '{print $3}'))

# Update the Jenkinsfile with the Ingress IPs
sed -i "s/IPflask1 = '.*/IPflask1 = '${ingress_ips[0]}'/" prod.sh
sed -i "s/IPflask2 = '.*/IPflask2 = '${ingress_ips[1]}'/" prod.sh
sed -i "s/IPflask3 = '.*/IPflask3 = '${ingress_ips[2]}'/" prod.sh
sed -i "s/IPprod = '.*/IPprod = '${ingress_ips[3]}'/" prod.sh

echo "Prod.sh updated successfully."
