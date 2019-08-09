import os, sys
from fman import DirectoryPaneCommand, DirectoryPaneListener
from fman import show_alert, show_status_message 

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "git"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "gitdb"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
	os.path.realpath(__file__))), "smmap"))
	
from git import Repo

repo = Repo("~/AppData/Roaming/fman/Plugins/User/Git Status")
branch = repo.active_branch

class SayHi(DirectoryPaneCommand):
	def __call__(self):
		show_status_message(branch.name)

class VerifyGitRepo(DirectoryPaneListener):
	def on_path_changed(self):
		current_path = self.pane.get_path()
		try:
			repo  = Repo(current_path).git_dir
			branch = repo.active_branch
			show_status_message(branch.name)
        	
		except:
			show_status_message("No active git repository")