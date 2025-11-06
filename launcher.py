#!/usr/bin/env python
"""
D&D Character Builder - Standalone Application Launcher

This script launches the Django development server and opens the application
in a native desktop window with an embedded browser.
"""

import os
import sys
import time
import socket
import threading
import webview
from pathlib import Path


def find_free_port():
    """Find a free port to run the Django server on."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


def is_server_running(port, max_attempts=30):
    """Check if the Django server is running and ready."""
    for _ in range(max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex(('127.0.0.1', port))
                if result == 0:
                    return True
        except:
            pass
        time.sleep(1)
    return False


def get_base_dir():
    """Get the base directory of the application."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return Path(sys._MEIPASS)
    else:
        # Running as script
        return Path(__file__).parent


def setup_django_environment():
    """Set up Django environment variables."""
    base_dir = get_base_dir()
    
    # Add the base directory to Python path
    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))
    
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dndcharbuilder.settings')
    
    return base_dir


def initialize_database(base_dir):
    """Initialize the database if it doesn't exist."""
    db_path = base_dir / 'db.sqlite3'
    
    if not db_path.exists():
        print("First run detected. Initializing database...")
        
        # Import Django and run setup
        import django
        django.setup()
        
        # Run migrations
        from django.core.management import call_command
        print("Running database migrations...")
        call_command('migrate', verbosity=0)
        
        # Populate D&D data
        print("Populating D&D data...")
        call_command('populate_dnd_data', verbosity=0)
        
        print("Database initialization complete!")
        return True
    
    return False


def run_django_server(port):
    """Run the Django development server."""
    base_dir = setup_django_environment()
    
    # Try to close PyInstaller splash screen if it exists
    try:
        import pyi_splash
        pyi_splash.update_text('Initializing database...')
    except:
        pass
    
    # Initialize database on first run
    first_run = initialize_database(base_dir)
    
    # Update splash screen
    try:
        import pyi_splash
        pyi_splash.update_text('Starting Django server...')
    except:
        pass
    
    # Import Django
    import django
    django.setup()
    
    # Start the server
    from django.core.management import execute_from_command_line
    
    print(f"Starting D&D Character Builder on http://127.0.0.1:{port}")
    print("Opening in native window...")
    print("-" * 60)
    
    # Run the Django server
    sys.argv = ['manage.py', 'runserver', f'127.0.0.1:{port}', '--noreload', '--insecure']
    execute_from_command_line(sys.argv)


def create_window(port):
    """Create and display the native application window."""
    url = f'http://127.0.0.1:{port}'
    
    # Get the icon path
    base_dir = get_base_dir()
    icon_path = base_dir / 'DnDCharBuilder.png'
    
    # Create window (initially blank while we wait for server)
    window = webview.create_window(
        title='D&D 5e Character Builder',
        url='about:blank',
        width=1400,
        height=900,
        resizable=True,
        fullscreen=False,
        min_size=(800, 600),
        confirm_close=True,
        background_color='#1a1a2e'
    )
    
    # Set the window icon if it exists
    if icon_path.exists():
        try:
            window.set_icon(str(icon_path))
        except Exception as e:
            print(f"Note: Could not set window icon: {e}")
    
    def load_app():
        """Wait for server and load the main app."""
        print("Waiting for server to start...")
        
        # Update splash screen if available
        try:
            import pyi_splash
            pyi_splash.update_text('Waiting for server...')
        except:
            pass
        
        if is_server_running(port):
            print("Server ready! Loading application...")
            
            # Close splash screen before showing main window
            try:
                import pyi_splash
                pyi_splash.close()
            except:
                pass
            
            time.sleep(0.3)  # Brief pause for smooth transition
            window.load_url(url)
        else:
            print("Server did not start in time.")
            
            # Close splash screen
            try:
                import pyi_splash
                pyi_splash.close()
            except:
                pass
            
            error_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Error</title>
                <style>
                    body {{
                        margin: 0;
                        padding: 40px;
                        height: 100vh;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                        color: #e0e0e0;
                        text-align: center;
                    }}
                    .error-icon {{
                        font-size: 64px;
                        margin-bottom: 20px;
                    }}
                    h1 {{ 
                        font-size: 32px; 
                        margin-bottom: 20px;
                        color: #dc3545;
                    }}
                    p {{ 
                        font-size: 18px; 
                        opacity: 0.9; 
                        max-width: 500px;
                        line-height: 1.6;
                    }}
                </style>
            </head>
            <body>
                <div class="error-icon">⚠️</div>
                <h1>Failed to Start Server</h1>
                <p>The Django server failed to start. Please try closing and reopening the application.</p>
            </body>
            </html>
            """
            window.load_html(error_html)
    
    # Start loading in a separate thread
    threading.Thread(target=load_app, daemon=True).start()
    
    # Start the webview (blocks until window closes)
    webview.start(debug=False)


def main():
    """Main application entry point."""
    print("=" * 60)
    print("D&D 5e Character Builder - Standalone Application")
    print("=" * 60)
    print()
    
    # Find a free port
    port = find_free_port()
    
    # Start Django server in a background thread
    server_thread = threading.Thread(target=run_django_server, args=(port,), daemon=True)
    server_thread.start()
    
    try:
        # Create and show the window (blocking)
        create_window(port)
    except KeyboardInterrupt:
        print("\n\nShutting down D&D Character Builder...")
        print("Thank you for using the app!")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError starting application: {e}")
        print("\nPlease report this issue if it persists.")
        input("Press Enter to exit...")
        sys.exit(1)


if __name__ == '__main__':
    main()
