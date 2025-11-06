# Icon Replacement Guide - Flaticon Integration

## Overview
This guide explains how to replace all emoji icons in the D&D Character Builder with black and white icons from Flaticon.

## Icons Directory Structure
```
characters/static/characters/images/
├── dice/           # Dice icons (d4, d6, d8, d10, d12, d20)
├── actions/        # Action icons (create, edit, delete, level-up)
└── ui/             # UI icons (info, lightbulb, sparkles)
```

## Required Icons

### 1. Dice Icons (Priority: HIGH - Already Integrated)
Location: `characters/static/characters/images/dice/`

- **d4.png** - Four-sided die (tetrahedron/pyramid) - Currently using: 🔺
- **d6.png** - Six-sided die (standard cube) - Currently using: 🎲
- **d8.png** - Eight-sided die (octahedron) - Currently using: 🔷
- **d10.png** - Ten-sided die - Currently using: 🔟
- **d12.png** - Twelve-sided die (dodecahedron) - Currently using: 🔶
- **d20.png** - Twenty-sided die (icosahedron) - Currently using: 🌟

Search terms: "polyhedral dice", "d4 dice", "d6 dice", "rpg dice", "tabletop dice"

### 2. Action Icons
Location: `characters/static/characters/images/actions/`

- **level-up.png** - Arrow up icon - Currently using: ⬆️
- **create.png** - Plus/add icon - Currently using: ➕
- **delete.png** - Trash/bin icon - Currently using: 🗑️
- **complete.png** - Star/sparkles icon - Currently using: ✨

Search terms: "arrow up", "plus icon", "trash icon", "delete icon", "star icon"

### 3. UI Icons
Location: `characters/static/characters/images/ui/`

- **info.png** - Information icon - Currently using: ℹ️
- **tip.png** - Light bulb icon - Currently using: 💡

Search terms: "info icon", "information circle", "light bulb", "idea icon"

## Icon Specifications

### Required Format:
- **File Type**: PNG with transparent background
- **Color**: Black silhouette (will be inverted to white for dark buttons using CSS filter)
- **Size**: Minimum 128x128px, preferably 256x256px or higher
- **Style**: Simple, clean, flat design

### CSS Styling Applied:
```css
/* For button icons (inverted to white) */
filter: invert(1);
width: 24px;
height: 24px;

/* For large display icons */
width: 64-80px;
height: 64-80px;
```

## Download Instructions

1. **Visit Flaticon**: https://www.flaticon.com
2. **Search** for each icon using the search terms above
3. **Filter** by:
   - Style: Outline or Glyph
   - Color: Black/Monochrome
   - Format: PNG
4. **Download** each icon
5. **Rename** according to the filenames above
6. **Place** in the appropriate directory

## Alternative Icon Sources

If Flaticon doesn't have suitable icons:
- **Iconfinder**: https://www.iconfinder.com
- **Noun Project**: https://thenounproject.com
- **Iconmonstr**: https://iconmonstr.com
- **Heroicons**: https://heroicons.com (free, MIT license)
- **Bootstrap Icons**: https://icons.getbootstrap.com (free, MIT license)

## Templates to Update (After Downloading Icons)

### Already Updated:
- ✅ `character_level_up.html` - Dice rolling animation

### Need Manual Update:
The following files still use emoji icons and need to be updated with `<img>` tags:

1. **character_list.html**:
   - Line 9: ➕ Create New Character
   - Line 48: ⬆️ Level Up
   - Line 54: 🗑️ Delete

2. **character_detail.html**:
   - Line 11: ⬆️ Level Up
   - Line 22: 🗑️ Delete

3. **character_level_up.html**:
   - Line 36: ⬆️ Level Up (heading)
   - Line 186: ℹ️ Next Feat/ASI Opportunity
   - Line 200: ✨ Complete Level Up
   - Line 208: 💡 Level Up Tips

4. **character_create_step1.html**:
   - Line 167: 💡 Need Help Choosing?

5. **home.html**:
   - Line 84: ℹ️ Features

## Example Replacement Code

### Before (Emoji):
```html
<button class="btn btn-success">⬆️ Level Up</button>
```

### After (Icon):
```django
{% load static %}
<button class="btn btn-success">
    <img src="{% static 'characters/images/actions/level-up.png' %}" 
         style="width: 20px; height: 20px; margin-right: 5px; filter: invert(1);" 
         alt="Level Up">
    Level Up
</button>
```

## License and Attribution

**Important**: Always check the license for each icon:
- Some Flaticon icons require attribution
- Include attribution in your footer or about page
- Keep a record of icon authors and licenses

## Testing After Implementation

1. Clear Django's staticfiles cache: `python manage.py collectstatic --clear --noinput`
2. Hard refresh browser (Ctrl+F5 or Cmd+Shift+R)
3. Check all pages where icons appear
4. Verify icons display correctly on different screen sizes
5. Test dark mode if applicable

## Current Status

✅ **Completed**: Dice rolling animation icons (character_level_up.html)
⏳ **Pending**: Download actual icon files from Flaticon
⏳ **Pending**: Update remaining templates with icon paths

## Next Steps

1. Download all required icons from Flaticon
2. Place icons in the appropriate folders
3. Update the remaining templates with icon references
4. Test thoroughly
5. Add attribution if required by license
