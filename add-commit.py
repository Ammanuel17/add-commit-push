import subprocess
print ("sttarting  add-commit-push")
print ("git status")

subprocess.run(["git", "status", "."])
print ("git add -A")

subprocess.run(["git", "commit", "-m", "Automated commit"])
print ("git commit -m" )

subprocess.run(["git", "commit", "-m", "\"update files\""])
print ("git push")
subprocess.run(["git", "push"])