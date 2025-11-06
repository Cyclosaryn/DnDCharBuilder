from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Feat(models.Model):
    """D&D 5e feats"""
    name = models.CharField(max_length=100, unique=True)
    prerequisite = models.CharField(max_length=200, blank=True, help_text="Prerequisites to take this feat")
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Equipment(models.Model):
    """D&D 5e equipment items"""
    CATEGORY_CHOICES = [
        ('Weapon', 'Weapon'),
        ('Armor', 'Armor'),
        ('Adventuring Gear', 'Adventuring Gear'),
        ('Tool', 'Tool'),
        ('Mount', 'Mount'),
        ('Vehicle', 'Vehicle'),
        ('Potion', 'Potion'),
        ('Scroll', 'Scroll'),
        ('Wondrous Item', 'Wondrous Item'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    cost_gold = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=6, decimal_places=2, default=0, help_text="Weight in pounds")
    
    def get_damage_info(self):
        """Extract damage information from weapon description"""
        import re
        if self.category != 'Weapon':
            return None
        # Pattern to match damage like "1d8", "1d10", "2d6", "1 piercing", etc.
        damage_pattern = r'(\d+(?:d\d+)?(?:/\d+d\d+)?)\s+(\w+)'
        match = re.search(damage_pattern, self.description)
        if match:
            damage_dice = match.group(1)
            damage_type = match.group(2)
            return f"{damage_dice} {damage_type}"
        return None
    
    def get_properties(self):
        """Extract weapon properties from description"""
        import re
        if self.category != 'Weapon':
            return []
        # Extract everything after the damage type
        parts = self.description.split(',')
        if len(parts) > 2:
            # Skip category and damage, return rest as properties
            properties = [p.strip() for p in parts[2:]]
            return properties
        return []
    
    def get_armor_class(self):
        """Extract AC from armor description"""
        import re
        if self.category != 'Armor':
            return None
        # Pattern to match AC like "AC 11", "AC 14", etc.
        ac_pattern = r'AC\s+(\d+(?:\s*\+\s*Dex)?)'
        match = re.search(ac_pattern, self.description)
        if match:
            return match.group(1)
        return None
    
    def __str__(self):
        return f"{self.name} ({self.category})"
    
    class Meta:
        ordering = ['category', 'name']
        verbose_name_plural = "Equipment"


class Race(models.Model):
    """D&D 5e races"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    speed = models.IntegerField(default=30)
    size = models.CharField(max_length=20, choices=[
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ], default='Medium')
    
    # Ability score increases
    strength_bonus = models.IntegerField(default=0)
    dexterity_bonus = models.IntegerField(default=0)
    constitution_bonus = models.IntegerField(default=0)
    intelligence_bonus = models.IntegerField(default=0)
    wisdom_bonus = models.IntegerField(default=0)
    charisma_bonus = models.IntegerField(default=0)
    
    traits = models.TextField(blank=True, help_text="Special racial traits")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class CharacterClass(models.Model):
    """D&D 5e classes"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    hit_die = models.IntegerField(help_text="Hit die (e.g., 6 for d6, 8 for d8)")
    
    # Primary ability scores
    primary_ability = models.CharField(max_length=100, help_text="Primary ability scores")
    
    # Saving throw proficiencies
    saving_throw_proficiencies = models.CharField(max_length=100)
    
    # Armor and weapon proficiencies
    armor_proficiencies = models.TextField(blank=True)
    weapon_proficiencies = models.TextField(blank=True)
    tool_proficiencies = models.TextField(blank=True)
    
    # Skills
    skill_choices = models.TextField(help_text="Available skill choices")
    num_skills = models.IntegerField(default=2, help_text="Number of skills to choose")
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Character Classes"


class Background(models.Model):
    """D&D 5e backgrounds"""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    skill_proficiencies = models.CharField(max_length=200)
    tool_proficiencies = models.CharField(max_length=200, blank=True)
    languages = models.IntegerField(default=0, help_text="Number of additional languages")
    equipment = models.TextField()
    feature = models.CharField(max_length=100)
    feature_description = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class Character(models.Model):
    """Player character"""
    # Basic information
    name = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100, blank=True)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)
    subrace = models.CharField(max_length=50, blank=True, help_text="Subrace (e.g., Hill Dwarf, High Elf)")
    character_class = models.ForeignKey(CharacterClass, on_delete=models.PROTECT)
    background = models.ForeignKey(Background, on_delete=models.PROTECT)
    level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    
    # Ability scores (base values before racial bonuses)
    strength = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dexterity = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    constitution = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    intelligence = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    wisdom = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    charisma = models.IntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(20)])
    
    # Hit points
    max_hit_points = models.IntegerField(default=0)
    current_hit_points = models.IntegerField(default=0)
    temporary_hit_points = models.IntegerField(default=0)
    hit_dice_used = models.IntegerField(default=0, help_text="Number of hit dice used (for short rest recovery)")
    
    # Feats and Ability Score Improvements
    feats = models.ManyToManyField(Feat, blank=True, related_name='characters')
    ability_score_improvements = models.TextField(blank=True, help_text="Record of ASI choices by level")
    
    # Skills (proficiency)
    acrobatics = models.BooleanField(default=False)
    animal_handling = models.BooleanField(default=False)
    arcana = models.BooleanField(default=False)
    athletics = models.BooleanField(default=False)
    deception = models.BooleanField(default=False)
    history = models.BooleanField(default=False)
    insight = models.BooleanField(default=False)
    intimidation = models.BooleanField(default=False)
    investigation = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    nature = models.BooleanField(default=False)
    perception = models.BooleanField(default=False)
    performance = models.BooleanField(default=False)
    persuasion = models.BooleanField(default=False)
    religion = models.BooleanField(default=False)
    sleight_of_hand = models.BooleanField(default=False)
    stealth = models.BooleanField(default=False)
    survival = models.BooleanField(default=False)
    
    # Skills (expertise - doubles proficiency bonus)
    acrobatics_expertise = models.BooleanField(default=False, help_text="Has expertise in Acrobatics (2x proficiency bonus)")
    animal_handling_expertise = models.BooleanField(default=False, help_text="Has expertise in Animal Handling (2x proficiency bonus)")
    arcana_expertise = models.BooleanField(default=False, help_text="Has expertise in Arcana (2x proficiency bonus)")
    athletics_expertise = models.BooleanField(default=False, help_text="Has expertise in Athletics (2x proficiency bonus)")
    deception_expertise = models.BooleanField(default=False, help_text="Has expertise in Deception (2x proficiency bonus)")
    history_expertise = models.BooleanField(default=False, help_text="Has expertise in History (2x proficiency bonus)")
    insight_expertise = models.BooleanField(default=False, help_text="Has expertise in Insight (2x proficiency bonus)")
    intimidation_expertise = models.BooleanField(default=False, help_text="Has expertise in Intimidation (2x proficiency bonus)")
    investigation_expertise = models.BooleanField(default=False, help_text="Has expertise in Investigation (2x proficiency bonus)")
    medicine_expertise = models.BooleanField(default=False, help_text="Has expertise in Medicine (2x proficiency bonus)")
    nature_expertise = models.BooleanField(default=False, help_text="Has expertise in Nature (2x proficiency bonus)")
    perception_expertise = models.BooleanField(default=False, help_text="Has expertise in Perception (2x proficiency bonus)")
    performance_expertise = models.BooleanField(default=False, help_text="Has expertise in Performance (2x proficiency bonus)")
    persuasion_expertise = models.BooleanField(default=False, help_text="Has expertise in Persuasion (2x proficiency bonus)")
    religion_expertise = models.BooleanField(default=False, help_text="Has expertise in Religion (2x proficiency bonus)")
    sleight_of_hand_expertise = models.BooleanField(default=False, help_text="Has expertise in Sleight of Hand (2x proficiency bonus)")
    stealth_expertise = models.BooleanField(default=False, help_text="Has expertise in Stealth (2x proficiency bonus)")
    survival_expertise = models.BooleanField(default=False, help_text="Has expertise in Survival (2x proficiency bonus)")
    
    # Other character details
    alignment = models.CharField(max_length=50, blank=True)
    personality_traits = models.TextField(blank=True)
    ideals = models.TextField(blank=True)
    bonds = models.TextField(blank=True)
    flaws = models.TextField(blank=True)
    features_and_traits = models.TextField(blank=True)
    
    # Languages and proficiencies
    languages = models.TextField(blank=True, help_text="Languages known (comma-separated)")
    tool_proficiencies = models.TextField(blank=True, help_text="Tool proficiencies (comma-separated)")
    
    # Combat and survival tracking
    inspiration = models.BooleanField(default=False, help_text="Has inspiration")
    death_save_successes = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    death_save_failures = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    exhaustion_level = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)], help_text="Exhaustion level (0-6)")
    conditions = models.TextField(blank=True, help_text="Active conditions (comma-separated)")
    
    # Damage types
    damage_immunities = models.TextField(blank=True, help_text="Damage immunities (e.g., Fire, Poison)")
    damage_resistances = models.TextField(blank=True, help_text="Damage resistances (e.g., Cold, Lightning)")
    damage_vulnerabilities = models.TextField(blank=True, help_text="Damage vulnerabilities (e.g., Fire, Radiant)")
    condition_immunities = models.TextField(blank=True, help_text="Condition immunities (e.g., Charmed, Frightened)")
    
    # Spellcasting
    spellcasting_ability = models.CharField(max_length=3, blank=True, choices=[
        ('INT', 'Intelligence'), ('WIS', 'Wisdom'), ('CHA', 'Charisma')
    ], help_text="Primary spellcasting ability")
    spell_slots_1_max = models.IntegerField(default=0, help_text="Max level 1 spell slots")
    spell_slots_1_used = models.IntegerField(default=0, help_text="Used level 1 spell slots")
    spell_slots_2_max = models.IntegerField(default=0, help_text="Max level 2 spell slots")
    spell_slots_2_used = models.IntegerField(default=0, help_text="Used level 2 spell slots")
    spell_slots_3_max = models.IntegerField(default=0, help_text="Max level 3 spell slots")
    spell_slots_3_used = models.IntegerField(default=0, help_text="Used level 3 spell slots")
    spell_slots_4_max = models.IntegerField(default=0, help_text="Max level 4 spell slots")
    spell_slots_4_used = models.IntegerField(default=0, help_text="Used level 4 spell slots")
    spell_slots_5_max = models.IntegerField(default=0, help_text="Max level 5 spell slots")
    spell_slots_5_used = models.IntegerField(default=0, help_text="Used level 5 spell slots")
    spell_slots_6_max = models.IntegerField(default=0, help_text="Max level 6 spell slots")
    spell_slots_6_used = models.IntegerField(default=0, help_text="Used level 6 spell slots")
    spell_slots_7_max = models.IntegerField(default=0, help_text="Max level 7 spell slots")
    spell_slots_7_used = models.IntegerField(default=0, help_text="Used level 7 spell slots")
    spell_slots_8_max = models.IntegerField(default=0, help_text="Max level 8 spell slots")
    spell_slots_8_used = models.IntegerField(default=0, help_text="Used level 8 spell slots")
    spell_slots_9_max = models.IntegerField(default=0, help_text="Max level 9 spell slots")
    spell_slots_9_used = models.IntegerField(default=0, help_text="Used level 9 spell slots")
    
    # Equipment
    equipment = models.TextField(blank=True)  # Free-form equipment notes
    equipment_items = models.ManyToManyField(Equipment, blank=True, related_name='characters')
    
    # Money
    copper_pieces = models.IntegerField(default=0)
    silver_pieces = models.IntegerField(default=0)
    electrum_pieces = models.IntegerField(default=0)
    gold_pieces = models.IntegerField(default=0)
    platinum_pieces = models.IntegerField(default=0)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - Level {self.level} {self.race.name} {self.character_class.name}"
    
    @property
    def total_strength(self):
        """Strength with racial bonus"""
        return self.strength + self.race.strength_bonus
    
    @property
    def total_dexterity(self):
        """Dexterity with racial bonus"""
        return self.dexterity + self.race.dexterity_bonus
    
    @property
    def total_constitution(self):
        """Constitution with racial bonus"""
        return self.constitution + self.race.constitution_bonus
    
    @property
    def total_intelligence(self):
        """Intelligence with racial bonus"""
        return self.intelligence + self.race.intelligence_bonus
    
    @property
    def total_wisdom(self):
        """Wisdom with racial bonus"""
        return self.wisdom + self.race.wisdom_bonus
    
    @property
    def total_charisma(self):
        """Charisma with racial bonus"""
        return self.charisma + self.race.charisma_bonus
    
    @property
    def available_hit_dice(self):
        """Calculate available (unused) hit dice"""
        return self.level - self.hit_dice_used
    
    @staticmethod
    def ability_modifier(score):
        """Calculate ability modifier from ability score"""
        return (score - 10) // 2
    
    @property
    def strength_modifier(self):
        return self.ability_modifier(self.total_strength)
    
    @property
    def dexterity_modifier(self):
        return self.ability_modifier(self.total_dexterity)
    
    @property
    def constitution_modifier(self):
        return self.ability_modifier(self.total_constitution)
    
    @property
    def intelligence_modifier(self):
        return self.ability_modifier(self.total_intelligence)
    
    @property
    def wisdom_modifier(self):
        return self.ability_modifier(self.total_wisdom)
    
    @property
    def charisma_modifier(self):
        return self.ability_modifier(self.total_charisma)
    
    @property
    def proficiency_bonus(self):
        """Calculate proficiency bonus based on level"""
        return ((self.level - 1) // 4) + 2
    
    @property
    def armor_class(self):
        """Calculate AC (base 10 + dex modifier)"""
        return 10 + self.dexterity_modifier
    
    @property
    def initiative(self):
        """Initiative bonus"""
        return self.dexterity_modifier
    
    @property
    def speed(self):
        """Character speed from race"""
        return self.race.speed
    
    @property
    def is_spellcaster(self):
        """Check if character can cast spells"""
        spellcasting_classes = ['Bard', 'Cleric', 'Druid', 'Paladin', 'Ranger', 'Sorcerer', 'Warlock', 'Wizard']
        return self.character_class.name in spellcasting_classes
    
    @property
    def spell_save_dc(self):
        """Calculate spell save DC"""
        if not self.spellcasting_ability:
            return None
        ability_mod = {
            'INT': self.intelligence_modifier,
            'WIS': self.wisdom_modifier,
            'CHA': self.charisma_modifier
        }.get(self.spellcasting_ability, 0)
        return 8 + self.proficiency_bonus + ability_mod
    
    @property
    def spell_attack_bonus(self):
        """Calculate spell attack bonus"""
        if not self.spellcasting_ability:
            return None
        ability_mod = {
            'INT': self.intelligence_modifier,
            'WIS': self.wisdom_modifier,
            'CHA': self.charisma_modifier
        }.get(self.spellcasting_ability, 0)
        return self.proficiency_bonus + ability_mod
    
    def get_spell_slots_available(self, level):
        """Get available spell slots for a given level"""
        if level < 1 or level > 9:
            return 0, 0
        max_slots = getattr(self, f'spell_slots_{level}_max', 0)
        used_slots = getattr(self, f'spell_slots_{level}_used', 0)
        return max_slots - used_slots, max_slots
    
    def use_spell_slot(self, level):
        """Use a spell slot of the given level"""
        if level < 1 or level > 9:
            return False
        available, max_slots = self.get_spell_slots_available(level)
        if available > 0:
            used_field = f'spell_slots_{level}_used'
            setattr(self, used_field, getattr(self, used_field) + 1)
            self.save()
            return True
        return False
    
    def restore_spell_slots(self):
        """Restore all spell slots (long rest)"""
        for level in range(1, 10):
            setattr(self, f'spell_slots_{level}_used', 0)
        self.save()
    
    def get_computed_damage_immunities(self):
        """Get damage immunities from race, subrace, class, and features"""
        from .damage_types import get_damage_types_for_character
        damage_types = get_damage_types_for_character(self)
        return damage_types['damage_immunities']
    
    def get_computed_damage_resistances(self):
        """Get damage resistances from race, subrace, class, and features"""
        from .damage_types import get_damage_types_for_character
        damage_types = get_damage_types_for_character(self)
        return damage_types['damage_resistances']
    
    def get_computed_damage_vulnerabilities(self):
        """Get damage vulnerabilities from race, subrace, class, and features"""
        from .damage_types import get_damage_types_for_character
        damage_types = get_damage_types_for_character(self)
        return damage_types['damage_vulnerabilities']
    
    def get_computed_condition_immunities(self):
        """Get condition immunities from race, subrace, class, and features"""
        from .damage_types import get_damage_types_for_character
        damage_types = get_damage_types_for_character(self)
        return damage_types['condition_immunities']
    
    class Meta:
        ordering = ['-updated_at']


class Spell(models.Model):
    """D&D 5e spells"""
    name = models.CharField(max_length=100, unique=True)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    school = models.CharField(max_length=50, choices=[
        ('Abjuration', 'Abjuration'),
        ('Conjuration', 'Conjuration'),
        ('Divination', 'Divination'),
        ('Enchantment', 'Enchantment'),
        ('Evocation', 'Evocation'),
        ('Illusion', 'Illusion'),
        ('Necromancy', 'Necromancy'),
        ('Transmutation', 'Transmutation'),
    ])
    casting_time = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    components = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    classes = models.CharField(max_length=200, help_text="Classes that can cast this spell")
    
    def __str__(self):
        return f"{self.name} (Level {self.level})"
    
    def get_damage_info(self):
        """Extract damage information from description"""
        import re
        # Look for damage patterns like "2d6", "3d8 fire damage", etc.
        damage_pattern = r'(\d+d\d+(?:\s*\+\s*\d+)?)\s*(?:(\w+)\s+)?damage'
        matches = re.findall(damage_pattern, self.description, re.IGNORECASE)
        if matches:
            damages = []
            for dice, dmg_type in matches:
                if dmg_type:
                    damages.append(f"{dice} {dmg_type}")
                else:
                    damages.append(dice)
            return ", ".join(damages) if damages else None
        return None
    
    def get_save_dc(self):
        """Extract saving throw information from description"""
        import re
        # Look for saving throw patterns
        save_pattern = r'(Constitution|Strength|Dexterity|Intelligence|Wisdom|Charisma)\s+saving throw'
        match = re.search(save_pattern, self.description, re.IGNORECASE)
        if match:
            return f"{match.group(1)} save"
        return None
    
    class Meta:
        ordering = ['level', 'name']


class CharacterSpell(models.Model):
    """Spells known/prepared by a character"""
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='spells')
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    is_prepared = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ['character', 'spell']


class CharacterClassFeature(models.Model):
    """Class features selected by a character"""
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='class_features')
    feature_type = models.CharField(max_length=100, help_text="E.g., 'Fighting Style', 'Metamagic', 'Eldritch Invocations'")
    feature_name = models.CharField(max_length=100, help_text="E.g., 'Archery', 'Careful Spell', 'Agonizing Blast'")
    feature_description = models.TextField(blank=True)
    level_gained = models.IntegerField(help_text="Character level when this feature was gained")
    sub_choice = models.CharField(max_length=100, blank=True, help_text="Secondary choice (e.g., 'Black Dragon', 'Arctic')")
    
    def __str__(self):
        if self.sub_choice:
            return f"{self.character.name} - {self.feature_type}: {self.feature_name} ({self.sub_choice})"
        return f"{self.character.name} - {self.feature_type}: {self.feature_name}"
    
    class Meta:
        ordering = ['level_gained', 'feature_type', 'feature_name']
