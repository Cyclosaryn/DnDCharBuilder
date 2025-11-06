#!/bin/bash
# Build script for creating the standalone D&D Character Builder application

echo "======================================================================"
echo "D&D Character Builder - Standalone Application Builder"
echo "======================================================================"
echo ""

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "❌ PyInstaller not found!"
    echo "Installing PyInstaller..."
    pip install pyinstaller
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install PyInstaller"
        exit 1
    fi
fi

echo "✅ PyInstaller found"
echo ""

# Clean previous builds
if [ -d "dist" ]; then
    echo "🧹 Cleaning previous build..."
    rm -rf dist
fi

if [ -d "build" ]; then
    rm -rf build
fi

echo "✅ Clean complete"
echo ""

# Run PyInstaller
echo "🔨 Building standalone application..."
echo "This may take 2-5 minutes..."
echo ""

pyinstaller build_standalone.spec

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Build failed!"
    echo "Check the error messages above for details."
    exit 1
fi

echo ""
echo "======================================================================"
echo "✅ Build Complete!"
echo "======================================================================"
echo ""
echo "Your standalone application is in: dist/DnDCharBuilder/"
echo ""
echo "To run the application:"
echo "  cd dist/DnDCharBuilder"
echo "  ./DnDCharBuilder"
echo ""
echo "To distribute:"
echo "  1. Zip the entire dist/DnDCharBuilder folder"
echo "  2. Share with users"
echo "  3. Users extract and run DnDCharBuilder executable"
echo ""
echo "See BUILD_INSTRUCTIONS.md for more details."
echo "======================================================================"
