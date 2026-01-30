# AWS Cloud Security Scanner

**Automated Python CLI tool for identifying security misconfigurations in AWS environments.**

---

## Description

The **AWS Cloud Security Scanner** is a Python-based command-line tool designed to help cloud security engineers, DevSecOps professionals, and security-conscious developers identify and remediate security risks in AWS environments.  

The tool performs automated checks across critical AWS resources, including IAM roles and policies, S3 buckets, and security groups, generating actionable reports that improve cloud security posture and reduce attack surface.  

This project demonstrates hands-on experience in **cloud security, IAM analysis, automated reporting, and Python scripting** — making it a strong addition to any security or cloud-focused portfolio.

---

## Features

- Detects **over-permissive IAM roles and policies**  
- Scans **S3 buckets** for public access or misconfigurations  
- Analyzes **security groups** for overly permissive network rules  
- Generates **JSON reports** with actionable remediation steps  
- Supports **CLI flags** for targeted scans and reporting  
- Modular architecture for easy future expansion (e.g., automated alerts, Terraform integration)  

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/derekdelaughter/aws-cloud-security-scanner.git
cd aws-cloud-security-scanner
pip install -r requirements.txt
