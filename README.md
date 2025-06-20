## Repo Backuper

![Language](https://img.shields.io/badge/language%20-%20Python-blue)
![License](https://img.shields.io/github/license/lina-torovoltas/KGB_Bot-telegram)</br>

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

1. Clone this repository and prepare your environment:
   ```bash
    git clone https://github.com/lina-torovoltas/Repo_Backuper
    cd Repo_Backuper
    python3 -m venv env
    source env/bin/activate
    chmod +x start.sh
   ```
2. Create a `repos.txt` file in the project directory containing the list of repository URLs to track, example:
    ```
    https://github.com/username1/repository1
    https://github.com/username2/repository2
    https://gitlab.com/username/repository
    https://codeberg.org/username/repository
    ```
3. And run:
    ```
    ./start.sh
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
