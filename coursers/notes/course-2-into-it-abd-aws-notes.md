# Course 2 – Introduction to Information Technology and AWS Cloud (Notes)

These are my notes from **"Introduction to Information Technology and AWS Cloud"**, which I am currently about two-thirds of the way through.

## 1. IT Fundamentals (My Summary)

- **Server:** A computer that provides resources or services to other computers.
- **Operating System:** Software that manages hardware and lets applications run (e.g., Linux, Windows).
- **Network:** How devices communicate with each other using IP addresses, ports, and protocols.
- **Storage:** Where data lives (disks, databases, object storage, etc.).

### Cloud Angle

- In AWS, these fundamental ideas map to:
  - Servers → **EC2 instances**
  - Storage → **EBS, S3**
  - Network → **VPC, subnets, route tables, security groups**
  - Identity/Access → **IAM**

---

## 2. On-Premises vs Cloud (What I Understand)

- **On-premises:**
  - Company owns and manages physical hardware.
  - Responsible for power, cooling, hardware failures, and scaling up.
- **Cloud (AWS):**
  - Company "rents" compute, storage, and network from AWS.
  - AWS manages the physical hardware and global infrastructure.
  - Customers focus more on configuration and applications.

### Why This Matters for Support

When something breaks, support needs to understand:
- Is it likely an AWS-side issue (infrastructure) or a misconfiguration on the customer’s side?
- What AWS guarantees (e.g., availability of a service in a region) vs. what the customer must configure correctly.

---

## 3. Basic Networking Concepts (As I See Them)

- **IP Address:** A unique address for a device on a network.
- **Port:** A logical “doorway” for specific types of traffic (e.g., 22 for SSH, 80 for HTTP).
- **Protocol:** Rules for communication (HTTP, HTTPS, SSH, etc.).

### AWS Context

- EC2 instances live inside a **VPC** (Virtual Private Cloud).
- To connect to them:
  - The instance needs the right **security group rules** (e.g., SSH allowed on port 22).
  - The network needs proper routing (e.g., Internet Gateway, route tables).
  - The instance may need a **public IP** if accessed from the internet.

This is directly related to common support issues like **“I can’t SSH into my instance”**, which I documented in my `/runbooks/ec2-connection-troubleshooting.md` file.

---

## 4. AWS Global Infrastructure (Regions and AZs)

- **Region:** A physical location in the world where AWS has multiple data centers.
- **Availability Zone (AZ):** One or more data centers within a region.

### Support Relevance

- Some issues are region-specific.
- When troubleshooting, it’s important to note:
  - Which region the resource is in.
  - Whether services are available/healthy in that region (based on AWS status pages and monitoring).

---

## 5. How This Course Helps Me as a Future AWS Support Engineer

- Gives me vocabulary to talk to both:
  - Traditional IT people (servers, networks, storage)
  - Cloud-native teams (EC2, VPC, S3, IAM)
- Strengthens my mental model of where problems can occur:
  - Application issue
  - OS issue
  - Network issue
  - AWS configuration/service issue

I will keep updating this file as I finish the course and start doing more hands-on labs.
