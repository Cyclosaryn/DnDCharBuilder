# Quick Start Guide

## Getting Started in 5 Minutes

### 1. Start the Server
```bash
cd /Users/michaelverbroekken/Repositories/DnDCharBuilder
source venv/bin/activate
python manage.py runserver
```

### 2. Access the Application
Open your browser and go to: **http://127.0.0.1:8000/**

### 3. Create Your First Character

1. Click **"Create New Character"**
2. Fill in the character name and select:
   - **Race** (e.g., Human, Elf, Dwarf)
   - **Class** (e.g., Fighter, Wizard, Rogue)
   - **Background** (e.g., Noble, Soldier, Acolyte)
3. Enter ability scores (use Standard Array: 15, 14, 13, 12, 10, 8)
4. Click **"Next: Select Skills"**
5. Choose your skill proficiencies (based on your class)
6. Click **"Next: Add Details"**
7. (Optional) Add personality traits and equipment
8. Click **"Create Character"**

### 4. View Your Character
You'll see a complete D&D 5e character sheet with:
- Ability scores and modifiers
- Skills with calculated bonuses
- Hit points, AC, initiative
- Personality and equipment

### 5. Access Admin Panel (Optional)
Create a superuser first:
```bash
python manage.py createsuperuser
```

Then visit: **http://127.0.0.1:8000/admin/**

## Quick Tips

### Standard Array for Ability Scores
Use these six numbers in any order: **15, 14, 13, 12, 10, 8**

### Popular Character Builds

**Tank Fighter:**
- Race: Dwarf
- Class: Fighter
- High Constitution and Strength

**Sneaky Rogue:**
- Race: Halfling
- Class: Rogue
- High Dexterity

**Wise Cleric:**
- Race: Human
- Class: Cleric
- High Wisdom

**Powerful Wizard:**
- Race: Elf
- Class: Wizard
- High Intelligence

## Navigation

- **Home** - Welcome page and overview
- **Characters** - List of all your characters
- **Create Character** - 3-step character creation wizard
- **Races** - Reference for all playable races
- **Classes** - Reference for all character classes
- **Backgrounds** - Reference for character backgrounds
- **Admin** - Database management interface

## Common Tasks

### Edit a Character
1. Go to "Characters"
2. Click on your character
3. Click "Edit" button
4. Make changes and save

### Delete a Character
1. Go to "Characters"
2. Click on your character
3. Click "Delete" button
4. Confirm deletion

### Add More Races/Classes/Backgrounds
1. Log into Admin panel
2. Navigate to Races, Classes, or Backgrounds
3. Click "Add" and fill in the details
4. Save

## Troubleshooting

**Server won't start?**
- Make sure virtual environment is activated: `source venv/bin/activate`
- Check if another server is running on port 8000

**Page not loading?**
- Verify server is running: look for "Starting development server at http://127.0.0.1:8000/"
- Check console for errors

**Database errors?**
- Run migrations: `python manage.py migrate`
- Repopulate data: `python manage.py populate_dnd_data`

## Need Help?

Consult the full README.md for detailed information about:
- Installation
- Project structure
- Advanced features
- Development guide

---

Happy adventuring! 🎲⚔️🐉
