#!/bin/bash

# Initialize the Minecraft Server project by pulling code from GitHub

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Git is not installed. Please install Git and try again."
    exit 1
fi

# Clone the GitHub repository
REPO_URL="https://github.com/your-username/your-repo-name.git"
PROJECT_DIR="minecraft_server"

if [ -d "$PROJECT_DIR" ]; then
    echo "Directory $PROJECT_DIR already exists. Pulling latest changes..."
    cd $PROJECT_DIR
    git pull origin main
else
    echo "Cloning repository from $REPO_URL..."
    git clone $REPO_URL $PROJECT_DIR
    cd $PROJECT_DIR
fi

# Install required Python libraries
echo "Installing required Python libraries..."
pip install -r requirements.txt

echo "Project initialized successfully! Run 'python main.py' to start."