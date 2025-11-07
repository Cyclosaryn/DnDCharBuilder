"""
Generate PDF character sheets in the style of the official D&D 5e 2014 character sheet.
Uses reportlab to create a detailed, formatted character sheet.
"""

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas


def draw_box(c, x, y, width, height, label="", value="", label_size=8, value_size=12, bold_value=False):
    """Helper to draw a labeled box with a value"""
    # Draw box
    c.rect(x, y, width, height)
    
    # Draw label at bottom
    c.setFont("Helvetica", label_size)
    c.drawString(x + 2, y + 2, label.upper())
    
    # Draw value centered
    if bold_value:
        c.setFont("Helvetica-Bold", value_size)
    else:
        c.setFont("Helvetica", value_size)
    text_width = c.stringWidth(str(value), "Helvetica-Bold" if bold_value else "Helvetica", value_size)
    c.drawString(x + (width - text_width) / 2, y + height / 2 - value_size / 3, str(value))


def draw_circle_box(c, x, y, radius, label="", value="", filled=False):
    """Draw a circular box (for ability scores)"""
    # Draw outer circle
    c.circle(x, y, radius, stroke=1, fill=0)
    
    # Draw inner circle for modifier
    if filled:
        c.circle(x, y, radius * 0.6, stroke=1, fill=1)
    else:
        c.circle(x, y, radius * 0.6, stroke=1, fill=0)
    
    # Draw value in center
    c.setFont("Helvetica-Bold", 14)
    text_width = c.stringWidth(str(value), "Helvetica-Bold", 14)
    c.drawString(x - text_width / 2, y - 5, str(value))
    
    # Draw label below
    c.setFont("Helvetica", 8)
    text_width = c.stringWidth(label.upper(), "Helvetica", 8)
    c.drawString(x - text_width / 2, y - radius - 12, label.upper())


def draw_checkbox(c, x, y, size=8, checked=False):
    """Draw a checkbox"""
    c.rect(x, y, size, size)
    if checked:
        c.line(x, y, x + size, y + size)
        c.line(x + size, y, x, y + size)


def generate_character_sheet_pdf(character):
    """
    Generate a PDF character sheet that mimics the official D&D 5e 2014 design.
    Returns a BytesIO buffer containing the PDF.
    """
    buffer = BytesIO()
    
    # Create canvas for custom drawing
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Set up fonts and styles
    c.setFont("Helvetica-Bold", 16)
    
    # PAGE 1 - Main Character Sheet
    
    # === HEADER SECTION ===
    y_pos = height - 0.5 * inch
    
    # Character Name (Large)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(0.5 * inch, y_pos, character.name.upper())
    y_pos -= 0.3 * inch
    
    # Class & Level, Background, Player Name, Race, Alignment, XP in boxes
    header_y = y_pos
    draw_box(c, 0.5 * inch, header_y - 0.3 * inch, 2.5 * inch, 0.3 * inch, 
             "Class & Level", f"{character.character_class.name} {character.level}", value_size=10)
    draw_box(c, 3.1 * inch, header_y - 0.3 * inch, 2 * inch, 0.3 * inch,
             "Background", character.background.name if character.background else "", value_size=10)
    draw_box(c, 5.2 * inch, header_y - 0.3 * inch, 2.8 * inch, 0.3 * inch,
             "Race", f"{character.subrace or ''} {character.race.name}".strip(), value_size=10)
    
    y_pos -= 0.5 * inch
    draw_box(c, 0.5 * inch, y_pos - 0.3 * inch, 2 * inch, 0.3 * inch,
             "Alignment", character.alignment or "", value_size=10)
    draw_box(c, 2.6 * inch, y_pos - 0.3 * inch, 2 * inch, 0.3 * inch,
             "Experience Points", "0", value_size=10)
    
    y_pos -= 0.8 * inch
    
    # === LEFT COLUMN - ABILITY SCORES ===
    ability_x = 0.5 * inch
    ability_y = y_pos
    ability_spacing = 0.85 * inch
    
    abilities = [
        ("Strength", character.total_strength, character.strength_modifier),
        ("Dexterity", character.total_dexterity, character.dexterity_modifier),
        ("Constitution", character.total_constitution, character.constitution_modifier),
        ("Intelligence", character.total_intelligence, character.intelligence_modifier),
        ("Wisdom", character.total_wisdom, character.wisdom_modifier),
        ("Charisma", character.total_charisma, character.charisma_modifier),
    ]
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(ability_x, ability_y + 0.2 * inch, "ABILITY SCORES")
    
    for i, (name, score, modifier) in enumerate(abilities):
        y = ability_y - i * ability_spacing
        
        # Draw ability score box
        draw_box(c, ability_x, y - 0.5 * inch, 0.9 * inch, 0.5 * inch,
                name, score, value_size=16, bold_value=True)
        
        # Draw modifier circle
        mod_str = f"{modifier:+d}"
        c.circle(ability_x + 0.45 * inch, y - 0.75 * inch, 0.25 * inch)
        c.setFont("Helvetica-Bold", 14)
        text_width = c.stringWidth(mod_str, "Helvetica-Bold", 14)
        c.drawString(ability_x + 0.45 * inch - text_width / 2, y - 0.8 * inch, mod_str)
    
    # === CENTER COLUMN - COMBAT STATS & SKILLS ===
    center_x = 2 * inch
    center_y = y_pos
    
    # Inspiration, Proficiency Bonus, Passive Perception
    combat_stats_y = center_y + 0.2 * inch
    
    draw_box(c, center_x, combat_stats_y - 0.4 * inch, 0.6 * inch, 0.4 * inch,
             "Inspiration", "✓" if character.inspiration else "", value_size=14, bold_value=True)
    draw_box(c, center_x + 0.7 * inch, combat_stats_y - 0.4 * inch, 0.6 * inch, 0.4 * inch,
             "Prof Bonus", f"+{character.proficiency_bonus}", value_size=14, bold_value=True)
    draw_box(c, center_x + 1.4 * inch, combat_stats_y - 0.4 * inch, 0.9 * inch, 0.4 * inch,
             "Passive Perception", 
             10 + character.wisdom_modifier + (character.proficiency_bonus if character.perception else 0),
             value_size=12, bold_value=True)
    
    # Saving Throws
    saves_y = combat_stats_y - 0.7 * inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(center_x, saves_y, "SAVING THROWS")
    
    # Determine which saves have proficiency based on class
    class_save_profs = []
    if hasattr(character, 'character_class') and hasattr(character.character_class, 'saving_throw_proficiencies'):
        class_save_text = character.character_class.saving_throw_proficiencies.lower()
        if 'str' in class_save_text:
            class_save_profs.append('strength')
        if 'dex' in class_save_text:
            class_save_profs.append('dexterity')
        if 'con' in class_save_text:
            class_save_profs.append('constitution')
        if 'int' in class_save_text:
            class_save_profs.append('intelligence')
        if 'wis' in class_save_text:
            class_save_profs.append('wisdom')
        if 'cha' in class_save_text:
            class_save_profs.append('charisma')
    
    saves = [
        ("Strength", character.strength_modifier + (character.proficiency_bonus if 'strength' in class_save_profs else 0), 'strength' in class_save_profs),
        ("Dexterity", character.dexterity_modifier + (character.proficiency_bonus if 'dexterity' in class_save_profs else 0), 'dexterity' in class_save_profs),
        ("Constitution", character.constitution_modifier + (character.proficiency_bonus if 'constitution' in class_save_profs else 0), 'constitution' in class_save_profs),
        ("Intelligence", character.intelligence_modifier + (character.proficiency_bonus if 'intelligence' in class_save_profs else 0), 'intelligence' in class_save_profs),
        ("Wisdom", character.wisdom_modifier + (character.proficiency_bonus if 'wisdom' in class_save_profs else 0), 'wisdom' in class_save_profs),
        ("Charisma", character.charisma_modifier + (character.proficiency_bonus if 'charisma' in class_save_profs else 0), 'charisma' in class_save_profs),
    ]
    
    c.setFont("Helvetica", 9)
    for i, (name, bonus, is_proficient) in enumerate(saves):
        y = saves_y - (i + 1) * 0.25 * inch
        # Checkbox for proficiency
        draw_checkbox(c, center_x, y - 0.08 * inch, 8, is_proficient)
        c.drawString(center_x + 0.15 * inch, y, f"{bonus:+d}  {name}")
    
    # Skills
    skills_y = saves_y - 1.9 * inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(center_x, skills_y, "SKILLS")
    
    skills_list = [
        ("Acrobatics", character.dexterity_modifier + (character.proficiency_bonus if character.acrobatics else 0), character.acrobatics, "Dex"),
        ("Animal Handling", character.wisdom_modifier + (character.proficiency_bonus if character.animal_handling else 0), character.animal_handling, "Wis"),
        ("Arcana", character.intelligence_modifier + (character.proficiency_bonus if character.arcana else 0), character.arcana, "Int"),
        ("Athletics", character.strength_modifier + (character.proficiency_bonus if character.athletics else 0), character.athletics, "Str"),
        ("Deception", character.charisma_modifier + (character.proficiency_bonus if character.deception else 0), character.deception, "Cha"),
        ("History", character.intelligence_modifier + (character.proficiency_bonus if character.history else 0), character.history, "Int"),
        ("Insight", character.wisdom_modifier + (character.proficiency_bonus if character.insight else 0), character.insight, "Wis"),
        ("Intimidation", character.charisma_modifier + (character.proficiency_bonus if character.intimidation else 0), character.intimidation, "Cha"),
        ("Investigation", character.intelligence_modifier + (character.proficiency_bonus if character.investigation else 0), character.investigation, "Int"),
        ("Medicine", character.wisdom_modifier + (character.proficiency_bonus if character.medicine else 0), character.medicine, "Wis"),
        ("Nature", character.intelligence_modifier + (character.proficiency_bonus if character.nature else 0), character.nature, "Int"),
        ("Perception", character.wisdom_modifier + (character.proficiency_bonus if character.perception else 0), character.perception, "Wis"),
        ("Performance", character.charisma_modifier + (character.proficiency_bonus if character.performance else 0), character.performance, "Cha"),
        ("Persuasion", character.charisma_modifier + (character.proficiency_bonus if character.persuasion else 0), character.persuasion, "Cha"),
        ("Religion", character.intelligence_modifier + (character.proficiency_bonus if character.religion else 0), character.religion, "Int"),
        ("Sleight of Hand", character.dexterity_modifier + (character.proficiency_bonus if character.sleight_of_hand else 0), character.sleight_of_hand, "Dex"),
        ("Stealth", character.dexterity_modifier + (character.proficiency_bonus if character.stealth else 0), character.stealth, "Dex"),
        ("Survival", character.wisdom_modifier + (character.proficiency_bonus if character.survival else 0), character.survival, "Wis"),
    ]
    
    c.setFont("Helvetica", 8)
    for i, (skill_name, bonus, is_proficient, ability) in enumerate(skills_list):
        y = skills_y - (i + 1) * 0.22 * inch
        draw_checkbox(c, center_x, y - 0.06 * inch, 8, is_proficient)
        c.drawString(center_x + 0.15 * inch, y, f"{bonus:+d}  {skill_name} ({ability})")
    
    # === RIGHT COLUMN - COMBAT INFO ===
    right_x = 5.5 * inch
    right_y = y_pos
    
    # AC, Initiative, Speed
    combat_y = right_y + 0.2 * inch
    draw_box(c, right_x, combat_y - 0.6 * inch, 0.7 * inch, 0.6 * inch,
             "Armor Class", character.armor_class, value_size=18, bold_value=True)
    draw_box(c, right_x + 0.8 * inch, combat_y - 0.6 * inch, 0.7 * inch, 0.6 * inch,
             "Initiative", f"{character.dexterity_modifier:+d}", value_size=18, bold_value=True)
    draw_box(c, right_x + 1.6 * inch, combat_y - 0.6 * inch, 0.7 * inch, 0.6 * inch,
             "Speed", f"{character.speed} ft", value_size=12, bold_value=True)
    
    # HP
    hp_y = combat_y - 1.0 * inch
    draw_box(c, right_x, hp_y - 0.5 * inch, 1.1 * inch, 0.5 * inch,
             "Hit Point Maximum", character.max_hit_points, value_size=16, bold_value=True)
    draw_box(c, right_x + 1.2 * inch, hp_y - 0.5 * inch, 1.1 * inch, 0.5 * inch,
             "Current Hit Points", character.current_hit_points, value_size=16, bold_value=True)
    
    # Temp HP
    temp_hp_y = hp_y - 0.7 * inch
    draw_box(c, right_x, temp_hp_y - 0.3 * inch, 2.3 * inch, 0.3 * inch,
             "Temporary Hit Points", character.temporary_hit_points or 0, value_size=12)
    
    # Hit Dice
    hd_y = temp_hp_y - 0.6 * inch
    hit_dice_total = character.level
    hit_dice_available = character.level - (character.hit_dice_used or 0)
    draw_box(c, right_x, hd_y - 0.4 * inch, 1.1 * inch, 0.4 * inch,
             "Hit Dice", f"{hit_dice_available}/{hit_dice_total}d{character.character_class.hit_die}", value_size=10)
    
    # Death Saves
    ds_y = hd_y - 0.5 * inch
    c.setFont("Helvetica-Bold", 9)
    c.drawString(right_x, ds_y, "DEATH SAVES")
    c.setFont("Helvetica", 8)
    c.drawString(right_x, ds_y - 0.15 * inch, "Successes")
    for i in range(3):
        draw_checkbox(c, right_x + 0.8 * inch + i * 0.15 * inch, ds_y - 0.18 * inch, 8, 
                     i < (character.death_save_successes or 0))
    c.drawString(right_x, ds_y - 0.3 * inch, "Failures")
    for i in range(3):
        draw_checkbox(c, right_x + 0.8 * inch + i * 0.15 * inch, ds_y - 0.33 * inch, 8,
                     i < (character.death_save_failures or 0))
    
    # Attacks & Spellcasting
    attacks_y = ds_y - 0.8 * inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_x, attacks_y, "ATTACKS & SPELLCASTING")
    
    # Draw attack table header
    c.setFont("Helvetica", 7)
    c.drawString(right_x, attacks_y - 0.15 * inch, "NAME")
    c.drawString(right_x + 1 * inch, attacks_y - 0.15 * inch, "ATK BONUS")
    c.drawString(right_x + 1.7 * inch, attacks_y - 0.15 * inch, "DAMAGE/TYPE")
    
    # List equipped weapons from equipment
    weapon_y = attacks_y - 0.3 * inch
    weapons_listed = 0
    if character.equipment_items.exists():
        for equipment in character.equipment_items.filter(category='Weapon')[:3]:
            damage_info = equipment.get_damage_info() or "See description"
            c.setFont("Helvetica", 7)
            c.drawString(right_x, weapon_y, equipment.name[:20])
            c.drawString(right_x + 1 * inch, weapon_y, f"+{character.strength_modifier + character.proficiency_bonus}")
            c.drawString(right_x + 1.7 * inch, weapon_y, damage_info[:15])
            weapon_y -= 0.15 * inch
            weapons_listed += 1
    
    # Add some blank lines
    for i in range(3 - weapons_listed):
        c.line(right_x, weapon_y, right_x + 2.3 * inch, weapon_y)
        weapon_y -= 0.15 * inch
    
    # Equipment & Money
    equipment_y = weapon_y - 0.3 * inch
    c.setFont("Helvetica-Bold", 10)
    c.drawString(right_x, equipment_y, "EQUIPMENT")
    
    # Money
    c.setFont("Helvetica", 8)
    money_y = equipment_y - 0.2 * inch
    currencies = [
        ("CP", character.copper_pieces or 0),
        ("SP", character.silver_pieces or 0),
        ("EP", character.electrum_pieces or 0),
        ("GP", character.gold_pieces or 0),
        ("PP", character.platinum_pieces or 0),
    ]
    for i, (curr, amount) in enumerate(currencies):
        draw_box(c, right_x + i * 0.45 * inch, money_y - 0.3 * inch, 0.4 * inch, 0.3 * inch,
                curr, amount, label_size=6, value_size=8)
    
    # Equipment list (abbreviated)
    eq_list_y = money_y - 0.6 * inch
    c.setFont("Helvetica", 7)
    if character.equipment:
        lines = character.equipment.split('\n')[:8]
        for i, line in enumerate(lines):
            c.drawString(right_x, eq_list_y - i * 0.12 * inch, line[:40])
    
    # === BOTTOM SECTION - PERSONALITY & FEATURES ===
    bottom_y = 3.5 * inch
    
    # Personality Traits
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.5 * inch, bottom_y, "PERSONALITY TRAITS")
    c.rect(0.5 * inch, bottom_y - 0.7 * inch, 2.5 * inch, 0.6 * inch)
    c.setFont("Helvetica", 7)
    if character.personality_traits:
        lines = character.personality_traits[:100].split('\n')[:3]
        for i, line in enumerate(lines):
            c.drawString(0.55 * inch, bottom_y - 0.2 * inch - i * 0.15 * inch, line[:50])
    
    # Ideals
    c.setFont("Helvetica-Bold", 9)
    c.drawString(3.1 * inch, bottom_y, "IDEALS")
    c.rect(3.1 * inch, bottom_y - 0.7 * inch, 2.4 * inch, 0.6 * inch)
    c.setFont("Helvetica", 7)
    if character.ideals:
        lines = character.ideals[:100].split('\n')[:3]
        for i, line in enumerate(lines):
            c.drawString(3.15 * inch, bottom_y - 0.2 * inch - i * 0.15 * inch, line[:50])
    
    # Bonds
    c.setFont("Helvetica-Bold", 9)
    c.drawString(5.6 * inch, bottom_y, "BONDS")
    c.rect(5.6 * inch, bottom_y - 0.7 * inch, 2.4 * inch, 0.6 * inch)
    c.setFont("Helvetica", 7)
    if character.bonds:
        lines = character.bonds[:100].split('\n')[:3]
        for i, line in enumerate(lines):
            c.drawString(5.65 * inch, bottom_y - 0.2 * inch - i * 0.15 * inch, line[:50])
    
    # Flaws
    flaws_y = bottom_y - 0.9 * inch
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.5 * inch, flaws_y, "FLAWS")
    c.rect(0.5 * inch, flaws_y - 0.7 * inch, 2.5 * inch, 0.6 * inch)
    c.setFont("Helvetica", 7)
    if character.flaws:
        lines = character.flaws[:100].split('\n')[:3]
        for i, line in enumerate(lines):
            c.drawString(0.55 * inch, flaws_y - 0.2 * inch - i * 0.15 * inch, line[:50])
    
    # Features & Traits
    c.setFont("Helvetica-Bold", 9)
    c.drawString(3.1 * inch, flaws_y, "FEATURES & TRAITS")
    c.rect(3.1 * inch, flaws_y - 2.2 * inch, 4.9 * inch, 2.1 * inch)
    c.setFont("Helvetica", 6)
    
    # List race features, class features, feats
    feature_y = flaws_y - 0.2 * inch
    feature_lines = []
    
    # Add background feature
    if character.background and character.background.feature:
        feature_lines.append(f"• {character.background.feature[:60]}")
    
    # Add racial traits
    if character.race.traits:
        traits = character.race.traits.split('\n')
        for trait in traits[:2]:
            feature_lines.append(f"• {trait[:60]}")
    
    # Add class features
    if hasattr(character, 'class_features'):
        for cf in character.class_features.all()[:5]:
            feature_lines.append(f"• {cf.feature_name}: {cf.feature_description[:50]}")
    
    # Add feats
    if character.feats.exists():
        for feat in character.feats.all()[:3]:
            feature_lines.append(f"• FEAT: {feat.name}")
    
    # Draw feature lines
    for i, line in enumerate(feature_lines[:12]):
        c.drawString(3.15 * inch, feature_y - i * 0.12 * inch, line[:85])
    
    # Proficiencies & Languages
    prof_y = flaws_y - 2.5 * inch
    c.setFont("Helvetica-Bold", 9)
    c.drawString(0.5 * inch, prof_y, "PROFICIENCIES & LANGUAGES")
    c.rect(0.5 * inch, prof_y - 0.9 * inch, 2.5 * inch, 0.8 * inch)
    c.setFont("Helvetica", 6)
    
    prof_text_y = prof_y - 0.15 * inch
    if character.languages:
        c.drawString(0.55 * inch, prof_text_y, f"Languages: {character.languages[:50]}")
        prof_text_y -= 0.12 * inch
    
    # Get armor and weapon proficiencies from class
    if hasattr(character, 'character_class'):
        if hasattr(character.character_class, 'armor_proficiencies') and character.character_class.armor_proficiencies:
            c.drawString(0.55 * inch, prof_text_y, f"Armor: {character.character_class.armor_proficiencies[:50]}")
            prof_text_y -= 0.12 * inch
        if hasattr(character.character_class, 'weapon_proficiencies') and character.character_class.weapon_proficiencies:
            c.drawString(0.55 * inch, prof_text_y, f"Weapons: {character.character_class.weapon_proficiencies[:50]}")
            prof_text_y -= 0.12 * inch
    
    if character.tool_proficiencies:
        c.drawString(0.55 * inch, prof_text_y, f"Tools: {character.tool_proficiencies[:50]}")
    
    # Page footer
    c.setFont("Helvetica", 6)
    c.drawString(0.5 * inch, 0.3 * inch, f"Character Sheet - {character.name} - Page 1")
    
    # === PAGE 2 - Spells & Additional Info ===
    c.showPage()
    
    # Second page header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(0.5 * inch, height - 0.5 * inch, f"{character.name.upper()} - SPELLS & DETAILS")
    
    page2_y = height - 1 * inch
    
    if character.is_spellcaster:
        # Spellcasting ability
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.5 * inch, page2_y, "SPELLCASTING")
        
        c.setFont("Helvetica", 9)
        spell_info_y = page2_y - 0.2 * inch
        c.drawString(0.5 * inch, spell_info_y, f"Spellcasting Ability: {character.get_spellcasting_ability_display()}")
        c.drawString(3 * inch, spell_info_y, f"Spell Save DC: {character.spell_save_dc}")
        c.drawString(5 * inch, spell_info_y, f"Spell Attack Bonus: +{character.spell_attack_bonus}")
        
        # Spell Slots
        slots_y = spell_info_y - 0.4 * inch
        c.setFont("Helvetica", 8)
        c.drawString(0.5 * inch, slots_y, "Spell Slots:")
        
        slot_x = 1.5 * inch
        for level in range(1, 10):
            max_slots = getattr(character, f'spell_slots_{level}_max', 0)
            used_slots = getattr(character, f'spell_slots_{level}_used', 0)
            if max_slots > 0:
                available = max_slots - used_slots
                c.drawString(slot_x, slots_y, f"Lvl {level}: {available}/{max_slots}")
                slot_x += 0.8 * inch
        
        # Cantrips
        cantrips_y = slots_y - 0.5 * inch
        c.setFont("Helvetica-Bold", 9)
        c.drawString(0.5 * inch, cantrips_y, "CANTRIPS")
        
        cantrips = character.spells.filter(spell__level=0).select_related('spell')
        c.setFont("Helvetica", 7)
        cantrip_y = cantrips_y - 0.15 * inch
        for spell_char in cantrips[:8]:
            c.drawString(0.5 * inch, cantrip_y, f"• {spell_char.spell.name}")
            cantrip_y -= 0.12 * inch
        
        # Spells by level
        spell_y = cantrip_y - 0.3 * inch
        
        for level in range(1, 10):
            spells = character.spells.filter(spell__level=level).select_related('spell')
            if spells.exists():
                c.setFont("Helvetica-Bold", 9)
                c.drawString(0.5 * inch, spell_y, f"LEVEL {level} SPELLS")
                spell_y -= 0.15 * inch
                
                c.setFont("Helvetica", 6)
                for spell_char in spells[:10]:
                    prep_marker = "○" if spell_char.is_prepared else "●"
                    c.drawString(0.5 * inch, spell_y, f"{prep_marker} {spell_char.spell.name}")
                    spell_y -= 0.10 * inch
                
                spell_y -= 0.1 * inch
                
                # Check if we need a new page
                if spell_y < 1 * inch:
                    c.showPage()
                    spell_y = height - 1 * inch
    else:
        c.setFont("Helvetica", 10)
        c.drawString(0.5 * inch, page2_y, "This character is not a spellcaster.")
    
    # Additional Notes section (on available space or new page if needed)
    if page2_y > 4 * inch or not character.is_spellcaster:
        notes_y = page2_y - 1 * inch if character.is_spellcaster else page2_y - 0.5 * inch
        c.setFont("Helvetica-Bold", 10)
        c.drawString(0.5 * inch, notes_y, "ADDITIONAL NOTES")
        c.rect(0.5 * inch, notes_y - 3 * inch, 7.5 * inch, 2.9 * inch)
        
        c.setFont("Helvetica", 7)
        # Use features_and_traits or other text field if backstory doesn't exist
        notes_text = ""
        if hasattr(character, 'backstory') and character.backstory:
            notes_text = character.backstory
        elif character.features_and_traits:
            notes_text = character.features_and_traits
        
        if notes_text:
            lines = notes_text[:500].split('\n')[:20]
            note_y = notes_y - 0.2 * inch
            for line in lines:
                c.drawString(0.55 * inch, note_y, line[:100])
                note_y -= 0.12 * inch
    
    # Page 2 footer
    c.setFont("Helvetica", 6)
    c.drawString(0.5 * inch, 0.3 * inch, f"Character Sheet - {character.name} - Page 2")
    
    # Finalize PDF
    c.save()
    
    buffer.seek(0)
    return buffer
