------- Git cheats --------

(if you created a repo after the files)



\# Map your local folder (which had the code existed from two yeas ago), to the repo (that you created just now)

git remote add origin git@github.com:sujeet-banerjee/Quantum\_py\_bits.git



\# For both pull and push.

git branch --set-upstream-to=origin/master





\# In case you had unrelated histories (say changes got into master for your files, while the git repo origin has just an initial README)

git merge master --allow-unrelated-histories



git push origin main

