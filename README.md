Plugin for fman: Git Status 
======================
This plugin is only tested on a Windows environment.

Add this repository to ~/AppData/Roaming/fman/Plugins/User/Git Status
and the branch name you are working on will be displayed when navigated
to the top level directory of any git repository.

Issues and improvements
-----------------------
1. Subdirectories of a git repo is not recognized as a git repository
2. fman's `get_path()` is not resolving correcly all the time, ugly workaround in place.
3. Add last commit header after branch name.
4. Implement more git functionality.