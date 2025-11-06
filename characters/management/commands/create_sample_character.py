from django.core.management.base import BaseCommand
from characters.models import Race, CharacterClass, Background, Character


class Command(BaseCommand):
    help = 'Creates a sample character for demonstration'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample character...')
        
        # Get race, class, and background
        try:
            human = Race.objects.get(name='Human')
            fighter = CharacterClass.objects.get(name='Fighter')
            soldier = Background.objects.get(name='Soldier')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
            self.stdout.write(self.style.ERROR('Make sure you\'ve run: python manage.py populate_dnd_data'))
            return
        
        # Create character
        character, created = Character.objects.get_or_create(
            name='Thorin Ironforge',
            defaults={
                'player_name': 'Demo Player',
                'race': human,
                'character_class': fighter,
                'background': soldier,
                'level': 1,
                'alignment': 'Lawful Good',
                
                # Ability scores (Standard Array)
                'strength': 15,
                'dexterity': 14,
                'constitution': 13,
                'intelligence': 10,
                'wisdom': 12,
                'charisma': 8,
                
                # Skills
                'athletics': True,
                'intimidation': True,
                'perception': True,
                
                # Personality
                'personality_traits': 'I face problems head-on. A simple, direct solution is the best path to success.',
                'ideals': 'Greater Good: Our lot is to lay down our lives in defense of others.',
                'bonds': 'I would still lay down my life for the people I served with.',
                'flaws': 'I made a terrible mistake in battle that cost many lives—and I would do anything to keep that mistake secret.',
                
                # Features
                'features_and_traits': '''Fighting Style: Defense (+1 AC while wearing armor)
Second Wind: Regain 1d10 + fighter level HP as a bonus action (once per short rest)

Soldier Feature - Military Rank:
You have a military rank and soldiers loyal to your former military organization still recognize your authority.''',
                
                # Equipment
                'equipment': '''Chain Mail (AC 16)
Longsword (1d8 slashing)
Shield (+2 AC)
Light Crossbow and 20 bolts
Explorer's Pack
Insignia of rank
Trophy from fallen enemy
Set of bone dice
Common clothes
Belt pouch''',
                
                # Money
                'gold_pieces': 10,
            }
        )
        
        if created:
            # Calculate HP: Fighter hit die (d10) = 10 at 1st level + CON modifier
            character.max_hit_points = 10 + character.constitution_modifier
            character.current_hit_points = character.max_hit_points
            character.save()
            
            self.stdout.write(self.style.SUCCESS(f'Successfully created character: {character.name}'))
            self.stdout.write(self.style.SUCCESS(f'  Race: {character.race.name}'))
            self.stdout.write(self.style.SUCCESS(f'  Class: {character.character_class.name}'))
            self.stdout.write(self.style.SUCCESS(f'  Level: {character.level}'))
            self.stdout.write(self.style.SUCCESS(f'  HP: {character.max_hit_points}'))
            self.stdout.write(self.style.SUCCESS(f'  AC: {character.armor_class + 6}'))  # +5 from chain mail + shield, +1 from Fighting Style
            self.stdout.write(self.style.SUCCESS(f'  Proficiency Bonus: +{character.proficiency_bonus}'))
        else:
            self.stdout.write(self.style.WARNING(f'Character "{character.name}" already exists!'))
