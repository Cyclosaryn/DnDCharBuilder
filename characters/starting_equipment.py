"""
D&D 5e Starting Equipment Packages by Class

Based on D&D 5e Basic Rules and Player's Handbook
"""

STARTING_EQUIPMENT_PACKAGES = {
    'Fighter': {
        'gold_roll': '5d4*10',  # Roll 5d4 and multiply by 10 for starting gold
        'packages': [
            {
                'name': 'Chainmail & Martial Weapon',
                'description': 'Heavy armor specialist',
                'equipment': [
                    'Chainmail',
                    'Shield',
                    'Longsword',
                    'Handaxe (2)',
                    'Explorer\'s Pack',
                    'Javelin (4)',
                ],
                'additional_notes': 'AC 18 with shield, good for frontline tanking'
            },
            {
                'name': 'Leather Armor & Ranged Weapon',
                'description': 'Dexterous fighter',
                'equipment': [
                    'Leather Armor',
                    'Longbow',
                    'Arrow (20)',
                    'Shortsword (2)',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Mobile combatant with ranged option'
            },
        ]
    },
    'Wizard': {
        'gold_roll': '4d4*10',
        'packages': [
            {
                'name': 'Quarterstaff Build',
                'description': 'Classic wizard',
                'equipment': [
                    'Quarterstaff',
                    'Component Pouch',
                    'Scholar\'s Pack',
                    'Spellbook',
                    'Dagger',
                ],
                'additional_notes': 'Versatile weapon, components for spells'
            },
            {
                'name': 'Dagger Build',
                'description': 'Subtle caster',
                'equipment': [
                    'Dagger',
                    'Arcane Focus',
                    'Explorer\'s Pack',
                    'Spellbook',
                ],
                'additional_notes': 'Lightweight, focus for easier casting'
            },
        ]
    },
    'Cleric': {
        'gold_roll': '5d4*10',
        'packages': [
            {
                'name': 'Mace & Shield',
                'description': 'Defensive cleric',
                'equipment': [
                    'Mace',
                    'Scale Mail',
                    'Shield',
                    'Holy Symbol',
                    'Priest\'s Pack',
                    'Light Crossbow',
                    'Crossbow Bolt (20)',
                ],
                'additional_notes': 'High AC, good for frontline support'
            },
            {
                'name': 'Warhammer',
                'description': 'Offensive cleric',
                'equipment': [
                    'Warhammer',
                    'Chainmail',
                    'Holy Symbol',
                    'Priest\'s Pack',
                    'Javelin (5)',
                ],
                'additional_notes': 'Heavy hitter, martial weapon'
            },
        ]
    },
    'Rogue': {
        'gold_roll': '4d4*10',
        'packages': [
            {
                'name': 'Rapier Build',
                'description': 'Finesse fighter',
                'equipment': [
                    'Rapier',
                    'Shortbow',
                    'Arrow (20)',
                    'Leather Armor',
                    'Burglar\'s Pack',
                    'Thieves\' Tools',
                    'Dagger (2)',
                ],
                'additional_notes': 'High damage finesse weapon'
            },
            {
                'name': 'Shortsword Build',
                'description': 'Two-weapon fighter',
                'equipment': [
                    'Shortsword (2)',
                    'Shortbow',
                    'Arrow (20)',
                    'Leather Armor',
                    'Burglar\'s Pack',
                    'Thieves\' Tools',
                ],
                'additional_notes': 'Dual-wielding option'
            },
        ]
    },
    'Ranger': {
        'gold_roll': '5d4*10',
        'packages': [
            {
                'name': 'Scale Mail & Longbow',
                'description': 'Armored archer',
                'equipment': [
                    'Scale Mail',
                    'Longbow',
                    'Arrow (20)',
                    'Shortsword (2)',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Balanced defense and ranged power'
            },
            {
                'name': 'Leather Armor & Longbow',
                'description': 'Mobile ranger',
                'equipment': [
                    'Leather Armor',
                    'Longbow',
                    'Arrow (20)',
                    'Shortsword (2)',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Better stealth, less AC'
            },
        ]
    },
    'Paladin': {
        'gold_roll': '5d4*10',
        'packages': [
            {
                'name': 'Martial Weapon & Shield',
                'description': 'Tank paladin',
                'equipment': [
                    'Longsword',
                    'Shield',
                    'Chainmail',
                    'Holy Symbol',
                    'Priest\'s Pack',
                    'Javelin (5)',
                ],
                'additional_notes': 'Maximum AC, defensive'
            },
            {
                'name': 'Greatsword',
                'description': 'Damage dealer',
                'equipment': [
                    'Greatsword',
                    'Chainmail',
                    'Holy Symbol',
                    'Priest\'s Pack',
                    'Javelin (5)',
                ],
                'additional_notes': 'Two-handed weapon, heavy hits'
            },
        ]
    },
    'Barbarian': {
        'gold_roll': '2d4*10',
        'packages': [
            {
                'name': 'Greataxe',
                'description': 'Raw power',
                'equipment': [
                    'Greataxe',
                    'Handaxe (2)',
                    'Explorer\'s Pack',
                    'Javelin (4)',
                ],
                'additional_notes': 'Massive damage, no armor'
            },
            {
                'name': 'Martial Weapons',
                'description': 'Versatile warrior',
                'equipment': [
                    'Battleaxe',
                    'Shield',
                    'Handaxe (2)',
                    'Explorer\'s Pack',
                    'Javelin (4)',
                ],
                'additional_notes': 'Shield for better AC'
            },
        ]
    },
    'Bard': {
        'gold_roll': '5d4*10',
        'packages': [
            {
                'name': 'Rapier & Lute',
                'description': 'Charismatic swordsman',
                'equipment': [
                    'Rapier',
                    'Lute',
                    'Leather Armor',
                    'Entertainer\'s Pack',
                    'Dagger',
                ],
                'additional_notes': 'Finesse weapon, musical instrument'
            },
            {
                'name': 'Longsword & Lute',
                'description': 'Martial bard',
                'equipment': [
                    'Longsword',
                    'Lute',
                    'Leather Armor',
                    'Entertainer\'s Pack',
                    'Dagger',
                ],
                'additional_notes': 'Versatile weapon option'
            },
        ]
    },
    'Druid': {
        'gold_roll': '2d4*10',
        'packages': [
            {
                'name': 'Wooden Shield',
                'description': 'Defensive druid',
                'equipment': [
                    'Wooden Shield',
                    'Scimitar',
                    'Leather Armor',
                    'Druidic Focus',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Higher AC, melee option'
            },
            {
                'name': 'Simple Weapon',
                'description': 'Mobile druid',
                'equipment': [
                    'Quarterstaff',
                    'Leather Armor',
                    'Druidic Focus',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Lightweight, versatile'
            },
        ]
    },
    'Monk': {
        'gold_roll': '5d4',  # Note: Monks get less starting gold
        'packages': [
            {
                'name': 'Shortsword',
                'description': 'Armed monk',
                'equipment': [
                    'Shortsword',
                    'Dart (10)',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Martial weapon for versatility'
            },
            {
                'name': 'Simple Weapon',
                'description': 'Pure monk',
                'equipment': [
                    'Quarterstaff',
                    'Dart (10)',
                    'Dungeoneer\'s Pack',
                ],
                'additional_notes': 'Traditional monk weapons'
            },
        ]
    },
    'Sorcerer': {
        'gold_roll': '3d4*10',
        'packages': [
            {
                'name': 'Light Crossbow',
                'description': 'Ranged sorcerer',
                'equipment': [
                    'Light Crossbow',
                    'Crossbow Bolt (20)',
                    'Component Pouch',
                    'Dungeoneer\'s Pack',
                    'Dagger (2)',
                ],
                'additional_notes': 'Ranged weapon for backup'
            },
            {
                'name': 'Dagger Focus',
                'description': 'Pure caster',
                'equipment': [
                    'Dagger (2)',
                    'Arcane Focus',
                    'Explorer\'s Pack',
                ],
                'additional_notes': 'Focus for easier spellcasting'
            },
        ]
    },
    'Warlock': {
        'gold_roll': '4d4*10',
        'packages': [
            {
                'name': 'Light Crossbow',
                'description': 'Ranged warlock',
                'equipment': [
                    'Light Crossbow',
                    'Crossbow Bolt (20)',
                    'Component Pouch',
                    'Scholar\'s Pack',
                    'Leather Armor',
                    'Dagger (2)',
                ],
                'additional_notes': 'Armor and ranged option'
            },
            {
                'name': 'Simple Weapon',
                'description': 'Melee warlock',
                'equipment': [
                    'Quarterstaff',
                    'Arcane Focus',
                    'Dungeoneer\'s Pack',
                    'Leather Armor',
                    'Dagger (2)',
                ],
                'additional_notes': 'Closer range combat'
            },
        ]
    },
}


def get_starting_gold_for_class(class_name):
    """Get the dice formula for starting gold for a given class"""
    if class_name in STARTING_EQUIPMENT_PACKAGES:
        return STARTING_EQUIPMENT_PACKAGES[class_name]['gold_roll']
    return '4d4*10'  # Default


def get_equipment_packages_for_class(class_name):
    """Get available starting equipment packages for a given class"""
    if class_name in STARTING_EQUIPMENT_PACKAGES:
        return STARTING_EQUIPMENT_PACKAGES[class_name]['packages']
    return []


def roll_starting_gold(dice_formula):
    """
    Roll starting gold based on dice formula (e.g., '5d4*10')
    Returns the rolled amount in gold pieces
    """
    import random
    import re
    
    # Parse the dice formula (e.g., "5d4*10" or "5d4")
    match = re.match(r'(\d+)d(\d+)(?:\*(\d+))?', dice_formula)
    if not match:
        return 0
    
    num_dice = int(match.group(1))
    die_size = int(match.group(2))
    multiplier = int(match.group(3)) if match.group(3) else 1
    
    total = 0
    for _ in range(num_dice):
        total += random.randint(1, die_size)
    
    return total * multiplier
