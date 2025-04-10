import os
import time
import subprocess
import hashlib
from datetime import datetime
import json



REPOS_FILE = "repos.txt"
HASHES_FILE = "hashes.json"
BACKUP_DIR = "backups"
CHECK_INTERVAL = 3600
last_hashes = {}


def load_hashes():
    if os.path.exists(HASHES_FILE):
        with open(HASHES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes():
    with open(HASHES_FILE, "w") as f:
        json.dump(last_hashes, f)

def get_repo_list():
    if not os.path.exists(REPOS_FILE):
        print("[!] repos.txt not found. Exiting.")
        exit()
    with open(REPOS_FILE, "r") as f:
        repos = [line.strip() for line in f if line.strip()]
    if not repos:
        print("[!] repos.txt is empty. Exiting.")
        exit()
    return repos

def get_repo_name(repo_url):
    name = repo_url.rstrip("/").split("/")[-1]
    return name.replace(".git", "")

def get_repo_hash(repo_url):
    try:
        output = subprocess.check_output(
            ["git", "ls-remote", repo_url, "HEAD"],
            stderr=subprocess.DEVNULL
        )
        return output.decode("utf-8").split()[0]
    except subprocess.CalledProcessError:
        return None

def backup_repo(repo_url):
    repo_hash = get_repo_hash(repo_url)
    if not repo_hash:
        print(f"[!] Failed to get hash: {repo_url}")
        return

    repo_name = get_repo_name(repo_url)

    if last_hashes.get(repo_name) == repo_hash:
        print(f"[=] No changes: {repo_name}")
        return

    last_hashes[repo_name] = repo_hash
    save_hashes()

    repo_dir = os.path.join(BACKUP_DIR, repo_name)

    if os.path.exists(repo_dir):
        subprocess.run(["rm", "-rf", repo_dir])

    print(f"[↑] Repository updated: {repo_name}")

    try:
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", repo_url, repo_dir],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"[✔] Backup completed: {repo_name}")
    except subprocess.CalledProcessError:
        print(f"[✘] Clone failed: {repo_url}")


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    global last_hashes
    last_hashes = load_hashes()

    while True:
        repos = get_repo_list()
        print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Checking {len(repos)} repositories...")
        for repo in repos:
            backup_repo(repo)
        time.sleep(CHECK_INTERVAL)




if __name__ == "__main__":
    main()
