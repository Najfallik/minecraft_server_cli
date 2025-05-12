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
set REPO_URL=https://github.com/Najfallik/minecraft_server_cli.git
set PROJECT_DIR=minecraft_server_cli

if exist %PROJECT_DIR% (
    echo Directory %PROJECT_DIR% already exists. Pulling latest changes...
    cd %PROJECT_DIR%
    git pull origin master
) else (
    echo Cloning repository from %REPO_URL%...
    git clone %REPO_URL% %PROJECT_DIR%
    cd %PROJECT_DIR%
)

REM Install required Python libraries
echo Installing required Python libraries...
pip install -r requirements.txt

REM Ask if the user wants to run the interface
set /p RUN_INTERFACE="Do you want to run the interface now? (y/N): "

if /i "%RUN_INTERFACE%"=="y" (
    echo Running the interface...
    cls
    python main.py
) else (
    echo Project initialized successfully! Run 'python main.py' to start the interface.
)

pause