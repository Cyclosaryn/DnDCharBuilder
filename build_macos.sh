#!/bin/bash
# Build script for macOS (without splash screen)

echo "======================================================================"
echo "D&D Character Builder - macOS Build (No Splash Screen)"
echo "======================================================================"
echo ""

# Check if PyInstaller is installed
if ! command -v pyinstaller &> /dev/null; then
    echo "❌ PyInstaller not found!"
    echo "   Install it with: pip install pyinstaller"
    exit 1
fi

echo "✅ PyInstaller found"
echo ""

# Clean previous builds
echo "🧹 Cleaning previous build..."
rm -rf build dist
echo "✅ Clean complete"
echo ""

# Build the application
echo "🔨 Building macOS application..."
echo "This may take 2-5 minutes..."
echo ""

pyinstaller build_macos.spec

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "======================================================================"
    echo "✅ Build Complete!"
    echo "======================================================================"
    echo ""
    echo "Your macOS application is in: dist/DnDCharBuilder.app"
    echo ""
    echo "To test the application:"
    echo "  open dist/DnDCharBuilder.app"
    echo ""
    echo "To distribute:"
    echo "  1. Right-click DnDCharBuilder.app and 'Compress'"
    echo "  2. Share the .zip file with macOS users"
    echo "  3. Users extract and run DnDCharBuilder.app"
    echo ""
    echo "See BUILD_INSTRUCTIONS.md for more details."
    echo "======================================================================"
else
    echo ""
    echo "❌ Build failed!"
    echo "Check the error messages above for details."
    exit 1
fi
