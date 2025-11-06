# 🎉 What's New - Must-Have D&D 5e Features!

## 🆕 New Character Sheet Features

Your D&D Character Builder now includes essential D&D 5e tracking features!

### 📖 Languages & Proficiencies
**Now automatically populated during character creation!**

- **Languages**: Your character's racial language is automatically added
  - Dwarves start with Common & Dwarvish
  - Elves start with Common & Elvish
  - Tieflings start with Common & Infernal
  - And more! Fully editable during creation.

- **Tool Proficiencies**: Auto-filled from your background
  - Example: Criminals get Thieves' Tools
  - Example: Guild Artisans get Artisan's Tools
  - Fully editable during creation.

### ⚔️ Combat Tracking Enhancements

Your character sheet now tracks:

1. **✨ Inspiration** 
   - Shows golden star icon when you have inspiration
   - Track your advantage on rolls!

2. **💀 Death Saves**
   - Track successes (0-3) and failures (0-3)
   - Displayed in green/red when making death saves
   - Essential for when your HP reaches 0

3. **🛡️ Temporary Hit Points**
   - Separate from regular HP
   - Shown next to your HP total
   - First buffer against damage

4. **😴 Exhaustion Levels**
   - Track exhaustion from 0-6
   - Displayed with tired icon
   - Know when you're pushing too hard

5. **⚠️ Active Conditions**
   - Track multiple conditions at once
   - Examples: Poisoned, Stunned, Frightened
   - See all active effects at a glance

## 📍 Where to Find These Features

### During Character Creation (Step 3)
- **Languages field**: Auto-filled based on your race
- **Tool Proficiencies field**: Auto-filled based on your background
- Both are editable - add extra languages or tools as needed!

### On Your Character Sheet
Look for the new sections:
- **"Languages & Proficiencies" card** (left column)
- **Enhanced "Combat Stats" card** with:
  - Temp HP display
  - Death saves (when applicable)
  - Exhaustion level (when applicable)
  - Active conditions (when applicable)
- **Inspiration indicator** in Character Information

### In the Admin Panel
All new fields are organized in the admin interface:
- **Combat & Survival** section for tracking during play
- **Languages & Proficiencies** section for character details

## 🎮 How to Use

### Setting Up a New Character
1. Create character as normal through Steps 1-2
2. In **Step 3**, languages and tool proficiencies are **auto-filled**
3. Edit them if needed (add bonus languages, etc.)
4. Complete character creation

### During Play
Use the **Django Admin** to update:
- Mark inspiration when earned
- Track death saves during combat
- Add temporary HP from spells/abilities
- Track exhaustion from forced marches
- Note active conditions from spells/effects

## 🔮 Coming Soon

We're working on even more features:
- 📦 **Starting Equipment Packages** - Class-specific gear recommendations
- ✨ **Spellcasting Management** - Track spell slots and known spells
- 🎲 **Quick Roll Buttons** - Click to roll skills, saves, and attacks
- 🏕️ **Rest Management** - One-click short and long rests
- ⚔️ **Weapon Attacks** - Track your weapons with auto-calculated bonuses

## 📋 D&D 5e Rules Compliance

All new features follow official D&D 5e 2014 rules:
- Languages from Player's Handbook Chapter 2 (Races)
- Tool proficiencies from Player's Handbook Chapter 4 (Backgrounds)
- Inspiration from Player's Handbook Chapter 8
- Death saves from Player's Handbook Chapter 9
- Exhaustion from Player's Handbook Chapter 8
- Conditions from Appendix A

## 💡 Tips

**For DMs:**
- Use the admin interface to quickly update conditions and exhaustion during play
- Award inspiration by checking the box in the admin
- Track death saves for unconscious characters

**For Players:**
- Your languages and tool proficiencies are now clearly visible
- Check your exhaustion level before taking long journeys
- Remember temp HP absorbs damage first!

## 🐛 Need Help?

All features have been tested and are ready to use. If you encounter any issues:
1. Check the admin interface for the character
2. Verify migrations have been applied (`python manage.py migrate`)
3. Create a new character to test the auto-population features

---

**Enjoy your enhanced D&D Character Builder!** 🎲⚔️✨
