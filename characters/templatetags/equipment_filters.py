from django import template

register = template.Library()


@register.filter
def filter_equipment_text(equipment_text, equipment_items):
    """
    Filter out lines from equipment text that contain items already in equipment_items.
    This prevents duplicate display of weapons and armor.
    """
    if not equipment_text or not equipment_items:
        return equipment_text
    
    # Get list of equipment item names (lowercase for case-insensitive matching)
    item_names = [item.name.lower() for item in equipment_items]
    
    # Filter lines
    filtered_lines = []
    for line in equipment_text.splitlines():
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Check if this line contains any of the equipment item names
        line_lower = line_stripped.lower()
        contains_item = False
        for item_name in item_names:
            if item_name in line_lower:
                contains_item = True
                break
        
        # Only include lines that don't contain existing equipment items
        if not contains_item:
            filtered_lines.append(line)
    
    return '\n'.join(filtered_lines) if filtered_lines else ''
