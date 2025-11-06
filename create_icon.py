#!/usr/bin/env python
"""
Create application icons for D&D Character Builder
Generates .icns (macOS), .ico (Windows), and .png (Linux) icons
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon_image(size):
    """Create a single icon image of the specified size."""
    # Create a new image with transparency
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Colors
    shield_color = (139, 0, 0)  # Dark red
    shield_border = (255, 215, 0)  # Gold
    d20_color = (255, 255, 255)  # White
    text_color = (139, 0, 0)  # Dark red
    
    # Calculate dimensions
    margin = size // 10
    shield_width = size - (2 * margin)
    shield_height = int(shield_width * 1.2)
    
    # Shield shape (pentagon-like)
    shield_top = margin
    shield_left = margin
    shield_right = size - margin
    shield_bottom = shield_top + shield_height
    shield_mid_x = size // 2
    
    # Draw shield outline (gold border)
    border_width = max(2, size // 40)
    shield_points = [
        (shield_left, shield_top + shield_height // 4),
        (shield_mid_x, shield_top),
        (shield_right, shield_top + shield_height // 4),
        (shield_right, shield_top + shield_height * 3 // 4),
        (shield_mid_x, shield_bottom),
        (shield_left, shield_top + shield_height * 3 // 4),
    ]
    
    # Draw border
    for i in range(border_width):
        offset_points = [(x + i - border_width//2, y + i - border_width//2) for x, y in shield_points]
        draw.polygon(offset_points, outline=shield_border)
    
    # Draw filled shield
    draw.polygon(shield_points, fill=shield_color, outline=shield_border)
    
    # Draw D20 (diamond shape) in center
    d20_size = shield_width // 2
    d20_center_x = shield_mid_x
    d20_center_y = shield_top + shield_height // 2
    
    d20_points = [
        (d20_center_x, d20_center_y - d20_size // 2),  # Top
        (d20_center_x + d20_size // 2, d20_center_y),  # Right
        (d20_center_x, d20_center_y + d20_size // 2),  # Bottom
        (d20_center_x - d20_size // 2, d20_center_y),  # Left
    ]
    draw.polygon(d20_points, fill=d20_color, outline=shield_border)
    
    # Add "D20" text - using default font to avoid font loading issues
    font_size = max(10, size // 6)
    font = ImageFont.load_default()
    
    text = "D20"
    # Get text size using getbbox with default font
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top
    text_x = d20_center_x - text_width // 2
    text_y = d20_center_y - text_height // 2
    
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    
    return img

def create_macos_icon():
    """Create .icns file for macOS"""
    print("Creating macOS icon (.icns)...")
    
    # macOS requires multiple sizes
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    iconset_dir = "DnDCharBuilder.iconset"
    
    # Create iconset directory
    os.makedirs(iconset_dir, exist_ok=True)
    
    # Generate all required sizes
    for size in sizes:
        img = create_icon_image(size)
        img.save(f"{iconset_dir}/icon_{size}x{size}.png")
        
        # Create @2x versions for Retina displays
        if size <= 512:
            img_2x = create_icon_image(size * 2)
            img_2x.save(f"{iconset_dir}/icon_{size}x{size}@2x.png")
    
    # Convert to .icns using iconutil (macOS only)
    if os.system("which iconutil > /dev/null 2>&1") == 0:
        os.system(f"iconutil -c icns {iconset_dir} -o DnDCharBuilder.icns")
        print("✅ Created DnDCharBuilder.icns")
        
        # Clean up iconset directory
        import shutil
        shutil.rmtree(iconset_dir)
    else:
        print("⚠️  iconutil not found. Keeping .iconset directory.")
        print("   Run: iconutil -c icns DnDCharBuilder.iconset -o DnDCharBuilder.icns")

def create_windows_icon():
    """Create .ico file for Windows"""
    print("Creating Windows icon (.ico)...")
    
    # Windows ICO supports multiple sizes in one file
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for size in sizes:
        images.append(create_icon_image(size))
    
    # Save as ICO
    images[0].save(
        "DnDCharBuilder.ico",
        format='ICO',
        sizes=[(img.width, img.height) for img in images],
        append_images=images[1:]
    )
    print("✅ Created DnDCharBuilder.ico")

def create_linux_icon():
    """Create .png file for Linux"""
    print("Creating Linux icon (.png)...")
    
    # Create 512x512 PNG
    img = create_icon_image(512)
    img.save("DnDCharBuilder.png")
    print("✅ Created DnDCharBuilder.png")

def main():
    print("=" * 60)
    print("D&D Character Builder - Icon Generator")
    print("=" * 60)
    print()
    
    try:
        # Create icons for all platforms
        create_macos_icon()
        create_windows_icon()
        create_linux_icon()
        
        print()
        print("=" * 60)
        print("✅ All icons created successfully!")
        print("=" * 60)
        print()
        print("Files created:")
        print("  - DnDCharBuilder.icns  (macOS)")
        print("  - DnDCharBuilder.ico   (Windows)")
        print("  - DnDCharBuilder.png   (Linux)")
        print()
        print("Next steps:")
        print("  1. Update build_standalone.spec:")
        print("     icon='DnDCharBuilder.icns'  # macOS")
        print("     icon='DnDCharBuilder.ico'   # Windows")
        print("  2. Rebuild the app: ./build.sh")
        print()
        
    except Exception as e:
        print(f"❌ Error creating icons: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
