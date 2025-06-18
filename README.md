## Repo Backuper

![License](https://img.shields.io/github/license/lina-torovoltas/Repo_Backuper)
![Version](https://img.shields.io/github/v/release/lina-torovoltas/Repo-Backuper)</br>
**Repo Backuper** is a Python tool that monitors Git repositories and automatically creates backups when changes are detected.

## Features

- Periodically checks remote repositories for new commits using `git ls-remote`.
- Creates `.zip` archives of updated repositories.
- Tracks last commit hashes to avoid redundant backups.
- Stores backups in a specified directory.
- Customizable backup interval and file paths.

## Dependencies

- Python 3.9+
- `git` must be installed and available in PATH

## Installation

1. Clone this repository.
2. Make sure Python 3 is installed.
3. Install any required dependencies (if needed).

## Configuration

Before running the program, create a `repos.txt` file in the project directory containing the list of repository URLs to track.

**Example:**
```
https://github.com/username/repository1
https://github.com/username/repository2
https://gitlab.com/username/repository3
```

## Usage

Simply run the program with Python:

```
python3 main.py
```

Example output:

```
[∞] [15:30:25] Checking 3 repositories...
[↑] Repository updated: username/repository1
[✔] Backup completed: username/repository1
[↑] Repository updated: username/repository2
[✔] Backup completed: username/repository2
[=] No changes: username/repository3
[∞] Checked backups of 3 repositories, waiting 3600 seconds...
```

## Contributing

Contributions are welcome!</br>
Feel free to open pull requests to improve this project.


## Author

Developed by <a href="https://github.com/lina-torovoltas" style="color:#ff4f00">Lina Torovoltas</a> — © 2025 All rights reserved.
