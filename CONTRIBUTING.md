# Contributing to SureNav

Thank you for your interest in contributing to SureNav! This document provides guidelines and instructions for contributing.

## 🚀 Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/surenav.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Install Playwright: `playwright install chromium`

## 📝 Making Changes

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `pytest tests/`
4. Format code: `black src/`
5. Commit with clear messages: `git commit -m "Add: description of changes"`

## 🧪 Testing

- Write tests for new features
- Ensure all tests pass before submitting PR
- Test manually with `python -m src.server`

## 📤 Submitting Pull Requests

1. Push to your fork: `git push origin feature/your-feature-name`
2. Open a PR against `main` branch
3. Describe what your PR does and why
4. Link any related issues

## 🐛 Reporting Bugs

Open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version, etc.)

## 💡 Feature Requests

Open an issue with the "enhancement" label describing:
- The feature you'd like
- Why it would be useful
- Any implementation ideas

## ⚖️ Legal Notice

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

Be respectful, constructive, and inclusive in all interactions.
