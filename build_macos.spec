# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for D&D Character Builder - MACOS BUILD

This file creates a macOS .app bundle without splash screen.
"""

import os
import sys
from pathlib import Path

# Get the project root directory
root_dir = Path(SPECPATH)

# Collect all Django template files
template_files = []
for template_dir in ['characters/templates', 'characters/static']:
    if (root_dir / template_dir).exists():
        for root, dirs, files in os.walk(root_dir / template_dir):
            for file in files:
                src = Path(root) / file
                dst = Path(root).relative_to(root_dir)
                template_files.append((str(src), str(dst)))

# Collect migration files
migration_files = []
migration_dir = root_dir / 'characters' / 'migrations'
if migration_dir.exists():
    for file in migration_dir.glob('*.py'):
        migration_files.append((str(file), 'characters/migrations'))

# Data files to include
datas = [
    # Templates and static files
    *template_files,
    # Migrations
    *migration_files,
    # Management commands
    ('characters/management', 'characters/management'),
]

# Hidden imports needed by Django
hiddenimports = [
    'django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.core.management',
    'django.core.management.commands',
    'django.core.management.commands.migrate',
    'django.core.management.commands.makemigrations',
    'django.db.backends.sqlite3',
    'characters',
    'characters.models',
    'characters.views',
    'characters.forms',
    'characters.admin',
    'characters.urls',
    'characters.apps',
    'characters.management',
    'characters.management.commands',
    'characters.management.commands.populate_dnd_data',
    'characters.class_features',
    'characters.subraces',
    'characters.spell_slots',
    'characters.damage_types',
    'characters.starting_equipment',
    'characters.widgets',
    'dndcharbuilder',
    'dndcharbuilder.settings',
    'dndcharbuilder.urls',
    'dndcharbuilder.wsgi',
    'sqlparse',
    'asgiref',
    'webview',
    'webview.window',
    'webview.menu',
    'webview.js',
    'webview.util',
    'webview.guilib',
    'webview.platforms',
    'webview.platforms.cocoa',  # macOS
    'pyobjc',
    'pyobjc_core',
    'objc',
    'Foundation',
    'AppKit',
    'WebKit',
]

# Analysis
a = Analysis(
    ['launcher.py'],
    pathex=[str(root_dir)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'numpy',
        'PIL',
        'scipy',
        'pandas',
    ],
    noarchive=False,
)

# Remove unnecessary files to reduce size
exclude_patterns = [
    'test',
    'tests',
    '__pycache__',
    '*.pyc',
    '*.pyo',
]

a.datas = [x for x in a.datas if not any(pattern in x[0] for pattern in exclude_patterns)]

# PYZ (Python zip archive)
pyz = PYZ(a.pure)

# EXE (Executable)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='DnDCharBuilder',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window for native GUI app
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='DnDCharBuilder.icns',  # Application icon
)

# BUNDLE (Create macOS .app bundle)
app = BUNDLE(
    exe,
    name='DnDCharBuilder.app',
    icon='DnDCharBuilder.icns',
    bundle_identifier='com.dndcharbuilder.app',
    info_plist={
        'NSPrincipalClass': 'NSApplication',
        'NSHighResolutionCapable': 'True',
        'LSBackgroundOnly': 'False',
        'CFBundleShortVersionString': '1.0.0',
        'CFBundleVersion': '1.0.0',
        'CFBundleDisplayName': 'D&D Character Builder',
        'NSHumanReadableCopyright': 'Copyright © 2025',
    }
)
