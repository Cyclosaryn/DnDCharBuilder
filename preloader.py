#!/usr/bin/env python3
"""
Pre-loader that shows a splash screen during PyInstaller extraction.
This runs before the main application to provide immediate visual feedback.
"""

import sys
import os
import threading
import time
import subprocess

def show_applescript_notification():
    """Show a macOS notification that the app is loading."""
    try:
        applescript = '''
        display notification "Please wait while the application loads..." with title "D&D Character Builder" subtitle "Loading..."
        '''
        subprocess.run(['osascript', '-e', applescript], check=False, capture_output=True)
    except:
        pass

def show_splash():
    """Show a splash screen using tkinter."""
    try:
        # Show notification immediately (works even during extraction)
        show_applescript_notification()
        
        import tkinter as tk
        from tkinter import PhotoImage
        
        # Create the splash window
        splash = tk.Tk()
        splash.title("D&D Character Builder")
        splash.overrideredirect(True)  # Remove window decorations
        
        # Get screen dimensions
        screen_width = splash.winfo_screenwidth()
        screen_height = splash.winfo_screenheight()
        
        # Set window size
        window_width = 600
        window_height = 400
        
        # Calculate position for center of screen
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        splash.geometry(f'{window_width}x{window_height}+{x}+{y}')
        splash.configure(bg='#1a1a2e')
        
        # Keep window on top
        splash.attributes('-topmost', True)
        
        # Create main frame
        main_frame = tk.Frame(splash, bg='#1a1a2e')
        main_frame.pack(expand=True, fill='both')
        
        # Try to load the logo
        try:
            from pathlib import Path
            if getattr(sys, 'frozen', False):
                # Running as compiled executable
                base_dir = Path(sys._MEIPASS)
            else:
                # Running as script
                base_dir = Path(__file__).parent
            
            logo_path = base_dir / 'DnDCharBuilder.png'
            if logo_path.exists():
                logo_image = PhotoImage(file=str(logo_path))
                # Subsample to resize
                logo_image = logo_image.subsample(2, 2)
                logo_label = tk.Label(main_frame, image=logo_image, bg='#1a1a2e')
                logo_label.image = logo_image  # Keep a reference
                logo_label.pack(pady=(60, 20))
            else:
                # Fallback to emoji
                logo_label = tk.Label(main_frame, text='🎲', font=('Helvetica', 80), bg='#1a1a2e', fg='white')
                logo_label.pack(pady=(60, 20))
        except:
            # Fallback to emoji
            logo_label = tk.Label(main_frame, text='🎲', font=('Helvetica', 80), bg='#1a1a2e', fg='white')
            logo_label.pack(pady=(60, 20))
        
        # Title
        title_label = tk.Label(
            main_frame,
            text='D&D Character Builder',
            font=('Helvetica', 28, 'bold'),
            bg='#1a1a2e',
            fg='white'
        )
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text='5th Edition',
            font=('Helvetica', 14),
            bg='#1a1a2e',
            fg='#b8b8b8'
        )
        subtitle_label.pack(pady=(5, 30))
        
        # Loading text
        loading_label = tk.Label(
            main_frame,
            text='Loading...',
            font=('Helvetica', 12),
            bg='#1a1a2e',
            fg='#dc3545'
        )
        loading_label.pack()
        
        # Disclaimer
        disclaimer_frame = tk.Frame(splash, bg='#1a1a2e')
        disclaimer_frame.pack(side='bottom', pady=20)
        
        disclaimer_label = tk.Label(
            disclaimer_frame,
            text='Unofficial fan-made tool • Not affiliated with Wizards of the Coast',
            font=('Helvetica', 10),
            bg='#1a1a2e',
            fg='#666666'
        )
        disclaimer_label.pack()
        
        copyright_label = tk.Label(
            disclaimer_frame,
            text='Created by CycloForge • © 2025',
            font=('Helvetica', 10),
            bg='#1a1a2e',
            fg='#555555'
        )
        copyright_label.pack()
        
        # Animate loading dots
        def animate_dots():
            dots = ['', '.', '..', '...']
            idx = 0
            while True:
                if not splash.winfo_exists():
                    break
                try:
                    loading_label.config(text=f'Loading{dots[idx]}')
                    idx = (idx + 1) % len(dots)
                    splash.update()
                    time.sleep(0.5)
                except:
                    break
        
        # Start animation in background
        animation_thread = threading.Thread(target=animate_dots, daemon=True)
        animation_thread.start()
        
        # Store splash reference for closing later
        global _splash_window
        _splash_window = splash
        
        # Update to ensure window appears
        splash.update()
        
        # Start the GUI loop
        splash.mainloop()
        
    except Exception as e:
        print(f"Could not show splash screen: {e}")
        # Continue anyway


def close_splash():
    """Close the splash screen."""
    try:
        global _splash_window
        if '_splash_window' in globals() and _splash_window:
            _splash_window.quit()
            _splash_window.destroy()
    except:
        pass


_splash_window = None

if __name__ == '__main__':
    # Show notification first (instant feedback)
    show_applescript_notification()
    
    # Show splash screen in a separate thread
    splash_thread = threading.Thread(target=show_splash, daemon=False)
    splash_thread.start()
    
    # Give splash time to appear
    time.sleep(1.0)
    
    # Import and run the main launcher
    try:
        import launcher
        close_splash()
        launcher.main()
    except Exception as e:
        close_splash()
        print(f"Error launching application: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

