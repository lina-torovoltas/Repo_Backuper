# Repo Backuper

This is a Python program that periodically checks the status of Git repositories listed in a configuration file and creates backups of repositories that have new commits since the last backup. The backup is stored as a `.zip` archive in the specified backup directory.

## Features
- Periodically checks repositories for new commits using the `git ls-remote` command.
- Creates backups of repositories with new commits.
- Saves the hashes of the last commits to track changes.
- Stores backups in `.zip` format for smaller size.
- Customizable back up interval and backups paths

## Note

Before running the program, make sure you have a `repos.txt` file with a list of repositories to back up.  
Example of the contents of the `repos.txt` file: 
```
https://github.com/username/repository1
https://github.com/username/repository2
https://gitlab.com/username/repository3
```

# Usage

1. Clone the repository.
2. Configure your repositories in the repos.txt file.
3. Run the Repo Buckuper:
  ```bash
  $ python3 main.py
  [∞] [15:30:25] Checking 3 repositories...
  [↑] Repository updated: username/repository1
  [✔] Backup completed: username/repository1
  [↑] Repository updated: username/repository2
  [✔] Backup completed: username/repository2
  [=] No changes: username/repository3
  [∞] Checked backups of 3 repositories, waiting 3600 seconds...
  ```
