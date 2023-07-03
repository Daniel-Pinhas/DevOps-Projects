#!/usr/bin/python3
import sys
import boto3

def create_ec2_instances(instance_count, tag_name, tag_value, security_group_id=None):
    ec2_client = boto3.client('ec2')

    # Define the parameters for creating the instances
    instance_params = {
        'ImageId': 'ami-0e820afa569e84cc1',  # Replace with the desired Amazon Linux AMI ID
        'InstanceType': 't2.micro',
        'MinCount': instance_count,
        'MaxCount': instance_count,
        'KeyName': 'dan',  # Replace with your key pair name
        'TagSpecifications': [{
            'ResourceType': 'instance',
            'Tags': [{
                'Key': tag_name,
                'Value': tag_value
            }]
        }]
    }

    if security_group_id:
        instance_params['SecurityGroupIds'] = [security_group_id]

    # Create the instances
    response = ec2_client.run_instances(**instance_params)

    # Get the instance IDs
    instance_ids = [instance['InstanceId'] for instance in response['Instances']]

    return instance_ids

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 4:
    print("Invalid number of arguments. Usage: ./run-instance.py <instance_count> <tag_name> <tag_value>")
else:
    # Extract the command-line arguments
    num_instances = int(sys.argv[1])
    tag_name = sys.argv[2]
    tag_value = sys.argv[3]

    security_group_id = 'sg-03e7670faca0d9b9c'  # Replace with the actual existing security group ID

    created_instances = create_ec2_instances(num_instances, tag_name, tag_value, security_group_id)
    print(f"Created instances: {', '.join(created_instances)}")
