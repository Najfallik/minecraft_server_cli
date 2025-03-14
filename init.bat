@echo off
REM Initialize the Minecraft Server project by pulling code from GitHub

REM Check if git is installed
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo Git is not installed. Please install Git from https://git-scm.com/ and try again.
    pause
    exit /b
)

REM Clone the GitHub repository
set REPO_URL=https://github.com/your-username/your-repo-name.git
set PROJECT_DIR=minecraft_server

if exist %PROJECT_DIR% (
    echo Directory %PROJECT_DIR% already exists. Pulling latest changes...
    cd %PROJECT_DIR%
    git pull origin main
) else (
    echo Cloning repository from %REPO_URL%...
    git clone %REPO_URL% %PROJECT_DIR%
    cd %PROJECT_DIR%
)

REM Install required Python libraries
echo Installing required Python libraries...
pip install -r requirements.txt

echo Project initialized successfully! Run 'python main.py' to start.
pause