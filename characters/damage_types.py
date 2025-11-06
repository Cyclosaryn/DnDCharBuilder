"""
D&D 5e Damage Types and Conditions Utility
Parses and aggregates damage immunities, resistances, vulnerabilities, and condition immunities
from race, subrace, class, and other sources
"""

from .subraces import get_subrace_data


def get_damage_resistance_from_subrace(race_name, subrace_name):
    """Extract damage resistance from subrace data"""
    if not subrace_name:
        return None
    
    subrace_data = get_subrace_data(race_name, subrace_name)
    if not subrace_data:
        return None
    
    # Parse traits for damage resistance
    traits = subrace_data.get('traits', [])
    for trait in traits:
        if 'Damage Resistance:' in trait:
            # Extract the damage type after "resistance to" or "resistance against"
            if 'resistance to' in trait.lower():
                damage_type = trait.lower().split('resistance to')[1].strip(' .').split()[0]
                return damage_type.capitalize()
            elif 'resistance against' in trait.lower():
                damage_type = trait.lower().split('resistance against')[1].strip(' .').split()[0]
                return damage_type.capitalize()
    
    return None


def get_damage_types_for_character(character):
    """
    Get all damage immunities, resistances, vulnerabilities, and condition immunities
    for a character based on their race, subrace, class, and other features.
    
    Returns a dictionary with keys:
    - damage_immunities: list of damage types
    - damage_resistances: list of damage types
    - damage_vulnerabilities: list of damage types
    - condition_immunities: list of conditions
    """
    immunities = []
    resistances = []
    vulnerabilities = []
    condition_immunities = []
    
    # Get from subrace (e.g., Dragonborn ancestry)
    if character.subrace:
        resistance = get_damage_resistance_from_subrace(character.race.name, character.subrace)
        if resistance:
            resistances.append(resistance)
    
    # Get from race traits
    race_resistances, race_immunities = get_damage_types_from_race(character.race)
    resistances.extend(race_resistances)
    immunities.extend(race_immunities)
    
    # Get from class features (future expansion)
    # class_types = get_damage_types_from_class(character.character_class, character.level)
    
    # Remove duplicates
    immunities = list(set(immunities))
    resistances = list(set(resistances))
    vulnerabilities = list(set(vulnerabilities))
    condition_immunities = list(set(condition_immunities))
    
    return {
        'damage_immunities': ', '.join(sorted(immunities)) if immunities else '—',
        'damage_resistances': ', '.join(sorted(resistances)) if resistances else '—',
        'damage_vulnerabilities': ', '.join(sorted(vulnerabilities)) if vulnerabilities else '—',
        'condition_immunities': ', '.join(sorted(condition_immunities)) if condition_immunities else '—',
    }


def get_damage_types_from_race(race):
    """Extract damage types from race traits"""
    resistances = []
    immunities = []
    
    if not race or not race.traits:
        return resistances, immunities
    
    traits_lower = race.traits.lower()
    
    # Common patterns for damage types
    damage_types = ['acid', 'cold', 'fire', 'lightning', 'poison', 'necrotic', 
                    'radiant', 'thunder', 'force', 'psychic', 'slashing', 
                    'piercing', 'bludgeoning']
    
    for damage_type in damage_types:
        if f'resistance to {damage_type}' in traits_lower or f'resistance against {damage_type}' in traits_lower:
            resistances.append(damage_type.capitalize())
        if f'immunity to {damage_type}' in traits_lower or f'immune to {damage_type}' in traits_lower:
            immunities.append(damage_type.capitalize())
    
    # Special case for Stout Halfling (has advantage vs poison, not full resistance)
    # This is handled separately as it's more complex
    
    return resistances, immunities


def format_resistance_display(subrace_name):
    """
    Format the resistance display text based on subrace.
    For Dragonborn, shows which draconic ancestry determines the resistance.
    """
    if not subrace_name:
        return "—"
    
    # Dragonborn subraces
    if "Dragon Ancestry" in subrace_name:
        dragon_type = subrace_name.replace(" Dragon Ancestry", "")
        return f"(Choose based on Draconic Ancestry: {dragon_type} Dragon)"
    
    return "—"
