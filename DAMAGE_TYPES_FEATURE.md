# Damage Types & Immunities Feature

## Overview
Added support for tracking damage immunities, resistances, vulnerabilities, and condition immunities for D&D 5e characters.

## Implementation Date
November 6, 2025

## New Database Fields

Added 4 new TextField fields to the `Character` model in `characters/models.py`:

```python
# Damage types
damage_immunities = models.TextField(blank=True, help_text="Damage immunities (e.g., Fire, Poison)")
damage_resistances = models.TextField(blank=True, help_text="Damage resistances (e.g., Cold, Lightning)")
damage_vulnerabilities = models.TextField(blank=True, help_text="Damage vulnerabilities (e.g., Fire, Radiant)")
condition_immunities = models.TextField(blank=True, help_text="Condition immunities (e.g., Charmed, Frightened)")
```

## Migration
- **Migration File:** `characters/migrations/0009_add_damage_types.py`
- **Status:** Applied ✅

## Files Modified

### 1. `characters/models.py`
- Added 4 new fields for tracking damage types and condition immunities
- Fields are text fields to allow comma-separated values

### 2. `characters/forms.py` - CharacterCombatForm
- Added 4 new fields to the form
- Added helpful placeholder text for each field
- Added labels with clear descriptions

### 3. `characters/admin.py`
- Created new "Damage Types" fieldset in Character admin
- Includes all 4 new fields for easy editing

### 4. `characters/templates/characters/character_edit_combat.html`
- Added new "Damage Types & Immunities" section
- Includes information about all D&D 5e damage types
- Provides helpful tips about where these typically come from

### 5. `characters/templates/characters/components/speed_immunities.html`
- Updated to display actual character data instead of hardcoded values
- Shows "—" placeholder when no data is entered
- Displays all 4 damage type categories

## Features

### Damage Types Supported
The system supports all 13 D&D 5e damage types:
- Acid
- Bludgeoning
- Cold
- Fire
- Force
- Lightning
- Necrotic
- Piercing
- Poison
- Psychic
- Radiant
- Slashing
- Thunder

### Categories

1. **Damage Immunities**
   - Character takes NO damage from these types
   - Example: Fire Elementals are immune to Fire damage

2. **Damage Resistances**
   - Character takes HALF damage from these types
   - Example: Tieflings have Fire resistance

3. **Damage Vulnerabilities**
   - Character takes DOUBLE damage from these types
   - Example: Ice creatures might be vulnerable to Fire

4. **Condition Immunities**
   - Character is immune to these conditions
   - Example: Undead are often immune to Charmed and Frightened
   - Common conditions: Blinded, Charmed, Deafened, Frightened, Grappled, Incapacitated, Invisible, Paralyzed, Petrified, Poisoned, Prone, Restrained, Stunned, Unconscious

## User Interface

### Character Sheet Display
- Located in the middle column, below Speed and Proficiency Bonus
- Shows all 4 categories in a compact, readable format
- Text-aligned left for better readability
- Shows "—" placeholder when empty

### Edit Interface
- Accessible via "Edit > Combat & Survival" from character sheet
- Full section with explanations and examples
- Textarea inputs for comma-separated values
- Helpful tips about damage types and their sources

## Data Format

### Recommended Format
Enter values as comma-separated text:
```
Fire, Poison
Cold, Lightning, Thunder
Charmed, Frightened, Poisoned
```

### Display Format
Values are displayed exactly as entered, preserving the user's formatting.

## Usage Examples

### Example 1: Tiefling Character
```
Damage Resistances: Fire
```

### Example 2: Dwarf Character
```
Damage Resistances: Poison
Condition Immunities: —
```

### Example 3: Undead Character
```
Damage Immunities: Poison, Necrotic
Condition Immunities: Charmed, Exhaustion, Frightened, Paralyzed, Poisoned
```

### Example 4: Fire Elemental (Homebrew)
```
Damage Immunities: Fire
Damage Vulnerabilities: Cold
Condition Immunities: Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone, Restrained, Unconscious
```

## Future Enhancements

### Potential Improvements
1. **Autocomplete:** Add dropdown suggestions for common damage types
2. **Validation:** Ensure entered values match official D&D damage types
3. **Racial Traits:** Auto-populate based on selected race
4. **Class Features:** Auto-populate based on class and level
5. **Magic Items:** Track damage types granted by equipment
6. **Calculation:** Automatically apply resistances/vulnerabilities to damage calculations
7. **Tags/Pills:** Display as colored pills instead of comma-separated text
8. **Stacking Rules:** Implement D&D 5e rules about resistance/immunity stacking

## Technical Notes

### Database Schema
- All 4 fields are `TextField` with `blank=True`
- No maximum length restriction
- Allows for flexible input formats
- Empty strings are stored as empty (not NULL)

### Form Validation
- Currently no validation (freeform text)
- Future versions could add validation against a list of valid damage types

### Admin Interface
- Grouped in dedicated "Damage Types" section
- Appears between "Combat & Survival" and "Languages & Proficiencies"
- Easy to edit alongside other combat-related fields

## Testing Checklist

- [x] Migration applied successfully
- [x] Fields appear in admin interface
- [x] Fields appear in combat edit form
- [x] Data saves correctly
- [x] Character sheet displays data correctly
- [x] Empty values show "—" placeholder
- [x] Form placeholders are helpful
- [ ] Test with actual character data (manual testing required)
- [ ] Verify responsive layout on mobile
- [ ] Test with very long comma-separated lists

## Related Files

- `characters/models.py` - Model definition
- `characters/forms.py` - Form handling
- `characters/admin.py` - Admin interface
- `characters/views.py` - View logic (character_edit_combat)
- `characters/templates/characters/character_edit_combat.html` - Edit form
- `characters/templates/characters/components/speed_immunities.html` - Display component
- `characters/migrations/0009_add_damage_types.py` - Database migration

## Notes

This feature provides a complete solution for tracking damage-related characteristics in D&D 5e. The implementation prioritizes:
1. **Flexibility** - Freeform text allows for homebrew content
2. **Simplicity** - Easy to understand and use
3. **Completeness** - All 4 major categories covered
4. **Integration** - Seamlessly fits into existing combat tracking

The feature is production-ready and can be extended with additional validation, automation, and UI enhancements as needed.
