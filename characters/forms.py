from django import forms
from .models import Character, Race, CharacterClass, Background, Equipment, Feat, Spell, CharacterSpell


class LevelUpForm(forms.Form):
    """Form for leveling up a character"""
    
    HP_CHOICE = [
        ('roll', 'Roll Hit Die'),
        ('average', 'Take Average'),
    ]
    
    ASI_CHOICE = [
        ('asi', 'Ability Score Improvement (+2 to one ability or +1 to two abilities)'),
        ('feat', 'Take a Feat'),
    ]
    
    hp_method = forms.ChoiceField(
        choices=HP_CHOICE,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Hit Points",
        help_text="Choose how to increase your HP"
    )
    
    hp_roll = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        label="HP Roll Result",
        help_text="This will be filled automatically if you choose to roll"
    )
    
    # ASI or Feat (only shown at levels 4, 8, 12, 16, 19)
    asi_or_feat = forms.ChoiceField(
        choices=ASI_CHOICE,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label="Ability Score Improvement or Feat",
        required=False
    )
    
    # ASI options
    asi_ability_1 = forms.ChoiceField(
        choices=[
            ('', 'Select Ability...'),
            ('strength', 'Strength'),
            ('dexterity', 'Dexterity'),
            ('constitution', 'Constitution'),
            ('intelligence', 'Intelligence'),
            ('wisdom', 'Wisdom'),
            ('charisma', 'Charisma'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="First Ability to Increase",
        required=False
    )
    
    asi_ability_1_amount = forms.ChoiceField(
        choices=[('1', '+1'), ('2', '+2')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Amount",
        required=False
    )
    
    asi_ability_2 = forms.ChoiceField(
        choices=[
            ('', 'None'),
            ('strength', 'Strength'),
            ('dexterity', 'Dexterity'),
            ('constitution', 'Constitution'),
            ('intelligence', 'Intelligence'),
            ('wisdom', 'Wisdom'),
            ('charisma', 'Charisma'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Second Ability to Increase (Optional)",
        required=False
    )
    
    # Feat selection
    feat = forms.ModelChoiceField(
        queryset=Feat.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'feat-select'}),
        label="Select Feat",
        required=False,
        help_text="Choose a feat from the list"
    )
    
    def __init__(self, *args, character=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.character = character
        
        # Only show ASI/Feat options at appropriate levels
        if character:
            new_level = character.level + 1
            # ASI levels for most classes are 4, 8, 12, 16, 19 (Fighter gets extras at 6, 14)
            asi_levels = [4, 8, 12, 16, 19]
            if character.character_class.name == 'Fighter':
                asi_levels.extend([6, 14])
            
            if new_level not in asi_levels:
                # Hide ASI/Feat fields if not an ASI level
                self.fields['asi_or_feat'].widget = forms.HiddenInput()
                self.fields['asi_ability_1'].widget = forms.HiddenInput()
                self.fields['asi_ability_1_amount'].widget = forms.HiddenInput()
                self.fields['asi_ability_2'].widget = forms.HiddenInput()
                self.fields['feat'].widget = forms.HiddenInput()
    
    def clean(self):
        cleaned_data = super().clean()
        asi_or_feat = cleaned_data.get('asi_or_feat')
        
        if asi_or_feat == 'asi':
            # Validate ASI choices
            ability_1 = cleaned_data.get('asi_ability_1')
            amount_1 = cleaned_data.get('asi_ability_1_amount')
            ability_2 = cleaned_data.get('asi_ability_2')
            
            if not ability_1:
                raise forms.ValidationError("You must select at least one ability to improve.")
            
            if amount_1 == '2' and ability_2:
                raise forms.ValidationError("You can either increase one ability by 2, or two abilities by 1 each.")
            
            if amount_1 == '1' and not ability_2:
                raise forms.ValidationError("If increasing by +1, you must select a second ability or choose +2 to one ability.")
            
            if ability_1 == ability_2 and ability_2:
                raise forms.ValidationError("Cannot increase the same ability twice.")
        
        elif asi_or_feat == 'feat':
            # Validate feat selection
            feat = cleaned_data.get('feat')
            if not feat:
                raise forms.ValidationError("You must select a feat.")
        
        return cleaned_data


class CharacterCreationForm(forms.ModelForm):
    """Form for creating a new character"""
    
    ALIGNMENT_CHOICES = [
        ('', 'Select Alignment...'),
        ('Lawful Good', 'Lawful Good'),
        ('Neutral Good', 'Neutral Good'),
        ('Chaotic Good', 'Chaotic Good'),
        ('Lawful Neutral', 'Lawful Neutral'),
        ('True Neutral', 'True Neutral'),
        ('Chaotic Neutral', 'Chaotic Neutral'),
        ('Lawful Evil', 'Lawful Evil'),
        ('Neutral Evil', 'Neutral Evil'),
        ('Chaotic Evil', 'Chaotic Evil'),
    ]
    
    alignment = forms.ChoiceField(
        choices=ALIGNMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=False
    )
    
    class Meta:
        model = Character
        fields = [
            'name', 'player_name', 'race', 'character_class', 'background',
            'strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma',
            'alignment'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Character Name'}),
            'player_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Player Name'}),
            'race': forms.Select(attrs={'class': 'form-select'}),
            'character_class': forms.Select(attrs={'class': 'form-select'}),
            'background': forms.Select(attrs={'class': 'form-select'}),
            'strength': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
            'dexterity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
            'constitution': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
            'intelligence': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
            'wisdom': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
            'charisma': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '20'}),
        }
        labels = {
            'character_class': 'Class',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add helpful text
        self.fields['strength'].help_text = "Natural athleticism, bodily power"
        self.fields['dexterity'].help_text = "Physical agility, reflexes, balance"
        self.fields['constitution'].help_text = "Health, stamina, vital force"
        self.fields['intelligence'].help_text = "Mental acuity, information recall, reasoning"
        self.fields['wisdom'].help_text = "Awareness, intuition, insight"
        self.fields['charisma'].help_text = "Confidence, eloquence, leadership"


class CharacterSkillsForm(forms.ModelForm):
    """Form for selecting character skills"""
    
    class Meta:
        model = Character
        fields = [
            'acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception',
            'history', 'insight', 'intimidation', 'investigation', 'medicine',
            'nature', 'perception', 'performance', 'persuasion', 'religion',
            'sleight_of_hand', 'stealth', 'survival'
        ]
        widgets = {
            'acrobatics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'animal_handling': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'arcana': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'athletics': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'deception': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'history': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'insight': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'intimidation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'investigation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'medicine': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nature': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'perception': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'performance': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'persuasion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'religion': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sleight_of_hand': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stealth': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'survival': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store the max skills allowed for validation
        if self.instance and self.instance.character_class:
            self.max_skills = self.instance.character_class.num_skills
        else:
            self.max_skills = None
    
    def clean(self):
        """Validate that no more skills are selected than allowed by the class"""
        cleaned_data = super().clean()
        
        if self.max_skills is not None:
            # Count selected skills
            selected_count = sum(1 for field_name in self.Meta.fields if cleaned_data.get(field_name))
            
            if selected_count > self.max_skills:
                raise forms.ValidationError(
                    f'You can only select {self.max_skills} skill(s) for your class, but you selected {selected_count}.'
                )
        
        return cleaned_data


class CharacterExpertiseForm(forms.ModelForm):
    """Form for selecting character expertise (double proficiency bonus)"""
    
    class Meta:
        model = Character
        fields = [
            'acrobatics_expertise', 'animal_handling_expertise', 'arcana_expertise', 
            'athletics_expertise', 'deception_expertise', 'history_expertise', 
            'insight_expertise', 'intimidation_expertise', 'investigation_expertise', 
            'medicine_expertise', 'nature_expertise', 'perception_expertise', 
            'performance_expertise', 'persuasion_expertise', 'religion_expertise', 
            'sleight_of_hand_expertise', 'stealth_expertise', 'survival_expertise'
        ]
        widgets = {
            'acrobatics_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'animal_handling_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'arcana_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'athletics_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'deception_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'history_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'insight_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'intimidation_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'investigation_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'medicine_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'nature_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'perception_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'performance_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'persuasion_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'religion_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sleight_of_hand_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'stealth_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'survival_expertise': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def __init__(self, *args, character=None, max_choices=2, check_proficiency=True, **kwargs):
        """
        Initialize the form with optional character and max_choices parameters.
        
        Args:
            character: Character instance (used to check proficient skills if check_proficiency=True)
            max_choices: Maximum number of expertise selections allowed (default: 2)
            check_proficiency: If True, disable expertise for non-proficient skills (default: True)
                             Set to False during character creation when skills haven't been saved yet
        """
        super().__init__(*args, **kwargs)
        self.max_choices = max_choices
        
        # If character provided and proficiency checking enabled, only allow expertise on proficient skills
        if character and check_proficiency:
            skill_mapping = {
                'acrobatics_expertise': character.acrobatics,
                'animal_handling_expertise': character.animal_handling,
                'arcana_expertise': character.arcana,
                'athletics_expertise': character.athletics,
                'deception_expertise': character.deception,
                'history_expertise': character.history,
                'insight_expertise': character.insight,
                'intimidation_expertise': character.intimidation,
                'investigation_expertise': character.investigation,
                'medicine_expertise': character.medicine,
                'nature_expertise': character.nature,
                'perception_expertise': character.perception,
                'performance_expertise': character.performance,
                'persuasion_expertise': character.persuasion,
                'religion_expertise': character.religion,
                'sleight_of_hand_expertise': character.sleight_of_hand,
                'stealth_expertise': character.stealth,
                'survival_expertise': character.survival,
            }
            
            # Disable expertise checkboxes for non-proficient skills
            for field_name, is_proficient in skill_mapping.items():
                if not is_proficient:
                    self.fields[field_name].widget.attrs['disabled'] = 'disabled'
                    self.fields[field_name].help_text = 'Must be proficient to gain expertise'
    
    def clean(self):
        """Validate that no more than max_choices expertise selections are made"""
        cleaned_data = super().clean()
        
        # Count selected expertise fields
        selected_count = sum(1 for field_name in self.Meta.fields if cleaned_data.get(field_name))
        
        if selected_count > self.max_choices:
            raise forms.ValidationError(
                f'You can only select {self.max_choices} skill(s) for expertise, but you selected {selected_count}.'
            )
        
        return cleaned_data


class CharacterDetailsForm(forms.ModelForm):
    """Form for character details, personality, and equipment"""
    
    equipment_items = forms.ModelMultipleChoiceField(
        queryset=Equipment.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select'
        }),
        help_text="Hold Ctrl/Cmd to select multiple items, or use the search box"
    )
    
    class Meta:
        model = Character
        fields = [
            'languages', 'tool_proficiencies',
            'personality_traits', 'ideals', 'bonds', 'flaws',
            'features_and_traits', 'equipment', 'equipment_items',
            'copper_pieces', 'silver_pieces', 'electrum_pieces', 'gold_pieces', 'platinum_pieces'
        ]
        widgets = {
            'languages': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2,
                'placeholder': 'E.g., Common, Elvish, Draconic'
            }),
            'tool_proficiencies': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2,
                'placeholder': 'E.g., Smith\'s Tools, Thieves\' Tools'
            }),
            'personality_traits': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'ideals': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'bonds': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'flaws': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'features_and_traits': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'equipment': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Additional equipment notes (custom items, enchantments, modifications, etc.)...'
            }),
            'copper_pieces': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'silver_pieces': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'electrum_pieces': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'gold_pieces': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'platinum_pieces': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }


class CharacterCombatForm(forms.ModelForm):
    """Form for combat and survival tracking"""
    
    class Meta:
        model = Character
        fields = [
            'current_hit_points', 'temporary_hit_points', 'hit_dice_used',
            'inspiration', 'death_save_successes', 'death_save_failures',
            'exhaustion_level', 'conditions',
            'damage_immunities', 'damage_resistances', 'damage_vulnerabilities', 'condition_immunities'
        ]
        widgets = {
            'current_hit_points': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'temporary_hit_points': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'hit_dice_used': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'inspiration': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'death_save_successes': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '3'}),
            'death_save_failures': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '3'}),
            'exhaustion_level': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '6'}),
            'conditions': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 2,
                'placeholder': 'E.g., Poisoned, Stunned, Frightened'
            }),
            'damage_immunities': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'E.g., Fire, Poison'
            }),
            'damage_resistances': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'E.g., Cold, Lightning'
            }),
            'damage_vulnerabilities': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'E.g., Fire, Radiant'
            }),
            'condition_immunities': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'E.g., Charmed, Frightened'
            }),
        }
        labels = {
            'current_hit_points': 'Current HP',
            'temporary_hit_points': 'Temporary HP',
            'hit_dice_used': 'Hit Dice Used',
            'death_save_successes': 'Death Save Successes (0-3)',
            'death_save_failures': 'Death Save Failures (0-3)',
            'exhaustion_level': 'Exhaustion Level (0-6)',
            'damage_immunities': 'Damage Immunities',
            'damage_resistances': 'Damage Resistances',
            'damage_vulnerabilities': 'Damage Vulnerabilities',
            'condition_immunities': 'Condition Immunities',
        }


class SpellManagementForm(forms.Form):
    """Form for managing character spells"""
    def __init__(self, *args, **kwargs):
        character = kwargs.pop('character', None)
        super().__init__(*args, **kwargs)
        
        # Store spells data for template access
        self.spells_by_level = {}
        
        if character and character.is_spellcaster:
            from .models import Spell
            from .spell_slots import get_max_spell_level
            
            # Get max spell level this character can cast
            max_spell_level = get_max_spell_level(character.character_class.name, character.level)
            
            # Get spells available to this character's class
            available_spells = Spell.objects.filter(
                classes__icontains=character.character_class.name
            ).order_by('level', 'name')
            
            # Group spells by level (only up to max castable level)
            for level in range(0, max_spell_level + 1):
                spells_at_level = available_spells.filter(level=level)
                if spells_at_level.exists():
                    level_name = 'Cantrips' if level == 0 else f'Level {level}'
                    
                    # Store spell objects for template
                    self.spells_by_level[level] = list(spells_at_level)
                    
                    choices = [(spell.id, f"{spell.name} ({spell.school})") 
                              for spell in spells_at_level]
                    
                    self.fields[f'spells_level_{level}'] = forms.MultipleChoiceField(
                        choices=choices,
                        required=False,
                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
                        label=level_name
                    )


class SpellSlotsForm(forms.ModelForm):
    """Form for managing spell slots - slots are auto-set based on level"""
    class Meta:
        model = Character
        fields = [
            'spellcasting_ability',
            'spell_slots_1_max', 'spell_slots_1_used',
            'spell_slots_2_max', 'spell_slots_2_used',
            'spell_slots_3_max', 'spell_slots_3_used',
            'spell_slots_4_max', 'spell_slots_4_used',
            'spell_slots_5_max', 'spell_slots_5_used',
            'spell_slots_6_max', 'spell_slots_6_used',
            'spell_slots_7_max', 'spell_slots_7_used',
            'spell_slots_8_max', 'spell_slots_8_used',
            'spell_slots_9_max', 'spell_slots_9_used',
        ]
        widgets = {
            'spellcasting_ability': forms.Select(attrs={'class': 'form-select'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Make max spell slots read-only (they're auto-calculated)
        for level in range(1, 10):
            max_field = f'spell_slots_{level}_max'
            self.fields[max_field].widget.attrs.update({
                'class': 'form-control', 
                'readonly': 'readonly',
                'disabled': 'disabled'
            })
            self.fields[max_field].required = False
            
            # Used slots are editable
            used_field = f'spell_slots_{level}_used'
            self.fields[used_field].widget.attrs.update({
                'class': 'form-control', 'min': '0'
            })
