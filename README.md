# Scalable Disk Monitoring Solution for AWS

A solution to monitor disk utilization across AWS EC2 instances using Ansible and CloudWatch.

## Architecture Overview
<img width="557" height="452" alt="Architecture" src="https://github.com/user-attachments/assets/9dcf2b4f-b2dc-468e-980b-5ffcd5f5a4dd" />

## Features
- Multi-account VM discovery
- Real-time disk metrics via CloudWatch
- Automated alarm creation

## Setup
1. Clone this repository
2. Run `ansible-playbook playbooks/disk_monitoring.yml`
