import os
from datetime import datetime

# File to track commit count
COUNTER_FILE = "commit_count.txt"
LOG_FILE = "activity_log.txt"

def get_commit_count():
    if not os.path.exists(COUNTER_FILE):
        return 1
    with open(COUNTER_FILE, "r") as f:
        return int(f.read().strip()) + 1

def save_commit_count(count):
    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))

def write_log(count):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"Commit #{count} at {now}\n")

def git_commit(count):
    os.system("git add .")
    os.system(f'git commit -m "Auto commit #{count}"')
    os.system("git push")

def main():
    count = get_commit_count()
    write_log(count)
    save_commit_count(count)
    git_commit(count)

if __name__ == "__main__":
    main()