# How to Build D&D Character Builder

Complete guide for setting up, running, and building the D&D Character Builder application.

## Table of Contents

- [First-Time Setup](#first-time-setup)
- [Running the Application](#running-the-application)
- [Building Standalone App](#building-standalone-app)
- [Database Management](#database-management)
- [Troubleshooting](#troubleshooting)

---

## First-Time Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Installation Steps

1. **Create a virtual environment:**
```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**
```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run database migrations:**
```bash
python manage.py migrate
```

6. **Populate the database with D&D 5e data:**
```bash
python manage.py populate_dnd_data
```

7. **(Optional) Create a superuser for admin access:**
```bash
python manage.py createsuperuser
```

8. **Run the development server:**
```bash
python manage.py runserver
```

9. **Open your browser and visit:**
- Main app: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

---

## Running the Application

### Starting the Server

```bash
# Activate virtual environment (if not already activated)
source venv/bin/activate

# Start Django development server
python manage.py runserver

# Server will run on http://127.0.0.1:8000/
```

### Stopping the Server

Press `Ctrl + C` in the terminal to stop the server.

### Running on a Different Port

```bash
python manage.py runserver 8080  # Run on port 8080
python manage.py runserver 0.0.0.0:8000  # Allow external connections
```

---

## Building Standalone App

Build the application as a standalone executable that doesn't require Python installation.

### Prerequisites

Install PyInstaller:
```bash
pip install pyinstaller
```

### Build Process

1. **Activate virtual environment:**
```bash
source venv/bin/activate
```

2. **Build using the spec file:**
```bash
# macOS
pyinstaller build_macos.spec

# Windows
pyinstaller build_windows.spec

# Generic/Standalone
pyinstaller build_standalone.spec
```

3. **Locate the built application:**
```
dist/
└── DnDCharBuilder/
    ├── DnDCharBuilder          # Executable (macOS/Linux)
    ├── DnDCharBuilder.exe      # Executable (Windows)
    └── [supporting files]
```

### Running the Standalone App

**macOS/Linux:**
```bash
cd dist/DnDCharBuilder
./DnDCharBuilder
```

**Windows:**
```cmd
cd dist\DnDCharBuilder
DnDCharBuilder.exe
```

### First Run Behavior

On first run, the standalone app will:
1. Initialize a new SQLite database
2. Run migrations to create database schema
3. Populate with D&D 5e data (races, classes, spells, etc.)
4. Start the Django server
5. Automatically open your default web browser

### Distributing the App

**Option 1: Zip the entire folder**
```bash
cd dist
zip -r DnDCharBuilder.zip DnDCharBuilder/
```

**Option 2: Create a single-file executable**
- Modify the spec file to bundle everything into one executable
- See PyInstaller documentation for one-file builds

**Option 3: Create platform-specific installer**
- **macOS:** Create .dmg or .app bundle
- **Windows:** Use NSIS or Inno Setup to create installer
- **Linux:** Create .deb, .rpm, or AppImage

---

## Database Management

### Reset Database

If you need to completely reset the database:

```bash
# Delete the database file
rm db.sqlite3

# Run migrations
python manage.py migrate

# Repopulate with D&D data
python manage.py populate_dnd_data

# (Optional) Recreate superuser
python manage.py createsuperuser
```

### Reset Script (macOS/Linux)

Use the included reset script:
```bash
./reset_database.sh
```

### Backup Database

```bash
# Create a backup
cp db.sqlite3 db.sqlite3.backup

# Restore from backup
cp db.sqlite3.backup db.sqlite3
```

### Export Character Data

```bash
# Export all characters to JSON
python manage.py dumpdata characters.Character --indent 2 > characters_backup.json

# Import characters from JSON
python manage.py loaddata characters_backup.json
```

---

## Troubleshooting

### Server Won't Start

**Issue:** Port already in use
```
Error: That port is already in use.
```

**Solution:**
```bash
# Use a different port
python manage.py runserver 8080

# Or find and kill the process using port 8000
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

**Issue:** Module not found
```
ModuleNotFoundError: No module named 'django'
```

**Solution:**
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Database Errors

**Issue:** No such table
```
django.db.utils.OperationalError: no such table: characters_race
```

**Solution:**
```bash
# Run migrations
python manage.py migrate

# If that doesn't work, reset database
rm db.sqlite3
python manage.py migrate
python manage.py populate_dnd_data
```

**Issue:** Database is locked
```
sqlite3.OperationalError: database is locked
```

**Solution:**
- Close all connections to the database
- Restart the server
- If persistent, restart your computer

### Build Errors

**Issue:** PyInstaller not found
```
pyinstaller: command not found
```

**Solution:**
```bash
pip install pyinstaller
```

**Issue:** Module import errors during build
```
ModuleNotFoundError during build
```

**Solution:**
- Ensure all dependencies are in requirements.txt
- Check hiddenimports in the spec file
- Add missing modules to hiddenimports list

**Issue:** Template files not found in built app
```
TemplateDoesNotExist
```

**Solution:**
- Verify datas paths in spec file include templates
- Check that TEMPLATES setting in settings.py is correct

### Standalone App Issues

**Issue:** Browser doesn't open automatically

**Solution:**
- Manually open browser and go to the URL shown in terminal
- Check terminal output for the port number
- Visit: http://127.0.0.1:[PORT]/

**Issue:** Static files not loading (no CSS/images)

**Solution:**
- Ensure static files are included in the build
- Check that characters/static is in the datas list in spec file
- Verify STATIC_URL and STATIC_ROOT settings

**Issue:** Permission denied on macOS

**Solution:**
```bash
chmod +x dist/DnDCharBuilder/DnDCharBuilder
```

**Issue:** Windows SmartScreen warning

**Solution:**
- This is normal for unsigned executables
- Click "More info" → "Run anyway"
- To avoid: sign the executable with a code signing certificate

---

## Development Tips

### Running Tests

```bash
python manage.py test characters
```

### Creating Sample Data

```bash
# Create a sample character
python manage.py create_sample_character
```

### Django Shell

```bash
# Access Django shell for debugging
python manage.py shell

# Example: Query characters
from characters.models import Character
Character.objects.all()
```

### Collecting Static Files (for production)

```bash
python manage.py collectstatic
```

### Checking for Issues

```bash
python manage.py check
```

---

## Production Deployment

Before deploying to production:

1. **Update settings.py:**
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Change `SECRET_KEY` to a secure random string

2. **Use a production database:**
   - PostgreSQL (recommended)
   - MySQL/MariaDB

3. **Set up a production server:**
   - Gunicorn or uWSGI
   - Nginx or Apache as reverse proxy

4. **Enable HTTPS:**
   - Use Let's Encrypt for free SSL certificates

5. **Configure static files:**
   - Run `collectstatic`
   - Serve via CDN or web server

6. **Set up monitoring:**
   - Log errors and performance metrics
   - Use tools like Sentry

---

## Updating the Application

### Updating Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Applying New Migrations

```bash
python manage.py migrate
```

### Updating D&D Data

```bash
python manage.py populate_dnd_data
```

---

## Additional Resources

- **Django Documentation:** https://docs.djangoproject.com/
- **PyInstaller Manual:** https://pyinstaller.org/
- **D&D 5e SRD:** https://www.dndbeyond.com/sources/dnd/basic-rules-2014
- **Bootstrap Documentation:** https://getbootstrap.com/docs/

---

## Support

For issues or questions:
1. Check this guide's Troubleshooting section
2. Review Django documentation
3. Check the project's issue tracker (if applicable)

---

**Happy character building!** 🎲⚔️🐉
