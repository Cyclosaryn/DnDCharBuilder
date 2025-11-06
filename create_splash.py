#!/usr/bin/env python3
"""
Generate a splash screen image for the D&D Character Builder.
This splash screen shows during PyInstaller extraction phase.
"""

from PIL import Image, ImageDraw, ImageFont

def create_splash_screen():
    """Create a splash screen image."""
    # Create image with dark background
    width, height = 600, 400
    img = Image.new('RGB', (width, height), color='#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    # Try to load the logo
    try:
        logo = Image.open('DnDCharBuilder.png')
        # Resize logo to fit
        logo_size = 120
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        
        # Paste logo in center-top
        logo_x = (width - logo_size) // 2
        logo_y = 60
        
        # Create a white background for transparency
        if logo.mode == 'RGBA':
            img.paste(logo, (logo_x, logo_y), logo)
        else:
            img.paste(logo, (logo_x, logo_y))
    except Exception as e:
        print(f"Could not load logo: {e}")
        # Draw a simple D20 emoji-style fallback
        draw.text((width//2, 100), "🎲", fill='#ffffff', anchor='mm', font=ImageFont.load_default())
    
    # Add title
    try:
        # Try to use a system font
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
        text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Title
    title = "D&D Character Builder"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_width) // 2, 200), title, fill='#ffffff', font=title_font)
    
    # Subtitle
    subtitle = "5th Edition"
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(((width - subtitle_width) // 2, 245), subtitle, fill='#b8b8b8', font=subtitle_font)
    
    # Loading text
    loading_text = "Loading..."
    loading_bbox = draw.textbbox((0, 0), loading_text, font=text_font)
    loading_width = loading_bbox[2] - loading_bbox[0]
    draw.text(((width - loading_width) // 2, 290), loading_text, fill='#dc3545', font=text_font)
    
    # Add disclaimer at bottom
    disclaimer = "Unofficial fan-made tool • Not affiliated with Wizards of the Coast"
    disclaimer_bbox = draw.textbbox((0, 0), disclaimer, font=text_font)
    disclaimer_width = disclaimer_bbox[2] - disclaimer_bbox[0]
    draw.text(((width - disclaimer_width) // 2, height - 30), disclaimer, fill='#666666', font=text_font)
    
    # Save the splash screen
    img.save('splash.png')
    print("✅ Created splash.png")
    print(f"   Size: {width}x{height}")

if __name__ == '__main__':
    print("=" * 60)
    print("D&D Character Builder - Splash Screen Generator")
    print("=" * 60)
    print()
    
    try:
        create_splash_screen()
        print()
        print("=" * 60)
        print("✅ Splash screen created successfully!")
        print("=" * 60)
    except Exception as e:
        print(f"❌ Error creating splash screen: {e}")
        import traceback
        traceback.print_exc()
