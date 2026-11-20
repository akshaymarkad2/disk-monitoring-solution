# Scalable Disk Monitoring Solution for AWS

A solution to monitor disk utilization across AWS EC2 instances using Ansible and CloudWatch.

## Table of Contents
1. [**Overview**](#overview)  
2. [**Architecture**](#architecture)  
3. [**Key Features**](#key-features)
4. **Setup & Installation**
5. [**Usage**](#usage)  
6. **Security & Compliance**
7. **Contact**


## Overview  
This solution addresses the critical need for proactive disk space monitoring in large-scale AWS environments. By leveraging Ansible for agentless data collection and Amazon CloudWatch for centralized metrics/alarming, it ensures zero downtime and operational efficiency.  

--- 
## Architecture
![Architecture Diagram](docs/architecture.png)

---
## Key Features  
- **Multi-Account Support:** Automatically discovers instances across AWS accounts using tags.  
- **Agentless Monitoring:** No software installation on EC2 instances.  
- **Real-Time Alerts:** CloudWatch alarms with **OKActions** for recovery notifications.  
- **Secure Credential Management:** SSH keys stored in **AWS SSM Parameter Store** (encrypted).  
- **Extensible:** Ready to expand to **Azure/GCP** with minimal changes.  
- **Compliance-Ready:** Aligns with **CIS AWS Benchmarks** and **AWS Well-Architected Framework**.
---
## Setup & Installation
**Prerequisites**
1. AWS Accounts:
   - IAM Role with permissions (ec2:DescribeInstances, cloudwatch:PutMetricData, ssm:GetParameter).
   - SNS Topic (DiskAlertTopic) for notifications.
2. Ansible Control Node:
   - Python 3.6+, ansible, aws-cli.
   - AWS credentials configured IAM Role.

**Step-by-Step Deployment**
1. Clone the Repository
   - git clone https://github.com/akshaymarkad2/disk-monitoring-solution.git
   - cd disk-monitoring-solution
2. Configure SSM Parameter Store
3. Create IAM Role
   - Attach the provided templates/iam_policy.json to an IAM Role trusted by the Ansible control node.
4. Generate Dynamic Inventory
   - python inventory/aws_inventory.py > inventory.ini
5. Run the Playbook
   - ansible-playbook -i inventory.ini playbooks/disk_monitoring.yml
6. Deploy CloudWatch Alarms
   - ansible-playbook -i inventory.ini playbooks/deploy_alarms.yml

---
## Usage
**1. Schedule Monitoring**
- Add to cron or AWS Systems Manager Automation:

**2. View Metrics**
  - CloudWatch Console: Navigate to Metrics → DiskMonitoring.
  - Alarms: Check CloudWatch → Alarms for HighDiskUsage-* alerts.

**3. Receive Alerts**
  - SNS Topic: Configured to send emails/Slack messages on ALARM and OK states.

---
## Security & Compliance
**Best Practices Implemented**
- Least Privilege IAM: Permissions scoped to tagged resources and specific actions.
- Encryption: All data in transit encrypted via AWS TLS.
- Audit Logging: CloudTrail logs all API calls for compliance audits.
- Tag-Based Access Control: Only instances tagged Monitor: true are scanned.

---
## Contact
- Name - Akshay Markad
- Email- akshay.markad2@gmail.com
  
