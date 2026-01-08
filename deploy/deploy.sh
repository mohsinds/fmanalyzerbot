#!/usr/bin/env bash
set -e

echo "🚀 Starting FMAnalyzerBot deployment..."

cd /opt/fmab

# Create virtual environment if it doesn't exist
if [ ! -d .venv ]; then
  echo "📦 Creating virtual environment..."
  python3 -m venv .venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip first
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Verify requirements.txt exists
if [ ! -f requirements.txt ]; then
  echo "❌ ERROR: requirements.txt not found!"
  exit 1
fi

# Install/upgrade all dependencies from requirements.txt
echo "📥 Installing dependencies from requirements.txt..."
pip install --upgrade -r requirements.txt

# Verify critical package is installed
echo "✅ Verifying installation..."
python -c "import telegram; print(f'python-telegram-bot version: {telegram.__version__}')" || {
  echo "❌ ERROR: Failed to import python-telegram-bot!"
  exit 1
}

# Reload systemd and restart service
echo "🔄 Reloading systemd and restarting service..."
sudo systemctl daemon-reload
sudo systemctl restart fmab

# Show service status
echo "📊 Service status:"
sudo systemctl status fmab --no-pager

echo "✅ Deployment completed!"
