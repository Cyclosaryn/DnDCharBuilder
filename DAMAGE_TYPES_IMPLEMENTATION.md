# Automatic Damage Types Implementation

This document explains how damage immunities, resistances, vulnerabilities, and condition immunities are automatically populated based on character race, subrace, and class.

## Overview

The system automatically computes damage types from:
1. **Race traits** - Parsed from the Race model's `traits` field
2. **Subrace data** - Extracted from subrace definitions in `subraces.py`
3. **Class features** - (Future expansion for class-specific immunities/resistances)

## Files Modified

### 1. `/characters/damage_types.py` (NEW)
Contains utility functions for parsing and aggregating damage types:

- `get_damage_resistance_from_subrace(race_name, subrace_name)` - Extracts resistance from subrace traits
- `get_damage_types_from_race(race)` - Parses race traits for damage types
- `get_damage_types_for_character(character)` - Main function that aggregates all sources
- `format_resistance_display(subrace_name)` - Formats special display text (e.g., for Dragonborn)

### 2. `/characters/models.py`
Added computed property methods to Character model:

```python
def get_computed_damage_immunities(self):
def get_computed_damage_resistances(self):
def get_computed_damage_vulnerabilities(self):
def get_computed_condition_immunities(self):
```

These methods call `get_damage_types_for_character()` and return formatted strings.

### 3. `/characters/views.py` - CharacterDetailView
Added context variables in `get_context_data()`:

```python
context['computed_damage_immunities'] = character.get_computed_damage_immunities()
context['computed_damage_resistances'] = character.get_computed_damage_resistances()
context['computed_damage_vulnerabilities'] = character.get_computed_damage_vulnerabilities()
context['computed_condition_immunities'] = character.get_computed_condition_immunities()
```

### 4. `/characters/templates/characters/components/speed_immunities.html`
Updated to display computed values:
- Shows computed immunities, resistances, vulnerabilities
- Added condition immunities display
- Special handling for Dragonborn (shows "Choose based on Draconic Ancestry" message)

## How It Works

### Subrace Damage Resistances
For subraces like Dragonborn dragon ancestries:

```python
# From subraces.py
{
    'name': 'Gold Dragon Ancestry',
    'traits': [
        'Damage Type: Fire',
        'Damage Resistance: You have resistance to fire damage.'
    ]
}
```

The system parses the trait text looking for patterns like:
- "resistance to [damage_type]"
- "resistance against [damage_type]"

Extracts: `Fire`

### Race Trait Parsing
For races with built-in traits:

```python
# From Race model
race.traits = "Dwarven Resilience: You have advantage on saving throws against poison, 
                and you have resistance against poison damage."
```

The system searches for keywords:
- "resistance to [type]" → adds to resistances
- "immunity to [type]" → adds to immunities

### Character Display

When viewing a character:
1. System checks race, subrace, class
2. Aggregates all damage types from each source
3. Removes duplicates
4. Formats as comma-separated list
5. Returns "—" if none found

### Special Cases

**Dragonborn:**
- Has 10 different dragon ancestries
- Each provides resistance to a specific damage type
- Display shows "(Choose based on Draconic Ancestry)" for resistances
- Actual resistance extracted from selected subrace

**Stout Halfling:**
- Has "advantage on saving throws against poison"
- Has "resistance against poison damage"
- System extracts: Resistance to Poison

## Supported Damage Types

The system recognizes these damage types:
- **Energy:** Acid, Cold, Fire, Lightning, Poison, Necrotic, Radiant, Thunder, Force, Psychic
- **Physical:** Slashing, Piercing, Bludgeoning

## Future Enhancements

To add more sources:

1. **Class Features:**
```python
def get_damage_types_from_class(character_class, level):
    # Barbarian Rage: resistance to physical damage
    # Monk features: immunity to poison/disease
    pass
```

2. **Equipment/Magic Items:**
```python
def get_damage_types_from_equipment(character):
    # Ring of Fire Resistance
    # Armor of Invulnerability
    pass
```

3. **Temporary Effects:**
```python
def get_damage_types_from_effects(character):
    # Active spells: Stoneskin, Protection from Energy
    # Temporary buffs
    pass
```

## Example Output

**Gold Dragonborn Sorcerer:**
- Immunities: —
- Resistances: Fire (from Gold Dragon Ancestry)
- Vulnerabilities: —
- Conditions: —

**Stout Halfling Rogue:**
- Immunities: —
- Resistances: Poison (from Stout Resilience)
- Vulnerabilities: —
- Conditions: —

**Human Fighter:**
- Immunities: —
- Resistances: —
- Vulnerabilities: —
- Conditions: —

## Database Fields

The original database fields remain for future use:
- `character.damage_immunities` (TextField)
- `character.damage_resistances` (TextField)
- `character.damage_vulnerabilities` (TextField)
- `character.condition_immunities` (TextField)

These can be used for:
- User overrides
- Temporary effects
- Magic item bonuses
- Custom homebrew traits

Current implementation prioritizes computed values for display, but stored values can be integrated later.
