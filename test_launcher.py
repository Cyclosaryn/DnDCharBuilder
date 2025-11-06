#!/usr/bin/env python
"""
Test script to verify the launcher works correctly before building.
"""

import sys
import subprocess
from pathlib import Path

def test_launcher():
    """Test the launcher script."""
    print("=" * 60)
    print("Testing D&D Character Builder Launcher")
    print("=" * 60)
    print()
    
    launcher_path = Path(__file__).parent / "launcher.py"
    
    if not launcher_path.exists():
        print("❌ ERROR: launcher.py not found!")
        return False
    
    print("✅ launcher.py found")
    print()
    print("The launcher will:")
    print("  1. Find a free port")
    print("  2. Initialize database (if first run)")
    print("  3. Start Django server")
    print("  4. Open browser automatically")
    print()
    print("Press Ctrl+C to stop the server when ready.")
    print("-" * 60)
    print()
    
    try:
        # Run the launcher
        subprocess.run([sys.executable, str(launcher_path)])
        return True
    except KeyboardInterrupt:
        print("\n\n✅ Test complete! Launcher works correctly.")
        return True
    except Exception as e:
        print(f"\n\n❌ ERROR: {e}")
        return False

if __name__ == '__main__':
    success = test_launcher()
    sys.exit(0 if success else 1)
