# Project Name: Application Server

## Table of Contents
- [Description](#description)
- [Background Context](#background-context)
- [Resources](#resources)
- [Requirements](#requirements)
- [Servers](#servers)

## Description
This project focuses on integrating an application server into an existing web infrastructure served by Nginx. The goal is to enhance the infrastructure to handle dynamic content effectively, specifically serving the Airbnb clone project.

## Background Context
Your web infrastructure currently serves web pages through Nginx, which was installed in the initial web stack project. While Nginx can handle static content, dynamic content delivery is typically delegated to an application server. The task involves adding an application server to the existing infrastructure, integrating it with Nginx, and configuring it to serve the Airbnb clone project.

## Resources
Read or watch:
- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (Note: Install Gunicorn globally, do not use virtualenv)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

## Requirements
### General
- A `README.md` file, at the root of the project folder, is mandatory.
- All Python-related tasks must be executed using Python 3.
- Configuration files must include comments for clarity.
### Bash Scripts
- All files will be interpreted on Ubuntu 16.04 LTS.
- All files should end with a new line.
- Bash script files must be executable.
- Bash scripts must pass Shellcheck without any errors (version 0.3.7-5~ubuntu16.04.1 via apt-get).
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line should be a comment explaining the script's purpose.
### Servers
| Name          | Username | IP             | State   |
|---------------|----------|----------------|---------|
| 221986-web-01 | ubuntu   | 3.85.41.84     | running |
| 221986-web-02 | ubuntu   | 54.90.17.105  | running |
| 221986-lb-01  | ubuntu   | 100.26.132.88 | running |

## Project Timeline
- **Start**: Apr 15, 2024, 6:00 AM
- **End**: Apr 19, 2024, 6:00 AM
- **Checker Release**: Apr 17, 2024, 8:24 PM
- **Auto Review**: An auto review will be launched at the deadline.
