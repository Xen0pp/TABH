#!/bin/bash

echo "🚀 Starting TABH Frontend Server..."
echo "📍 Location: $(pwd)"

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start Next.js development server
echo "🌟 Starting Next.js server on http://localhost:3000"
echo "🏠 Portal: http://localhost:3000/portal"
echo ""
echo "Press Ctrl+C to stop the server"
echo "================================"

npm run dev
