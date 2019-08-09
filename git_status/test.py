import os, sys


sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "git"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "gitdb"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "gitdb\\ext\\smmap"))


print(sys.path)
""" from ..git import Repo
repo = Repo(os.getcwd())
branch = repo.active_branch
print (branch.name) """