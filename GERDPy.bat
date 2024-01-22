@echo off

REM Check if Python 3 is installed
python3 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3 is not installed. Please install it to run GERDPy.
    exit /b 1
)

REM Run the guiman.py script
python3 guiman.py
pause
