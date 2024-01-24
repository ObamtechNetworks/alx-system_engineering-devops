# 0x0C Web Server Project Readme
### Overview
This project, titled "0x0C. Web server," is centered around DevOps and SysAdmin tasks. The project is managed by Sylvain Kalache and has a weight of 1. The project timeline is from Jan 22, 2024, 6:00 AM, to Jan 24, 2024, 6:00 AM. The checker was released on Jan 22, 2024, 6:00 PM, and an auto-review will be conducted at the deadline.

# Concepts
The primary concept to focus on in this project is understanding "What is a Child Process?" The background context emphasizes configuring the web-01 server according to specified requirements and automating tasks using Bash scripts without human intervention.

# Grading Criteria
Tasks will be evaluated based on the configuration of the web-01 server and the presence of Bash scripts automating tasks. The goal is to encourage automation, making the work more efficient.

# Example Script
An example script is provided to illustrate how to automate tasks. The key is to avoid manual intervention and script the configurations.

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
```

# Testing
To test the Bash script, it's recommended to reproduce the checker environment:

# Start a Ubuntu 16.04 sandbox.
Run the script on it.
Observe the behavior.

# Resources
Several resources are provided to aid in understanding and completing the project. These include information on how the web works, Nginx configuration, child process concepts, DNS, HTTP requests, and more.

# Learning Objectives
Upon completing this project, you should be able to explain the following without relying on Google:

- The main role of a web server.
- What a child process is.
- Why web servers have parent and child processes.
- Main HTTP requests.
- DNS and its main role.
- DNS Record Types: A, CNAME, TXT, MX.

# Requirements
The project has specific requirements, including the choice of editors, interpreting files on Ubuntu 16.04 LTS, newline endings, a mandatory README.md file, executable Bash scripts, passing Shellcheck without errors, and specific comments in the Bash scripts.

Servers
The project involves managing a server named "221986-web-01" with the username "ubuntu" and IP address "54.237.76.176," currently in a running state.
