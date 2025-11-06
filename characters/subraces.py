"""
D&D 5e Subraces from Basic Rules 2014
Defines subraces for races that have them
"""

SUBRACES = {
    'Dwarf': {
        'has_subraces': True,
        'subraces': [
            {
                'name': 'Hill Dwarf',
                'description': 'As a hill dwarf, you have keen senses, deep intuition, and remarkable resilience.',
                'ability_bonuses': {'wisdom': 1},
                'traits': ['Dwarven Toughness: Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.']
            },
            {
                'name': 'Mountain Dwarf',
                'description': 'As a mountain dwarf, you\'re strong and hardy, accustomed to a difficult life in rugged terrain.',
                'ability_bonuses': {'strength': 2},
                'traits': ['Dwarven Armor Training: You have proficiency with light and medium armor.']
            }
        ]
    },
    'Elf': {
        'has_subraces': True,
        'subraces': [
            {
                'name': 'High Elf',
                'description': 'As a high elf, you have a keen mind and a mastery of at least the basics of magic.',
                'ability_bonuses': {'intelligence': 1},
                'traits': [
                    'Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.',
                    'Cantrip: You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it.',
                    'Extra Language: You can speak, read, and write one extra language of your choice.'
                ]
            },
            {
                'name': 'Wood Elf',
                'description': 'As a wood elf, you have keen senses and intuition, and your fleet feet carry you quickly and stealthily through your native forests.',
                'ability_bonuses': {'wisdom': 1},
                'traits': [
                    'Elf Weapon Training: You have proficiency with the longsword, shortsword, shortbow, and longbow.',
                    'Fleet of Foot: Your base walking speed increases to 35 feet.',
                    'Mask of the Wild: You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.'
                ]
            }
        ]
    },
    'Halfling': {
        'has_subraces': True,
        'subraces': [
            {
                'name': 'Lightfoot',
                'description': 'As a lightfoot halfling, you can easily hide from notice, even using other people as cover.',
                'ability_bonuses': {'charisma': 1},
                'traits': ['Naturally Stealthy: You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.']
            },
            {
                'name': 'Stout',
                'description': 'As a stout halfling, you\'re hardier than average and have some resistance to poison.',
                'ability_bonuses': {'constitution': 1},
                'traits': ['Stout Resilience: You have advantage on saving throws against poison, and you have resistance against poison damage.']
            }
        ]
    },
    'Gnome': {
        'has_subraces': True,
        'subraces': [
            {
                'name': 'Rock Gnome',
                'description': 'As a rock gnome, you have a natural inventiveness and hardiness beyond that of other gnomes.',
                'ability_bonuses': {'constitution': 1},
                'traits': [
                    'Artificer\'s Lore: Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus.',
                    'Tinker: You have proficiency with artisan\'s tools (tinker\'s tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp).'
                ]
            }
        ]
    },
    'Dragonborn': {
        'has_subraces': True,
        'subraces': [
            {
                'name': 'Black Dragon Ancestry',
                'description': 'You have draconic ancestry from a black dragon. Your breath weapon is a 5 by 30 ft. line (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Acid',
                    'Breath Weapon: 5 by 30 ft. line (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to acid damage.'
                ]
            },
            {
                'name': 'Blue Dragon Ancestry',
                'description': 'You have draconic ancestry from a blue dragon. Your breath weapon is a 5 by 30 ft. line (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Lightning',
                    'Breath Weapon: 5 by 30 ft. line (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to lightning damage.'
                ]
            },
            {
                'name': 'Brass Dragon Ancestry',
                'description': 'You have draconic ancestry from a brass dragon. Your breath weapon is a 5 by 30 ft. line (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Fire',
                    'Breath Weapon: 5 by 30 ft. line (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to fire damage.'
                ]
            },
            {
                'name': 'Bronze Dragon Ancestry',
                'description': 'You have draconic ancestry from a bronze dragon. Your breath weapon is a 5 by 30 ft. line (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Lightning',
                    'Breath Weapon: 5 by 30 ft. line (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to lightning damage.'
                ]
            },
            {
                'name': 'Copper Dragon Ancestry',
                'description': 'You have draconic ancestry from a copper dragon. Your breath weapon is a 5 by 30 ft. line (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Acid',
                    'Breath Weapon: 5 by 30 ft. line (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to acid damage.'
                ]
            },
            {
                'name': 'Gold Dragon Ancestry',
                'description': 'You have draconic ancestry from a gold dragon. Your breath weapon is a 15 ft. cone (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Fire',
                    'Breath Weapon: 15 ft. cone (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to fire damage.'
                ]
            },
            {
                'name': 'Green Dragon Ancestry',
                'description': 'You have draconic ancestry from a green dragon. Your breath weapon is a 15 ft. cone (Con. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Poison',
                    'Breath Weapon: 15 ft. cone (Constitution saving throw)',
                    'Damage Resistance: You have resistance to poison damage.'
                ]
            },
            {
                'name': 'Red Dragon Ancestry',
                'description': 'You have draconic ancestry from a red dragon. Your breath weapon is a 15 ft. cone (Dex. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Fire',
                    'Breath Weapon: 15 ft. cone (Dexterity saving throw)',
                    'Damage Resistance: You have resistance to fire damage.'
                ]
            },
            {
                'name': 'Silver Dragon Ancestry',
                'description': 'You have draconic ancestry from a silver dragon. Your breath weapon is a 15 ft. cone (Con. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Cold',
                    'Breath Weapon: 15 ft. cone (Constitution saving throw)',
                    'Damage Resistance: You have resistance to cold damage.'
                ]
            },
            {
                'name': 'White Dragon Ancestry',
                'description': 'You have draconic ancestry from a white dragon. Your breath weapon is a 15 ft. cone (Con. save).',
                'ability_bonuses': {},
                'traits': [
                    'Damage Type: Cold',
                    'Breath Weapon: 15 ft. cone (Constitution saving throw)',
                    'Damage Resistance: You have resistance to cold damage.'
                ]
            }
        ]
    },
    # Races without subraces in Basic Rules 2014
    'Human': {
        'has_subraces': False
    },
    'Half-Elf': {
        'has_subraces': False
    },
    'Half-Orc': {
        'has_subraces': False
    },
    'Tiefling': {
        'has_subraces': False
    }
}


def get_subraces_for_race(race_name):
    """Get subraces for a given race"""
    race_data = SUBRACES.get(race_name, {})
    if race_data.get('has_subraces', False):
        return race_data.get('subraces', [])
    return []


def has_subraces(race_name):
    """Check if a race has subraces"""
    race_data = SUBRACES.get(race_name, {})
    return race_data.get('has_subraces', False)


def get_subrace_data(race_name, subrace_name):
    """Get data for a specific subrace"""
    subraces = get_subraces_for_race(race_name)
    for subrace in subraces:
        if subrace['name'] == subrace_name:
            return subrace
    return None
