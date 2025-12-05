# Git Setup Guide for HNM Bot

## Step-by-Step GitHub Upload

### Step 1: Configure Git (First Time Only)

```bash
# Set your name and email
git config --global user.name "Harihar Mishra"
git config --global user.email "harihar.mishra@hcltech.com"

# Verify configuration
git config --list
```

### Step 2: Initialize Repository

```bash
# Navigate to the folder
cd hnm_bot_production_ver_1.0

# Initialize git
git init

# Check status
git status
```

### Step 3: Add Files

```bash
# Add all files
git add .

# Or add specific files
git add hnm_linux_bot.py
git add README.md
git add LICENSE

# Check what will be committed
git status
```

### Step 4: Create First Commit

```bash
# Commit with message
git commit -m "Initial release v1.0.0 - HNM Bot for Linux Administration"

# Verify commit
git log
```

### Step 5: Create GitHub Repository

1. Go to https://github.com
2. Click "New repository" or "+"
3. Repository name: `hnm-bot`
4. Description: "HNM Bot - Linux System Administration Tool"
5. Choose: Public or Private
6. **DO NOT** initialize with README, .gitignore, or license (we have them)
7. Click "Create repository"

### Step 6: Connect to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/hnm-bot.git

# Verify remote
git remote -v
```

### Step 7: Push to GitHub

```bash
# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Common Errors and Solutions

### Error 1: "fatal: not a git repository"
**Solution:**
```bash
git init
```

### Error 2: "Author identity unknown"
**Solution:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Error 3: "remote origin already exists"
**Solution:**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/hnm-bot.git
```

### Error 4: "failed to push some refs"
**Solution:**
```bash
# If remote has files you don't have locally
git pull origin main --allow-unrelated-histories
git push -u origin main

# Or force push (use with caution)
git push -u origin main --force
```

### Error 5: "Support for password authentication was removed"
**Solution:** Use Personal Access Token (PAT)

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo` (full control)
4. Copy the token
5. Use token as password when pushing

**Or use SSH:**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key

# Change remote to SSH
git remote set-url origin git@github.com:YOUR_USERNAME/hnm-bot.git
```

### Error 6: "Permission denied (publickey)"
**Solution:**
```bash
# Test SSH connection
ssh -T git@github.com

# If fails, add SSH key to GitHub (see Error 5)
```

### Error 7: "refusing to merge unrelated histories"
**Solution:**
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

## Alternative: Upload via GitHub Web Interface

If git commands are not working:

1. Go to https://github.com/YOUR_USERNAME/hnm-bot
2. Click "uploading an existing file"
3. Drag and drop all files from `hnm_bot_production_ver_1.0` folder
4. Add commit message: "Initial release v1.0.0"
5. Click "Commit changes"

## Verify Upload

After successful push:
1. Go to https://github.com/YOUR_USERNAME/hnm-bot
2. You should see all files
3. README.md will display on the homepage
4. LICENSE will be recognized by GitHub

## Create Release (Optional)

```bash
# Create and push tag
git tag -a v1.0.0 -m "Version 1.0.0 - Initial Release"
git push origin v1.0.0
```

Then on GitHub:
1. Go to repository → Releases
2. Click "Create a new release"
3. Choose tag: v1.0.0
4. Release title: "HNM Bot v1.0.0"
5. Description: Copy from CHANGELOG.md
6. Click "Publish release"

## Quick Reference

```bash
# Complete workflow
cd hnm_bot_production_ver_1.0
git init
git add .
git commit -m "Initial release v1.0.0"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/hnm-bot.git
git push -u origin main

# Create release tag
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin v1.0.0
```

## Need Help?

If you're still getting errors:
1. Copy the exact error message
2. Check which step is failing
3. Look for the error in the "Common Errors" section above
4. Contact: harihar.mishra@hcltech.com

## Windows-Specific Notes

If using Windows:
- Use Git Bash or PowerShell
- Line endings: `git config --global core.autocrlf true`
- Path issues: Use forward slashes `/` not backslashes `\`

## Troubleshooting Checklist

- [ ] Git is installed: `git --version`
- [ ] User configured: `git config --list`
- [ ] In correct directory: `pwd` or `cd`
- [ ] Repository initialized: `ls -la .git`
- [ ] Files added: `git status`
- [ ] Commit created: `git log`
- [ ] Remote added: `git remote -v`
- [ ] Authentication working: Personal Access Token or SSH key

---

**Still having issues? Share the exact error message for specific help!**
