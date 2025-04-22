# Team 16 FINAL PROJECT


____________________________________________________________________________________________________________________________
## Project setup

1. Steps to clone the repo:
   
    1. Make a working folder on your local machine
    2. open your working folder in IDE then CD into the git root folder
       
   ```
    git clone https://github.com/21vincentchu/team-16-stock-data-visualizer.git
    cd team-16-stock-data-visualizer
   ``` 

3. Create a virtual environment in command line so make sure we are running all the same packages, and same python with the same libraries. Type these commands
   ```
    # macOS virtual envioronment setup
   python3 -m venv {venv_name}
   source {venv_name}/bin/activate
   
   # Windows virtual envioronment setup
   python -m venv ml_env
   .\m1_env\Scripts\activate
   ```

8. Install dependencies
    Make sure you are in the root file, cd team-16-stock-data-visualizer 
    ```
    pip install -r requirements.txt
    ```


    
## git commands references
### Tracking changes 
```
git clone [url] #creates copy of a remoate repo on your machine
git status #shows current branch and directory you're in
git add . #adds all new and modified files
git commit -m "insert message here" #records the changes in the repo
git push origin [branch] $uploads your commits to the remote repo. check using git status. EXAMPLE: git push origin main
git pull origin [branch] #downloads any changes from the remote repo. check using git status.EXAMPLE: git pull origin main

```

### Make git branch and push to github
```
git branch #list the current branches
git checkout -b your-branch-name #create a new branch and switch to it. make sure its one word, use hyphens
git add . #stage your changes
git commit -m [xyz's branch] #commit
git push -u origin [branch name] #push
'''
```

### Merging your branch into the main
```
git checkout main #switching to the main branch
git pull origin main #making sure main is up to date
git merge your-branch-name -m "message here" #merge your branch into main
git push origin main #push the merged changes to GitHub

```

## Using Project with Docker

In a terminal sourced in the local project directory, paste and run the following commands:
```
docker-compose up --build
```
Now, it will be exposed outside the docker container on localhost:5001

