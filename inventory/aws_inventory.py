#!/usr/bin/env python3
import boto3
import os

def get_instances(account_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    instances = ec2.describe_instances(Filters=[
        {'Name': 'tag:Monitor', 'Values': ['true']}
    ])['Reservations']
    
    hosts = []
    for reservation in instances:
        for instance in reservation['Instances']:
            tags = {t['Key']: t['Value'] for t in instance.get('Tags', [])}
            hosts.append(instance['InstanceId'])
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
                "aws_region": "us-east-1"
            }
        }
    })
