from lib.git import git_commit_and_push
from lib.status_checker import check_websites
import time

COMMIT_INTERVAL = 120  # Wait for 2 minutes before running again

while True:
    check_websites()
    git_commit_and_push()
    time.sleep(COMMIT_INTERVAL) 
