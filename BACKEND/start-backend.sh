#!/bin/bash

echo "🚀 Starting TABH Backend Server..."
echo "📍 Location: $(pwd)"

# Run migrations
echo "🔄 Running database migrations..."
python manage.py migrate

# Start Django server on port 8000
echo "🌟 Starting Django server on http://localhost:8000"
echo "📊 Admin panel: http://localhost:8000/admin"
echo "�� API docs: http://localhost:8000/api/v1/swagger/"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================"

python manage.py runserver 8000
