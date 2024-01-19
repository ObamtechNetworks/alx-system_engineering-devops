# Configuration Management and DevOps Automation
#### Overview
Welcome to the README for the Configuration Management and DevOps project! In this endeavor, we will explore the world of configuration management, DevOps practices, and automation. This project is inspired by Sylvain Kalache's experiences and the lessons learned during his time at SlideShare, particularly a memorable incident involving an auto-remediation tool named Skynet.

# Background Context
#### The Skynet Incident
During Sylvain's tenure at SlideShare, he developed an auto-remediation tool named Skynet. This tool was crucial for monitoring, scaling, and fixing the Cloud infrastructure. One unfortunate day, a bug in the code sent a nil value to the filter method, causing two critical issues:

1. MCollective, the parallel job-execution system, interpreted nil as 'all servers.'
2. The action triggered was to terminate the selected servers.

This resulted in 75% of SlideShare's conversion infrastructure servers being shut down, disrupting user capabilities to convert PDFs, PowerPoints, and videos. The aftermath was a major setback.

Fortunately, the use of Puppet, a configuration management tool, allowed for a swift restoration of the infrastructure within an hour. This incident underscores the importance of automation tools in managing complex infrastructures.

# Lessons Learned
Puppet proved invaluable for rapid infrastructure recovery.
Automation significantly reduces downtime in critical situations.
Investing time and energy in writing Puppet code is a long-term necessity for robust infrastructure management.

[Check Sylvain's tweet about the incident](https://twitter.com/devopsreact/status/836971570136375296)

# Resources
Before diving into the project, it's recommended to go through the following resources:

Intro to Configuration Management
Puppet resource type: file (check "Resource types" for all manifest types in the left menu)
Puppet’s Declarative Language: Modeling Instead of Scripting
Puppet lint
Puppet emacs mode

# Requirements
### General
All files will be interpreted on Ubuntu 20.04 LTS.
Files should end with a new line.
A README.md file at the root of the folder is mandatory.
Puppet manifests must pass puppet-lint version 2.1.1 without errors.
Puppet manifests must run without error.
The first line of Puppet manifests must be a comment explaining the manifest's purpose.
Puppet manifests files must end with the extension .pp.

# Versioning
Ensure that your Ubuntu 20.04 VM has Puppet 5.5 preinstalled. Use the following commands:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
No need to attempt upgrades; this project focuses on basic syntax, which remains virtually identical in newer Puppet versions.

Puppet 5 Docs
For additional guidance, refer to the Puppet 5 Docs.

Install puppet-lint
To ensure code quality, install puppet-lint:

```bash
$ gem install puppet-lint
```
