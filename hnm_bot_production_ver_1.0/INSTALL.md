# HNM Bot - Installation Guide

## Quick Installation

### For RHEL/CentOS

```bash
# 1. Transfer the file
scp hnm_linux_bot.py root@your-server:/root/

# 2. SSH to server
ssh root@your-server

# 3. Make executable
chmod +x hnm_linux_bot.py

# 4. Test run
python3 hnm_linux_bot.py

# 5. Install globally (optional)
cp hnm_linux_bot.py /usr/local/bin/hnm-bot
chmod +x /usr/local/bin/hnm-bot

# 6. Install recommended packages
yum install -y sysstat net-tools ipmitool
# or for RHEL 8+
dnf install -y sysstat net-tools ipmitool
```

### For Ubuntu

```bash
# 1. Transfer the file
scp hnm_linux_bot.py user@your-server:/home/user/

# 2. SSH to server
ssh user@your-server

# 3. Make executable
chmod +x hnm_linux_bot.py

# 4. Test run
python3 hnm_linux_bot.py

# 5. Install globally (optional)
sudo cp hnm_linux_bot.py /usr/local/bin/hnm-bot
sudo chmod +x /usr/local/bin/hnm-bot

# 6. Install recommended packages
sudo apt-get update
sudo apt-get install -y sysstat net-tools ipmitool
```

### For SUSE Linux

```bash
# 1. Transfer the file
scp hnm_linux_bot.py root@your-server:/root/

# 2. SSH to server
ssh root@your-server

# 3. Make executable
chmod +x hnm_linux_bot.py

# 4. Test run
python3 hnm_linux_bot.py

# 5. Install globally (optional)
cp hnm_linux_bot.py /usr/local/bin/hnm-bot
chmod +x /usr/local/bin/hnm-bot

# 6. Install recommended packages
zypper install -y sysstat net-tools ipmitool
```

## Requirements

- Python 3.6 or higher
- Linux operating system (RHEL 6+, Ubuntu 16.04+, SUSE 11+)
- Root/sudo access for full functionality

## Verification

After installation, verify it works:

```bash
# Run the bot
hnm-bot

# Try basic commands
🐧 hnm-bot> help
🐧 hnm-bot> disk
🐧 hnm-bot> memory
🐧 hnm-bot> exit
```

## Troubleshooting

### Python not found
```bash
# Check Python version
python3 --version

# Install Python 3 if needed
# RHEL/CentOS: yum install python3
# Ubuntu: apt-get install python3
# SUSE: zypper install python3
```

### Permission denied
```bash
# Run with sudo
sudo hnm-bot

# Or fix permissions
chmod +x /usr/local/bin/hnm-bot
```

## Next Steps

1. Read DEPLOYMENT_GUIDE.md for detailed deployment instructions
2. Review PRODUCTION_CHECKLIST.md before production deployment
3. Check COMMANDS_REFERENCE.md for all available commands

## Support

For issues or questions:
- Email: harihar.mishra@hcltech.com
- Check documentation in the docs folder
