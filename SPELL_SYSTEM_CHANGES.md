# Spell System Changes

## Overview
Updated the spell system to:
1. **Restrict spell selection** - Only allow adding spells up to the character's maximum castable spell level
2. **Auto-set spell slots** - Automatically set max spell slots based on class and level
3. **Apply to all scenarios** - Character creation, editing, and leveling up

## New File: `characters/spell_slots.py`

### Spell Slot Progression Tables
- `FULL_CASTER_SLOTS` - Wizard, Cleric, Druid, Bard, Sorcerer (levels 1-20)
- `HALF_CASTER_SLOTS` - Paladin, Ranger (levels 1-20)
- `WARLOCK_SLOTS` - Warlock's unique Pact Magic progression (levels 1-20)
- `CLASS_SPELL_PROGRESSION` - Maps each class to its progression type

### Key Functions

#### `get_spell_slots_for_level(class_name, level)`
Returns a list of 9 integers representing spell slots for spell levels 1-9 at the given character level.

Example:
- Wizard Level 5: `[4, 3, 2, 0, 0, 0, 0, 0, 0]` (4 1st-level, 3 2nd-level, 2 3rd-level slots)
- Paladin Level 5: `[4, 2, 0, 0, 0, 0, 0, 0, 0]` (4 1st-level, 2 2nd-level slots)
- Warlock Level 5: `[0, 0, 2, 0, 0, 0, 0, 0, 0]` (2 3rd-level slots only)

#### `get_max_spell_level(class_name, level)`
Returns the highest spell level a character can cast at their current level.

Example:
- Wizard Level 1: `1` (can cast up to 1st-level spells)
- Wizard Level 5: `3` (can cast up to 3rd-level spells)
- Paladin Level 1: `0` (no spellcasting yet)
- Paladin Level 5: `2` (can cast up to 2nd-level spells)

#### `set_spell_slots(character)`
Updates a character's spell slots based on their class and level. Sets both max slots and resets used slots to 0. Does **not** save the character (caller must save).

## Updated Files

### `characters/forms.py`

#### `SpellManagementForm`
- Now imports `get_max_spell_level` from `spell_slots`
- Only creates spell selection fields for levels 0 (cantrips) through the character's max castable level
- Prevents characters from seeing/selecting spells they can't cast yet

**Before**: Showed all spell levels 0-9 regardless of character level
**After**: Only shows spell levels the character can actually cast

#### `SpellSlotsForm`
- Max spell slot fields are now **read-only** and **disabled**
- Only "used" spell slot fields are editable
- Max slots are automatically calculated and displayed

**Before**: Users could manually edit max spell slots
**After**: Max slots are auto-set based on class/level, only used slots are editable

### `characters/views.py`

#### `character_create_step4(pk)` - Character Creation Step 4
**Changes:**
- Imports `set_spell_slots` function
- Calls `set_spell_slots(character)` before displaying the form (GET)
- Calls `set_spell_slots(character)` when saving (POST)
- Only saves spellcasting ability from the form, not max spell slots

**Behavior:**
- Spell slots are automatically set when entering the spell selection page
- Spell slots are updated again when saving
- Only spells up to the character's max level are shown

#### `character_manage_spells(pk)` - Manage Spells (After Level Up / Edit)
**Changes:**
- Calls `set_spell_slots(character)` before displaying (GET)
- Calls `set_spell_slots(character)` when saving (POST)
- Updates success message to inform user that spell slots were set automatically

**Behavior:**
- Spell slots are recalculated every time this page is accessed
- Ensures spell slots are always correct for current level
- Only shows spells the character can currently cast

#### `character_level_up(pk)` - Level Up
**Changes:**
- Imports `set_spell_slots` from `spell_slots`
- For spellcasters, calls `set_spell_slots(character)` after increasing level
- Updates success message to mention automatic spell slot updates

**Behavior:**
- When a spellcaster levels up, spell slots are automatically updated
- User is informed that spell slots were updated automatically
- Redirects to spell management to review/update known spells

#### `character_spell_slots(pk)` - Manage Spell Slots
**Changes:**
- Calls `set_spell_slots(character)` before displaying (GET)
- Calls `set_spell_slots(character)` before saving (POST)
- Updates success message

**Behavior:**
- Max spell slots are always recalculated before displaying
- Only "used" slots can be edited by the user
- Max slots are protected from manual editing

## User Experience Changes

### Character Creation
1. User creates character (steps 1-3)
2. If spellcaster, proceeds to step 4
3. **Spell slots are automatically set** based on level 1 and class
4. User can only select cantrips and 1st-level spells (or higher if starting above level 1)
5. Spell slot max fields are read-only and show correct values

### Leveling Up
1. User levels up character
2. **Spell slots are automatically updated** to new level's values
3. User is redirected to spell management
4. Can now select spells up to their new maximum level
5. Previous spell selections are preserved

### Editing Spells
1. User accesses "Manage Spells" page
2. **Spell slots are recalculated** (in case class or level changed)
3. Can only select spells up to their current maximum level
4. Spell slots display shows correct max values

### Managing Spell Slots
1. User accesses "Manage Spell Slots" page
2. **Max slots are auto-set** and displayed as read-only
3. User can only edit "used" spell slots
4. Cannot accidentally set incorrect max values

## Validation

### Spell Level Restriction
- **Level 1 Wizard**: Can select cantrips and 1st-level spells only
- **Level 3 Wizard**: Can select cantrips, 1st, and 2nd-level spells
- **Level 5 Wizard**: Can select cantrips through 3rd-level spells
- **Level 1 Paladin**: Can only select cantrips (no spell slots yet)
- **Level 2 Paladin**: Can select cantrips and 1st-level spells
- **Level 5 Paladin**: Can select cantrips, 1st, and 2nd-level spells

### Spell Slot Values (Level 5 Examples)
- **Wizard**: 4/3/2 (4 1st, 3 2nd, 2 3rd-level slots)
- **Paladin**: 4/2 (4 1st, 2 2nd-level slots)
- **Warlock**: 2 (2 3rd-level Pact Magic slots)
- **Fighter**: No spell slots (not a spellcaster)

## Benefits

1. **Accuracy**: Spell slots always match D&D 5e rules
2. **Simplicity**: Users don't need to look up spell slot tables
3. **Safety**: Prevents incorrect spell slot values
4. **Consistency**: Same logic applies everywhere (creation, editing, leveling)
5. **Better UX**: Users can't select spells they can't cast
6. **Clear Feedback**: Success messages inform users when slots are auto-updated

## Testing

Tested with:
- Full casters (Wizard, Cleric, Druid, Bard, Sorcerer)
- Half casters (Paladin, Ranger)
- Warlock (unique progression)
- Non-spellcasters (Fighter) - correctly returns None/0

All spell slot progressions match D&D 5e Basic Rules 2014.
