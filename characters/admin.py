from django.contrib import admin
from .models import Race, CharacterClass, Background, Character, Spell, CharacterSpell, Equipment, Feat, CharacterClassFeature


@admin.register(Feat)
class FeatAdmin(admin.ModelAdmin):
    list_display = ['name', 'prerequisite']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'cost_gold', 'weight']
    list_filter = ['category']
    search_fields = ['name', 'description']
    ordering = ['category', 'name']


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'size', 'speed']
    search_fields = ['name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'size', 'speed', 'traits')
        }),
        ('Ability Score Bonuses', {
            'fields': ('strength_bonus', 'dexterity_bonus', 'constitution_bonus', 
                      'intelligence_bonus', 'wisdom_bonus', 'charisma_bonus')
        }),
    )


@admin.register(CharacterClass)
class CharacterClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'hit_die', 'num_skills']
    search_fields = ['name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'hit_die', 'primary_ability')
        }),
        ('Proficiencies', {
            'fields': ('saving_throw_proficiencies', 'armor_proficiencies', 
                      'weapon_proficiencies', 'tool_proficiencies')
        }),
        ('Skills', {
            'fields': ('skill_choices', 'num_skills')
        }),
    )


@admin.register(Background)
class BackgroundAdmin(admin.ModelAdmin):
    list_display = ['name', 'skill_proficiencies']
    search_fields = ['name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description')
        }),
        ('Proficiencies', {
            'fields': ('skill_proficiencies', 'tool_proficiencies', 'languages')
        }),
        ('Equipment & Features', {
            'fields': ('equipment', 'feature', 'feature_description')
        }),
    )


class CharacterSpellInline(admin.TabularInline):
    model = CharacterSpell
    extra = 1
    autocomplete_fields = ['spell']


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'race', 'character_class', 'level', 'player_name']
    list_filter = ['race', 'character_class', 'level']
    search_fields = ['name', 'player_name']
    inlines = [CharacterSpellInline]
    filter_horizontal = ['feats', 'equipment_items']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'player_name', 'race', 'character_class', 'background', 'level', 'alignment')
        }),
        ('Ability Scores', {
            'fields': ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')
        }),
        ('Hit Points & Leveling', {
            'fields': ('max_hit_points', 'current_hit_points', 'temporary_hit_points', 'hit_dice_used', 
                      'feats', 'ability_score_improvements')
        }),
        ('Combat & Survival', {
            'fields': ('inspiration', 'death_save_successes', 'death_save_failures', 'exhaustion_level', 'conditions')
        }),
        ('Damage Types', {
            'fields': ('damage_immunities', 'damage_resistances', 'damage_vulnerabilities', 'condition_immunities')
        }),
        ('Languages & Proficiencies', {
            'fields': ('languages', 'tool_proficiencies')
        }),
        ('Skill Proficiencies', {
            'fields': ('acrobatics', 'animal_handling', 'arcana', 'athletics', 'deception', 
                      'history', 'insight', 'intimidation', 'investigation', 'medicine', 
                      'nature', 'perception', 'performance', 'persuasion', 'religion', 
                      'sleight_of_hand', 'stealth', 'survival'),
            'classes': ['collapse']
        }),
        ('Personality', {
            'fields': ('personality_traits', 'ideals', 'bonds', 'flaws'),
            'classes': ['collapse']
        }),
        ('Features & Equipment', {
            'fields': ('features_and_traits', 'equipment', 'equipment_items'),
            'classes': ['collapse']
        }),
        ('Money', {
            'fields': ('copper_pieces', 'silver_pieces', 'electrum_pieces', 'gold_pieces', 'platinum_pieces'),
            'classes': ['collapse']
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'school', 'classes']
    list_filter = ['level', 'school']
    search_fields = ['name', 'description']
    ordering = ['level', 'name']


@admin.register(CharacterSpell)
class CharacterSpellAdmin(admin.ModelAdmin):
    list_display = ['character', 'spell', 'is_prepared']
    list_filter = ['is_prepared', 'spell__level']
    search_fields = ['character__name', 'spell__name']
    autocomplete_fields = ['character', 'spell']


@admin.register(CharacterClassFeature)
class CharacterClassFeatureAdmin(admin.ModelAdmin):
    list_display = ['character', 'feature_type', 'feature_name', 'level_gained']
    list_filter = ['feature_type', 'level_gained']
    search_fields = ['character__name', 'feature_name']
    ordering = ['character', 'level_gained', 'feature_type']
