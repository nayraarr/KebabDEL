@echo off

REM Ask for environment folder name
set /p ENV_FOLDER="Enter the environment folder name (default: env): "

if "%ENV_FOLDER%"=="" (
    set ENV_FOLDER=env
)

REM Check if env folder exists
if exist "%ENV_FOLDER%" (
    echo Activating existing Django environment...
    call "%ENV_FOLDER%\Scripts\activate"
) else (
    echo Creating a new Django environment...
    python -m venv "%ENV_FOLDER%"
    call "%ENV_FOLDER%\Scripts\activate"
    echo Virtual environment with name "%ENV_FOLDER%" created and activated.
)

REM Install dependencies
if exist requirements.txt (
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found in the working directory!
    exit /b 1
)

REM Run Django migrations
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

set PORT=8000

:: Check if port 8000 is already in use and warn
netstat -ano | findstr /r /c:":%PORT% " >nul
if %errorlevel% equ 0 (
    echo [WARNING] Port %PORT% is already in use.
    echo           Please terminate the process using port %PORT% and try again.
    exit /b 1
)

REM Start Django server
echo Starting Django server on port %PORT%...
python manage.py runserver %PORT%
