#!/usr/bin/env python3
import boto3
import os
from botocore.exceptions import ClientError

def get_instances(account_id):
    region = os.getenv('AWS_REGION', 'us-east-1')
    ec2 = boto3.client('ec2', region_name=region)
    try:
        instances = ec2.describe_instances(Filters=[
            {'Name': 'tag:Monitor', 'Values': ['true']}
        ])['Reservations']
        hosts = [i['InstanceId'] for r in instances for i in r['Instances']]
        return hosts
    except ClientError as e:
        print(f"Error fetching instances for {account_id}: {e}")
        return []

if __name__ == '__main__':
    accounts = os.getenv('AWS_ACCOUNT_IDS', '').split(',')
    all_hosts = []
    for acct in accounts:
        all_hosts.extend(get_instances(acct))
    
    print({
        "all": {
            "hosts": all_hosts,
            "vars": {
                "ansible_user": os.getenv('ANSIBLE_USER', 'ec2-user'),
                "aws_region": os.getenv('AWS_REGION', 'us-east-1')
            }
        }
    })
