# AWS Core Services – Support-Focused Overview

These notes connect what I'm learning in the **Cloud Technology Consultant** program to concrete AWS services.

## Compute – EC2

- Virtual servers in the cloud.
- Common support tasks:
  - Troubleshooting connection issues (SSH/RDP).
  - Investigating high CPU/memory usage.
  - Checking instance states and status checks.

## Storage – S3

- Object storage for files, backups, and logs.
- Common support tasks:
  - Access denied errors (IAM policies, bucket policies).
  - Incorrect bucket region.
  - Versioning / lifecycle configuration questions.

## Identity & Access – IAM

- Manages users, roles, and permissions.
- Common support tasks:
  - “Access Denied” for specific API calls.
  - Misconfigured IAM roles for EC2 or Lambda.
  - MFA and credential issues.

## Monitoring – CloudWatch

- Metrics, logs, and alarms.
- Common support tasks:
  - Investigating why an alarm triggered.
  - Checking logs for application errors.
  - Helping customers set up basic alarms (CPU, disk, status checks).

---

These notes are updated as I go deeper into both AWS documentation and my Coursera program.
