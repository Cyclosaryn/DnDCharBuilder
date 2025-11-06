# Expertise System Validation

This document describes the validation implemented for the D&D 5e expertise system.

## Client-Side Validation (JavaScript)

### Character Creation (character_create_step2.html)

1. **Skill Proficiency Limit**
   - Tracks number of selected skill proficiencies
   - Shows counter: "Skills Selected: X of Y"
   - When limit reached: Shows warning and disables unchecked boxes
   - Maximum determined by `character.character_class.num_skills`

2. **Expertise Selection Limit (Rogues only)**
   - Tracks number of selected expertise skills
   - Shows counter: "Expertise Selected: X of 2"
   - When limit reached (2 for Rogues): Shows warning and disables unchecked boxes
   - All checkboxes enabled during creation (proficiency not yet checked)

### Level-Up (character_level_up.html)

1. **Expertise Selection Limit**
   - Tracks number of selected expertise skills
   - Shows counter: "Expertise Selected: X of Y" (Y = 2 for both Bards and Rogues)
   - When limit reached: Shows warning and disables unchecked boxes
   - Respects permanently disabled checkboxes (non-proficient skills)
   - Only temporarily disables available checkboxes when limit reached

## Server-Side Validation (Django Forms & Views)

### CharacterSkillsForm

```python
def clean(self):
    # Validates that no more skills are selected than allowed by the class
    # Raises ValidationError if exceeded
```

### CharacterExpertiseForm

```python
def __init__(self, check_proficiency=True):
    # check_proficiency=False during character creation
    # check_proficiency=True during level-up (default)
    # Disables non-proficient skills when check_proficiency=True

def clean(self):
    # Validates that no more than max_choices expertise selections are made
    # Raises ValidationError if exceeded
```

### character_create_step2 View

**Additional Validation After Form Save:**
- After saving skill proficiencies, validates that expertise is only granted for proficient skills
- Prevents exploit where user selects expertise for skills they didn't choose proficiency in
- Shows error message and returns to form if invalid expertise detected

### character_level_up View

**Automatic Proficiency Checking:**
- Uses `check_proficiency=True` (default) so form automatically disables non-proficient skills
- Form validation ensures max_choices limit

## Validation Flow

### Character Creation (Rogue Level 1)

1. User selects skill proficiencies (JS enforces class limit)
2. User selects expertise (JS enforces 2 max, all enabled)
3. **Server validates:**
   - Skill count ≤ class.num_skills
   - Expertise count ≤ 2
   - All expertise skills are in proficient skills list
4. If valid: Save both, proceed to step 3
5. If invalid: Show error, return to form with data

### Level-Up (Bard 3/10, Rogue 6)

1. User completes HP/ASI/Features sections
2. User selects expertise (JS enforces limit, respects proficiency)
3. **Server validates:**
   - Expertise count ≤ max (2 for both)
   - Form automatically filtered to proficient skills only
4. If valid: Save and level up
5. If invalid: Show error, return to form

## Edge Cases Handled

1. **Character Creation - Non-proficient Expertise:**
   - Client: All checkboxes enabled (skills not saved yet)
   - Server: Validates expertise against saved proficiencies
   - Protection: Prevents selecting expertise for skills user didn't make proficient

2. **Level-Up - Disabled Checkboxes:**
   - Form marks non-proficient checkboxes as permanently disabled
   - JS distinguishes permanent vs temporary disabling
   - Only temporarily disables checkboxes when limit reached
   - Doesn't re-enable permanently disabled checkboxes

3. **Form Resubmission:**
   - All validations run again on POST
   - Can't bypass by manipulating form data
   - Server-side checks are final authority

4. **Already Has Expertise:**
   - Level-up form shows current expertise state
   - Can't select same skill for expertise twice
   - Validation counts only newly selected expertise

## Error Messages

- **Too many skills:** "You can only select X skill(s) for your class, but you selected Y."
- **Too many expertise:** "You can only select X skill(s) for expertise, but you selected Y."
- **Non-proficient expertise:** "You cannot select expertise for non-proficient skills: [list]"
