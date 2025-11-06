@echo off
REM Build script for Windows (with splash screen)

echo ======================================================================
echo D^&D Character Builder - Windows Build (With Splash Screen)
echo ======================================================================
echo.

REM Check if PyInstaller is installed
pyinstaller --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X PyInstaller not found!
    echo    Install it with: pip install pyinstaller
    exit /b 1
)

echo √ PyInstaller found
echo.

REM Clean previous builds
echo Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
echo √ Clean complete
echo.

REM Build the application
echo Building Windows application...
echo This may take 2-5 minutes...
echo.

pyinstaller build_windows.spec

REM Check if build was successful
if %errorlevel% equ 0 (
    echo.
    echo ======================================================================
    echo √ Build Complete!
    echo ======================================================================
    echo.
    echo Your Windows application is in: dist\DnDCharBuilder.exe
    echo.
    echo To test the application:
    echo   dist\DnDCharBuilder.exe
    echo.
    echo To distribute:
    echo   1. Share the DnDCharBuilder.exe file with Windows users
    echo   2. Users just double-click to run
    echo.
    echo Note: Windows may show a security warning on first run.
    echo Users should click "More info" then "Run anyway"
    echo.
    echo See BUILD_INSTRUCTIONS.md for more details.
    echo ======================================================================
) else (
    echo.
    echo X Build failed!
    echo Check the error messages above for details.
    exit /b 1
)
