"""
Populate the database with D&D 5e Basic Rules (2014) spells
Based on: https://www.dndbeyond.com/sources/dnd/basic-rules-2014
"""

from django.core.management.base import BaseCommand
from characters.models import Spell


class Command(BaseCommand):
    help = 'Populate database with D&D 5e Basic Rules spells'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating D&D 5e spells from Basic Rules...')
        
        spells_data = [
            # CANTRIPS (Level 0)
            {
                'name': 'Acid Splash',
                'level': 0,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "You hurl a bubble of acid. Choose one creature within range, or choose two creatures within range that are within 5 feet of each other. A target must succeed on a Dexterity saving throw or take 1d6 acid damage. This spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6)."
            },
            {
                'name': 'Blade Ward',
                'level': 0,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V, S',
                'duration': '1 round',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "You extend your hand and trace a sigil of warding in the air. Until the end of your next turn, you have resistance against bludgeoning, piercing, and slashing damage dealt by weapon attacks."
            },
            {
                'name': 'Dancing Lights',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S, M (a bit of phosphorus or wychwood, or a glowworm)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Bard, Sorcerer, Wizard',
                "description": "You create up to four torch-sized lights within range, making them appear as torches, lanterns, or glowing orbs that hover in the air for the duration."
            },
            {
                'name': 'Fire Bolt',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "You hurl a mote of fire at a creature or object within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 fire damage. The spell's damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10)."
            },
            {
                'name': 'Light',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, M (a firefly or phosphorescent moss)',
                'duration': '1 hour',
                'classes': 'Bard, Cleric, Sorcerer, Wizard',
                "description": "You touch one object that is no larger than 10 feet in any dimension. Until the spell ends, the object sheds bright light in a 20-foot radius and dim light for an additional 20 feet."
            },
            {
                'name': 'Mage Hand',
                'level': 0,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'V, S',
                'duration': '1 minute',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "A spectral, floating hand appears at a point you choose within range. The hand lasts for the duration or until you dismiss it as an action. You can use your action to control the hand."
            },
            {
                'name': 'Mending',
                'level': 0,
                'school': 'Transmutation',
                'casting_time': '1 minute',
                'range': 'Touch',
                'components': 'V, S, M (two lodestones)',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Druid, Sorcerer, Wizard',
                "description": "This spell repairs a single break or tear in an object you touch, such as a broken chain link, two halves of a broken key, a torn cloak, or a leaking wineskin."
            },
            {
                'name': 'Minor Illusion',
                'level': 0,
                'school': 'Illusion',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'S, M (a bit of fleece)',
                'duration': '1 minute',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "You create a sound or an image of an object within range that lasts for the duration. The illusion also ends if you dismiss it as an action or cast this spell again."
            },
            {
                'name': 'Poison Spray',
                'level': 0,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '10 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Druid, Sorcerer, Warlock, Wizard',
                "description": "You extend your hand toward a creature you can see within range and project a puff of noxious gas from your palm. The creature must succeed on a Constitution saving throw or take 1d12 poison damage. This spell's damage increases by 1d12 when you reach 5th level (2d12), 11th level (3d12), and 17th level (4d12)."
            },
            {
                'name': 'Prestidigitation',
                'level': 0,
                'school': 'Transmutation',
                'casting_time': '1 action',
                'range': '10 feet',
                'components': 'V, S',
                'duration': 'Up to 1 hour',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "This spell is a minor magical trick that novice spellcasters use for practice. You create one of several minor effects."
            },
            {
                'name': 'Ray of Frost',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "A frigid beam of blue-white light streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, it takes 1d8 cold damage, and its speed is reduced by 10 feet until the start of your next turn. The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
            },
            {
                'name': 'Shocking Grasp',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "Lightning springs from your hand to deliver a shock to a creature you try to touch. Make a melee spell attack against the target. You have advantage on the attack roll if the target is wearing armor made of metal. On a hit, the target takes 1d8 lightning damage, and it can't take reactions until the start of its next turn. The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
            },
            {
                'name': 'True Strike',
                'level': 0,
                'school': 'Divination',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'S',
                'duration': 'Concentration, up to 1 round',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "You extend your hand and point a finger at a target in range. Your magic grants you a brief insight into the target's defenses. On your next turn, you gain advantage on your first attack roll against the target, provided that this spell hasn't ended."
            },
            {
                'name': 'Sacred Flame',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Cleric',
                "description": "Flame-like radiance descends on a creature that you can see within range. The target must succeed on a Dexterity saving throw or take 1d8 radiant damage. The target gains no benefit from cover for this saving throw. The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
            },
            {
                'name': 'Spare the Dying',
                'level': 0,
                'school': 'Necromancy',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Cleric',
                "description": "You touch a living creature that has 0 hit points. The creature becomes stable. This spell has no effect on undead or constructs."
            },
            {
                'name': 'Thaumaturgy',
                'level': 0,
                'school': 'Transmutation',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'V',
                'duration': '1 minute',
                'classes': 'Cleric',
                "description": "You manifest a minor wonder, a sign of supernatural power, within range. You create one of several effects that demonstrate your power."
            },
            {
                'name': 'Guidance',
                'level': 0,
                'school': 'Divination',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Cleric, Druid',
                "description": "You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one ability check of its choice."
            },
            {
                'name': 'Produce Flame',
                'level': 0,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V, S',
                'duration': '10 minutes',
                'classes': 'Druid',
                "description": "A flickering flame appears in your hand. The flame remains there for the duration and harms neither you nor your equipment. The flame sheds bright light in a 10-foot radius and dim light for an additional 10 feet. You can also attack with the flame as part of casting this spell. The spell's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8)."
            },
            {
                'name': 'Resistance',
                'level': 0,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (a miniature cloak)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Cleric, Druid',
                "description": "You touch one willing creature. Once before the spell ends, the target can roll a d4 and add the number rolled to one saving throw of its choice."
            },
            {
                'name': 'Shillelagh',
                'level': 0,
                'school': 'Transmutation',
                'casting_time': '1 bonus action',
                'range': 'Touch',
                'components': 'V, S, M (mistletoe, a shamrock leaf, and a club or quarterstaff)',
                'duration': '1 minute',
                'classes': 'Druid',
                "description": "The wood of a club or quarterstaff you are holding is imbued with nature's power. For the duration, you can use your spellcasting ability instead of Strength for the attack and damage rolls of melee attacks using that weapon."
            },
            {
                'name': 'Eldritch Blast',
                'level': 0,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Warlock',
                "description": "A beam of crackling energy streaks toward a creature within range. Make a ranged spell attack against the target. On a hit, the target takes 1d10 force damage. The spell creates more than one beam when you reach higher levels: two beams at 5th level, three beams at 11th level, and four beams at 17th level."
            },
            
            # 1ST LEVEL SPELLS
            {
                'name': 'Burning Hands',
                'level': 1,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Self (15-foot cone)',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "As you hold your hands with thumbs touching and fingers spread, a thin sheet of flames shoots forth from your outstretched fingertips. Each creature in a 15-foot cone must make a Dexterity saving throw. A creature takes 3d6 fire damage on a failed save, or half as much damage on a successful one. At Higher Levels: +1d6 fire damage for each slot level above 1st."
            },
            {
                'name': 'Charm Person',
                'level': 1,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'V, S',
                'duration': '1 hour',
                'classes': 'Bard, Druid, Sorcerer, Warlock, Wizard',
                "description": "You attempt to charm a humanoid you can see within range. It must make a Wisdom saving throw, and does so with advantage if you or your companions are fighting it. If it fails, it is charmed by you until the spell ends or until you or your companions do anything harmful to it."
            },
            {
                'name': 'Cure Wounds',
                'level': 1,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Druid, Paladin, Ranger',
                "description": "A creature you touch regains a number of hit points equal to 1d8 + your spellcasting ability modifier. This spell has no effect on undead or constructs. At Higher Levels: +1d8 for each slot level above 1st."
            },
            {
                'name': 'Detect Magic',
                'level': 1,
                'school': 'Divination',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V, S',
                'duration': 'Concentration, up to 10 minutes',
                'classes': 'Bard, Cleric, Druid, Paladin, Ranger, Sorcerer, Wizard',
                "description": "For the duration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn its school of magic, if any."
            },
            {
                'name': 'Disguise Self',
                'level': 1,
                'school': 'Illusion',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V, S',
                'duration': '1 hour',
                'classes': 'Bard, Sorcerer, Wizard',
                "description": "You make yourself—including your clothing, armor, weapons, and other belongings on your person—look different until the spell ends or until you use your action to dismiss it."
            },
            {
                'name': 'Mage Armor',
                'level': 1,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (a piece of cured leather)',
                'duration': '8 hours',
                'classes': 'Sorcerer, Wizard',
                "description": "You touch a willing creature who isn't wearing armor, and a protective magical force surrounds it until the spell ends. The target's base AC becomes 13 + its Dexterity modifier."
            },
            {
                'name': 'Magic Missile',
                'level': 1,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously. At Higher Levels: One more dart for each slot level above 1st."
            },
            {
                'name': 'Shield',
                'level': 1,
                'school': 'Abjuration',
                'casting_time': '1 reaction',
                'range': 'Self',
                'components': 'V, S',
                'duration': 'Until your next turn',
                'classes': 'Sorcerer, Wizard',
                "description": "An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile."
            },
            {
                'name': 'Sleep',
                'level': 1,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '90 feet',
                'components': 'V, S, M (a pinch of fine sand, rose petals, or a cricket)',
                'duration': 'One minute',
                'classes': 'Bard, Sorcerer, Wizard',
                "description": "This spell sends creatures into a magical slumber. Roll 5d8; the total is how many hit points of creatures this spell can affect. Creatures within 20 feet of a point you choose within range are affected in ascending order of their current hit points."
            },
            {
                'name': 'Thunderwave',
                'level': 1,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Self (15-foot cube)',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Bard, Druid, Sorcerer, Wizard',
                "description": "A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. On a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn't pushed."
            },
            {
                'name': 'Bless',
                'level': 1,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'V, S, M (a sprinkling of holy water)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Cleric, Paladin',
                "description": "You bless up to three creatures of your choice within range. Whenever a target makes an attack roll or a saving throw before the spell ends, the target can roll a d4 and add the number rolled to the attack roll or saving throw."
            },
            {
                'name': 'Healing Word',
                'level': 1,
                'school': 'Evocation',
                'casting_time': '1 bonus action',
                'range': '60 feet',
                'components': 'V',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Druid',
                "description": "A creature of your choice that you can see within range regains hit points equal to 1d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs. At Higher Levels: +1d4 for each slot level above 1st."
            },
            {
                'name': 'Sanctuary',
                'level': 1,
                'school': 'Abjuration',
                'casting_time': '1 bonus action',
                'range': '30 feet',
                'components': 'V, S, M (a small silver mirror)',
                'duration': 'One minute',
                'classes': 'Cleric',
                "description": "You ward a creature within range against attack. Until the spell ends, any creature who targets the warded creature with an attack or a harmful spell must first make a Wisdom saving throw. On a failed save, the creature must choose a new target or lose the attack or spell."
            },
            {
                'name': 'Entangle',
                'level': 1,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '90 feet',
                'components': 'V, S',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Druid',
                "description": "Grasping weeds and vines sprout from the ground in a 20-foot square starting from a point within range. For the duration, these plants turn the ground in the area into difficult terrain. A creature in the area when you cast the spell must succeed on a Strength saving throw or be restrained by the entangling plants until the spell ends."
            },
            {
                'name': 'Goodberry',
                'level': 1,
                'school': 'Transmutation',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (a sprig of mistletoe)',
                'duration': 'Instantaneous',
                'classes': 'Druid, Ranger',
                "description": "Up to ten berries appear in your hand and are infused with magic for the duration. A creature can use its action to eat one berry. Eating a berry restores 1 hit point, and the berry provides enough nourishment to sustain a creature for one day."
            },
            {
                'name': 'Speak with Animals',
                'level': 1,
                'school': 'Divination',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V, S',
                'duration': '10 minutes',
                'classes': 'Bard, Druid, Ranger',
                "description": "You gain the ability to comprehend and verbally communicate with beasts for the duration. The knowledge and awareness of many beasts is limited by their intelligence, but at minimum, beasts can give you information about nearby locations and monsters, including whatever they can perceive or have perceived within the past day."
            },
            {
                'name': 'Hex',
                'level': 1,
                'school': 'Enchantment',
                'casting_time': '1 bonus action',
                'range': '90 feet',
                'components': 'V, S, M (the petrified eye of a newt)',
                'duration': 'Concentration, up to 1 hour',
                'classes': 'Warlock',
                "description": "You place a curse on a creature that you can see within range. Until the spell ends, you deal an extra 1d6 necrotic damage to the target whenever you hit it with an attack. Also, choose one ability when you cast the spell. The target has disadvantage on ability checks made with the chosen ability."
            },
            
            # 2ND LEVEL SPELLS (Selection)
            {
                'name': 'Scorching Ray',
                'level': 2,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "You create three rays of fire and hurl them at targets within range. You can hurl them at one target or several. Make a ranged spell attack for each ray. On a hit, the target takes 2d6 fire damage. At Higher Levels: One additional ray for each slot level above 2nd."
            },
            {
                'name': 'Invisibility',
                'level': 2,
                'school': 'Illusion',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (an eyelash encased in gum arabic)',
                'duration': 'Concentration, up to 1 hour',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "A creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target's person. The spell ends for a target that attacks or casts a spell."
            },
            {
                'name': 'Hold Person',
                'level': 2,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S, M (a small, straight piece of iron)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Bard, Cleric, Druid, Sorcerer, Warlock, Wizard',
                "description": "Choose a humanoid that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration. At the end of each of its turns, the target can make another Wisdom saving throw. On a success, the spell ends on the target."
            },
            {
                'name': 'Lesser Restoration',
                'level': 2,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Druid, Paladin, Ranger',
                "description": "You touch a creature and can end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned."
            },
            {
                'name': 'Spiritual Weapon',
                'level': 2,
                'school': 'Evocation',
                'casting_time': '1 bonus action',
                'range': '60 feet',
                'components': 'V, S',
                'duration': 'One minute',
                'classes': 'Cleric',
                "description": "You create a floating, spectral weapon within range that lasts for the duration or until you cast this spell again. When you cast the spell, you can make a melee spell attack against a creature within 5 feet of the weapon. On a hit, the target takes force damage equal to 1d8 + your spellcasting ability modifier."
            },
            
            # 3RD LEVEL SPELLS (Selection)
            {
                'name': 'Fireball',
                'level': 3,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '150 feet',
                'components': 'V, S, M (a tiny ball of bat guano and sulfur)',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "A bright streak flashes from your pointing finger to a point you choose within range and then blossoms with a low roar into an explosion of flame. Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one."
            },
            {
                'name': 'Counterspell',
                'level': 3,
                'school': 'Abjuration',
                'casting_time': '1 reaction',
                'range': '60 feet',
                'components': 'S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Warlock, Wizard',
                "description": "You attempt to interrupt a creature in the process of casting a spell. If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a success, the creature's spell fails and has no effect."
            },
            {
                'name': 'Dispel Magic',
                'level': 3,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Druid, Paladin, Sorcerer, Warlock, Wizard',
                "description": "Choose one creature, object, or magical effect within range. Any spell of 3rd level or lower on the target ends. For each spell of 4th level or higher on the target, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a successful check, the spell ends."
            },
            {
                'name': 'Revivify',
                'level': 3,
                'school': 'Necromancy',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (diamonds worth 300 gp, which the spell consumes)',
                'duration': 'Instantaneous',
                'classes': 'Cleric, Paladin',
                "description": "You touch a creature that has died within the last minute. That creature returns to life with 1 hit point. This spell can't return to life a creature that has died of old age, nor can it restore any missing body parts."
            },
            
            # LEVEL 4 SPELLS
            {
                'name': 'Banishment',
                'level': 4,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S, M (an item distasteful to the target)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Cleric, Paladin, Sorcerer, Warlock, Wizard',
                "description": "You attempt to send one creature that you can see within range to another plane of existence. The target must succeed on a Charisma saving throw or be banished. If the target is native to a different plane of existence, it disappears, returning to its home plane. If the spell ends before 1 minute has passed, the target reappears. Otherwise, if native to another plane, the target doesn't return."
            },
            {
                'name': 'Blight',
                'level': 4,
                'school': 'Necromancy',
                'casting_time': '1 action',
                'range': '30 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Druid, Sorcerer, Warlock, Wizard',
                "description": "Necromantic energy washes over a creature of your choice that you can see within range, draining moisture and vitality from it. The target must make a Constitution saving throw. The target takes 8d8 necrotic damage on a failed save, or half as much damage on a successful one. This spell has no effect on undead or constructs."
            },
            {
                'name': 'Confusion',
                'level': 4,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '90 feet',
                'components': 'V, S, M (three nut shells)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Bard, Druid, Sorcerer, Wizard',
                "description": "This spell assaults and twists creatures' minds, spawning delusions and provoking uncontrolled action. Each creature in a 10-foot-radius sphere centered on a point you choose within range must succeed on a Wisdom saving throw or be affected by this spell."
            },
            {
                'name': 'Greater Invisibility',
                'level': 4,
                'school': 'Illusion',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Bard, Sorcerer, Wizard',
                "description": "You or a creature you touch becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target's person."
            },
            {
                'name': 'Ice Storm',
                'level': 4,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '300 feet',
                'components': 'V, S, M (a pinch of dust and a few drops of water)',
                'duration': 'Instantaneous',
                'classes': 'Druid, Sorcerer, Wizard',
                "description": "A hail of rock-hard ice pounds to the ground in a 20-foot-radius, 40-foot-high cylinder centered on a point within range. Each creature in the cylinder must make a Dexterity saving throw. A creature takes 2d8 bludgeoning damage and 4d6 cold damage on a failed save, or half as much damage on a successful one."
            },
            {
                'name': 'Polymorph',
                'level': 4,
                'school': 'Transmutation',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S, M (a caterpillar cocoon)',
                'duration': 'Concentration, up to 1 hour',
                'classes': 'Bard, Druid, Sorcerer, Wizard',
                "description": "This spell transforms a creature that you can see within range into a new form. An unwilling creature must make a Wisdom saving throw to avoid the effect. The transformation lasts for the duration, or until the target drops to 0 hit points or dies."
            },
            {
                'name': 'Wall of Fire',
                'level': 4,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '120 feet',
                'components': 'V, S, M (a small piece of phosphorus)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Druid, Sorcerer, Wizard',
                "description": "You create a wall of fire on a solid surface within range. You can make the wall up to 60 feet long, 20 feet high, and 1 foot thick, or a ringed wall up to 20 feet in diameter, 20 feet high, and 1 foot thick. The wall is opaque and lasts for the duration. When the wall appears, each creature within its area must make a Dexterity saving throw. On a failed save, a creature takes 5d8 fire damage, or half as much on a successful save."
            },
            
            # LEVEL 5 SPELLS
            {
                'name': 'Cone of Cold',
                'level': 5,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Self (60-foot cone)',
                'components': 'V, S, M (a small crystal or glass cone)',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "A blast of cold air erupts from your hands. Each creature in a 60-foot cone must make a Constitution saving throw. A creature takes 8d8 cold damage on a failed save, or half as much damage on a successful one. A creature killed by this spell becomes a frozen statue until it thaws."
            },
            {
                'name': 'Flame Strike',
                'level': 5,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S, M (pinch of sulfur)',
                'duration': 'Instantaneous',
                'classes': 'Cleric',
                "description": "A vertical column of divine fire roars down from the heavens in a location you specify. Each creature in a 10-foot-radius, 40-foot-high cylinder centered on a point within range must make a Dexterity saving throw. A creature takes 4d6 fire damage and 4d6 radiant damage on a failed save, or half as much damage on a successful one."
            },
            {
                'name': 'Greater Restoration',
                'level': 5,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (diamond dust worth at least 100 gp, which the spell consumes)',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Druid',
                "description": "You imbue a creature you touch with positive energy to undo a debilitating effect. You can reduce the target's exhaustion level by one, or end one of the following effects on the target: one effect that charmed or petrified the target, one curse, any reduction to one of the target's ability scores, or one effect reducing the target's hit point maximum."
            },
            {
                'name': 'Hold Monster',
                'level': 5,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '90 feet',
                'components': 'V, S, M (a small, straight piece of iron)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "Choose a creature that you can see within range. The target must succeed on a Wisdom saving throw or be paralyzed for the duration. This spell has no effect on undead. At the end of each of its turns, the target can make another Wisdom saving throw. On a success, the spell ends on the target."
            },
            {
                'name': 'Scrying',
                'level': 5,
                'school': 'Divination',
                'casting_time': '10 minutes',
                'range': 'Self',
                'components': 'V, S, M (a focus worth at least 1,000 gp)',
                'duration': 'Concentration, up to 10 minutes',
                'classes': 'Bard, Cleric, Druid, Warlock, Wizard',
                "description": "You can see and hear a particular creature you choose that is on the same plane of existence as you. The target must make a Wisdom saving throw, which is modified by how well you know the target and the sort of physical connection you have to it."
            },
            {
                'name': 'Teleportation Circle',
                'level': 5,
                'school': 'Conjuration',
                'casting_time': '1 minute',
                'range': '10 feet',
                'components': 'V, M (rare chalks and inks infused with precious gems worth 50 gp)',
                'duration': '1 round',
                'classes': 'Bard, Sorcerer, Wizard',
                "description": "As you cast the spell, you draw a 10-foot-diameter circle on the ground inscribed with sigils that link your location to a permanent teleportation circle of your choice whose sigil sequence you know and that is on the same plane of existence as you."
            },
            
            # LEVEL 6 SPELLS
            {
                'name': 'Chain Lightning',
                'level': 6,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '150 feet',
                'components': 'V, S, M (a bit of fur; a piece of amber, glass, or a crystal rod; and three silver pins)',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "You create a bolt of lightning that arcs toward a target of your choice that you can see within range. Three bolts then leap from that target to as many as three other targets, each of which must be within 30 feet of the first target. A target can be a creature or an object and can be targeted by only one of the bolts. A target must make a Dexterity saving throw. The target takes 10d8 lightning damage on a failed save, or half as much damage on a successful one."
            },
            {
                'name': 'Circle of Death',
                'level': 6,
                'school': 'Necromancy',
                'casting_time': '1 action',
                'range': '150 feet',
                'components': 'V, S, M (the powder of a crushed black pearl worth at least 500 gp)',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Warlock, Wizard',
                "description": "A sphere of negative energy ripples out in a 60-foot-radius sphere from a point within range. Each creature in that area must make a Constitution saving throw. A target takes 8d6 necrotic damage on a failed save, or half as much damage on a successful one."
            },
            {
                'name': 'Disintegrate',
                'level': 6,
                'school': 'Transmutation',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S, M (a lodestone and a pinch of dust)',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "A thin green ray springs from your pointing finger to a target that you can see within range. The target can be a creature, an object, or a creation of magical force. A creature targeted by this spell must make a Dexterity saving throw. On a failed save, the target takes 10d6 + 40 force damage. If this damage reduces the target to 0 hit points, it is disintegrated."
            },
            {
                'name': 'Heal',
                'level': 6,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Cleric, Druid',
                "description": "Choose a creature that you can see within range. A surge of positive energy washes through the creature, causing it to regain 70 hit points. This spell also ends blindness, deafness, and any diseases affecting the target."
            },
            {
                'name': 'True Seeing',
                'level': 6,
                'school': 'Divination',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (an ointment for the eyes that costs 25 gp)',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric, Sorcerer, Warlock, Wizard',
                "description": "This spell gives the willing creature you touch the ability to see things as they actually are. For the duration, the creature has truesight, notices secret doors hidden by magic, and can see into the Ethereal Plane, all out to a range of 120 feet."
            },
            
            # LEVEL 7 SPELLS
            {
                'name': 'Delayed Blast Fireball',
                'level': 7,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '150 feet',
                'components': 'V, S, M (a tiny ball of bat guano and sulfur)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Sorcerer, Wizard',
                "description": "A beam of yellow light flashes from your pointing finger, then condenses to linger at a chosen point within range as a glowing bead for the duration. When the spell ends, either because your concentration is broken or because you decide to end it, the bead blossoms with a low roar into an explosion of flame. Each creature in a 20-foot-radius sphere centered on that point must make a Dexterity saving throw. A creature takes fire damage equal to the total accumulated damage on a failed save, or half as much on a successful one. The spell's base damage is 12d6."
            },
            {
                'name': 'Finger of Death',
                'level': 7,
                'school': 'Necromancy',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Warlock, Wizard',
                "description": "You send negative energy coursing through a creature that you can see within range, causing it searing pain. The target must make a Constitution saving throw. It takes 7d8 + 30 necrotic damage on a failed save, or half as much damage on a successful one. A humanoid killed by this spell rises at the start of your next turn as a zombie that is permanently under your command."
            },
            {
                'name': 'Plane Shift',
                'level': 7,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': 'Touch',
                'components': 'V, S, M (a forked, metal rod worth at least 250 gp, attuned to a particular plane)',
                'duration': 'Instantaneous',
                'classes': 'Cleric, Druid, Sorcerer, Warlock, Wizard',
                "description": "You and up to eight willing creatures who link hands in a circle are transported to a different plane of existence. You can specify a target destination in general terms, and you appear in or near that destination."
            },
            {
                'name': 'Resurrection',
                'level': 7,
                'school': 'Necromancy',
                'casting_time': '1 hour',
                'range': 'Touch',
                'components': 'V, S, M (a diamond worth at least 1,000 gp, which the spell consumes)',
                'duration': 'Instantaneous',
                'classes': 'Bard, Cleric',
                "description": "You touch a dead creature that has been dead for no more than a century, that didn't die of old age, and that isn't undead. If its soul is free and willing, the target returns to life with all its hit points."
            },
            {
                'name': 'Teleport',
                'level': 7,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '10 feet',
                'components': 'V',
                'duration': 'Instantaneous',
                'classes': 'Bard, Sorcerer, Wizard',
                "description": "This spell instantly transports you and up to eight willing creatures of your choice that you can see within range, or a single object that you can see within range, to a destination you select."
            },
            
            # LEVEL 8 SPELLS
            {
                'name': 'Antimagic Field',
                'level': 8,
                'school': 'Abjuration',
                'casting_time': '1 action',
                'range': 'Self (10-foot-radius sphere)',
                'components': 'V, S, M (a pinch of powdered iron or iron filings)',
                'duration': 'Concentration, up to 1 hour',
                'classes': 'Cleric, Wizard',
                "description": "A 10-foot-radius invisible sphere of antimagic surrounds you. This area is divorced from the magical energy that suffuses the multiverse. Within the sphere, spells can't be cast, summoned creatures disappear, and even magic items become mundane."
            },
            {
                'name': 'Earthquake',
                'level': 8,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '500 feet',
                'components': 'V, S, M (a pinch of dirt, a piece of rock, and a lump of clay)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Cleric, Druid, Sorcerer',
                "description": "You create a seismic disturbance at a point on the ground that you can see within range. For the duration, an intense tremor rips through the ground in a 100-foot-radius circle centered on that point and shakes creatures and structures in contact with the ground in that area."
            },
            {
                'name': 'Incendiary Cloud',
                'level': 8,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '150 feet',
                'components': 'V, S',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Sorcerer, Wizard',
                "description": "A swirling cloud of smoke shot through with white-hot embers appears in a 20-foot-radius sphere centered on a point within range. The cloud spreads around corners and is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed disperses it. When the cloud appears, each creature in it must make a Dexterity saving throw. A creature takes 10d8 fire damage on a failed save, or half as much on a successful one."
            },
            {
                'name': 'Power Word Stun',
                'level': 8,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V',
                'duration': 'Instantaneous',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "You speak a word of power that can overwhelm the mind of one creature you can see within range, leaving it dumbfounded. If the target has 150 hit points or fewer, it is stunned. Otherwise, the spell has no effect. The stunned target must make a Constitution saving throw at the end of each of its turns. On a successful save, this stunning effect ends."
            },
            
            # LEVEL 9 SPELLS
            {
                'name': 'Foresight',
                'level': 9,
                'school': 'Divination',
                'casting_time': '1 minute',
                'range': 'Touch',
                'components': 'V, S, M (a hummingbird feather)',
                'duration': '8 hours',
                'classes': 'Bard, Druid, Warlock, Wizard',
                "description": "You touch a willing creature and bestow a limited ability to see into the immediate future. For the duration, the target can't be surprised and has advantage on attack rolls, ability checks, and saving throws. Additionally, other creatures have disadvantage on attack rolls against the target for the duration."
            },
            {
                'name': 'Gate',
                'level': 9,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S, M (a diamond worth at least 5,000 gp)',
                'duration': 'Concentration, up to 1 minute',
                'classes': 'Cleric, Sorcerer, Wizard',
                "description": "You conjure a portal linking an unoccupied space you can see within range to a precise location on a different plane of existence. The portal is a circular opening, which you can make 5 to 20 feet in diameter. You can orient the portal in any direction you choose. The portal lasts for the duration."
            },
            {
                'name': 'Mass Heal',
                'level': 9,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Cleric',
                "description": "A flood of healing energy flows from you into injured creatures around you. You restore up to 700 hit points, divided as you choose among any number of creatures that you can see within range. Creatures healed by this spell are also cured of all diseases and any effect making them blinded or deafened."
            },
            {
                'name': 'Meteor Swarm',
                'level': 9,
                'school': 'Evocation',
                'casting_time': '1 action',
                'range': '1 mile',
                'components': 'V, S',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "Blazing orbs of fire plummet to the ground at four different points you can see within range. Each creature in a 40-foot-radius sphere centered on each point you choose must make a Dexterity saving throw. The sphere spreads around corners. A creature takes 20d6 fire damage and 20d6 bludgeoning damage on a failed save, or half as much damage on a successful one."
            },
            {
                'name': 'Power Word Kill',
                'level': 9,
                'school': 'Enchantment',
                'casting_time': '1 action',
                'range': '60 feet',
                'components': 'V',
                'duration': 'Instantaneous',
                'classes': 'Bard, Sorcerer, Warlock, Wizard',
                "description": "You utter a word of power that can compel one creature you can see within range to die instantly. If the creature you choose has 100 hit points or fewer, it dies. Otherwise, the spell has no effect."
            },
            {
                'name': 'Time Stop',
                'level': 9,
                'school': 'Transmutation',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "You briefly stop the flow of time for everyone but yourself. No time passes for other creatures, while you take 1d4 + 1 turns in a row, during which you can use actions and move as normal."
            },
            {
                'name': 'True Resurrection',
                'level': 9,
                'school': 'Necromancy',
                'casting_time': '1 hour',
                'range': 'Touch',
                'components': 'V, S, M (a sprinkle of holy water and diamonds worth at least 25,000 gp, which the spell consumes)',
                'duration': 'Instantaneous',
                'classes': 'Cleric, Druid',
                "description": "You touch a creature that has been dead for no longer than 200 years and that died for any reason except old age. If the creature's soul is free and willing, the creature is restored to life with all its hit points."
            },
            {
                'name': 'Wish',
                'level': 9,
                'school': 'Conjuration',
                'casting_time': '1 action',
                'range': 'Self',
                'components': 'V',
                'duration': 'Instantaneous',
                'classes': 'Sorcerer, Wizard',
                "description": "Wish is the mightiest spell a mortal creature can cast. By simply speaking aloud, you can alter the very foundations of reality in accord with your desires. The basic use of this spell is to duplicate any other spell of 8th level or lower. You don't need to meet any requirements in that spell. The spell simply takes effect. Alternatively, you can create one of many other effects at the DM's discretion."
            },
        ]
        
        created_count = 0
        updated_count = 0
        
        for spell_data in spells_data:
            spell, created = Spell.objects.update_or_create(
                name=spell_data['name'],
                defaults=spell_data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Created: {spell.name}'))
            else:
                updated_count += 1
                self.stdout.write(f'  Updated: {spell.name}')
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Spell population complete!'))
        self.stdout.write(f'   Created: {created_count} spells')
        self.stdout.write(f'   Updated: {updated_count} spells')
        self.stdout.write(f'   Total: {Spell.objects.count()} spells in database')
