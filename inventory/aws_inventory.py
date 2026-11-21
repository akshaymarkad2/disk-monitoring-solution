#!/usr/bin/env python3
import argparse
import json
import os
import boto3


def get_instances(account_id, region):
    sts = boto3.client("sts")
    assumed_role = sts.assume_role(
        RoleArn=f"arn:aws:iam::{account_id}:role/MonitoringRole",
        RoleSessionName="MonitoringSession",
    )
    creds = assumed_role["Credentials"]

    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=creds["AccessKeyId"],
        aws_secret_access_key=creds["SecretAccessKey"],
        aws_session_token=creds["SessionToken"],
        region_name=region,
    )

    paginator = ec2.get_paginator("describe_instances")
    pages = paginator.paginate(
        Filters=[
            {"Name": "tag:Monitor", "Values": ["true"]},
            {"Name": "instance-state-name", "Values": ["running"]},
        ]
    )

    hosts = []
    hostvars = {}
    for page in pages:
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                platform = instance.get("Platform", "linux").lower()
                hosts.append(instance_id)
                hostvars[instance_id] = {
                    "ansible_host": instance_id,
                    "ansible_connection": "amazon.aws.aws_ssm",
                    "ansible_aws_ssm_region": region,
                    "ansible_shell_type": "powershell" if platform == "windows" else "sh",
                    "aws_account_id": account_id,
                }
    return hosts, hostvars


def build_inventory():
    region = os.getenv("AWS_REGION", "us-east-1")
    raw_accounts = os.getenv("AWS_ACCOUNT_IDS", "")
    accounts = [a.strip() for a in raw_accounts.split(",") if a.strip()]

    all_hosts = []
    all_hostvars = {}

    for acct in accounts:
        hosts, hostvars = get_instances(acct, region)
        all_hosts.extend(hosts)
        all_hostvars.update(hostvars)

    return {
        "_meta": {"hostvars": all_hostvars},
        "all": {
            "hosts": all_hosts,
            "vars": {"aws_region": region},
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-account AWS EC2 Dynamic Inventory")
    parser.add_argument("--list", action="store_true", help="List all active hosts")
    parser.add_argument("--host", help="Get variables for a specific host")
    args = parser.parse_args()

    if args.host:
        print(json.dumps({}))
    else:
        print(json.dumps(build_inventory(), indent=2))
