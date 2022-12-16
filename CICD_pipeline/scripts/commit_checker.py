from github import Github
from datetime import datetime,timedelta
from pytz import timezone
import pytz
import os

g = Github("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")

repo = g.get_repo("UnpredictablePrashant/LearnDevOps")
branch = repo.get_branch("main")
sh = branch.commit.sha
current_time = str(datetime.now(pytz.timezone('GMT'))).split('.')[0].split(' ')

chu = []
for i in current_time[0].split('-'):
    chu.append(i)
for i in current_time[1].split(':'):
    chu.append(i)

commit = repo.get_commit(sha=sh)
commit_time = str(commit.commit.author.date).split(' ')
shu = []
for i in commit_time[0].split('-'):
    shu.append(i)
for i in commit_time[1].split(':'):
    shu.append(i)

a = datetime(int(chu[0]), int(chu[1]), int(chu[2]), int(chu[3]), int(chu[4]), int(chu[5]))
b = datetime(int(shu[0]), int(shu[1]), int(shu[2]), int(shu[3]), int(shu[4]), int(shu[5]))

print(a-b)
if a-b < timedelta(minutes=5):
    print("[+] Recent Commit Detected")
    print("[+] Testing")
    os.system('bash test_script.sh')
    if os.path.getsize('test.txt') == 0:
        print("[+] All Test Cases passed")
        print("[+] Deploying...")
        os.system("bash start.sh")
        print("[+] Deployment Done")
    else:
        print("[+] Test Cases Failed")
else:
    print("[+] No Recent Commit Detected")