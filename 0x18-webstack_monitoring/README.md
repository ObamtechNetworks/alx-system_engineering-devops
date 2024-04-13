# Webstack Monitoring

## Table of Contents
1. [Background Context](#background-context)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Servers](#servers)
6. [Output](#output)

## Background Context
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

- Application monitoring: getting data about your running software and making sure it is behaving as expected
- Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)

## Resources
Read or watch:

- [What is server monitoring](#)
- [What is application monitoring](#)
- [System monitoring by Google](#)
- [Nginx logging and monitoring](#)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Why is monitoring needed
- What are the 2 main areas of monitoring
- What are access logs for a web server (such as Nginx)
- What are error logs for a web server (such as Nginx)

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what the script is doing

### Servers
| Name           | Username | IP           | State   |
|----------------|----------|--------------|---------|
| 221986-web-01  | ubuntu   | 3.85.41.84   | running |
| 221986-web-02  | ubuntu   | 54.90.17.105 | running |
| 221986-lb-01   | ubuntu   | 100.26.132.88| running |

## Output
Output should be in markdown syntax.
