'''
	This plugin is only tested on a Windows environment. 
	Add this repository to ~/AppData/Roaming/fman/Plugins/User/Git Status
	and the branch name you are working on will be displayed when navigated
	to the top level directory of any git repository.
'''

import os, sys
from fman import DirectoryPaneListener
from fman import show_status_message 

# Need to add the modules locally to get the plugin to work
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "git"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
    os.path.realpath(__file__))), "gitdb"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(
	os.path.realpath(__file__))), "smmap"))
	
from git import Repo

class VerifyGitRepo(DirectoryPaneListener):
	''' 
		This method listens for directory changes in the pane,
		checks if we are currently in a directory containing a .git
		and acts accordingly
	'''
	def on_path_changed(self):
		# Some times, get_path returns two paths, but the last is always correct
		try:
			current_path = self.pane.get_path().split("file://")[1]
		except:
			current_path = self.pane.get_path().split("file://")
		try:
			# This will throw an exception if it is not a repository here
			repo = Repo(current_path)
			branch_name = repo.active_branch
			show_status_message(branch_name.name)
		except:
			show_status_message("Not at a top level git repository")