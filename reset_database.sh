#!/bin/bash
# Reset and repopulate the database

echo "🔄 Resetting D&D Character Builder database..."

# Activate virtual environment
source venv/bin/activate

# Remove existing database
echo "📦 Removing old database..."
rm -f db.sqlite3

# Run migrations
echo "🗄️  Creating new database..."
python manage.py migrate

# Populate D&D data
echo "📚 Populating D&D 5e content..."
python manage.py populate_dnd_data

# Create sample character
echo "👤 Creating sample character..."
python manage.py create_sample_character

echo ""
echo "✅ Database reset complete!"
echo ""
echo "To create a superuser for admin access, run:"
echo "   python manage.py createsuperuser"
echo ""
echo "To start the server, run:"
echo "   python manage.py runserver"
echo ""
