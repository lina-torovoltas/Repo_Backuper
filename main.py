import os
import time
import subprocess
import json
import shutil
from datetime import datetime




REPOS_FILE = "repos.txt"
HASHES_FILE = "hashes.json"
BACKUP_DIR = "backups"
CHECK_INTERVAL = 3600
TEMP_DIR = os.path.join(BACKUP_DIR, "__temp__")
last_hashes = {}



def load_hashes():
    if os.path.exists(HASHES_FILE):
        with open(HASHES_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes():
    with open(HASHES_FILE, "w") as f:
        json.dump(last_hashes, f, indent=2)


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

def get_full_repo_name(repo_url):
    parts = repo_url.rstrip("/").split("/")
    if len(parts) >= 2:
        username = parts[-2]
        reponame = parts[-1].replace(".git", "")
        return f"{username}/{reponame}"
    return repo_url

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

    full_name = get_full_repo_name(repo_url)
    archive_name = full_name.replace("/", "_") + ".zip"
    archive_path = os.path.join(BACKUP_DIR, archive_name)

    if last_hashes.get(full_name) == repo_hash:
        print(f"[=] No changes: {full_name}")
        return

    last_hashes[full_name] = repo_hash
    save_hashes()

    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    print(f"[↑] Repository updated: {full_name}")

    try:
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", repo_url, TEMP_DIR],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if os.path.exists(archive_path):
            os.remove(archive_path)

        shutil.make_archive(archive_path.replace(".zip", ""), 'zip', TEMP_DIR)
        print(f"[✔] Backup completed: {full_name}")
    except subprocess.CalledProcessError:
        print(f"[✘] Clone failed: {full_name}")
    finally:
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    global last_hashes
    last_hashes = load_hashes()

    while True:
        repos = get_repo_list()
        print(f"\n[∞] [{datetime.now().strftime('%H:%M:%S')}] Checking {len(repos)} repositories...")
        for repo in repos:
            backup_repo(repo)
        print(f"[∞] Checked backups of {len(repos)} repositories, waiting {CHECK_INTERVAL} seconds...")
        time.sleep(CHECK_INTERVAL)



if __name__ == "__main__":
    main()
