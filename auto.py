import subprocess
import time

def git_auto_commit(comment):
    subprocess.run(["git", "status"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", comment])
    subprocess.run(["git", "push"])

while True:
    git_auto_commit("Update")
    time.sleep(10)  # Sleep for 10 seconds
