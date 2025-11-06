# D&D 5e Character Builder - Project Summary

## Overview
A complete Django web application for creating and managing D&D 5th Edition (2014) characters. Built with Python, Django, Bootstrap 5, and SQLite.

## What's Included

### Core Features
✅ **Character Creation** - 3-step wizard process
✅ **Character Management** - View, edit, delete characters
✅ **Reference Library** - Browse races, classes, backgrounds
✅ **Automatic Calculations** - Modifiers, bonuses, AC, HP
✅ **Admin Interface** - Full CRUD for all game data
✅ **Responsive Design** - Works on desktop, tablet, mobile

### D&D 5e Content Included
- **9 Races**: Human, Elf, Dwarf, Halfling, Dragonborn, Gnome, Half-Elf, Half-Orc, Tiefling
- **12 Classes**: Fighter, Wizard, Rogue, Cleric, Ranger, Paladin, Barbarian, Bard, Druid, Monk, Sorcerer, Warlock
- **6 Backgrounds**: Acolyte, Criminal, Folk Hero, Noble, Sage, Soldier
- **Sample Character**: Thorin Ironforge (Human Fighter)

### Technical Stack
- **Backend**: Django 5.2.7
- **Database**: SQLite (easily upgradeable to PostgreSQL/MySQL)
- **Frontend**: Bootstrap 5, vanilla JavaScript
- **Python**: 3.8+

## File Structure

```
DnDCharBuilder/
├── characters/                          # Main Django app
│   ├── models.py                       # 6 models (Race, Class, Background, Character, Spell, CharacterSpell)
│   ├── views.py                        # 11 views (list, detail, create, update, delete)
│   ├── forms.py                        # 3 forms (creation, skills, details)
│   ├── admin.py                        # Admin interface for all models
│   ├── urls.py                         # URL routing
│   ├── templates/characters/           # 10 HTML templates
│   │   ├── base.html                   # Base template with Bootstrap
│   │   ├── home.html                   # Landing page
│   │   ├── character_list.html         # All characters
│   │   ├── character_detail.html       # Full character sheet
│   │   ├── character_create_step1.html # Step 1: Basics
│   │   ├── character_create_step2.html # Step 2: Skills
│   │   ├── character_create_step3.html # Step 3: Details
│   │   ├── character_edit.html         # Edit character
│   │   ├── character_confirm_delete.html
│   │   ├── race_list.html              # Race reference
│   │   ├── class_list.html             # Class reference
│   │   └── background_list.html        # Background reference
│   ├── management/commands/
│   │   ├── populate_dnd_data.py        # Seeds database with D&D content
│   │   └── create_sample_character.py  # Creates demo character
│   └── migrations/
├── dndcharbuilder/                     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/                               # Virtual environment (in .gitignore)
├── db.sqlite3                          # Database (in .gitignore)
├── manage.py                           # Django management script
├── requirements.txt                    # Python dependencies
├── README.md                           # Full documentation
├── QUICKSTART.md                       # Quick start guide
└── .gitignore                          # Git ignore file
```

## Database Schema

### Race
- Basic info: name, description, size, speed
- Ability bonuses: STR, DEX, CON, INT, WIS, CHA
- Traits: special racial features

### CharacterClass
- Basic info: name, description, hit_die
- Proficiencies: armor, weapons, tools, saving throws
- Skills: available choices and number to choose

### Background
- Basic info: name, description
- Proficiencies: skills, tools, languages
- Equipment: starting gear
- Feature: special background ability

### Character
- Identity: name, player_name, level, alignment
- Core: race, class, background (ForeignKeys)
- Abilities: 6 ability scores (base values)
- Combat: HP (max/current/temp), AC (calculated)
- Skills: 18 boolean fields for proficiency
- Personality: traits, ideals, bonds, flaws
- Inventory: equipment (text), money (5 coin types)
- Metadata: created_at, updated_at

### Spell
- Basic: name, level, school
- Casting: time, range, components, duration
- Details: description, available classes

### CharacterSpell
- Links characters to their spells
- Tracks prepared status

## Key Calculations

The Character model includes properties for automatic calculation:

```python
# Racial bonuses applied
total_strength = strength + race.strength_bonus

# Ability modifiers
strength_modifier = (total_strength - 10) // 2

# Proficiency bonus by level
proficiency_bonus = ((level - 1) // 4) + 2

# Armor Class (base, can be enhanced with armor)
armor_class = 10 + dexterity_modifier

# Initiative
initiative = dexterity_modifier

# Skill bonuses (with proficiency if applicable)
skill_bonus = ability_modifier + (proficiency_bonus if proficient else 0)
```

## Pages & Functionality

### 1. Home Page (/)
- Welcome message
- Quick links to create character or view list
- Feature overview cards
- Links to reference pages

### 2. Character List (/characters/)
- Grid of character cards
- Shows: name, level, race, class, HP, AC, speed
- Actions: View, Edit
- Create new character button
- Pagination (10 per page)

### 3. Character Detail (/characters/<id>/)
- Complete character sheet display
- 3-column layout:
  - Left: Basic info, combat stats, ability scores
  - Middle: Skills, features, money
  - Right: Personality, equipment, spells
- Edit and Delete buttons

### 4. Character Creation - Step 1 (/characters/create/step1/)
- Name and player name
- Race, class, background selection
- Ability score input (6 fields)
- Alignment
- Links to reference pages

### 5. Character Creation - Step 2 (/characters/create/step2/<id>/)
- 18 skill checkboxes
- Shows class skill allowance
- Shows background proficiencies

### 6. Character Creation - Step 3 (/characters/create/step3/<id>/)
- Personality traits, ideals, bonds, flaws
- Features and traits
- Equipment
- Starting money (5 coin types)

### 7. Character Edit (/characters/<id>/edit/)
- Update basic info, race, class, background
- Modify ability scores
- Note: Skills/personality edited in admin or future enhancement

### 8. Character Delete (/characters/<id>/delete/)
- Confirmation page
- Warning about permanent deletion

### 9. Race Reference (/races/)
- Cards for each race
- Shows size, speed, ability bonuses, traits

### 10. Class Reference (/classes/)
- Cards for each class
- Shows hit die, primary ability, proficiencies, skills

### 11. Background Reference (/backgrounds/)
- Cards for each background
- Shows proficiencies, equipment, features

### 12. Admin Interface (/admin/)
- Full CRUD for all models
- Inline editing for character spells
- Search and filtering

## Setup Commands

```bash
# Initial setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Database setup
python manage.py migrate
python manage.py populate_dnd_data
python manage.py create_sample_character

# Create admin user
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Access Points

- **Main App**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/
- **API**: None (future enhancement)

## Testing the App

1. **View Sample Character**: 
   - Go to Characters page
   - Click on "Thorin Ironforge"
   - See complete character sheet

2. **Create New Character**:
   - Click "Create New Character"
   - Complete all 3 steps
   - View your character sheet

3. **Browse References**:
   - Check out Races, Classes, Backgrounds
   - Learn about options before creating

4. **Admin Interface**:
   - Log in to /admin/
   - Add/edit races, classes, backgrounds
   - Manage characters

## Future Enhancements

Potential additions:
- [ ] User authentication & accounts
- [ ] Character export to PDF
- [ ] Spell management for casters
- [ ] Equipment with weight/cost
- [ ] Character advancement (level up)
- [ ] Dice roller
- [ ] Character sharing
- [ ] Import/export JSON
- [ ] Image uploads
- [ ] Class features by level
- [ ] More races/classes (Xanathar's, Tasha's, etc.)

## Compliance

This application follows D&D 5e 2014 rules from the System Reference Document (SRD) and Basic Rules, which are freely available under the Open Gaming License (OGL).

**Reference**: https://www.dndbeyond.com/sources/dnd/basic-rules-2014

## Notes

- Database uses SQLite for simplicity (production should use PostgreSQL)
- SECRET_KEY in settings.py should be changed for production
- DEBUG=True should be False in production
- Static files should be collected for production
- ALLOWED_HOSTS should be configured for production

---

**Status**: ✅ Fully Functional & Ready to Use

The application is complete and ready for character creation!
