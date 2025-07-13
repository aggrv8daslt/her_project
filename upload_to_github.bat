@echo off
set REPO_URL=https://github.com/aggrv8daslt/Her_project.git
set COMMIT_MSG=Updated project files

IF NOT EXIST .git (
    git init
    git remote add origin %REPO_URL%
)

REM Optional: Force reset main branch if needed
git branch -M main
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git add .
git commit -m "%COMMIT_MSG%"
git push -u origin main --force

pause
