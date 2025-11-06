# D&D Character Builder

A Django-based web application for creating and managing Dungeons & Dragons 5th Edition characters with full spellcasting support, leveling system, and comprehensive character management.

## Features

- **Complete Character Creation** - 4-step wizard for spellcasters, 3-step for martial classes
- **Spell System** - Full spellcasting with 82+ spells from D&D 5e SRD
- **Level-Up System** - Complete advancement with ASI/Feats and class features
- **Combat Tracking** - HP, temp HP, death saves, exhaustion, conditions
- **Rest Management** - Short and long rest mechanics with resource restoration
- **Expertise System** - Bard and Rogue expertise selection with validation
- **Damage Types** - Track immunities, resistances, and vulnerabilities
- **Reference Library** - Browse races, classes, backgrounds, and spells
- **Responsive Design** - Bootstrap 5 UI that works on all devices
- **Admin Interface** - Full Django admin for managing game data

## Quick Start

```bash
# Activate virtual environment
source venv/bin/activate

# Run server
python manage.py runserver

# Visit http://127.0.0.1:8000/
```

For first-time setup or detailed build instructions, see **[HOWTOBUILD.md](HOWTOBUILD.md)**

## D&D 5e Content

Based on D&D 5th Edition (2014) rules from the System Reference Document:
- **9 Races** - Human, Dwarf, Elf, Halfling, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling
- **12 Classes** - All core classes with full level progression
- **6+ Backgrounds** - Acolyte, Criminal, Folk Hero, Noble, Sage, Soldier
- **82+ Spells** - Complete spell list from D&D 5e Basic Rules

## Project Structure

```
DnDCharBuilder/
├── characters/              # Main Django app
│   ├── models.py           # Database models (Race, Class, Character, Spell, etc.)
│   ├── views.py            # View logic (20+ views)
│   ├── forms.py            # Character forms (10+ forms)
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, images
│   └── management/         # Custom Django commands
├── dndcharbuilder/         # Django project settings
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Technologies

- **Backend:** Django 5.2.7, Python 3.8+
- **Database:** SQLite (upgradable to PostgreSQL/MySQL)
- **Frontend:** Bootstrap 5, JavaScript, HTML5/CSS3

## Key Features

### Automatic Calculations
- Ability modifiers from scores
- Proficiency bonuses by level
- Skill bonuses with expertise support
- Spell save DC and attack bonus
- Armor class and initiative

### Character Management
- Create characters with 3 or 4-step wizard
- Level up with HP rolling and ASI/Feats
- Take short and long rests
- Track combat statistics
- Manage spells (known, prepared, slots)

### Spellcasting
- 82+ spells from D&D 5e SRD
- Spell slot tracking by class
- Prepared spell management
- Interactive spell tooltips
- Spell filtering by class and level

## Standalone Application

Build as a desktop app without requiring Python:

```bash
# Install PyInstaller
pip install pyinstaller

# Build standalone app
pyinstaller build_standalone.spec

# Run from dist folder
./dist/DnDCharBuilder/DnDCharBuilder
```

See [HOWTOBUILD.md](HOWTOBUILD.md) for complete build instructions and distribution options.

## Quick Commands

```bash
# Start server
python manage.py runserver

# Create admin user
python manage.py createsuperuser

# Reset database
python manage.py migrate --run-syncdb
python manage.py populate_dnd_data

# Access admin
# Visit http://127.0.0.1:8000/admin/
```

## License

Educational project. Dungeons & Dragons is a trademark of Wizards of the Coast LLC. This is an unofficial tool using content from the D&D 5e System Reference Document under the Open Gaming License.

## Credits

Based on D&D 5th Edition (2014) rules:
- https://www.dndbeyond.com/sources/dnd/basic-rules-2014
- Built with Django, Bootstrap 5, and Python
