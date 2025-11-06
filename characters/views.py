from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Character, Race, CharacterClass, Background, Equipment, Feat
from .forms import CharacterCreationForm, CharacterSkillsForm, CharacterDetailsForm, LevelUpForm, CharacterCombatForm


def auto_populate_racial_traits(character):
    """Auto-populate damage resistances/immunities based on race and subrace"""
    race_name = character.race.name
    subrace_name = character.subrace
    
    # Mapping of races to their damage resistances/immunities
    racial_resistances = {
        'Dwarf': {'resistances': 'Poison'},
        'Tiefling': {'resistances': 'Fire'},
    }
    
    # Dragonborn damage resistance based on ancestry (subrace)
    dragonborn_resistances = {
        'Black Dragon Ancestry': 'Acid',
        'Blue Dragon Ancestry': 'Lightning',
        'Brass Dragon Ancestry': 'Fire',
        'Bronze Dragon Ancestry': 'Lightning',
        'Copper Dragon Ancestry': 'Acid',
        'Gold Dragon Ancestry': 'Fire',
        'Green Dragon Ancestry': 'Poison',
        'Red Dragon Ancestry': 'Fire',
        'Silver Dragon Ancestry': 'Cold',
        'White Dragon Ancestry': 'Cold',
    }
    
    # Handle Dragonborn with subrace
    if race_name == 'Dragonborn' and subrace_name in dragonborn_resistances:
        if not character.damage_resistances:
            character.damage_resistances = dragonborn_resistances[subrace_name]
        character.save()
        return
    
    # Handle other races
    if race_name in racial_resistances:
        traits = racial_resistances[race_name]
        
        # Only set if not already populated (don't override user changes)
        if 'resistances' in traits and not character.damage_resistances:
            character.damage_resistances = traits['resistances']
        
        if 'immunities' in traits and not character.damage_immunities:
            character.damage_immunities = traits['immunities']
        
        if 'vulnerabilities' in traits and not character.damage_vulnerabilities:
            character.damage_vulnerabilities = traits['vulnerabilities']
        
        character.save()


def home(request):
    """Home page"""
    return render(request, 'characters/home.html')


class CharacterListView(ListView):
    """List all characters"""
    model = Character
    template_name = 'characters/character_list.html'
    context_object_name = 'characters'
    paginate_by = 10


class CharacterDetailView(DetailView):
    """View a single character"""
    model = Character
    template_name = 'characters/character_detail.html'
    context_object_name = 'character'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        character = self.object
        
        # Add ability scores data for the new layout
        ability_data = [
            ('Strength', character.total_strength, character.strength_modifier),
            ('Dexterity', character.total_dexterity, character.dexterity_modifier),
            ('Constitution', character.total_constitution, character.constitution_modifier),
            ('Intelligence', character.total_intelligence, character.intelligence_modifier),
            ('Wisdom', character.total_wisdom, character.wisdom_modifier),
            ('Charisma', character.total_charisma, character.charisma_modifier),
        ]
        context['ability_data'] = ability_data
        
        # Calculate skill bonuses
        skills = {
            'Acrobatics': (character.acrobatics, character.acrobatics_expertise, character.dexterity_modifier, 'DEX'),
            'Animal Handling': (character.animal_handling, character.animal_handling_expertise, character.wisdom_modifier, 'WIS'),
            'Arcana': (character.arcana, character.arcana_expertise, character.intelligence_modifier, 'INT'),
            'Athletics': (character.athletics, character.athletics_expertise, character.strength_modifier, 'STR'),
            'Deception': (character.deception, character.deception_expertise, character.charisma_modifier, 'CHA'),
            'History': (character.history, character.history_expertise, character.intelligence_modifier, 'INT'),
            'Insight': (character.insight, character.insight_expertise, character.wisdom_modifier, 'WIS'),
            'Intimidation': (character.intimidation, character.intimidation_expertise, character.charisma_modifier, 'CHA'),
            'Investigation': (character.investigation, character.investigation_expertise, character.intelligence_modifier, 'INT'),
            'Medicine': (character.medicine, character.medicine_expertise, character.wisdom_modifier, 'WIS'),
            'Nature': (character.nature, character.nature_expertise, character.intelligence_modifier, 'INT'),
            'Perception': (character.perception, character.perception_expertise, character.wisdom_modifier, 'WIS'),
            'Performance': (character.performance, character.performance_expertise, character.charisma_modifier, 'CHA'),
            'Persuasion': (character.persuasion, character.persuasion_expertise, character.charisma_modifier, 'CHA'),
            'Religion': (character.religion, character.religion_expertise, character.intelligence_modifier, 'INT'),
            'Sleight of Hand': (character.sleight_of_hand, character.sleight_of_hand_expertise, character.dexterity_modifier, 'DEX'),
            'Stealth': (character.stealth, character.stealth_expertise, character.dexterity_modifier, 'DEX'),
            'Survival': (character.survival, character.survival_expertise, character.wisdom_modifier, 'WIS'),
        }
        
        skill_bonuses = {}
        for skill_name, (is_proficient, has_expertise, ability_mod, ability) in skills.items():
            # Calculate bonus: base ability mod + proficiency (doubled if expertise)
            if has_expertise:
                bonus = ability_mod + (character.proficiency_bonus * 2)
            elif is_proficient:
                bonus = ability_mod + character.proficiency_bonus
            else:
                bonus = ability_mod
            
            skill_bonuses[skill_name] = {
                'bonus': bonus,
                'proficient': is_proficient,
                'expertise': has_expertise,
                'ability': ability
            }
        
        context['skill_bonuses'] = skill_bonuses
        
        # Add computed damage types and conditions
        context['computed_damage_immunities'] = character.get_computed_damage_immunities()
        context['computed_damage_resistances'] = character.get_computed_damage_resistances()
        context['computed_damage_vulnerabilities'] = character.get_computed_damage_vulnerabilities()
        context['computed_condition_immunities'] = character.get_computed_condition_immunities()
        
        # Add spell slot data for spellcasters
        if character.is_spellcaster:
            spell_slots = []
            for level in range(1, 10):
                max_slots = getattr(character, f'spell_slots_{level}_max', 0)
                used_slots = getattr(character, f'spell_slots_{level}_used', 0)
                if max_slots > 0:
                    spell_slots.append({
                        'level': level,
                        'max': max_slots,
                        'used': used_slots,
                        'available': max_slots - used_slots
                    })
            context['spell_slots'] = spell_slots
        
        return context


def character_create_step1(request):
    """Step 1: Basic character info and ability scores"""
    from .subraces import get_subraces_for_race, has_subraces
    import json
    
    if request.method == 'POST':
        form = CharacterCreationForm(request.POST)
        if form.is_valid():
            character = form.save(commit=False)
            
            # Handle subrace if selected
            subrace = request.POST.get('subrace')
            if subrace:
                character.subrace = subrace
            
            # Calculate initial HP: class hit die + constitution modifier
            character.max_hit_points = character.character_class.hit_die + character.constitution_modifier
            character.current_hit_points = character.max_hit_points
            character.save()
            
            # Auto-populate racial traits like damage resistances
            auto_populate_racial_traits(character)
            
            messages.success(request, 'Character basics created! Now select skills.')
            return redirect('character_create_step2', pk=character.pk)
    else:
        form = CharacterCreationForm()
    
    # Prepare subrace data for JavaScript
    subrace_data = {}
    for race in Race.objects.all():
        if has_subraces(race.name):
            subrace_data[race.name] = get_subraces_for_race(race.name)
    
    context = {
        'form': form,
        'step': 1,
        'races': Race.objects.all(),
        'classes': CharacterClass.objects.all(),
        'backgrounds': Background.objects.all(),
        'subrace_data': json.dumps(subrace_data),
    }
    return render(request, 'characters/character_create_step1.html', context)


def character_create_step2(request, pk):
    """Step 2: Select skills and level 1 class features"""
    from .class_features import has_feature_choice_at_level, get_class_features_for_level
    from .models import CharacterClassFeature
    from .forms import CharacterExpertiseForm
    import json
    
    character = get_object_or_404(Character, pk=pk)
    
    # Check if this class has level 1 feature choices (Cleric, Sorcerer, Warlock)
    has_level1_feature = has_feature_choice_at_level(character.character_class.name, 1)
    feature_data = get_class_features_for_level(character.character_class.name, 1) if has_level1_feature else None
    feature_data_json = json.dumps(feature_data) if feature_data else None
    
    # Check if Rogue (gets expertise at level 1)
    is_rogue = character.character_class.name.lower() == 'rogue'
    
    if request.method == 'POST':
        form = CharacterSkillsForm(request.POST, instance=character)
        expertise_form = None
        if is_rogue:
            # Don't check proficiency during character creation - skills aren't saved yet
            expertise_form = CharacterExpertiseForm(request.POST, instance=character, character=character, max_choices=2, check_proficiency=False)
        
        forms_valid = form.is_valid()
        if expertise_form:
            forms_valid = forms_valid and expertise_form.is_valid()
        
        if forms_valid:
            # Save skills first
            character = form.save()
            
            # Validate expertise against newly saved proficiencies
            if expertise_form:
                # Check that all selected expertise skills are actually proficient
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
                
                invalid_expertise = []
                for field_name, is_proficient in skill_mapping.items():
                    if expertise_form.cleaned_data.get(field_name) and not is_proficient:
                        skill_display = field_name.replace('_expertise', '').replace('_', ' ').title()
                        invalid_expertise.append(skill_display)
                
                if invalid_expertise:
                    messages.error(request, f'You cannot select expertise for non-proficient skills: {", ".join(invalid_expertise)}')
                    context = {
                        'form': form,
                        'expertise_form': expertise_form,
                        'is_rogue': is_rogue,
                        'character': character,
                        'step': 2,
                        'has_level1_feature': has_level1_feature,
                        'feature_data': feature_data,
                        'feature_data_json': feature_data_json,
                    }
                    return render(request, 'characters/character_create_step2.html', context)
                
                expertise_form.save()
            
            # Process level 1 class feature choices if applicable
            if has_level1_feature and feature_data:
                num_choices = feature_data['num_choices']
                feature_type = feature_data['name']
                
                # Get selected features from form
                selected_features = []
                sub_choices = {}  # Store sub-choices keyed by feature index
                validation_errors = []
                
                for i in range(num_choices):
                    feature_choice = request.POST.get(f'feature_choice_{i}')
                    sub_choice = request.POST.get(f'sub_choice_{i}')  # Get sub-choice if exists
                    
                    if feature_choice is not None:
                        try:
                            option_index = int(feature_choice)
                            if 0 <= option_index < len(feature_data['options']):
                                selected_option = feature_data['options'][option_index]
                                
                                # Validate sub-choice if required
                                if selected_option.get('has_sub_choice', False):
                                    if not sub_choice or sub_choice == '':
                                        sub_choice_name = selected_option.get('sub_choice', {}).get('name', 'sub-choice')
                                        validation_errors.append(f'Please select a {sub_choice_name} for {selected_option["name"]}.')
                                        continue
                                
                                selected_features.append(selected_option)
                                
                                # Store sub-choice if it exists and was selected
                                if sub_choice:
                                    sub_choices[len(selected_features) - 1] = sub_choice
                        except (ValueError, IndexError):
                            pass
                
                # Check for validation errors
                if validation_errors:
                    for error in validation_errors:
                        messages.error(request, error)
                    context = {
                        'form': form,
                        'expertise_form': expertise_form,
                        'is_rogue': is_rogue,
                        'character': character,
                        'step': 2,
                        'has_level1_feature': has_level1_feature,
                        'feature_data': feature_data,
                        'feature_data_json': feature_data_json,
                    }
                    return render(request, 'characters/character_create_step2.html', context)
                
                # Validate that required number of features were selected
                if len(selected_features) < num_choices:
                    messages.error(request, f'Please select {num_choices} {feature_type} option(s).')
                    context = {
                        'form': form,
                        'expertise_form': expertise_form,
                        'is_rogue': is_rogue,
                        'character': character,
                        'step': 2,
                        'has_level1_feature': has_level1_feature,
                        'feature_data': feature_data,
                        'feature_data_json': feature_data_json,
                    }
                    return render(request, 'characters/character_create_step2.html', context)
                
                # Save selected features
                for idx, feature_option in enumerate(selected_features):
                    sub_choice_value = sub_choices.get(idx, '')
                    
                    CharacterClassFeature.objects.create(
                        character=character,
                        feature_type=feature_type,
                        feature_name=feature_option['name'],
                        feature_description=feature_option['description'],
                        level_gained=1,
                        sub_choice=sub_choice_value
                    )
            
            messages.success(request, 'Skills and class features selected! Add final details.')
            return redirect('character_create_step3', pk=character.pk)
    else:
        form = CharacterSkillsForm(instance=character)
        expertise_form = None
        if is_rogue:
            # Don't check proficiency during character creation - skills aren't saved yet
            expertise_form = CharacterExpertiseForm(instance=character, character=character, max_choices=2, check_proficiency=False)
    
    context = {
        'form': form,
        'expertise_form': expertise_form,
        'is_rogue': is_rogue,
        'character': character,
        'step': 2,
        'has_level1_feature': has_level1_feature,
        'feature_data': feature_data,
        'feature_data_json': feature_data_json,
    }
    return render(request, 'characters/character_create_step2.html', context)


def character_create_step3(request, pk):
    """Step 3: Personality and equipment"""
    from .starting_equipment import get_equipment_packages_for_class, get_starting_gold_for_class, roll_starting_gold
    
    character = get_object_or_404(Character, pk=pk)
    
    if request.method == 'POST':
        # Process the regular form first
        form = CharacterDetailsForm(request.POST, instance=character)
        if form.is_valid():
            # Save the form but don't commit yet if we need to handle equipment
            character = form.save(commit=False)
            
            # Check if equipment method was selected and handle it
            equipment_method = request.POST.get('equipment_method')
            
            if equipment_method == 'package':
                # Handle starting equipment package selection
                package_index = request.POST.get('equipment_package')
                if package_index is not None:
                    packages = get_equipment_packages_for_class(character.character_class.name)
                    try:
                        selected_package = packages[int(package_index)]
                        # Add equipment as text notes
                        equipment_list = '\n'.join(['• ' + item for item in selected_package['equipment']])
                        character.equipment = f"{selected_package['name']}\n{equipment_list}"
                        
                        # Try to match equipment items to database and add them
                        for item_text in selected_package['equipment']:
                            # Try to find matching equipment in database
                            # Remove quantity indicators like "(2)" and extra descriptors
                            clean_name = item_text.split('(')[0].strip()
                            
                            # Try exact match first
                            equipment_item = Equipment.objects.filter(name__iexact=clean_name).first()
                            
                            # If not found, try to find by partial match (first word)
                            if not equipment_item and ' ' in clean_name:
                                first_word = clean_name.split()[0]
                                equipment_item = Equipment.objects.filter(name__icontains=first_word).first()
                            
                            # Add to character's equipment_items if found
                            if equipment_item:
                                character.equipment_items.add(equipment_item)
                        
                        messages.success(request, f'Starting equipment package applied: {selected_package["name"]}')
                    except (IndexError, ValueError):
                        messages.error(request, 'Invalid equipment package selected.')
            
            elif equipment_method == 'gold':
                # Handle rolling for starting gold
                gold_formula = get_starting_gold_for_class(character.character_class.name)
                rolled_gold = roll_starting_gold(gold_formula)
                character.gold_pieces = rolled_gold
                messages.success(request, f'Rolled {rolled_gold} gp starting gold! ({gold_formula})')
            
            # Now save the character with all changes
            character.save()
            
            # If character is a spellcaster, go to spell selection
            if character.is_spellcaster:
                messages.success(request, 'Details saved! Now select your spells.')
                return redirect('character_create_step4', pk=character.pk)
            else:
                messages.success(request, f'{character.name} has been created successfully!')
                return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterDetailsForm(instance=character)
        
        # Auto-populate languages based on race
        default_languages = []
        if character.race.name in ['Human', 'Half-Elf', 'Half-Orc']:
            default_languages.append('Common')
        elif character.race.name == 'Dwarf':
            default_languages.extend(['Common', 'Dwarvish'])
        elif character.race.name == 'Elf':
            default_languages.extend(['Common', 'Elvish'])
        elif character.race.name == 'Halfling':
            default_languages.extend(['Common', 'Halfling'])
        elif character.race.name == 'Dragonborn':
            default_languages.extend(['Common', 'Draconic'])
        elif character.race.name == 'Gnome':
            default_languages.extend(['Common', 'Gnomish'])
        elif character.race.name == 'Tiefling':
            default_languages.extend(['Common', 'Infernal'])
        
        if not character.languages and default_languages:
            form.initial['languages'] = ', '.join(default_languages)
        
        # Auto-populate tool proficiencies from background
        if not character.tool_proficiencies and character.background.tool_proficiencies:
            form.initial['tool_proficiencies'] = character.background.tool_proficiencies
    
    # Get equipment packages for this class
    equipment_packages = get_equipment_packages_for_class(character.character_class.name)
    gold_formula = get_starting_gold_for_class(character.character_class.name)
    
    context = {
        'form': form,
        'character': character,
        'step': 3,
        'equipment_items': Equipment.objects.all().order_by('category', 'name'),
        'equipment_packages': equipment_packages,
        'gold_formula': gold_formula,
    }
    return render(request, 'characters/character_create_step3.html', context)


def character_create_step4(request, pk):
    """Step 4: Spell selection (for spellcasters only)"""
    character = get_object_or_404(Character, pk=pk)
    
    if not character.is_spellcaster:
        messages.warning(request, f'{character.name} is not a spellcasting class.')
        return redirect('character_detail', pk=character.pk)
    
    if request.method == 'POST':
        from .models import Spell, CharacterSpell
        from .forms import SpellSlotsForm
        from .spell_slots import set_spell_slots
        
        # Auto-set spell slots based on class and level
        set_spell_slots(character)
        
        # Save spellcasting ability
        spell_slots_form = SpellSlotsForm(request.POST, instance=character)
        if spell_slots_form.is_valid():
            # Only save spellcasting ability and used slots
            character.spellcasting_ability = spell_slots_form.cleaned_data.get('spellcasting_ability')
            character.save()
        
        # Clear existing spells and add selected ones
        CharacterSpell.objects.filter(character=character).delete()
        
        added_count = 0
        for key, value in request.POST.items():
            if key.startswith('spells_level_') and value:
                spell_ids = request.POST.getlist(key)
                for spell_id in spell_ids:
                    try:
                        spell = Spell.objects.get(id=spell_id)
                        CharacterSpell.objects.create(
                            character=character,
                            spell=spell,
                            is_prepared=True
                        )
                        added_count += 1
                    except Spell.DoesNotExist:
                        pass
        
        messages.success(request, f'{character.name} created successfully with {added_count} spells!')
        return redirect('character_detail', pk=character.pk)
    
    from .forms import SpellManagementForm, SpellSlotsForm
    from .spell_slots import set_spell_slots
    
    # Auto-set spell slots based on class and level
    set_spell_slots(character)
    
    # Get recommended spellcasting ability based on class
    spellcasting_ability_recommendations = {
        'Wizard': 'INT',
        'Cleric': 'WIS',
        'Druid': 'WIS',
        'Ranger': 'WIS',
        'Bard': 'CHA',
        'Paladin': 'CHA',
        'Sorcerer': 'CHA',
        'Warlock': 'CHA',
    }
    
    # Set default spellcasting ability if not set
    if not character.spellcasting_ability:
        recommended = spellcasting_ability_recommendations.get(character.character_class.name)
        if recommended:
            character.spellcasting_ability = recommended
    
    # Save character with updated spell slots
    character.save()
    
    spell_form = SpellManagementForm(character=character)
    spell_slots_form = SpellSlotsForm(instance=character)
    
    context = {
        'character': character,
        'spell_form': spell_form,
        'spell_slots_form': spell_slots_form,
        'step': 4,
    }
    return render(request, 'characters/character_create_step4.html', context)


class CharacterUpdateView(UpdateView):
    """Edit a character - Basic Info"""
    model = Character
    form_class = CharacterCreationForm
    template_name = 'characters/character_edit.html'
    
    def form_valid(self, form):
        # Check if race has changed
        old_race = Character.objects.get(pk=self.object.pk).race
        new_race = form.cleaned_data.get('race')
        
        response = super().form_valid(form)
        
        # Auto-populate racial traits if race changed or fields are empty
        if old_race != new_race or not self.object.damage_resistances:
            auto_populate_racial_traits(self.object)
        
        return response
    
    def get_success_url(self):
        messages.success(self.request, 'Character updated successfully!')
        return reverse_lazy('character_detail', kwargs={'pk': self.object.pk})


def character_edit_skills(request, pk):
    """Edit character skills"""
    character = get_object_or_404(Character, pk=pk)
    
    if request.method == 'POST':
        form = CharacterSkillsForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            messages.success(request, f'{character.name} skills updated successfully!')
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterSkillsForm(instance=character)
    
    context = {
        'form': form,
        'character': character,
    }
    return render(request, 'characters/character_edit_skills.html', context)


def character_edit_details(request, pk):
    """Edit character details, personality, and equipment"""
    character = get_object_or_404(Character, pk=pk)
    
    if request.method == 'POST':
        form = CharacterDetailsForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            messages.success(request, f'{character.name} details updated successfully!')
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterDetailsForm(instance=character)
    
    context = {
        'form': form,
        'character': character,
        'equipment_items': Equipment.objects.all().order_by('category', 'name'),
    }
    return render(request, 'characters/character_edit_details.html', context)


def character_edit_combat(request, pk):
    """Edit character combat stats and tracking"""
    from django.http import JsonResponse
    
    character = get_object_or_404(Character, pk=pk)
    
    if request.method == 'POST':
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        # Handle inline death save checkboxes
        death_save_successes = 0
        death_save_failures = 0
        
        # Count checked death save success boxes
        for i in range(1, 4):
            if f'death_save_successes_{i}' in request.POST:
                death_save_successes = i
                
        # Count checked death save failure boxes
        for i in range(1, 4):
            if f'death_save_failures_{i}' in request.POST:
                death_save_failures = i
        
        # Update death saves if submitted
        if any(f'death_save_successes_{i}' in request.POST for i in range(1, 4)) or \
           any(f'death_save_failures_{i}' in request.POST for i in range(1, 4)):
            character.death_save_successes = death_save_successes
            character.death_save_failures = death_save_failures
            character.save()
            
            if is_ajax:
                return JsonResponse({'success': True, 'message': 'Death saves updated'})
            
            messages.success(request, f'{character.name} death saves updated!')
            return redirect('character_detail', pk=character.pk)
        
        # Handle individual field updates (for AJAX inline editing)
        if is_ajax:
            # Update only the fields that are present in the POST data
            updated_fields = []
            
            if 'current_hit_points' in request.POST:
                try:
                    value = int(request.POST.get('current_hit_points'))
                    if 0 <= value <= character.max_hit_points:
                        character.current_hit_points = value
                        updated_fields.append('current_hit_points')
                except (ValueError, TypeError):
                    return JsonResponse({'success': False, 'error': 'Invalid current HP value'}, status=400)
            
            if 'temporary_hit_points' in request.POST:
                try:
                    value = int(request.POST.get('temporary_hit_points'))
                    if value >= 0:
                        character.temporary_hit_points = value
                        updated_fields.append('temporary_hit_points')
                except (ValueError, TypeError):
                    return JsonResponse({'success': False, 'error': 'Invalid temp HP value'}, status=400)
            
            if 'exhaustion_level' in request.POST:
                try:
                    value = int(request.POST.get('exhaustion_level'))
                    if 0 <= value <= 6:
                        character.exhaustion_level = value
                        updated_fields.append('exhaustion_level')
                except (ValueError, TypeError):
                    return JsonResponse({'success': False, 'error': 'Invalid exhaustion level'}, status=400)
            
            if 'conditions' in request.POST:
                character.conditions = request.POST.get('conditions', '')
                updated_fields.append('conditions')
            
            if 'inspiration' in request.POST:
                character.inspiration = request.POST.get('inspiration') == 'on'
                updated_fields.append('inspiration')
            
            if updated_fields:
                character.save()
                return JsonResponse({
                    'success': True, 
                    'message': f'Updated {", ".join(updated_fields)}'
                })
            else:
                return JsonResponse({'success': False, 'error': 'No valid fields to update'}, status=400)
        
        # Handle regular form submission (full form from edit page)
        form = CharacterCombatForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            messages.success(request, f'{character.name} combat stats updated successfully!')
            return redirect('character_detail', pk=character.pk)
    else:
        form = CharacterCombatForm(instance=character)
    
    context = {
        'form': form,
        'character': character,
    }
    return render(request, 'characters/character_edit_combat.html', context)


def character_level_up(request, pk):
    """Level up a character"""
    import random
    from .class_features import has_feature_choice_at_level, get_class_features_for_level
    from .models import CharacterClassFeature
    from .forms import CharacterExpertiseForm
    
    character = get_object_or_404(Character, pk=pk)
    
    # Check if character can level up (max level 20)
    if character.level >= 20:
        messages.error(request, 'Character is already at maximum level (20)!')
        return redirect('character_detail', pk=character.pk)
    
    new_level = character.level + 1
    
    # Check if this level grants class features that require choices
    has_feature_choice = has_feature_choice_at_level(character.character_class.name, new_level)
    feature_data = get_class_features_for_level(character.character_class.name, new_level) if has_feature_choice else None
    
    # Determine if this is an ASI level
    asi_levels = [4, 8, 12, 16, 19]
    if character.character_class.name == 'Fighter':
        asi_levels.extend([6, 14])
    is_asi_level = new_level in asi_levels
    
    # Check if this level grants expertise
    # Bard: levels 3, 10 (2 skills each)
    # Rogue: levels 1, 6 (2 skills each - but level 1 handled in creation)
    class_name = character.character_class.name.lower()
    is_expertise_level = False
    expertise_count = 0
    
    if class_name == 'bard' and new_level in [3, 10]:
        is_expertise_level = True
        expertise_count = 2
    elif class_name == 'rogue' and new_level == 6:
        is_expertise_level = True
        expertise_count = 2
    
    if request.method == 'POST':
        form = LevelUpForm(request.POST, character=character)
        expertise_form = None
        if is_expertise_level:
            expertise_form = CharacterExpertiseForm(request.POST, instance=character, character=character, max_choices=expertise_count)
        
        forms_valid = form.is_valid()
        if expertise_form:
            forms_valid = forms_valid and expertise_form.is_valid()
        
        if forms_valid:
            # Save expertise if applicable
            if expertise_form:
                expertise_form.save()
            
            # Process HP increase
            hp_method = form.cleaned_data['hp_method']
            hit_die = character.character_class.hit_die
            con_modifier = character.constitution_modifier
            
            if hp_method == 'roll':
                hp_roll = form.cleaned_data.get('hp_roll')
                if not hp_roll:
                    # Roll if not provided (shouldn't happen with JS but just in case)
                    hp_roll = random.randint(1, hit_die)
                hp_increase = hp_roll + con_modifier
            else:  # average
                hp_increase = ((hit_die // 2) + 1) + con_modifier
            
            # Ensure minimum of 1 HP per level
            hp_increase = max(1, hp_increase)
            
            # Process ASI or Feat
            asi_record = ""
            if is_asi_level:
                asi_or_feat = form.cleaned_data.get('asi_or_feat')
                
                if asi_or_feat == 'asi':
                    # Apply ability score improvements
                    ability_1 = form.cleaned_data['asi_ability_1']
                    amount_1 = int(form.cleaned_data['asi_ability_1_amount'])
                    ability_2 = form.cleaned_data.get('asi_ability_2')
                    
                    # Increase abilities (note: these are base values, max 20)
                    current_val_1 = getattr(character, ability_1)
                    new_val_1 = min(20, current_val_1 + amount_1)
                    setattr(character, ability_1, new_val_1)
                    asi_record = f"Level {new_level}: +{amount_1} {ability_1.capitalize()}"
                    
                    if ability_2 and amount_1 == 1:
                        current_val_2 = getattr(character, ability_2)
                        new_val_2 = min(20, current_val_2 + 1)
                        setattr(character, ability_2, new_val_2)
                        asi_record += f", +1 {ability_2.capitalize()}"
                    
                    # Record the ASI
                    if character.ability_score_improvements:
                        character.ability_score_improvements += f"\n{asi_record}"
                    else:
                        character.ability_score_improvements = asi_record
                
                elif asi_or_feat == 'feat':
                    # Add the feat to the character
                    feat = form.cleaned_data['feat']
                    character.feats.add(feat)
                    asi_record = f"Level {new_level}: Took feat '{feat.name}'"
                    
                    # Record in ability_score_improvements for tracking
                    if character.ability_score_improvements:
                        character.ability_score_improvements += f"\n{asi_record}"
                    else:
                        character.ability_score_improvements = asi_record
            
            # Process class feature choices
            if has_feature_choice and feature_data:
                num_choices = feature_data['num_choices']
                feature_type = feature_data['name']
                
                # Get selected features from form
                selected_features = []
                for i in range(num_choices):
                    feature_choice = request.POST.get(f'feature_choice_{i}')
                    if feature_choice is not None:
                        try:
                            option_index = int(feature_choice)
                            if 0 <= option_index < len(feature_data['options']):
                                selected_features.append(feature_data['options'][option_index])
                        except (ValueError, IndexError):
                            pass
                
                # Save selected features
                for feature_option in selected_features:
                    CharacterClassFeature.objects.create(
                        character=character,
                        feature_type=feature_type,
                        feature_name=feature_option['name'],
                        feature_description=feature_option['description'],
                        level_gained=new_level
                    )
            
            # Update character
            character.level = new_level
            character.max_hit_points += hp_increase
            character.current_hit_points += hp_increase
            
            # If spellcaster, auto-update spell slots
            if character.is_spellcaster:
                from .spell_slots import set_spell_slots
                set_spell_slots(character)
            
            character.save()
            
            # If spellcaster, prompt to update spells
            if character.is_spellcaster:
                messages.success(
                    request,
                    f'Congratulations! {character.name} is now level {new_level}! '
                    f'HP increased by {hp_increase}. Spell slots have been updated automatically. Now update your spells.'
                )
                return redirect('character_manage_spells', pk=character.pk)
            else:
                messages.success(
                    request,
                    f'Congratulations! {character.name} is now level {new_level}! '
                    f'HP increased by {hp_increase} (new max: {character.max_hit_points})'
                )
                return redirect('character_detail', pk=character.pk)
    else:
        form = LevelUpForm(character=character)
        expertise_form = None
        if is_expertise_level:
            expertise_form = CharacterExpertiseForm(instance=character, character=character, max_choices=expertise_count)
    
    # Calculate what the character will gain
    hit_die = character.character_class.hit_die
    con_modifier = character.constitution_modifier
    average_hp = ((hit_die // 2) + 1) + con_modifier
    
    # Get all feats for the JavaScript
    import json
    feats_data = {}
    for feat in Feat.objects.all():
        feats_data[feat.id] = {
            'name': feat.name,
            'prerequisite': feat.prerequisite,
            'description': feat.description
        }
    
    # Calculate next ASI level
    next_asi_level = None
    if not is_asi_level:
        all_asi_levels = [4, 8, 12, 16, 19]
        if character.character_class.name == 'Fighter':
            all_asi_levels.extend([6, 14])
            all_asi_levels.sort()
        
        for level in all_asi_levels:
            if new_level < level:
                next_asi_level = level
                break
    
    context = {
        'character': character,
        'form': form,
        'expertise_form': expertise_form,
        'is_expertise_level': is_expertise_level,
        'expertise_count': expertise_count,
        'new_level': new_level,
        'is_asi_level': is_asi_level,
        'next_asi_level': next_asi_level,
        'hit_die': hit_die,
        'average_hp': max(1, average_hp),
        'con_modifier': con_modifier,
        'old_proficiency_bonus': character.proficiency_bonus,
        'new_proficiency_bonus': ((new_level - 1) // 4) + 2,
        'feats_json': json.dumps(feats_data),
        'has_feature_choice': has_feature_choice,
        'feature_data': feature_data,
    }
    return render(request, 'characters/character_level_up.html', context)


class CharacterDeleteView(DeleteView):
    """Delete a character"""
    model = Character
    template_name = 'characters/character_confirm_delete.html'
    success_url = reverse_lazy('character_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Character deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Reference views for races, classes, and backgrounds
class RaceListView(ListView):
    model = Race
    template_name = 'characters/race_list.html'
    context_object_name = 'races'


class ClassListView(ListView):
    model = CharacterClass
    template_name = 'characters/class_list.html'
    context_object_name = 'classes'


class BackgroundListView(ListView):
    model = Background
    template_name = 'characters/background_list.html'
    context_object_name = 'backgrounds'


def character_manage_spells(request, pk):
    """Manage spells for a character"""
    character = get_object_or_404(Character, pk=pk)
    
    if not character.is_spellcaster:
        messages.warning(request, f'{character.name} is not a spellcasting class.')
        return redirect('character_detail', pk=character.pk)
    
    if request.method == 'POST':
        from .models import Spell, CharacterSpell
        from .spell_slots import set_spell_slots
        
        # Auto-set spell slots based on current class and level
        set_spell_slots(character)
        character.save()
        
        # Clear existing spells
        CharacterSpell.objects.filter(character=character).delete()
        
        # Add selected spells
        added_count = 0
        for key, value in request.POST.items():
            if key.startswith('spells_level_') and value:
                # value is a list of spell IDs
                spell_ids = request.POST.getlist(key)
                for spell_id in spell_ids:
                    try:
                        spell = Spell.objects.get(id=spell_id)
                        CharacterSpell.objects.create(
                            character=character,
                            spell=spell,
                            is_prepared=True
                        )
                        added_count += 1
                    except Spell.DoesNotExist:
                        pass
        
        messages.success(request, f'Updated spells for {character.name}! Added {added_count} spells. Spell slots have been set automatically.')
        return redirect('character_detail', pk=character.pk)
    
    from .forms import SpellManagementForm
    from .spell_slots import set_spell_slots
    
    # Auto-set spell slots before displaying the form
    set_spell_slots(character)
    character.save()
    
    form = SpellManagementForm(character=character)
    
    # Pre-select existing spells
    existing_spell_ids = set(character.spells.values_list('spell_id', flat=True))
    for field_name, field in form.fields.items():
        if field_name.startswith('spells_level_'):
            # Set initial selected values
            field.initial = [choice[0] for choice in field.choices if choice[0] in existing_spell_ids]
    
    return render(request, 'characters/character_manage_spells.html', {
        'character': character,
        'form': form
    })


def character_spell_slots(request, pk):
    """Manage spell slots for a character - only used slots are editable, max is auto-set"""
    character = get_object_or_404(Character, pk=pk)
    
    if not character.is_spellcaster:
        messages.warning(request, f'{character.name} is not a spellcasting class.')
        return redirect('character_detail', pk=character.pk)
    
    if request.method == 'POST':
        from .forms import SpellSlotsForm
        from .spell_slots import set_spell_slots
        
        # Auto-set max spell slots based on class and level
        set_spell_slots(character)
        
        # Save the form (only used slots are editable)
        form = SpellSlotsForm(request.POST, instance=character)
        if form.is_valid():
            form.save()
            messages.success(request, f'Updated spell slots for {character.name}! Max slots have been set automatically based on level.')
            return redirect('character_detail', pk=character.pk)
    else:
        from .forms import SpellSlotsForm
        from .spell_slots import set_spell_slots
        
        # Auto-set max spell slots before displaying
        set_spell_slots(character)
        character.save()
        
        form = SpellSlotsForm(instance=character)
    
    # Prepare spell slot data for template
    spell_slots = []
    for level in range(1, 10):
        available, max_slots = character.get_spell_slots_available(level)
        used = max_slots - available if max_slots else 0
        spell_slots.append({
            'level': level,
            'max': max_slots,
            'used': used,
            'available': available
        })
    
    return render(request, 'characters/character_spell_slots.html', {
        'character': character,
        'form': form,
        'spell_slots': spell_slots
    })


def use_spell_slot(request, pk, level):
    """Use a spell slot"""
    if request.method == 'POST':
        character = get_object_or_404(Character, pk=pk)
        if character.use_spell_slot(level):
            messages.success(request, f'Used a level {level} spell slot!')
        else:
            messages.error(request, f'No level {level} spell slots available!')
        return redirect('character_detail', pk=character.pk)
    return redirect('character_list')


def long_rest(request, pk):
    """Perform a long rest"""
    from django.http import JsonResponse
    
    if request.method == 'POST':
        character = get_object_or_404(Character, pk=pk)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        # Restore HP to max
        character.current_hit_points = character.max_hit_points
        
        # Restore spell slots
        character.restore_spell_slots()
        
        # Reset death saves
        character.death_save_successes = 0
        character.death_save_failures = 0
        
        # Reduce exhaustion by 1
        if character.exhaustion_level > 0:
            character.exhaustion_level -= 1
        
        # Reset hit dice (restore all hit dice)
        character.hit_dice_used = 0
        
        character.save()
        
        if is_ajax:
            return JsonResponse({
                'success': True, 
                'message': 'Long rest completed! HP, spell slots, and hit dice restored.',
                'reload': True  # Signal to reload the page to show all updates
            })
        
        messages.success(request, f'{character.name} completed a long rest! HP, spell slots, and hit dice restored.')
        return redirect('character_detail', pk=character.pk)
    return redirect('character_list')


def short_rest(request, pk):
    """Perform a short rest"""
    from django.http import JsonResponse
    import random
    
    if request.method == 'POST':
        character = get_object_or_404(Character, pk=pk)
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        # Get number of hit dice to use from request
        hit_dice_to_use = request.POST.get('hit_dice_count')
        
        if hit_dice_to_use:
            try:
                hit_dice_count = int(hit_dice_to_use)
                
                # Validate hit dice count
                available_hit_dice = character.level - character.hit_dice_used
                if hit_dice_count < 0 or hit_dice_count > available_hit_dice:
                    if is_ajax:
                        return JsonResponse({
                            'success': False, 
                            'error': f'Invalid number of hit dice. You have {available_hit_dice} available.'
                        }, status=400)
                    messages.error(request, f'Invalid number of hit dice. You have {available_hit_dice} available.')
                    return redirect('character_detail', pk=character.pk)
                
                # Get hit die size from character class
                hit_die_size = character.character_class.hit_die if character.character_class else 10
                
                # Roll hit dice and add constitution modifier per die
                con_mod = (character.constitution - 10) // 2
                total_healing = 0
                rolls = []
                
                for i in range(hit_dice_count):
                    roll = random.randint(1, hit_die_size)
                    healing = max(1, roll + con_mod)  # Minimum 1 HP per hit die
                    total_healing += healing
                    rolls.append(f"d{hit_die_size}: {roll} + {con_mod} = {healing}")
                
                # Apply healing
                old_hp = character.current_hit_points
                character.current_hit_points = min(character.max_hit_points, character.current_hit_points + total_healing)
                actual_healing = character.current_hit_points - old_hp
                
                # Use hit dice
                character.hit_dice_used += hit_dice_count
                character.save()
                
                if is_ajax:
                    return JsonResponse({
                        'success': True, 
                        'message': f'Short rest complete! Rolled {hit_dice_count} hit dice.<br>Rolls: {", ".join(rolls)}<br>Healed {actual_healing} HP (from {old_hp} to {character.current_hit_points})',
                        'reload': True
                    })
                
                messages.success(request, f'Short rest complete! Used {hit_dice_count} hit dice and healed {actual_healing} HP.')
                return redirect('character_detail', pk=character.pk)
                
            except (ValueError, TypeError):
                if is_ajax:
                    return JsonResponse({'success': False, 'error': 'Invalid hit dice count'}, status=400)
                messages.error(request, 'Invalid hit dice count')
                return redirect('character_detail', pk=character.pk)
        
        # If no hit dice count provided, return available info for prompt
        if is_ajax:
            available_hit_dice = character.level - character.hit_dice_used
            hit_die_size = character.character_class.hit_die if character.character_class else 10
            con_mod = (character.constitution - 10) // 2
            
            return JsonResponse({
                'prompt_for_dice': True,
                'available_hit_dice': available_hit_dice,
                'hit_die_size': hit_die_size,
                'con_modifier': con_mod,
                'message': f'You have {available_hit_dice} hit dice (d{hit_die_size}) available. Each die heals 1d{hit_die_size} + {con_mod} HP.'
            })
        
        messages.info(request, f'{character.name} took a short rest. Use hit dice to recover HP.')
        return redirect('character_detail', pk=character.pk)
    return redirect('character_list')


def spell_detail_ajax(request, spell_id):
    """Get spell details for modal display"""
    from django.http import JsonResponse
    from .models import Spell
    
    try:
        spell = Spell.objects.get(id=spell_id)
        
        # Get the character for spell save DC
        character_pk = request.GET.get('character_pk')
        spell_save_dc = None
        if character_pk:
            try:
                character = Character.objects.get(pk=character_pk)
                spell_save_dc = character.spell_save_dc
            except Character.DoesNotExist:
                pass
        
        data = {
            'name': spell.name,
            'level': spell.level,
            'school': spell.school,
            'casting_time': spell.casting_time,
            'range': spell.range,
            'components': spell.components,
            'duration': spell.duration,
            'description': spell.description,
            'damage': spell.get_damage_info(),
            'save': spell.get_save_dc(),
            'spell_save_dc': spell_save_dc,
        }
        
        return JsonResponse(data)
    except Spell.DoesNotExist:
        return JsonResponse({'error': 'Spell not found'}, status=404)


def equipment_detail_ajax(request, equipment_id):
    """Get equipment details for modal display"""
    from django.http import JsonResponse
    from .models import Equipment
    
    try:
        equipment = Equipment.objects.get(id=equipment_id)
        
        data = {
            'name': equipment.name,
            'category': equipment.category,
            'description': equipment.description,
            'cost_gold': str(equipment.cost_gold),
            'weight': str(equipment.weight),
            'damage': equipment.get_damage_info(),
            'properties': equipment.get_properties(),
            'armor_class': equipment.get_armor_class(),
        }
        
        return JsonResponse(data)
    except Equipment.DoesNotExist:
        return JsonResponse({'error': 'Equipment not found'}, status=404)
