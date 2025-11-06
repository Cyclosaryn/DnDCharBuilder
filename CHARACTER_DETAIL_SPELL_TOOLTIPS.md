# Character Detail Page - Spell Hover Tooltips

## ✨ New Feature: Interactive Spell Tooltips on Character Sheet

### Overview
Added hover tooltips to spell names on the character detail page, matching the functionality from the spell selection pages.

### What Changed

#### 1. Updated `spells_section.html` Component
**Location:** `characters/templates/characters/components/spells_section.html`

**Changes:**
- Wrapped each spell name in a `<span>` with `spell-name-hover` class
- Added Bootstrap tooltip data attributes
- Tooltip displays:
  - Spell name (bold)
  - Level and school
  - Casting time
  - Range
  - Components
  - Duration
  - Description preview (25 words)

**Visual Effect:**
- Dotted underline on spell names
- Cursor changes to "help" icon
- Color changes to blue on hover
- Tooltip appears to the **left** (optimized for right-side column placement)

#### 2. Updated `character_detail.html`
**Location:** `characters/templates/characters/character_detail.html`

**Added CSS:**
```css
.spell-name-hover {
    cursor: help;
    transition: all 0.2s ease;
    border-bottom: 1px dotted rgba(13, 110, 253, 0.4);
}

.spell-name-hover:hover {
    color: #0d6efd;
    border-bottom-color: #0d6efd;
}

.spell-tooltip-detail {
    text-align: left;
    max-width: 320px;
    font-size: 0.8rem;
    line-height: 1.4;
}
```

#### 3. Updated `character_sheet_scripts.html`
**Location:** `characters/templates/characters/components/character_sheet_scripts.html`

**Added JavaScript:**
- Bootstrap tooltip initialization on page load
- Configured with:
  - HTML support for formatted tooltips
  - Hover and focus triggers (keyboard accessible)
  - 300ms show delay
  - 100ms hide delay
  - Window boundary for proper positioning

### User Experience

**Before:**
```
Cantrips
• Fire Bolt
• Prestidigitation

Level 1
• Magic Missile
• Shield
```

**After:**
```
Cantrips
• Fire Bolt ← hover shows full spell details
  ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣
• Prestidigitation ← hover shows full spell details
  ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣

Level 1
• Magic Missile ← hover shows full spell details
  ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣ ̣̣̣
• Shield ← hover shows full spell details
  ̣̣̣ ̣̣̣ ̣̣̣
```

### Tooltip Example

When hovering over "Fire Bolt":

```
┌─────────────────────────────────┐
│ Fire Bolt                       │
│ Level 0 Evocation               │
│ Casting Time: 1 action          │
│ Range: 120 feet                 │
│ Components: V, S                │
│ Duration: Instantaneous         │
│ ─────────────────────────────   │
│ You hurl a mote of fire at a    │
│ creature or object within       │
│ range. Make a ranged spell...   │
└─────────────────────────────────┘
```

### Features

✅ **Compact Display:** Tooltips appear on the left side (optimal for right column placement)
✅ **Keyboard Accessible:** Works with Tab + Focus
✅ **Smooth Animations:** 300ms delay prevents accidental triggers
✅ **Visual Feedback:** Dotted underline + color change on hover
✅ **Responsive:** Adjusts to window boundaries automatically
✅ **Consistent:** Matches spell selection page tooltips

### Benefits

1. **Quick Reference:** View spell details without leaving the character sheet
2. **No Navigation:** No need to open spell management page for quick lookups
3. **Combat Ready:** Check spell details during gameplay
4. **Clean UI:** Compact spell list with detailed info on demand
5. **Accessibility:** Works with mouse hover and keyboard focus

### Where It Works

The spell tooltips are now active on:
- ✅ **Character Detail Page** (main character sheet)
- ✅ **Character Creation Step 4** (spell selection)
- ✅ **Manage Spells Page** (editing existing characters)

### Technical Notes

- Uses Bootstrap 5 tooltip component
- Tooltip placement set to "left" for right-side column
- Maximum tooltip width: 350px
- Font size: 0.8rem for compact display
- Description truncated to 25 words to keep tooltips concise
- Boundary set to "window" to prevent overflow issues

### Browser Compatibility

Works in all modern browsers that support:
- CSS transitions
- Bootstrap 5
- JavaScript DOM manipulation
