#!/bin/bash

# Get the Ingress IPs
ingress_ips=($(kubectl describe service | grep Ingress | awk '{print $3}'))

# Define the placeholders and their corresponding Ingress IPs
placeholders=("IPflask1" "IPflask2" "IPflask3" "IPprod")
replace_ips=("${ingress_ips[0]}" "${ingress_ips[1]}" "${ingress_ips[2]}" "${ingress_ips[3]}")

# Iterate over the placeholders and replace them with the corresponding Ingress IPs
for ((i = 0; i < ${#placeholders[@]}; i++)); do
    sed -i "s/${placeholders[i]} = '.*/${placeholders[i]} = '${replace_ips[i]}'/" prod.sh
done

echo "prod.sh updated successfully."
