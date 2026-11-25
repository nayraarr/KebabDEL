#!/bin/bash

# Ask for environment folder name
read -p "Enter the environment folder name (default: env): " ENV_FOLDER

if [ -z "$ENV_FOLDER" ]; then
    ENV_FOLDER="env"
fi

# Check if the specified env folder exists
if [ -d "$ENV_FOLDER" ]; then
    echo "Activating existing Django environment ($ENV_FOLDER)..."
    source "$ENV_FOLDER/bin/activate"
else
    echo "Creating a new Django environment ($ENV_FOLDER)..."
    python3 -m venv "$ENV_FOLDER"
    source "$ENV_FOLDER/bin/activate"
    echo "Virtual environment $ENV_FOLDER created and activated."
fi

# Install dependencies
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found in the working directory!"
    exit 1
fi

# Run Django migrations
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

PORT=8000

# Warn if port 8000 is already in use
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "[WARNING] Port $PORT is already in use."
    echo "          Please terminate the process using port $PORT and try again."
    exit 1
fi

# Start Django server
echo "Starting Django server on port $PORT..."
python manage.py runserver $PORT
