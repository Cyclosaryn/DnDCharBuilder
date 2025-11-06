"""
D&D 5e Class Features that require player choices

Based on D&D 5e Basic Rules 2014
"""

CLASS_FEATURES = {
    'Fighter': {
        1: {
            'name': 'Fighting Style',
            'required': True,
            'num_choices': 1,
            'description': 'You adopt a particular style of fighting as your specialty.',
            'options': [
                {
                    'name': 'Archery',
                    'description': 'You gain a +2 bonus to attack rolls you make with ranged weapons.',
                },
                {
                    'name': 'Defense',
                    'description': 'While you are wearing armor, you gain a +1 bonus to AC.',
                },
                {
                    'name': 'Dueling',
                    'description': 'When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.',
                },
                {
                    'name': 'Great Weapon Fighting',
                    'description': 'When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll. The weapon must have the two-handed or versatile property.',
                },
                {
                    'name': 'Protection',
                    'description': 'When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.',
                },
                {
                    'name': 'Two-Weapon Fighting',
                    'description': 'When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.',
                },
            ]
        },
        3: {
            'name': 'Martial Archetype',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a martial archetype that represents your focus.',
            'options': [
                {
                    'name': 'Champion',
                    'description': 'Focuses on the development of raw physical power honed to deadly perfection. You gain improved critical hits, additional fighting styles, and remarkable athleticism.',
                },
            ]
        },
    },
    'Wizard': {
        2: {
            'name': 'Arcane Tradition',
            'required': True,
            'num_choices': 1,
            'description': 'Choose an arcane tradition that shapes your practice of magic.',
            'options': [
                {
                    'name': 'School of Evocation',
                    'description': 'Focuses on creating powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid. You can sculpt spells to protect allies and empower your evocations.',
                },
            ]
        },
    },
    'Cleric': {
        1: {
            'name': 'Divine Domain',
            'required': True,
            'num_choices': 1,
            'description': 'Choose one domain related to your deity.',
            'options': [
                {
                    'name': 'Life Domain',
                    'description': 'Focuses on vibrant positive energy that sustains all life. Grants bonus proficiency with heavy armor and domain spells.',
                    'bonus_proficiencies': 'Heavy Armor',
                    'domain_spells': {
                        1: ['Bless', 'Cure Wounds'],
                        3: ['Lesser Restoration', 'Spiritual Weapon'],
                        5: ['Beacon of Hope', 'Revivify'],
                        7: ['Death Ward', 'Guardian of Faith'],
                        9: ['Mass Cure Wounds', 'Raise Dead'],
                    }
                },
                {
                    'name': 'Light Domain',
                    'description': 'Represents deities of light, truth, beauty, and vigilance against darkness. Grants Warding Flare reaction and Light cantrip.',
                    'bonus_proficiencies': None,
                    'domain_spells': {
                        1: ['Burning Hands', 'Faerie Fire'],
                        3: ['Flaming Sphere', 'Scorching Ray'],
                        5: ['Daylight', 'Fireball'],
                        7: ['Guardian of Faith', 'Wall of Fire'],
                        9: ['Flame Strike', 'Scrying'],
                    }
                },
                {
                    'name': 'Knowledge Domain',
                    'description': 'Deities of knowledge value learning and understanding. You gain expertise in two skills and learn two languages.',
                    'bonus_proficiencies': 'Choose two: Arcana, History, Nature, or Religion',
                    'domain_spells': {
                        1: ['Command', 'Identify'],
                        3: ['Augury', 'Suggestion'],
                        5: ['Nondetection', 'Speak with Dead'],
                        7: ['Arcane Eye', 'Confusion'],
                        9: ['Legend Lore', 'Scrying'],
                    }
                },
                {
                    'name': 'Nature Domain',
                    'description': 'Gods of nature are as varied as the natural world itself. You gain proficiency in heavy armor and a druid cantrip.',
                    'bonus_proficiencies': 'Heavy Armor',
                    'domain_spells': {
                        1: ['Animal Friendship', 'Speak with Animals'],
                        3: ['Barkskin', 'Spike Growth'],
                        5: ['Plant Growth', 'Wind Wall'],
                        7: ['Dominate Beast', 'Grasping Vine'],
                        9: ['Insect Plague', 'Tree Stride'],
                    }
                },
                {
                    'name': 'Tempest Domain',
                    'description': 'Gods of the tempest send their clerics to inspire fear, wield thunder and lightning. Grants heavy armor and martial weapons.',
                    'bonus_proficiencies': 'Heavy Armor, Martial Weapons',
                    'domain_spells': {
                        1: ['Fog Cloud', 'Thunderwave'],
                        3: ['Gust of Wind', 'Shatter'],
                        5: ['Call Lightning', 'Sleet Storm'],
                        7: ['Control Water', 'Ice Storm'],
                        9: ['Destructive Wave', 'Insect Plague'],
                    }
                },
                {
                    'name': 'Trickery Domain',
                    'description': 'Gods of trickery are mischief-makers and instigators. You can create an illusory duplicate of yourself.',
                    'bonus_proficiencies': None,
                    'domain_spells': {
                        1: ['Charm Person', 'Disguise Self'],
                        3: ['Mirror Image', 'Pass without Trace'],
                        5: ['Blink', 'Dispel Magic'],
                        7: ['Dimension Door', 'Polymorph'],
                        9: ['Dominate Person', 'Modify Memory'],
                    }
                },
                {
                    'name': 'War Domain',
                    'description': 'War gods inspire warriors and reward acts of bravery. You gain heavy armor and martial weapons proficiency.',
                    'bonus_proficiencies': 'Heavy Armor, Martial Weapons',
                    'domain_spells': {
                        1: ['Divine Favor', 'Shield of Faith'],
                        3: ['Magic Weapon', 'Spiritual Weapon'],
                        5: ['Crusader\'s Mantle', 'Spirit Guardians'],
                        7: ['Freedom of Movement', 'Stoneskin'],
                        9: ['Flame Strike', 'Hold Monster'],
                    }
                },
            ]
        },
    },
    'Rogue': {
        1: {
            'name': 'Expertise',
            'required': False,
            'num_choices': 0,
            'description': 'At 1st level, choose 2 of your skill proficiencies, or one skill proficiency and your proficiency with thieves\' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies. Note: Expertise selection is handled during character creation.',
            'options': []
        },
        3: {
            'name': 'Roguish Archetype',
            'required': True,
            'num_choices': 1,
            'description': 'Choose an archetype that represents your focus.',
            'options': [
                {
                    'name': 'Thief',
                    'description': 'Hones skills in stealth and thievery. You have supreme sneak, can use Fast Hands to use bonus actions for Sleight of Hand, Use an Object, or use thieves\' tools, and gain Second-Story Work for climbing.',
                },
            ]
        },
        6: {
            'name': 'Additional Expertise',
            'required': False,
            'num_choices': 0,
            'description': 'At 6th level, you can choose 2 more of your proficiencies (in skills or with thieves\' tools) to gain expertise, doubling your proficiency bonus for those skills.',
            'options': []
        },
    },
    'Ranger': {
        1: {
            'name': 'Favored Enemy',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a type of favored enemy.',
            'options': [
                {'name': 'Aberrations', 'description': 'Strange beings from beyond reality.'},
                {'name': 'Beasts', 'description': 'Natural animals.'},
                {'name': 'Celestials', 'description': 'Creatures from the Upper Planes.'},
                {'name': 'Constructs', 'description': 'Artificial beings.'},
                {'name': 'Dragons', 'description': 'True dragons and dragonborn.'},
                {'name': 'Elementals', 'description': 'Beings from the Elemental Planes.'},
                {'name': 'Fey', 'description': 'Creatures of the Feywild.'},
                {'name': 'Fiends', 'description': 'Demons, devils, and other evil outsiders.'},
                {'name': 'Giants', 'description': 'Huge humanoids.'},
                {'name': 'Monstrosities', 'description': 'Frightening creatures.'},
                {'name': 'Oozes', 'description': 'Amorphous creatures.'},
                {'name': 'Plants', 'description': 'Vegetable creatures.'},
                {'name': 'Undead', 'description': 'Once-living creatures brought back.'},
                {'name': 'Two Humanoid Races', 'description': 'Choose two humanoid races (e.g., gnolls and orcs).'},
            ]
        },
        3: {
            'name': 'Ranger Archetype',
            'required': True,
            'num_choices': 1,
            'description': 'Choose an archetype that represents your focus.',
            'options': [
                {
                    'name': 'Hunter',
                    'description': 'Emulates the classic heroes of the wild, defending civilization from monstrous threats. Masters techniques for fighting crowds of enemies or single powerful foes.',
                },
            ]
        },
    },
    'Paladin': {
        3: {
            'name': 'Sacred Oath',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a sacred oath that guides your actions.',
            'options': [
                {
                    'name': 'Oath of Devotion',
                    'description': 'Commits you to the highest ideals of justice, virtue, and order. The paladin archetype, sworn to uphold the principles of honesty, courage, compassion, honor, and duty.',
                },
            ]
        },
    },
    'Barbarian': {
        3: {
            'name': 'Primal Path',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a primal path that shapes your rage.',
            'options': [
                {
                    'name': 'Path of the Berserker',
                    'description': 'A path of untrammeled fury, slick with blood. You can go into a frenzy when you rage, making an additional melee weapon attack as a bonus action each turn.',
                },
            ]
        },
    },
    'Bard': {
        3: {
            'name': 'Bard College',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a bard college that represents your focus. Note: Bards also gain Expertise at this level - choose 2 skills you are proficient in to double your proficiency bonus.',
            'options': [
                {
                    'name': 'College of Lore',
                    'description': 'Gathers knowledge from every corner of the multiverse. You gain bonus proficiencies, Cutting Words to reduce enemy rolls, and additional Magical Secrets.',
                },
            ]
        },
        10: {
            'name': 'Additional Expertise',
            'required': False,
            'num_choices': 0,
            'description': 'At 10th level, you can choose 2 more of your skill proficiencies to gain expertise, doubling your proficiency bonus for those skills.',
            'options': []
        },
    },
    'Druid': {
        2: {
            'name': 'Druid Circle',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a circle that grants you features.',
            'options': [
                {
                    'name': 'Circle of the Land',
                    'description': 'Mystics and sages who safeguard ancient knowledge and rites. Your magic is influenced by the land where you were initiated.',
                    'has_sub_choice': True,
                    'sub_choice': {
                        'name': 'Land Type',
                        'description': 'Choose the type of land where you became a druid. This determines your circle spells.',
                        'num_choices': 1,
                        'options': [
                            {'name': 'Arctic', 'description': 'Frozen tundras and icy wastes. Spells: Hold Person, Spike Growth, Sleet Storm, Slow, Freedom of Movement, Ice Storm, Commune with Nature, Cone of Cold.'},
                            {'name': 'Coast', 'description': 'Beaches, cliffs, and coastal waters. Spells: Mirror Image, Misty Step, Water Breathing, Water Walk, Control Water, Freedom of Movement, Conjure Elemental, Scrying.'},
                            {'name': 'Desert', 'description': 'Sandy wastes and rocky badlands. Spells: Blur, Silence, Create Food and Water, Protection from Energy, Blight, Hallucinatory Terrain, Insect Plague, Wall of Stone.'},
                            {'name': 'Forest', 'description': 'Woodlands and wild groves. Spells: Barkskin, Spider Climb, Call Lightning, Plant Growth, Divination, Freedom of Movement, Commune with Nature, Tree Stride.'},
                            {'name': 'Grassland', 'description': 'Plains and meadows. Spells: Invisibility, Pass without Trace, Daylight, Haste, Divination, Freedom of Movement, Dream, Insect Plague.'},
                            {'name': 'Mountain', 'description': 'Rocky peaks and highland regions. Spells: Spider Climb, Spike Growth, Lightning Bolt, Meld into Stone, Stone Shape, Stoneskin, Passwall, Wall of Stone.'},
                            {'name': 'Swamp', 'description': 'Wetlands and marshes. Spells: Darkness, Acid Arrow, Water Walk, Stinking Cloud, Freedom of Movement, Locate Creature, Insect Plague, Scrying.'},
                            {'name': 'Underdark', 'description': 'Subterranean caverns. Spells: Spider Climb, Web, Gaseous Form, Stinking Cloud, Greater Invisibility, Stone Shape, Cloudkill, Insect Plague.'},
                        ]
                    }
                },
                {
                    'name': 'Circle of the Moon',
                    'description': 'Fierce guardians of the wilds who take on powerful animal forms. You gain the ability to use Wild Shape on your turn as a bonus action and can transform into more powerful beasts.',
                },
            ]
        },
    },
    'Monk': {
        3: {
            'name': 'Monastic Tradition',
            'required': True,
            'num_choices': 1,
            'description': 'Choose a monastic tradition.',
            'options': [
                {
                    'name': 'Way of the Open Hand',
                    'description': 'Masters of martial arts combat, armed or unarmed. You learn techniques to push, trip, and manipulate opponents, and can use ki to heal yourself or enter a protective meditative state.',
                },
            ]
        },
    },
        'Sorcerer': {
        1: {
            'name': 'Sorcerous Origin',
            'required': True,
            'num_choices': 1,
            'description': 'Choose the source of your innate magical power.',
            'options': [
                {
                    'name': 'Draconic Bloodline',
                    'description': 'Your innate magic comes from draconic magic that was mingled with your blood. Choose one dragon type as your ancestor.',
                    'prerequisites': None,
                    'bonus_proficiencies': None,
                    'has_sub_choice': True,
                    'sub_choice': {
                        'name': 'Draconic Ancestry',
                        'description': 'Choose the type of dragon that influenced your bloodline. This determines your damage resistance and breath weapon type.',
                        'num_choices': 1,
                        'options': [
                            {'name': 'Black Dragon', 'damage_type': 'Acid', 'description': 'Acidic corruption flows through your veins.'},
                            {'name': 'Blue Dragon', 'damage_type': 'Lightning', 'description': 'Crackling lightning energy empowers you.'},
                            {'name': 'Brass Dragon', 'damage_type': 'Fire', 'description': 'The flames of the desert burn within you.'},
                            {'name': 'Bronze Dragon', 'damage_type': 'Lightning', 'description': 'Storm and sea magic courses through you.'},
                            {'name': 'Copper Dragon', 'damage_type': 'Acid', 'description': 'Corrosive wit and acid merge in your blood.'},
                            {'name': 'Gold Dragon', 'damage_type': 'Fire', 'description': 'Noble flames of the sun dragon empower you.'},
                            {'name': 'Green Dragon', 'damage_type': 'Poison', 'description': 'Toxic breath and poisonous cunning flow through you.'},
                            {'name': 'Red Dragon', 'damage_type': 'Fire', 'description': 'Infernal flames of greed and power burn within.'},
                            {'name': 'Silver Dragon', 'damage_type': 'Cold', 'description': 'Frost and winter winds chill your enemies.'},
                            {'name': 'White Dragon', 'damage_type': 'Cold', 'description': 'Arctic fury and icy breath freeze your foes.'},
                        ]
                    }
                },
                {
                    'name': 'Wild Magic',
                    'description': 'Your innate magic comes from the wild forces of chaos. Your spells can trigger unpredictable wild magic surges.',
                    'prerequisites': None,
                    'bonus_proficiencies': None,
                },
            ]
        },
        3: {
            'name': 'Metamagic',
            'required': True,
            'num_choices': 2,
            'description': 'You gain the ability to twist your spells to suit your needs. You gain two Metamagic options.',
            'options': [
                {
                    'name': 'Careful Spell',
                    'description': 'When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell\'s full force. Choose a number of creatures up to your Charisma modifier (minimum of one). A chosen creature automatically succeeds on its saving throw against the spell.',
                    'cost': '1 sorcery point',
                },
                {
                    'name': 'Distant Spell',
                    'description': 'When you cast a spell that has a range of 5 feet or greater, you can double the range of the spell. When you cast a spell that has a range of touch, you can make the range of the spell 30 feet.',
                    'cost': '1 sorcery point',
                },
                {
                    'name': 'Empowered Spell',
                    'description': 'When you roll damage for a spell, you can reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls.',
                    'cost': '1 sorcery point',
                },
                {
                    'name': 'Extended Spell',
                    'description': 'When you cast a spell that has a duration of 1 minute or longer, you can double its duration, to a maximum duration of 24 hours.',
                    'cost': '1 sorcery point',
                },
                {
                    'name': 'Heightened Spell',
                    'description': 'When you cast a spell that forces a creature to make a saving throw to resist its effects, you can give one target of the spell disadvantage on its first saving throw made against the spell.',
                    'cost': '3 sorcery points',
                },
                {
                    'name': 'Quickened Spell',
                    'description': 'When you cast a spell that has a casting time of 1 action, you can change the casting time to 1 bonus action for this casting.',
                    'cost': '2 sorcery points',
                },
                {
                    'name': 'Subtle Spell',
                    'description': 'When you cast a spell, you can cast it without any somatic or verbal components.',
                    'cost': '1 sorcery point',
                },
                {
                    'name': 'Twinned Spell',
                    'description': 'When you cast a spell that targets only one creature and doesn\'t have a range of self, you can target a second creature in range with the same spell.',
                    'cost': 'Sorcery points equal to the spell\'s level (1 sorcery point if the spell is a cantrip)',
                },
            ]
        },
        10: {
            'name': 'Additional Metamagic',
            'required': True,
            'num_choices': 1,
            'description': 'You gain one additional Metamagic option.',
            'options': [
                # Same options as level 3 Metamagic
                {'name': 'Careful Spell', 'description': 'When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell\'s full force. Choose a number of creatures up to your Charisma modifier (minimum of one). A chosen creature automatically succeeds on its saving throw against the spell.', 'cost': '1 sorcery point'},
                {'name': 'Distant Spell', 'description': 'When you cast a spell that has a range of 5 feet or greater, you can double the range of the spell. When you cast a spell that has a range of touch, you can make the range of the spell 30 feet.', 'cost': '1 sorcery point'},
                {'name': 'Empowered Spell', 'description': 'When you roll damage for a spell, you can reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls.', 'cost': '1 sorcery point'},
                {'name': 'Extended Spell', 'description': 'When you cast a spell that has a duration of 1 minute or longer, you can double its duration, to a maximum duration of 24 hours.', 'cost': '1 sorcery point'},
                {'name': 'Heightened Spell', 'description': 'When you cast a spell that forces a creature to make a saving throw to resist its effects, you can give one target of the spell disadvantage on its first saving throw made against the spell.', 'cost': '3 sorcery points'},
                {'name': 'Quickened Spell', 'description': 'When you cast a spell that has a casting time of 1 action, you can change the casting time to 1 bonus action for this casting.', 'cost': '2 sorcery points'},
                {'name': 'Subtle Spell', 'description': 'When you cast a spell, you can cast it without any somatic or verbal components.', 'cost': '1 sorcery point'},
                {'name': 'Twinned Spell', 'description': 'When you cast a spell that targets only one creature and doesn\'t have a range of self, you can target a second creature in range with the same spell.', 'cost': 'Sorcery points equal to the spell\'s level (1 sorcery point if the spell is a cantrip)'},
            ]
        },
    },
    'Warlock': {
        1: {
            'name': 'Otherworldly Patron',
            'required': True,
            'num_choices': 1,
            'description': 'Choose the otherworldly patron you have struck a bargain with.',
            'options': [
                {
                    'name': 'The Archfey',
                    'description': 'Your patron is a lord or lady of the fey, a creature of legend who holds secrets that were forgotten before mortals were born.',
                    'expanded_spell_list': {
                        1: ['Faerie Fire', 'Sleep'],
                        3: ['Calm Emotions', 'Phantasmal Force'],
                        5: ['Blink', 'Plant Growth'],
                        7: ['Dominate Beast', 'Greater Invisibility'],
                        9: ['Dominate Person', 'Seeming'],
                    }
                },
                {
                    'name': 'The Fiend',
                    'description': 'Your patron is a fiend from the lower planes of existence, a being whose aims are evil.',
                    'expanded_spell_list': {
                        1: ['Burning Hands', 'Command'],
                        3: ['Blindness/Deafness', 'Scorching Ray'],
                        5: ['Fireball', 'Stinking Cloud'],
                        7: ['Fire Shield', 'Wall of Fire'],
                        9: ['Flame Strike', 'Hallow'],
                    }
                },
                {
                    'name': 'The Great Old One',
                    'description': 'Your patron is a mysterious entity whose nature is utterly foreign to the fabric of reality, from the Far Realm beyond.',
                    'expanded_spell_list': {
                        1: ['Dissonant Whispers', 'Tasha\'s Hideous Laughter'],
                        3: ['Detect Thoughts', 'Phantasmal Force'],
                        5: ['Clairvoyance', 'Sending'],
                        7: ['Dominate Beast', 'Evard\'s Black Tentacles'],
                        9: ['Dominate Person', 'Telekinesis'],
                    }
                },
            ]
        },
        2: {
            'name': 'Eldritch Invocations',
            'required': True,
            'num_choices': 2,
            'description': 'You gain two eldritch invocations of your choice.',
            'options': [
                {'name': 'Agonizing Blast', 'prerequisite': 'Eldritch blast cantrip', 'description': 'Add your Charisma modifier to the damage of eldritch blast.'},
                {'name': 'Armor of Shadows', 'prerequisite': None, 'description': 'You can cast mage armor on yourself at will, without expending a spell slot or material components.'},
                {'name': 'Beast Speech', 'prerequisite': None, 'description': 'You can cast speak with animals at will, without expending a spell slot.'},
                {'name': 'Beguiling Influence', 'prerequisite': None, 'description': 'You gain proficiency in the Deception and Persuasion skills.'},
                {'name': 'Devil\'s Sight', 'prerequisite': None, 'description': 'You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.'},
                {'name': 'Eldritch Sight', 'prerequisite': None, 'description': 'You can cast detect magic at will, without expending a spell slot.'},
                {'name': 'Fiendish Vigor', 'prerequisite': None, 'description': 'You can cast false life on yourself at will as a 1st-level spell, without expending a spell slot or material components.'},
                {'name': 'Mask of Many Faces', 'prerequisite': None, 'description': 'You can cast disguise self at will, without expending a spell slot.'},
                {'name': 'Repelling Blast', 'prerequisite': 'Eldritch blast cantrip', 'description': 'When you hit a creature with eldritch blast, you can push the creature up to 10 feet away from you in a straight line.'},
                {'name': 'Thief of Five Fates', 'prerequisite': None, 'description': 'You can cast bane once using a warlock spell slot. You can\'t do so again until you finish a long rest.'},
            ]
        },
    },
}


def get_class_features_for_level(class_name, level):
    """
    Get all class features available at a specific level for a given class.
    
    Returns a dict of features or None if no features at this level.
    """
    if class_name not in CLASS_FEATURES:
        return None
    
    if level not in CLASS_FEATURES[class_name]:
        return None
    
    return CLASS_FEATURES[class_name][level]


def get_all_class_features(class_name):
    """
    Get all class features for a given class, organized by level.
    """
    if class_name not in CLASS_FEATURES:
        return {}
    
    return CLASS_FEATURES[class_name]


def has_feature_choice_at_level(class_name, level):
    """
    Check if a class has a feature choice at a specific level that requires UI selection.
    This excludes informational-only features like Expertise (which has its own form).
    """
    if class_name not in CLASS_FEATURES or level not in CLASS_FEATURES[class_name]:
        return False
    
    feature = CLASS_FEATURES[class_name][level]
    
    # Check if this feature requires UI selection (num_choices > 0 and has options)
    return feature.get('required', False) and feature.get('num_choices', 0) > 0 and len(feature.get('options', [])) > 0
