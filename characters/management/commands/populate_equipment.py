from django.core.management.base import BaseCommand
from characters.models import Equipment


class Command(BaseCommand):
    help = 'Populate the database with D&D 5e equipment'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating equipment...')
        
        equipment_data = [
            # Weapons - Simple Melee
            {'name': 'Club', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d4 bludgeoning', 'cost_gold': 0.1, 'weight': 2},
            {'name': 'Dagger', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d4 piercing, finesse, light, thrown (20/60)', 'cost_gold': 2, 'weight': 1},
            {'name': 'Greatclub', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d8 bludgeoning, two-handed', 'cost_gold': 0.2, 'weight': 10},
            {'name': 'Handaxe', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d6 slashing, light, thrown (20/60)', 'cost_gold': 5, 'weight': 2},
            {'name': 'Javelin', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d6 piercing, thrown (30/120)', 'cost_gold': 0.5, 'weight': 2},
            {'name': 'Light Hammer', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d4 bludgeoning, light, thrown (20/60)', 'cost_gold': 2, 'weight': 2},
            {'name': 'Mace', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d6 bludgeoning', 'cost_gold': 5, 'weight': 4},
            {'name': 'Quarterstaff', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d6/1d8 bludgeoning, versatile', 'cost_gold': 0.2, 'weight': 4},
            {'name': 'Sickle', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d4 slashing, light', 'cost_gold': 1, 'weight': 2},
            {'name': 'Spear', 'category': 'Weapon', 'description': 'Simple melee weapon, 1d6/1d8 piercing, thrown (20/60), versatile', 'cost_gold': 1, 'weight': 3},
            
            # Weapons - Simple Ranged
            {'name': 'Light Crossbow', 'category': 'Weapon', 'description': 'Simple ranged weapon, 1d8 piercing, ammunition (80/320), loading, two-handed', 'cost_gold': 25, 'weight': 5},
            {'name': 'Dart', 'category': 'Weapon', 'description': 'Simple ranged weapon, 1d4 piercing, finesse, thrown (20/60)', 'cost_gold': 0.05, 'weight': 0.25},
            {'name': 'Shortbow', 'category': 'Weapon', 'description': 'Simple ranged weapon, 1d6 piercing, ammunition (80/320), two-handed', 'cost_gold': 25, 'weight': 2},
            {'name': 'Sling', 'category': 'Weapon', 'description': 'Simple ranged weapon, 1d4 bludgeoning, ammunition (30/120)', 'cost_gold': 0.1, 'weight': 0},
            
            # Weapons - Martial Melee
            {'name': 'Battleaxe', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8/1d10 slashing, versatile', 'cost_gold': 10, 'weight': 4},
            {'name': 'Flail', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8 bludgeoning', 'cost_gold': 10, 'weight': 2},
            {'name': 'Glaive', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d10 slashing, heavy, reach, two-handed', 'cost_gold': 20, 'weight': 6},
            {'name': 'Greataxe', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d12 slashing, heavy, two-handed', 'cost_gold': 30, 'weight': 7},
            {'name': 'Greatsword', 'category': 'Weapon', 'description': 'Martial melee weapon, 2d6 slashing, heavy, two-handed', 'cost_gold': 50, 'weight': 6},
            {'name': 'Halberd', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d10 slashing, heavy, reach, two-handed', 'cost_gold': 20, 'weight': 6},
            {'name': 'Lance', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d12 piercing, reach, special', 'cost_gold': 10, 'weight': 6},
            {'name': 'Longsword', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8/1d10 slashing, versatile', 'cost_gold': 15, 'weight': 3},
            {'name': 'Maul', 'category': 'Weapon', 'description': 'Martial melee weapon, 2d6 bludgeoning, heavy, two-handed', 'cost_gold': 10, 'weight': 10},
            {'name': 'Morningstar', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8 piercing', 'cost_gold': 15, 'weight': 4},
            {'name': 'Pike', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d10 piercing, heavy, reach, two-handed', 'cost_gold': 5, 'weight': 18},
            {'name': 'Rapier', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8 piercing, finesse', 'cost_gold': 25, 'weight': 2},
            {'name': 'Scimitar', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d6 slashing, finesse, light', 'cost_gold': 25, 'weight': 3},
            {'name': 'Shortsword', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d6 piercing, finesse, light', 'cost_gold': 10, 'weight': 2},
            {'name': 'Trident', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d6/1d8 piercing, thrown (20/60), versatile', 'cost_gold': 5, 'weight': 4},
            {'name': 'War Pick', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8 piercing', 'cost_gold': 5, 'weight': 2},
            {'name': 'Warhammer', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d8/1d10 bludgeoning, versatile', 'cost_gold': 15, 'weight': 2},
            {'name': 'Whip', 'category': 'Weapon', 'description': 'Martial melee weapon, 1d4 slashing, finesse, reach', 'cost_gold': 2, 'weight': 3},
            
            # Weapons - Martial Ranged
            {'name': 'Blowgun', 'category': 'Weapon', 'description': 'Martial ranged weapon, 1 piercing, ammunition (25/100), loading', 'cost_gold': 10, 'weight': 1},
            {'name': 'Hand Crossbow', 'category': 'Weapon', 'description': 'Martial ranged weapon, 1d6 piercing, ammunition (30/120), light, loading', 'cost_gold': 75, 'weight': 3},
            {'name': 'Heavy Crossbow', 'category': 'Weapon', 'description': 'Martial ranged weapon, 1d10 piercing, ammunition (100/400), heavy, loading, two-handed', 'cost_gold': 50, 'weight': 18},
            {'name': 'Longbow', 'category': 'Weapon', 'description': 'Martial ranged weapon, 1d8 piercing, ammunition (150/600), heavy, two-handed', 'cost_gold': 50, 'weight': 2},
            {'name': 'Net', 'category': 'Weapon', 'description': 'Martial ranged weapon, special, thrown (5/15)', 'cost_gold': 1, 'weight': 3},
            
            # Armor - Light
            {'name': 'Padded Armor', 'category': 'Armor', 'description': 'Light armor, AC 11 + Dex modifier, disadvantage on Stealth', 'cost_gold': 5, 'weight': 8},
            {'name': 'Leather Armor', 'category': 'Armor', 'description': 'Light armor, AC 11 + Dex modifier', 'cost_gold': 10, 'weight': 10},
            {'name': 'Studded Leather Armor', 'category': 'Armor', 'description': 'Light armor, AC 12 + Dex modifier', 'cost_gold': 45, 'weight': 13},
            
            # Armor - Medium
            {'name': 'Hide Armor', 'category': 'Armor', 'description': 'Medium armor, AC 12 + Dex modifier (max 2)', 'cost_gold': 10, 'weight': 12},
            {'name': 'Chain Shirt', 'category': 'Armor', 'description': 'Medium armor, AC 13 + Dex modifier (max 2)', 'cost_gold': 50, 'weight': 20},
            {'name': 'Scale Mail', 'category': 'Armor', 'description': 'Medium armor, AC 14 + Dex modifier (max 2), disadvantage on Stealth', 'cost_gold': 50, 'weight': 45},
            {'name': 'Breastplate', 'category': 'Armor', 'description': 'Medium armor, AC 14 + Dex modifier (max 2)', 'cost_gold': 400, 'weight': 20},
            {'name': 'Half Plate', 'category': 'Armor', 'description': 'Medium armor, AC 15 + Dex modifier (max 2), disadvantage on Stealth', 'cost_gold': 750, 'weight': 40},
            
            # Armor - Heavy
            {'name': 'Ring Mail', 'category': 'Armor', 'description': 'Heavy armor, AC 14, disadvantage on Stealth', 'cost_gold': 30, 'weight': 40},
            {'name': 'Chain Mail', 'category': 'Armor', 'description': 'Heavy armor, AC 16, Str 13 required, disadvantage on Stealth', 'cost_gold': 75, 'weight': 55},
            {'name': 'Splint Armor', 'category': 'Armor', 'description': 'Heavy armor, AC 17, Str 15 required, disadvantage on Stealth', 'cost_gold': 200, 'weight': 60},
            {'name': 'Plate Armor', 'category': 'Armor', 'description': 'Heavy armor, AC 18, Str 15 required, disadvantage on Stealth', 'cost_gold': 1500, 'weight': 65},
            
            # Armor - Shields
            {'name': 'Shield', 'category': 'Armor', 'description': '+2 AC', 'cost_gold': 10, 'weight': 6},
            
            # Adventuring Gear
            {'name': 'Backpack', 'category': 'Adventuring Gear', 'description': 'Holds up to 30 lbs of gear', 'cost_gold': 2, 'weight': 5},
            {'name': 'Bedroll', 'category': 'Adventuring Gear', 'description': 'For sleeping', 'cost_gold': 1, 'weight': 7},
            {'name': 'Rope, Hempen (50 feet)', 'category': 'Adventuring Gear', 'description': '50 feet of rope', 'cost_gold': 1, 'weight': 10},
            {'name': 'Rope, Silk (50 feet)', 'category': 'Adventuring Gear', 'description': '50 feet of silk rope', 'cost_gold': 10, 'weight': 5},
            {'name': 'Torches (10)', 'category': 'Adventuring Gear', 'description': '10 torches, each burns for 1 hour', 'cost_gold': 0.1, 'weight': 1},
            {'name': 'Tinderbox', 'category': 'Adventuring Gear', 'description': 'For starting fires', 'cost_gold': 0.5, 'weight': 1},
            {'name': 'Rations (1 day)', 'category': 'Adventuring Gear', 'description': 'One day of food', 'cost_gold': 0.5, 'weight': 2},
            {'name': 'Waterskin', 'category': 'Adventuring Gear', 'description': 'Holds 4 pints of liquid', 'cost_gold': 0.2, 'weight': 5},
            {'name': 'Crowbar', 'category': 'Adventuring Gear', 'description': 'Advantage on Strength checks where leverage can be applied', 'cost_gold': 2, 'weight': 5},
            {'name': 'Hammer', 'category': 'Adventuring Gear', 'description': 'For driving spikes', 'cost_gold': 1, 'weight': 3},
            {'name': 'Pitons (10)', 'category': 'Adventuring Gear', 'description': '10 iron spikes', 'cost_gold': 0.5, 'weight': 2.5},
            {'name': 'Lantern, Hooded', 'category': 'Adventuring Gear', 'description': 'Casts bright light 30 ft, dim light 30 ft more', 'cost_gold': 5, 'weight': 2},
            {'name': 'Lantern, Bullseye', 'category': 'Adventuring Gear', 'description': 'Casts 60-ft cone of bright light, 60 ft more dim', 'cost_gold': 10, 'weight': 3},
            {'name': 'Oil (flask)', 'category': 'Adventuring Gear', 'description': 'Fuel for lantern or weapon', 'cost_gold': 0.1, 'weight': 1},
            {'name': 'Grappling Hook', 'category': 'Adventuring Gear', 'description': 'For climbing', 'cost_gold': 2, 'weight': 4},
            {'name': 'Chain (10 feet)', 'category': 'Adventuring Gear', 'description': '10 feet of chain', 'cost_gold': 5, 'weight': 10},
            {'name': 'Manacles', 'category': 'Adventuring Gear', 'description': 'DC 20 to break, DC 20 to pick lock', 'cost_gold': 2, 'weight': 6},
            {'name': 'Mirror, Steel', 'category': 'Adventuring Gear', 'description': 'Useful for looking around corners', 'cost_gold': 5, 'weight': 0.5},
            {'name': 'Flask or Tankard', 'category': 'Adventuring Gear', 'description': 'For drinking', 'cost_gold': 0.02, 'weight': 1},
            {'name': 'Jug or Pitcher', 'category': 'Adventuring Gear', 'description': 'Holds 1 gallon', 'cost_gold': 0.02, 'weight': 4},
            {'name': 'Chest', 'category': 'Adventuring Gear', 'description': 'Holds 12 cubic feet', 'cost_gold': 5, 'weight': 25},
            {'name': 'Tent, Two-person', 'category': 'Adventuring Gear', 'description': 'Shelter for 2', 'cost_gold': 2, 'weight': 20},
            {'name': 'Blanket', 'category': 'Adventuring Gear', 'description': 'For warmth', 'cost_gold': 0.5, 'weight': 3},
            {'name': 'Caltrops (bag of 20)', 'category': 'Adventuring Gear', 'description': 'Cover 5-ft square, DC 15 Dex save or stop moving and take 1 piercing damage', 'cost_gold': 1, 'weight': 2},
            {'name': "Climber's Kit", 'category': 'Adventuring Gear', 'description': 'Includes pitons, boot tips, gloves, and harness', 'cost_gold': 25, 'weight': 12},
            {'name': 'Healer\'s Kit', 'category': 'Adventuring Gear', 'description': '10 uses, stabilize dying creature without check', 'cost_gold': 5, 'weight': 3},
            {'name': 'Spellbook', 'category': 'Adventuring Gear', 'description': 'Blank book with 100 pages', 'cost_gold': 50, 'weight': 3},
            
            # Tools
            {'name': "Alchemist's Supplies", 'category': 'Tool', 'description': 'For crafting alchemical items', 'cost_gold': 50, 'weight': 8},
            {'name': "Brewer's Supplies", 'category': 'Tool', 'description': 'For brewing beer and ale', 'cost_gold': 20, 'weight': 9},
            {'name': "Calligrapher's Supplies", 'category': 'Tool', 'description': 'For creating written works', 'cost_gold': 10, 'weight': 5},
            {'name': "Carpenter's Tools", 'category': 'Tool', 'description': 'For woodworking', 'cost_gold': 8, 'weight': 6},
            {'name': "Cartographer's Tools", 'category': 'Tool', 'description': 'For making maps', 'cost_gold': 15, 'weight': 6},
            {'name': "Cook's Utensils", 'category': 'Tool', 'description': 'For preparing meals', 'cost_gold': 1, 'weight': 8},
            {'name': "Disguise Kit", 'category': 'Tool', 'description': 'For creating disguises', 'cost_gold': 25, 'weight': 3},
            {'name': "Herbalism Kit", 'category': 'Tool', 'description': 'For identifying and using herbs', 'cost_gold': 5, 'weight': 3},
            {'name': "Navigator's Tools", 'category': 'Tool', 'description': 'For plotting courses', 'cost_gold': 25, 'weight': 2},
            {'name': "Poisoner's Kit", 'category': 'Tool', 'description': 'For handling poisons', 'cost_gold': 50, 'weight': 2},
            {'name': "Thieves' Tools", 'category': 'Tool', 'description': 'For picking locks and disarming traps', 'cost_gold': 25, 'weight': 1},
            
            # Potions
            {'name': 'Potion of Healing', 'category': 'Potion', 'description': 'Restores 2d4+2 hit points', 'cost_gold': 50, 'weight': 0.5},
            {'name': 'Potion of Greater Healing', 'category': 'Potion', 'description': 'Restores 4d4+4 hit points', 'cost_gold': 150, 'weight': 0.5},
            {'name': 'Antitoxin', 'category': 'Potion', 'description': 'Advantage on saving throws vs poison for 1 hour', 'cost_gold': 50, 'weight': 0},
            
            # Mounts
            {'name': 'Horse, Riding', 'category': 'Mount', 'description': 'Speed 60 ft', 'cost_gold': 75, 'weight': 0},
            {'name': 'Horse, Draft', 'category': 'Mount', 'description': 'Speed 40 ft, can pull heavy loads', 'cost_gold': 50, 'weight': 0},
            {'name': 'Pony', 'category': 'Mount', 'description': 'Speed 40 ft', 'cost_gold': 30, 'weight': 0},
            {'name': 'Saddle, Riding', 'category': 'Adventuring Gear', 'description': 'For riding a mount', 'cost_gold': 10, 'weight': 25},
            {'name': 'Saddle, Pack', 'category': 'Adventuring Gear', 'description': 'For carrying cargo', 'cost_gold': 5, 'weight': 15},
        ]
        
        created_count = 0
        for item_data in equipment_data:
            equipment, created = Equipment.objects.get_or_create(
                name=item_data['name'],
                defaults=item_data
            )
            if created:
                created_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully populated {created_count} equipment items. '
                f'Total equipment in database: {Equipment.objects.count()}'
            )
        )
