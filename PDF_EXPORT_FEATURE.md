# PDF Export Feature

## Overview
This feature adds the ability to export D&D character sheets to PDF format, mimicking the official D&D 5e 2014 character sheet design.

## Installation

1. Install the required dependency:
```bash
pip install reportlab
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to any character detail page
2. Click the "Print to PDF" button in the top button group
3. The PDF will be generated and downloaded automatically

## Features

The PDF export includes:

### Page 1 - Main Character Sheet
- **Header**: Character name, class & level, background, race, alignment, experience
- **Left Column**: 
  - Ability scores (with modifiers)
- **Center Column**: 
  - Inspiration, proficiency bonus, passive perception
  - Saving throws (with proficiency indicators)
  - Skills (all 18 skills with bonuses and proficiency indicators)
- **Right Column**:
  - Combat stats (AC, Initiative, Speed)
  - Hit points (max, current, temporary)
  - Hit dice
  - Death saves
  - Attacks & spellcasting section
  - Equipment list
  - Currency
- **Bottom Section**:
  - Personality traits
  - Ideals
  - Bonds
  - Flaws
  - Features & Traits
  - Proficiencies & Languages

### Page 2 - Spells & Details
- **Spellcasting Info** (for spellcasters):
  - Spellcasting ability
  - Spell save DC
  - Spell attack bonus
  - Spell slots by level
  - Cantrips
  - Spells organized by level (with prepared indicators)
- **Additional Notes**:
  - Character backstory or additional features

## Technical Details

### Files Modified/Created
1. `requirements.txt` - Added reportlab dependency
2. `characters/pdf_generator.py` - New file containing PDF generation logic
3. `characters/views.py` - Added `character_sheet_pdf` view function
4. `characters/urls.py` - Added URL route for PDF export
5. `characters/templates/characters/character_detail.html` - Added "Print to PDF" button

### Key Functions

#### `generate_character_sheet_pdf(character)`
Main function that generates the PDF. Takes a Character model instance and returns a BytesIO buffer containing the PDF.

#### Helper Functions
- `draw_box()` - Draws labeled boxes for stats
- `draw_circle_box()` - Draws circular ability score boxes
- `draw_checkbox()` - Draws checkboxes for proficiencies and death saves

### Design Philosophy
The PDF mimics the official D&D 5e 2014 character sheet layout, including:
- Two-page format
- Traditional layout with ability scores on left, skills in center, combat stats on right
- Checkboxes for proficiencies
- Circular ability score modifiers
- Proper formatting for spells, equipment, and features

## Customization

To customize the PDF layout, edit `characters/pdf_generator.py`:
- Adjust positioning by modifying the x/y coordinates (in inches)
- Change fonts and sizes using `c.setFont()`
- Modify box sizes in the `draw_box()` calls
- Add or remove sections as needed

## Notes

- The PDF is generated dynamically from the current character data
- All computed values (modifiers, bonuses, etc.) are calculated at PDF generation time
- The PDF uses the reportlab library for rendering
- Skills with expertise show doubled proficiency bonus automatically
- Saving throw proficiencies are determined from the character's class
- Equipment and spells are pulled from the character's current inventory

## Future Enhancements

Possible improvements:
- Add character portrait/image
- Include more detailed spell descriptions
- Add equipment weight calculations
- Include background feature details
- Add class feature descriptions in more detail
- Support for custom character sheet templates
- Export multiple characters at once
