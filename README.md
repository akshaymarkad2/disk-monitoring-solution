# Scalable Disk Monitoring Solution for AWS

A solution to monitor disk utilization across AWS EC2 instances using Ansible and CloudWatch.

# Table of Contents
1. [**Overview**](#overview)  
2. [**Architecture**](#architecture)  
3. [**Key Features**](#key-features)   
4. [**Usage**](#usage)  
5. **Security & Compliance**
6. **Contact**


## Overview  
This solution addresses the critical need for proactive disk space monitoring in large-scale AWS environments. By leveraging Ansible for agentless data collection and Amazon CloudWatch for centralized metrics/alarming, it ensures zero downtime and operational efficiency.  

--- 
## Architecture
<img width="557" height="452" alt="Architecture" src="https://github.com/user-attachments/assets/9dcf2b4f-b2dc-468e-980b-5ffcd5f5a4dd" />

---
## Key Features  
- **Multi-Account Support:** Automatically discovers instances across AWS accounts using tags.  
- **Agentless Monitoring:** No software installation on EC2 instances.  
- **Real-Time Alerts:** CloudWatch alarms with **OKActions** for recovery notifications.  
- **Secure Credential Management:** SSH keys stored in **AWS SSM Parameter Store** (encrypted).  
- **Extensible:** Ready to expand to **Azure/GCP** with minimal changes.  
- **Compliance-Ready:** Aligns with **CIS AWS Benchmarks** and **AWS Well-Architected Framework**.

---
## Usage
**Schedule Monitoring**
- Add to cron or AWS Systems Manager Automation:
**View Metrics**
- CloudWatch Console: Navigate to Metrics → DiskMonitoring.
- Alarms: Check CloudWatch → Alarms for HighDiskUsage-* alerts.
**Receive Alerts**
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
  
