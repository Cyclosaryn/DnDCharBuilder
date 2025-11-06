@echo off
REM Build script for creating the standalone D&D Character Builder application (Windows)

echo ======================================================================
echo D&D Character Builder - Standalone Application Builder
echo ======================================================================
echo.

REM Check if PyInstaller is installed
where pyinstaller >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo PyInstaller not found!
    echo Installing PyInstaller...
    pip install pyinstaller
    if %ERRORLEVEL% NEQ 0 (
        echo Failed to install PyInstaller
        exit /b 1
    )
)

echo PyInstaller found
echo.

REM Clean previous builds
if exist dist (
    echo Cleaning previous build...
    rmdir /s /q dist
)

if exist build (
    rmdir /s /q build
)

echo Clean complete
echo.

REM Run PyInstaller
echo Building standalone application...
echo This may take 2-5 minutes...
echo.

pyinstaller build_standalone.spec

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Build failed!
    echo Check the error messages above for details.
    exit /b 1
)

echo.
echo ======================================================================
echo Build Complete!
echo ======================================================================
echo.
echo Your standalone application is in: dist\DnDCharBuilder\
echo.
echo To run the application:
echo   cd dist\DnDCharBuilder
echo   DnDCharBuilder.exe
echo.
echo To distribute:
echo   1. Zip the entire dist\DnDCharBuilder folder
echo   2. Share with users
echo   3. Users extract and run DnDCharBuilder.exe
echo.
echo See BUILD_INSTRUCTIONS.md for more details.
echo ======================================================================
