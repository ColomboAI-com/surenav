# Publishing SureNav to GitHub

## Prerequisites

- GitHub account
- Git installed locally
- Python 3.9+ installed

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `surenav`
3. Description: "Open-source web unblocker for AI agents - no API keys required"
4. Make it **Public**
5. **Do NOT** initialize with README (we already have one)
6. Click "Create repository"

## Step 2: Update Configuration Files

Replace `YOUR_USERNAME` with your actual GitHub username in:
- `README.md` (line 20)
- `setup.py` (line 11)
- `pyproject.toml` (lines 16-19)
- `CONTRIBUTING.md` (line 13)

Also update author information in:
- `setup.py` (lines 8-9)
- `pyproject.toml` (line 9)
- `src/__init__.py` (line 6)

## Step 3: Initialize Git and Push

```bash
cd c:\Users\yasha\git\surenav
git init
git add .
git commit -m "Initial release: SureNav v1.0.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/surenav.git
git push -u origin main
```

## Step 4: Create GitHub Release

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: "SureNav v1.0.0 - Initial Release"
5. Description:
   ```
   🎉 First release of SureNav!
   
   Features:
   - 🔓 No API keys required
   - 🕵️ Stealth browser automation
   - 🌍 Free proxy rotation
   - ⚡ JavaScript rendering
   - 🔍 Google search scraping
   - 🐳 Docker support
   ```
6. Click "Publish release"

## Step 5: Enable GitHub Actions

GitHub Actions will automatically run on push. Check the "Actions" tab to see CI/CD status.

## Step 6 (Optional): Publish to PyPI

```bash
pip install build twine
python -m build
twine upload dist/*
```

You'll need a PyPI account and API token.

## Step 7 (Optional): Set Up Docker Hub

1. Create account at https://hub.docker.com
2. Create repository: `surenav`
3. Build and push:
   ```bash
   docker build -t YOUR_USERNAME/surenav:latest .
   docker push YOUR_USERNAME/surenav:latest
   ```

## Verification

After publishing, verify:
- ✅ Repository is public and accessible
- ✅ README displays correctly
- ✅ GitHub Actions pass
- ✅ License is visible
- ✅ Release is created

## Updating the Package

For future updates:
```bash
# Update version in setup.py, pyproject.toml, and src/__init__.py
git add .
git commit -m "Release v1.1.0: Add new features"
git tag v1.1.0
git push origin main --tags
```

Then create a new release on GitHub.
