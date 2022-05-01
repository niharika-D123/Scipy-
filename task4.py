from pydriller import Repository
from datetime import datetime
import re


for commit in Repository('https://github.com/scipy/scipy.git',since=datetime(2021, 10, 1)).traverse_commits():
   

    for file in commit.modified_files:
        if(re.search('^test',file.filename)):
            print(
            ' {},{},{},{},{}'.format(file.filename,commit.author_date,file.change_type.name,commit.committer_date,commit.author.name),
          

        )
