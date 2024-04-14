# 0x17. Web stack debugging #3

## Description
This ongoing second chance project, initiated on Apr 9, 2024 at 6:00 AM, must conclude by Apr 17, 2024 at 6:00 AM. An automatic review will be launched at the deadline.

### Auto QA review:
- Mandatory: 0.0/2
- Altogether: 0.0%
- Mandatory: 0.0%
- Optional: no optional tasks

## Background Context
In the realm of debugging, logs often fall short in providing sufficient insight. This could be due to unexpected software behavior resulting in unlogged errors or inadequate information in the logs. In such scenarios, traversing down the stack becomes necessary. Fortunately, this is a skill Holberton students are equipped with.

Wordpress, a ubiquitous tool, serves various purposes from running blogs to e-commerce websites. It holds a significant share, powering 26% of the web, indicating high chances of encountering it in one's career.

Wordpress typically operates on a LAMP stack - Linux, Apache, MySQL, and PHP - a widely adopted technology suite.

The web stack under scrutiny in this project is a Wordpress website operating on a LAMP stack.

## Requirements
### General
- All files will be interpreted on Ubuntu 14.04 LTS.
- Ensure all files conclude with a new line.
- A README.md file at the root of the project folder is mandatory.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must execute without errors.
- The first line of Puppet manifests must be a comment explaining the manifest's purpose.
- Puppet manifests files must have the .pp extension.
- Files will undergo validation with Puppet v3.4.

## More Info
Install puppet-lint:
```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
