# Web Stack Debugging #0 - Project Readme
### Overview
This project, titled "Web Stack Debugging #0," is a part of the curriculum in DevOps and System Administration. It focuses on debugging skills, particularly in the context of web stacks. The project aims to train participants in the art of debugging by providing broken or bugged web stacks that need to be fixed using Bash scripts.

# Project Details
Author: Sylvain Kalache, Co-founder at Holberton School
Weight: 1
Project Start: Jan 22, 2024, 6:00 AM
Project End: Jan 24, 2024, 6:00 AM
Checker Release: Jan 23, 2024, 6:00 PM
Auto Review: A review will be launched automatically at the deadline.
Concepts Covered
Participants are expected to be familiar with the following concepts:

# Network basics
- Docker
- Web stack debugging

# Background Context
Debugging is an essential skill for Full-Stack Software Engineers. The project simulates real-world scenarios where web stacks are not working correctly. The goal is to manually identify the issues and create a Bash script that, when executed, will bring the web stack to a working state.

Example Scenario
For instance, a server must have a copy of the /etc/passwd file in /tmp and a file named /tmp/isworking containing the string "OK." The absence of these elements renders the web application non-functional. Participants need to fix this scenario by figuring out the issues and creating a Bash script.

```bash
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
```
Note: Interactive software like emacs or vi cannot be used in the Bash script; everything must be done from the command line, including file editing.

Installing Docker
A container will be provided for this project, but participants can install Docker locally for experimentation. Installation guides are provided for Mac OS, Windows, and Ubuntu 14.04/16.04.

# Resources
man or help: curl

# Requirements
- Editors: vi, vim, emacs
- Interpretation: Ubuntu 14.04 LTS
- File Endings: All files should end with a new line
- README.md: A mandatory file at the root of the project folder
- Bash Scripts: All must be executable and pass Shellcheck without any errors
- Shebang: The first line of all Bash scripts should be #!/usr/bin/env bash
- Comments: The second line of all Bash scripts should be a comment explaining the script's purpose.

# Conclusion
This project provides a practical understanding of debugging web stacks, a crucial skill for DevOps and System Administration roles. Participants will gain hands-on experience in identifying and fixing issues within a web environment.
