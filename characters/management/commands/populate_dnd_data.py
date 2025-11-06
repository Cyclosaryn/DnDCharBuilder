from django.core.management.base import BaseCommand
from characters.models import Race, CharacterClass, Background


class Command(BaseCommand):
    help = 'Populates the database with basic D&D 5e races, classes, and backgrounds'

    def handle(self, *args, **options):
        self.stdout.write('Populating D&D 5e data...')
        
        # Create Races
        races_data = [
            {
                'name': 'Human',
                'description': 'Humans are the most adaptable and ambitious people among the common races. Whatever drives them, humans are the innovators, the achievers, and the pioneers of the worlds.',
                'size': 'Medium',
                'speed': 30,
                'strength_bonus': 1,
                'dexterity_bonus': 1,
                'constitution_bonus': 1,
                'intelligence_bonus': 1,
                'wisdom_bonus': 1,
                'charisma_bonus': 1,
                'traits': 'Age: Humans reach adulthood in their late teens and live less than a century.\nSize: Medium\nSpeed: 30 feet\nLanguages: Common and one extra language of your choice.'
            },
            {
                'name': 'Elf',
                'description': 'Elves are a magical people of otherworldly grace, living in the world but not entirely part of it. They live in places of ethereal beauty, in the midst of ancient forests or in silvery spires.',
                'size': 'Medium',
                'speed': 30,
                'dexterity_bonus': 2,
                'traits': 'Darkvision: 60 feet\nKeen Senses: Proficiency in Perception\nFey Ancestry: Advantage on saves against being charmed, magic can\'t put you to sleep\nTrance: Elves don\'t need to sleep, meditate 4 hours instead'
            },
            {
                'name': 'Dwarf',
                'description': 'Bold and hardy, dwarves are known as skilled warriors, miners, and workers of stone and metal. Though they stand well under 5 feet tall, they are so broad and compact that they can weigh as much as a human.',
                'size': 'Medium',
                'speed': 25,
                'constitution_bonus': 2,
                'traits': 'Darkvision: 60 feet\nDwarven Resilience: Advantage on saves against poison, resistance to poison damage\nDwarven Combat Training: Proficiency with battleaxe, handaxe, light hammer, warhammer\nStonecunning: Add double proficiency to History checks related to stonework'
            },
            {
                'name': 'Halfling',
                'description': 'The diminutive halflings survive in a world full of larger creatures by avoiding notice or, barring that, avoiding offense. They are inclined to be affable and get along well with others.',
                'size': 'Small',
                'speed': 25,
                'dexterity_bonus': 2,
                'traits': 'Lucky: When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die\nBrave: Advantage on saves against being frightened\nHalfling Nimbleness: Can move through space of larger creatures'
            },
            {
                'name': 'Dragonborn',
                'description': 'Born of dragons, as their name proclaims, the dragonborn walk proudly through a world that greets them with fearful incomprehension. Shaped by draconic gods or dragons themselves, dragonborn originally hatched from dragon eggs.',
                'size': 'Medium',
                'speed': 30,
                'strength_bonus': 2,
                'charisma_bonus': 1,
                'traits': 'Draconic Ancestry: Choose one dragon type, gain resistance to its damage type\nBreath Weapon: Exhale destructive energy (5x30 ft line or 15 ft cone, DC 8+CON+prof)\nDamage Resistance: Resistance to damage type associated with draconic ancestry'
            },
            {
                'name': 'Gnome',
                'description': 'A constant hum of busy activity pervades the warrens and neighborhoods where gnomes form their close-knit communities. Louder sounds punctuate the hum: a crunch of grinding gears here, a minor explosion there.',
                'size': 'Small',
                'speed': 25,
                'intelligence_bonus': 2,
                'traits': 'Darkvision: 60 feet\nGnome Cunning: Advantage on all INT, WIS, and CHA saves against magic'
            },
            {
                'name': 'Half-Elf',
                'description': 'Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by elven senses, love of nature, and artistic tastes.',
                'size': 'Medium',
                'speed': 30,
                'charisma_bonus': 2,
                'traits': 'Darkvision: 60 feet\nFey Ancestry: Advantage on saves against being charmed, magic can\'t put you to sleep\nSkill Versatility: Proficiency in two skills of your choice\nAbility Score Increase: Two different ability scores of your choice increase by 1'
            },
            {
                'name': 'Half-Orc',
                'description': 'Whether united under the leadership of a mighty warlock or having fought to a standstill after years of conflict, orc and human tribes sometimes form alliances, joining forces into a larger horde to the terror of civilized lands nearby.',
                'size': 'Medium',
                'speed': 30,
                'strength_bonus': 2,
                'constitution_bonus': 1,
                'traits': 'Darkvision: 60 feet\nMenacing: Proficiency in Intimidation\nRelentless Endurance: Drop to 1 HP instead of 0 once per long rest\nSavage Attacks: Roll one additional weapon damage die on critical hit'
            },
            {
                'name': 'Tiefling',
                'description': 'To be greeted with stares and whispers, to suffer violence and insult on the street, to see mistrust and fear in every eye: this is the lot of the tiefling. Tieflings are derived from human bloodlines touched by infernal heritage.',
                'size': 'Medium',
                'speed': 30,
                'charisma_bonus': 2,
                'intelligence_bonus': 1,
                'traits': 'Darkvision: 60 feet\nHellish Resistance: Resistance to fire damage\nInfernal Legacy: Know thaumaturgy cantrip; cast hellish rebuke at 3rd level, darkness at 5th level (once per long rest each)'
            }
        ]
        
        for race_data in races_data:
            race, created = Race.objects.get_or_create(name=race_data['name'], defaults=race_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created race: {race.name}'))
        
        # Create Classes
        classes_data = [
            {
                'name': 'Fighter',
                'description': 'A master of martial combat, skilled with a variety of weapons and armor.',
                'hit_die': 10,
                'primary_ability': 'Strength or Dexterity',
                'saving_throw_proficiencies': 'Strength, Constitution',
                'armor_proficiencies': 'All armor, shields',
                'weapon_proficiencies': 'Simple weapons, martial weapons',
                'skill_choices': 'Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, Survival',
                'num_skills': 2
            },
            {
                'name': 'Wizard',
                'description': 'A scholarly magic-user capable of manipulating the structures of reality.',
                'hit_die': 6,
                'primary_ability': 'Intelligence',
                'saving_throw_proficiencies': 'Intelligence, Wisdom',
                'armor_proficiencies': 'None',
                'weapon_proficiencies': 'Daggers, darts, slings, quarterstaffs, light crossbows',
                'skill_choices': 'Arcana, History, Insight, Investigation, Medicine, Religion',
                'num_skills': 2
            },
            {
                'name': 'Rogue',
                'description': 'A scoundrel who uses stealth and trickery to overcome obstacles and enemies.',
                'hit_die': 8,
                'primary_ability': 'Dexterity',
                'saving_throw_proficiencies': 'Dexterity, Intelligence',
                'armor_proficiencies': 'Light armor',
                'weapon_proficiencies': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
                'tool_proficiencies': 'Thieves\' tools',
                'skill_choices': 'Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, Stealth',
                'num_skills': 4
            },
            {
                'name': 'Cleric',
                'description': 'A priestly champion who wields divine magic in service of a higher power.',
                'hit_die': 8,
                'primary_ability': 'Wisdom',
                'saving_throw_proficiencies': 'Wisdom, Charisma',
                'armor_proficiencies': 'Light armor, medium armor, shields',
                'weapon_proficiencies': 'Simple weapons',
                'skill_choices': 'History, Insight, Medicine, Persuasion, Religion',
                'num_skills': 2
            },
            {
                'name': 'Ranger',
                'description': 'A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization.',
                'hit_die': 10,
                'primary_ability': 'Dexterity and Wisdom',
                'saving_throw_proficiencies': 'Strength, Dexterity',
                'armor_proficiencies': 'Light armor, medium armor, shields',
                'weapon_proficiencies': 'Simple weapons, martial weapons',
                'skill_choices': 'Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, Survival',
                'num_skills': 3
            },
            {
                'name': 'Paladin',
                'description': 'A holy warrior bound to a sacred oath, wielding divine magic and martial prowess.',
                'hit_die': 10,
                'primary_ability': 'Strength and Charisma',
                'saving_throw_proficiencies': 'Wisdom, Charisma',
                'armor_proficiencies': 'All armor, shields',
                'weapon_proficiencies': 'Simple weapons, martial weapons',
                'skill_choices': 'Athletics, Insight, Intimidation, Medicine, Persuasion, Religion',
                'num_skills': 2
            },
            {
                'name': 'Barbarian',
                'description': 'A fierce warrior who can enter a battle rage, channeling primal fury.',
                'hit_die': 12,
                'primary_ability': 'Strength',
                'saving_throw_proficiencies': 'Strength, Constitution',
                'armor_proficiencies': 'Light armor, medium armor, shields',
                'weapon_proficiencies': 'Simple weapons, martial weapons',
                'skill_choices': 'Animal Handling, Athletics, Intimidation, Nature, Perception, Survival',
                'num_skills': 2
            },
            {
                'name': 'Bard',
                'description': 'An inspiring magician whose power echoes the music of creation.',
                'hit_die': 8,
                'primary_ability': 'Charisma',
                'saving_throw_proficiencies': 'Dexterity, Charisma',
                'armor_proficiencies': 'Light armor',
                'weapon_proficiencies': 'Simple weapons, hand crossbows, longswords, rapiers, shortswords',
                'tool_proficiencies': 'Three musical instruments of your choice',
                'skill_choices': 'Any three skills',
                'num_skills': 3
            },
            {
                'name': 'Druid',
                'description': 'A priest of nature, wielding the power of the natural world.',
                'hit_die': 8,
                'primary_ability': 'Wisdom',
                'saving_throw_proficiencies': 'Intelligence, Wisdom',
                'armor_proficiencies': 'Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)',
                'weapon_proficiencies': 'Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears',
                'tool_proficiencies': 'Herbalism kit',
                'skill_choices': 'Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival',
                'num_skills': 2
            },
            {
                'name': 'Monk',
                'description': 'A master of martial arts, harnessing the power of the body in pursuit of perfection.',
                'hit_die': 8,
                'primary_ability': 'Dexterity and Wisdom',
                'saving_throw_proficiencies': 'Strength, Dexterity',
                'armor_proficiencies': 'None',
                'weapon_proficiencies': 'Simple weapons, shortswords',
                'tool_proficiencies': 'Choose one type of artisan\'s tools or one musical instrument',
                'skill_choices': 'Acrobatics, Athletics, History, Insight, Religion, Stealth',
                'num_skills': 2
            },
            {
                'name': 'Sorcerer',
                'description': 'A spellcaster who draws on inherent magic from a gift or bloodline.',
                'hit_die': 6,
                'primary_ability': 'Charisma',
                'saving_throw_proficiencies': 'Constitution, Charisma',
                'armor_proficiencies': 'None',
                'weapon_proficiencies': 'Daggers, darts, slings, quarterstaffs, light crossbows',
                'skill_choices': 'Arcana, Deception, Insight, Intimidation, Persuasion, Religion',
                'num_skills': 2
            },
            {
                'name': 'Warlock',
                'description': 'A wielder of magic derived from a bargain with an extraplanar entity.',
                'hit_die': 8,
                'primary_ability': 'Charisma',
                'saving_throw_proficiencies': 'Wisdom, Charisma',
                'armor_proficiencies': 'Light armor',
                'weapon_proficiencies': 'Simple weapons',
                'skill_choices': 'Arcana, Deception, History, Intimidation, Investigation, Nature, Religion',
                'num_skills': 2
            }
        ]
        
        for class_data in classes_data:
            char_class, created = CharacterClass.objects.get_or_create(name=class_data['name'], defaults=class_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created class: {char_class.name}'))
        
        # Create Backgrounds
        backgrounds_data = [
            {
                'name': 'Acolyte',
                'description': 'You have spent your life in the service of a temple to a specific god or pantheon of gods.',
                'skill_proficiencies': 'Insight, Religion',
                'tool_proficiencies': '',
                'languages': 2,
                'equipment': 'A holy symbol, a prayer book or prayer wheel, 5 sticks of incense, vestments, common clothes, and a pouch containing 15 gp',
                'feature': 'Shelter of the Faithful',
                'feature_description': 'You and your companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith.'
            },
            {
                'name': 'Criminal',
                'description': 'You are an experienced criminal with a history of breaking the law.',
                'skill_proficiencies': 'Deception, Stealth',
                'tool_proficiencies': 'One type of gaming set, thieves\' tools',
                'languages': 0,
                'equipment': 'A crowbar, dark common clothes with a hood, and a pouch containing 15 gp',
                'feature': 'Criminal Contact',
                'feature_description': 'You have a reliable contact who acts as your liaison to a network of other criminals.'
            },
            {
                'name': 'Folk Hero',
                'description': 'You come from a humble social rank, but you are destined for so much more.',
                'skill_proficiencies': 'Animal Handling, Survival',
                'tool_proficiencies': 'One type of artisan\'s tools, vehicles (land)',
                'languages': 0,
                'equipment': 'A set of artisan\'s tools, a shovel, an iron pot, common clothes, and a pouch containing 10 gp',
                'feature': 'Rustic Hospitality',
                'feature_description': 'Common folk are willing to hide you or help you, unless you have shown yourself to be a danger to them.'
            },
            {
                'name': 'Noble',
                'description': 'You understand wealth, power, and privilege. You carry a noble title.',
                'skill_proficiencies': 'History, Persuasion',
                'tool_proficiencies': 'One type of gaming set',
                'languages': 1,
                'equipment': 'Fine clothes, a signet ring, a scroll of pedigree, and a purse containing 25 gp',
                'feature': 'Position of Privilege',
                'feature_description': 'You are welcome in high society, and people assume you have the right to be wherever you are.'
            },
            {
                'name': 'Sage',
                'description': 'You spent years learning the lore of the multiverse.',
                'skill_proficiencies': 'Arcana, History',
                'tool_proficiencies': '',
                'languages': 2,
                'equipment': 'A bottle of black ink, a quill, a small knife, a letter from a dead colleague, common clothes, and a pouch containing 10 gp',
                'feature': 'Researcher',
                'feature_description': 'When you attempt to learn or recall a piece of lore, if you don\'t know it, you often know where to find it.'
            },
            {
                'name': 'Soldier',
                'description': 'War has been your life for as long as you can remember.',
                'skill_proficiencies': 'Athletics, Intimidation',
                'tool_proficiencies': 'One type of gaming set, vehicles (land)',
                'languages': 0,
                'equipment': 'An insignia of rank, a trophy from a fallen enemy, a set of bone dice or deck of cards, common clothes, and a pouch containing 10 gp',
                'feature': 'Military Rank',
                'feature_description': 'You have a military rank and soldiers loyal to your former military organization still recognize your authority.'
            }
        ]
        
        for bg_data in backgrounds_data:
            background, created = Background.objects.get_or_create(name=bg_data['name'], defaults=bg_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created background: {background.name}'))
        
        self.stdout.write(self.style.SUCCESS('Successfully populated D&D 5e data!'))
