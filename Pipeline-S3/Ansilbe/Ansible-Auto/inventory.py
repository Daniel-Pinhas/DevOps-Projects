#!/usr/bin/python3

import boto3
import json

# Connect to AWS EC2 using boto3
ec2_client = boto3.client('ec2', region_name='us-east-2')

# Fetch EC2 instances based on specific filters for Flask instances
flask_response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Flask']
        }
    ]
)

# Fetch EC2 instances based on specific filters for web instances
web_response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'tag:Environment',
            'Values': ['Web']
        }
    ]
)

# Prepare the inventory structure
inventory = {'flask': {'hosts': []}, 'web': {'hosts': []}, '_meta': {'hostvars': {}}}

# Process each Flask EC2 instance and add it to the inventory
for reservation in flask_response['Reservations']:
    for instance in reservation['Instances']:
        network_interfaces = instance.get('NetworkInterfaces', [])
        if network_interfaces:
            private_ip = network_interfaces[0]['PrivateIpAddress']
        else:
            continue

        public_ip = instance.get('PublicIpAddress')

        inventory['flask']['hosts'].append(private_ip)

        host_vars = {
            'ansible_user': 'ec2-user',
            'ansible_ssh_private_key_file': '/var/lib/jenkins/.ssh/dan.pem'
        }

        if public_ip:
            host_vars['ansible_host'] = public_ip

        inventory['_meta']['hostvars'][private_ip] = host_vars

# Process each web EC2 instance and add it to the inventory
for reservation in web_response['Reservations']:
    for instance in reservation['Instances']:
        network_interfaces = instance.get('NetworkInterfaces', [])
        if network_interfaces:
            private_ip = network_interfaces[0]['PrivateIpAddress']
        else:
            continue

        public_ip = instance.get('PublicIpAddress')

        inventory['web']['hosts'].append(private_ip)

        host_vars = {
            'ansible_user': 'ec2-user',
            'ansible_ssh_private_key_file': '/var/lib/jenkins/.ssh/dan.pem'
        }

        if public_ip:
            host_vars['ansible_host'] = public_ip

        inventory['_meta']['hostvars'][private_ip] = host_vars

# Add the newly created instances to the inventory
inventory['flask']['hosts'].append('YOUR_NEW_FLASK_INSTANCE_PRIVATE_IP')
inventory['_meta']['hostvars']['YOUR_NEW_FLASK_INSTANCE_PRIVATE_IP'] = {
    'ansible_user': 'ec2-user',
    'ansible_ssh_private_key_file': '/var/lib/jenkins/.ssh/dan.pem'
}

inventory['web']['hosts'].append('YOUR_NEW_WEB_INSTANCE_PRIVATE_IP')
inventory['_meta']['hostvars']['YOUR_NEW_WEB_INSTANCE_PRIVATE_IP'] = {
    'ansible_user': 'ec2-user',
    'ansible_ssh_private_key_file': '/var/lib/jenkins/.ssh/dan.pem'
}

# Print the inventory as JSON
print(json.dumps(inventory))
