"""
D&D 5e Spell Slot Progression Tables
Based on D&D Basic Rules 2014
"""

# Full caster progression (Wizard, Cleric, Druid, Bard, Sorcerer)
FULL_CASTER_SLOTS = {
    1: [2, 0, 0, 0, 0, 0, 0, 0, 0],
    2: [3, 0, 0, 0, 0, 0, 0, 0, 0],
    3: [4, 2, 0, 0, 0, 0, 0, 0, 0],
    4: [4, 3, 0, 0, 0, 0, 0, 0, 0],
    5: [4, 3, 2, 0, 0, 0, 0, 0, 0],
    6: [4, 3, 3, 0, 0, 0, 0, 0, 0],
    7: [4, 3, 3, 1, 0, 0, 0, 0, 0],
    8: [4, 3, 3, 2, 0, 0, 0, 0, 0],
    9: [4, 3, 3, 3, 1, 0, 0, 0, 0],
    10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
    11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
    12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
    13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
    14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
    15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
    16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
    17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
    18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
    19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
    20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
}

# Half caster progression (Paladin, Ranger)
HALF_CASTER_SLOTS = {
    1: [0, 0, 0, 0, 0, 0, 0, 0, 0],
    2: [2, 0, 0, 0, 0, 0, 0, 0, 0],
    3: [3, 0, 0, 0, 0, 0, 0, 0, 0],
    4: [3, 0, 0, 0, 0, 0, 0, 0, 0],
    5: [4, 2, 0, 0, 0, 0, 0, 0, 0],
    6: [4, 2, 0, 0, 0, 0, 0, 0, 0],
    7: [4, 3, 0, 0, 0, 0, 0, 0, 0],
    8: [4, 3, 0, 0, 0, 0, 0, 0, 0],
    9: [4, 3, 2, 0, 0, 0, 0, 0, 0],
    10: [4, 3, 2, 0, 0, 0, 0, 0, 0],
    11: [4, 3, 3, 0, 0, 0, 0, 0, 0],
    12: [4, 3, 3, 0, 0, 0, 0, 0, 0],
    13: [4, 3, 3, 1, 0, 0, 0, 0, 0],
    14: [4, 3, 3, 1, 0, 0, 0, 0, 0],
    15: [4, 3, 3, 2, 0, 0, 0, 0, 0],
    16: [4, 3, 3, 2, 0, 0, 0, 0, 0],
    17: [4, 3, 3, 3, 1, 0, 0, 0, 0],
    18: [4, 3, 3, 3, 1, 0, 0, 0, 0],
    19: [4, 3, 3, 3, 2, 0, 0, 0, 0],
    20: [4, 3, 3, 3, 2, 0, 0, 0, 0],
}

# Warlock has unique progression (Pact Magic)
WARLOCK_SLOTS = {
    1: [1, 0, 0, 0, 0, 0, 0, 0, 0],  # 1 slot, 1st level
    2: [2, 0, 0, 0, 0, 0, 0, 0, 0],  # 2 slots, 1st level
    3: [0, 2, 0, 0, 0, 0, 0, 0, 0],  # 2 slots, 2nd level
    4: [0, 2, 0, 0, 0, 0, 0, 0, 0],  # 2 slots, 2nd level
    5: [0, 0, 2, 0, 0, 0, 0, 0, 0],  # 2 slots, 3rd level
    6: [0, 0, 2, 0, 0, 0, 0, 0, 0],  # 2 slots, 3rd level
    7: [0, 0, 2, 0, 0, 0, 0, 0, 0],  # 2 slots, 3rd level
    8: [0, 0, 2, 0, 0, 0, 0, 0, 0],  # 2 slots, 3rd level
    9: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level
    10: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level
    11: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level (Mystic Arcanum 6th)
    12: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level
    13: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level (Mystic Arcanum 7th)
    14: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level
    15: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level (Mystic Arcanum 8th)
    16: [0, 0, 3, 0, 0, 0, 0, 0, 0],  # 3 slots, 3rd level
    17: [0, 0, 4, 0, 0, 0, 0, 0, 0],  # 4 slots, 3rd level (Mystic Arcanum 9th)
    18: [0, 0, 4, 0, 0, 0, 0, 0, 0],  # 4 slots, 3rd level
    19: [0, 0, 4, 0, 0, 0, 0, 0, 0],  # 4 slots, 3rd level
    20: [0, 0, 4, 0, 0, 0, 0, 0, 0],  # 4 slots, 3rd level
}

# Class to spell progression mapping
CLASS_SPELL_PROGRESSION = {
    'Wizard': 'full',
    'Cleric': 'full',
    'Druid': 'full',
    'Bard': 'full',
    'Sorcerer': 'full',
    'Paladin': 'half',
    'Ranger': 'half',
    'Warlock': 'warlock',
}


def get_spell_slots_for_level(class_name, level):
    """
    Get the spell slot progression for a class at a given level.
    
    Args:
        class_name: Name of the character class (e.g., 'Wizard', 'Paladin')
        level: Character level (1-20)
    
    Returns:
        List of 9 integers representing spell slots for levels 1-9,
        or None if the class is not a spellcaster
    """
    if class_name not in CLASS_SPELL_PROGRESSION:
        return None
    
    progression_type = CLASS_SPELL_PROGRESSION[class_name]
    
    if progression_type == 'full':
        return FULL_CASTER_SLOTS.get(level, [0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif progression_type == 'half':
        return HALF_CASTER_SLOTS.get(level, [0, 0, 0, 0, 0, 0, 0, 0, 0])
    elif progression_type == 'warlock':
        return WARLOCK_SLOTS.get(level, [0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    return None


def get_max_spell_level(class_name, level):
    """
    Get the maximum spell level a character can cast.
    
    Args:
        class_name: Name of the character class
        level: Character level (1-20)
    
    Returns:
        Maximum spell level (0-9) the character can cast
    """
    slots = get_spell_slots_for_level(class_name, level)
    if not slots:
        return 0
    
    # Find the highest spell level with at least 1 slot
    for spell_level in range(8, -1, -1):  # Check from 9th to 1st level
        if slots[spell_level] > 0:
            return spell_level + 1  # spell_level is 0-indexed, so add 1
    
    return 0  # No spell slots (shouldn't happen for spellcasters)


def set_spell_slots(character):
    """
    Set spell slots for a character based on their class and level.
    Updates the character instance but does not save it.
    
    Args:
        character: Character model instance
    """
    class_name = character.character_class.name
    level = character.level
    
    slots = get_spell_slots_for_level(class_name, level)
    
    if slots:
        # Set spell slots for levels 1-9
        for i in range(9):
            setattr(character, f'spell_slots_{i+1}_max', slots[i])
            # Reset used slots to 0 when updating max slots
            setattr(character, f'spell_slots_{i+1}_used', 0)
