# D&D 5e Character Builder

A Django-based web application for creating and managing Dungeons & Dragons 5th Edition (2014 rules) characters.

## Features

- **Complete Character Creation**: Create characters with all core races, classes, and backgrounds from D&D 5e 2014 rules
- **Step-by-Step Builder**: Easy 3-step process for character creation
- **Automatic Calculations**: Automatically calculates ability modifiers, proficiency bonuses, skill bonuses, AC, and more
- **Character Management**: View, edit, and delete characters
- **Reference Library**: Browse available races, classes, and backgrounds
- **Responsive Design**: Beautiful Bootstrap-based UI that works on all devices
- **Admin Interface**: Full Django admin for managing game data

## Based on D&D 5e 2014 Rules

This character builder follows the official D&D 5th Edition rules from 2014, as found in the Basic Rules:
https://www.dndbeyond.com/sources/dnd/basic-rules-2014

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
cd /Users/michaelverbroekken/Repositories/DnDCharBuilder
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Populate the database with D&D 5e data:
```bash
python manage.py populate_dnd_data
```

6. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Open your browser and navigate to:
- Main app: http://127.0.0.1:8000/
- Admin interface: http://127.0.0.1:8000/admin/

## Usage

### Creating a Character

1. Click "Create New Character" from the home page
2. **Step 1**: Enter basic information, choose race/class/background, and assign ability scores
3. **Step 2**: Select skill proficiencies
4. **Step 3**: Add personality traits, equipment, and starting money
5. Click "Create Character" to finish

### Managing Characters

- **View**: Click on a character to see their complete character sheet
- **Edit**: Use the Edit button to modify character details
- **Delete**: Remove characters you no longer need

### Reference Pages

Browse the available options:
- **Races**: View all playable races with traits and bonuses
- **Classes**: See class features, hit dice, and proficiencies
- **Backgrounds**: Explore background features and equipment

## Project Structure

```
DnDCharBuilder/
├── characters/              # Main Django app
│   ├── models.py           # Character, Race, Class, Background models
│   ├── views.py            # Views for character creation and management
│   ├── forms.py            # Forms for character creation
│   ├── admin.py            # Admin interface configuration
│   ├── urls.py             # URL routing
│   ├── templates/          # HTML templates
│   │   └── characters/     # Character-specific templates
│   └── management/         # Custom management commands
│       └── commands/
│           └── populate_dnd_data.py  # Populate initial D&D data
├── dndcharbuilder/         # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── db.sqlite3             # SQLite database (created after migration)
```

## Models

### Race
- Basic racial information (name, description, size, speed)
- Ability score bonuses
- Special traits

### CharacterClass
- Class information (name, description, hit die)
- Proficiencies (armor, weapons, tools, saving throws)
- Available skill choices

### Background
- Background description
- Skill and tool proficiencies
- Starting equipment
- Special feature

### Character
- All character information (name, level, abilities, etc.)
- Automatic calculation of modifiers and bonuses
- Skill proficiencies
- Personality traits
- Equipment and money

### Spell & CharacterSpell
- Spell information (level, school, description)
- Character spell relationships

## Features in Detail

### Ability Scores
- Manual entry of base ability scores
- Automatic application of racial bonuses
- Automatic calculation of ability modifiers

### Skills
- 18 D&D 5e skills
- Automatic calculation of skill bonuses
- Proficiency bonus based on character level

### Combat Stats
- Armor Class (AC) - base 10 + DEX modifier
- Initiative - DEX modifier
- Proficiency Bonus - calculated by level
- Hit Points - based on class hit die + CON modifier

### Character Progression
- Supports levels 1-20
- Proficiency bonus scales correctly

## Admin Interface

Access the admin interface at `/admin/` to:
- Add/edit/delete races, classes, and backgrounds
- Manage characters
- Add spells
- View all database entries

## Development

### Adding New Data

You can add more races, classes, backgrounds, or spells through:
1. The Django admin interface (recommended for small additions)
2. Modifying the `populate_dnd_data.py` management command
3. Creating fixtures

### Customization

The app uses Bootstrap 5 for styling. To customize the appearance:
- Edit templates in `characters/templates/characters/`
- Modify CSS in the `base.html` template's `<style>` block
- Add custom CSS files in a `static/` directory

## Technologies Used

- **Django 5.2.7**: Web framework
- **SQLite**: Database (can be changed to PostgreSQL, MySQL, etc.)
- **Bootstrap 5**: Frontend framework
- **Python 3**: Programming language

## Future Enhancements

Potential features to add:
- Character export to PDF
- Spell management for spellcasters
- Character advancement (level up)
- Equipment calculator with weight/cost
- Dice roller integration
- Multi-user support with authentication
- Character sharing and collaboration
- Import/export characters (JSON)

## License

This project is for educational purposes. Dungeons & Dragons is a trademark of Wizards of the Coast LLC.

## Credits

Based on the D&D 5th Edition (2014) System Reference Document and Basic Rules.

## Support

For issues or questions about D&D 5e rules, consult:
- [D&D Beyond - Basic Rules 2014](https://www.dndbeyond.com/sources/dnd/basic-rules-2014)
- Official D&D Player's Handbook (2014)

---

**Note**: This is an unofficial tool and is not affiliated with or endorsed by Wizards of the Coast.
