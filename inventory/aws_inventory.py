#!/usr/bin/env python3
import boto3
import os

def get_instances(account_id):
    # Get region from environment variable or default to us-east-1
    region = os.getenv('AWS_REGION', 'us-east-1')
    
    # Assume MonitoringRole in the target account
    sts = boto3.client('sts')
    assumed_role = sts.assume_role(
        RoleArn=f"arn:aws:iam::{account_id}:role/MonitoringRole",
        RoleSessionName="MonitoringSession"
    )
    credentials = assumed_role['Credentials']
    
    # Create EC2 client with assumed credentials AND dynamic region
    ec2 = boto3.client(
        'ec2',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
        region_name=region  # <-- Dynamic region here!
    )
    
    # Discover instances tagged for monitoring
    instances = ec2.describe_instances(Filters=[
        {'Name': 'tag:Monitor', 'Values': ['true']}
    ])['Reservations']
    
    hosts = [i['InstanceId'] for r in instances for i in r['Instances']]
    return hosts

if __name__ == '__main__':
    accounts = os.getenv('AWS_ACCOUNT_IDS', '').split(',')
    all_hosts = []
    for acct in accounts:
        all_hosts.extend(get_instances(acct))
    
    print({
        "all": {
            "hosts": all_hosts,
            "vars": {
                "ansible_user": "ec2-user",
                "aws_region": os.getenv('AWS_REGION', 'us-east-1') 
            }
        }
    }
         )
