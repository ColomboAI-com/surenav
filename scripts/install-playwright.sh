#!/bin/bash
# Install Playwright and browsers

echo "Installing Playwright..."
pip install playwright

echo "Installing Chromium browser..."
playwright install chromium

echo "Installing system dependencies..."
playwright install-deps chromium

echo "✅ Playwright installation complete!"
