@echo off
echo Changing directory to the script location...
cd /d "C:\Users\lalka\OneDrive\DOCUME~1\GitHub\Conversionista\etl_converstionista"
if %errorlevel% neq 0 (
    echo Failed to change directory.
    pause
    exit /b %errorlevel%
)

echo Current directory is:
cd

echo Running the ETL pipeline...
python etl_sales_pipeline.py
if %errorlevel% neq 0 (
    echo Failed to run the Python script.
    pause
    exit /b %errorlevel%
)

pause