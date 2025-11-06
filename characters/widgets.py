"""
Custom form widgets to add tooltips to select options
"""
from django import forms
from .models import Race, CharacterClass, Background


class RaceSelectWidget(forms.Select):
    """Select widget with race descriptions in title attributes"""
    
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            try:
                # Handle ModelChoiceIteratorValue objects
                pk = value.value if hasattr(value, 'value') else value
                if pk:
                    race = Race.objects.get(pk=pk)
                    # Truncate description for tooltip
                    desc = race.description[:100] + '...' if len(race.description) > 100 else race.description
                    option['attrs']['title'] = f"{race.name}: {desc}"
                    option['attrs']['data-description'] = race.description
                    option['attrs']['data-bonuses'] = self._get_race_bonuses(race)
            except (Race.DoesNotExist, ValueError, TypeError):
                pass
        return option
    
    def _get_race_bonuses(self, race):
        bonuses = []
        if race.strength_bonus > 0:
            bonuses.append(f"+{race.strength_bonus} STR")
        if race.dexterity_bonus > 0:
            bonuses.append(f"+{race.dexterity_bonus} DEX")
        if race.constitution_bonus > 0:
            bonuses.append(f"+{race.constitution_bonus} CON")
        if race.intelligence_bonus > 0:
            bonuses.append(f"+{race.intelligence_bonus} INT")
        if race.wisdom_bonus > 0:
            bonuses.append(f"+{race.wisdom_bonus} WIS")
        if race.charisma_bonus > 0:
            bonuses.append(f"+{race.charisma_bonus} CHA")
        return ", ".join(bonuses)


class ClassSelectWidget(forms.Select):
    """Select widget with class descriptions in title attributes"""
    
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            try:
                # Handle ModelChoiceIteratorValue objects
                pk = value.value if hasattr(value, 'value') else value
                if pk:
                    char_class = CharacterClass.objects.get(pk=pk)
                    desc = char_class.description[:100] + '...' if len(char_class.description) > 100 else char_class.description
                    option['attrs']['title'] = f"{char_class.name}: {desc}"
                    option['attrs']['data-description'] = char_class.description
                    option['attrs']['data-hit-die'] = f"d{char_class.hit_die}"
            except (CharacterClass.DoesNotExist, ValueError, TypeError):
                pass
        return option


class BackgroundSelectWidget(forms.Select):
    """Select widget with background descriptions in title attributes"""
    
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            try:
                # Handle ModelChoiceIteratorValue objects
                pk = value.value if hasattr(value, 'value') else value
                if pk:
                    background = Background.objects.get(pk=pk)
                    desc = background.description[:100] + '...' if len(background.description) > 100 else background.description
                    option['attrs']['title'] = f"{background.name}: {desc}"
                    option['attrs']['data-description'] = background.description
                    option['attrs']['data-feature'] = background.feature
            except (Background.DoesNotExist, ValueError, TypeError):
                pass
        return option
