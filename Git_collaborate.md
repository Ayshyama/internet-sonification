1. clone repository
```
git clone https://github.com/Ayshyama/forTutoring
```
2. check remote
```
git remote -v
```
3. if remote is not Ayshyama/forTutoring, then add remote
```
git remote add origin https://github.com/Ayshyama/forTutoring.git
```

# If you want to have the same repository inside your Git account, you can fork it.

- When you fork a project, you essentially create a copy of the original (upstream) repository under your own GitHub account. 
- This gives you full control over your forked repository, and you can push updates to it as you wish. 

## Working with forks:

### Two Remote Repositories

- Origin: This is your forked repository. When you clone your fork to your local machine, 
- Git automatically names this remote "origin".

- Upstream: This is the original repository that you forked. 
- Generally, you would add this as a second remote named "upstream" to pull in changes from the original project.

## Pulling Updates from the Original Repository(Upstream)

1. Navigate to Local Repository: Open your terminal and navigate to the directory of your local Git repository.
2. Add Upstream Remote: If you haven't already added the original repository as an "upstream" remote, you can do so with:
```
git remote add upstream https://github.com/original_owner/original_repository.git
```
or ssh
```
git remote add upstream git@github.com:original_owner/original_repository.git
```
3. verify remote (you should see origin and upstream) 
```
git remote -v
```
4. Fetch and Merge Changes from Upstream (original repo)
- Fetch will only download the changes from the upstream repository, but not merge them with your local commits.
- Before pushing new changes, it's often good to fetch and merge changes from the "upstream" repository so that your fork stays up-to-date.
```
git fetch upstream
```
5. Checkout Branch: Make sure you are on the branch into which you want to merge the updates.
```
git branch
```
```
git checkout branch_name
```
6. Merge Changes: Merge the changes from the upstream repository's main branch into your local main branch.
```
git merge upstream/branch_name
```
7. Push to Your Fork: Finally, push these merged changes to your own forked repository on GitHub.
- Push Changes to Your Fork: After resolving any conflicts and committing your changes, you can push to your fork.
```
git push origin main
```

## Pulling Updates from Your Fork (Origin)
1. Navigate to Local Repository: Open your terminal and navigate to the directory of your local Git repository.
2. Checkout Branch: Make sure you are on the branch into which you want to merge the updates.
```
git checkout branch_name
```
3. Pull updates from your fork
```
git pull origin branch_name
```

### If you have set wrong remote origin or upstream follow these steps:
- to change remote origin
```
git remote set-url origin https://github.com/username/repository.git
```
- to change remote upstream
```
git remote set-url upstream https://github.com/username/repository.git
```

## Here's how you can manage where to push your updates:
- You generally can't push to upstream unless you are an authorized contributor.
- So, you can push to your fork: git push origin <branch_name>.
- Or ask for permission to push to upstream.
- Or create a pull request to propose changes to the upstream project.
- Most often, you'll be pushing to your own fork and then creating a pull request to propose changes to the upstream project.

## Decide Where to Push: Now you have two remotes: "origin" and "upstream".
- Push to your fork: git push origin <branch_name>
- You generally can't push to upstream unless you are an authorized contributor.

- Push to your fork: 
```
git push origin <branch_name>
```

- Push to upstream: 
```
git push upstream <branch_name>
```
- Fetch and Merge Changes from Upstream: Before pushing new changes, 
- it's often good to fetch and merge changes from the "upstream" repository so that your fork stays up-to-date.