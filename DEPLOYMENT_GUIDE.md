# HNM Bot - Deployment Guide

## Quick Deployment

### For RHEL/CentOS 6.x, 7.x, 8.x, 9.x

```bash
# 1. Transfer the file
scp hnm_linux_bot.py root@your-server:/root/

# 2. SSH to server
ssh root@your-server

# 3. Make executable
chmod +x hnm_linux_bot.py

# 4. Test run
python3 hnm_linux_bot.py
# or for RHEL 6 with Python 2.7
python hnm_linux_bot.py

# 5. Install globally (optional)
cp hnm_linux_bot.py /usr/local/bin/hnm-bot
chmod +x /usr/local/bin/hnm-bot

# 6. Run from anywhere
hnm-bot
```

### For Ubuntu 16.04, 18.04, 20.04, 22.04, 24.04

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

# 6. Run from anywhere
hnm-bot
```

### For SUSE Linux 11.x, 12.x, 15.x

```bash
# 1. Transfer the file
scp hnm_linux_bot.py root@your-server:/root/

# 2. SSH to server
ssh root@your-server

# 3. Make executable
chmod +x hnm_linux_bot.py

# 4. Test run (SUSE 15+)
python3 hnm_linux_bot.py
# or for SUSE 11/12
python hnm_linux_bot.py

# 5. Install globally (optional)
cp hnm_linux_bot.py /usr/local/bin/hnm-bot
chmod +x /usr/local/bin/hnm-bot

# 6. Run from anywhere
hnm-bot
```

## Recommended Packages

### RHEL/CentOS
```bash
# For full functionality, install these packages:
yum install -y sysstat net-tools ipmitool
# or for RHEL 8+
dnf install -y sysstat net-tools ipmitool
```

### Ubuntu
```bash
# For full functionality, install these packages:
apt-get update
apt-get install -y sysstat net-tools ipmitool
```

### SUSE
```bash
# For full functionality, install these packages:
zypper install -y sysstat net-tools ipmitool
```

## Usage Examples

### Quick System Check
```bash
hnm-bot
🐧 hnm-bot> disk
🐧 hnm-bot> memory
🐧 hnm-bot> cpu
🐧 hnm-bot> exit
```

### Generate Full Report
```bash
sudo hnm-bot
🐧 hnm-bot> fullreport
# Report saved to: system_report_20251205_162345.txt
🐧 hnm-bot> exit

# View the report
cat system_report_*.txt
```

### Network Troubleshooting
```bash
hnm-bot
🐧 hnm-bot> network
🐧 hnm-bot> netconfig
🐧 hnm-bot> ports
🐧 hnm-bot> exit
```

### Performance Analysis
```bash
hnm-bot
🐧 hnm-bot> performance
🐧 hnm-bot> processes
🐧 hnm-bot> exit
```

## Running with Sudo

Many advanced features require root privileges:

```bash
# Method 1: Run as root
sudo hnm-bot

# Method 2: Switch to root
su -
hnm-bot

# Method 3: Run specific commands with sudo
hnm-bot
🐧 hnm-bot> custom
Enter command to execute: sudo dmidecode -t 1
Execute 'sudo dmidecode -t 1'? (yes/no): yes
```

## Automation Examples

### Generate Daily Reports
```bash
# Add to crontab
crontab -e

# Add this line for daily report at 2 AM
0 2 * * * echo "fullreport" | /usr/local/bin/hnm-bot > /var/log/hnm-bot-daily-$(date +\%Y\%m\%d).log 2>&1
```

### Quick Health Check Script
```bash
#!/bin/bash
# health-check.sh

echo "disk
memory
cpu
services
exit" | hnm-bot
```

### Email Reports
```bash
#!/bin/bash
# email-report.sh

REPORT_FILE="/tmp/system_report_$(date +%Y%m%d).txt"
echo "fullreport
exit" | hnm-bot > $REPORT_FILE

mail -s "System Report - $(hostname)" admin@example.com < $REPORT_FILE
```

## Troubleshooting

### Python not found
```bash
# Check Python version
python --version
python3 --version

# Install Python 3 if needed
# RHEL/CentOS
yum install python3
# Ubuntu
apt-get install python3
# SUSE
zypper install python3
```

### Permission denied errors
```bash
# Run with sudo
sudo hnm-bot

# Or change file permissions
chmod +x /usr/local/bin/hnm-bot
```

### Command not found (after installation)
```bash
# Check if /usr/local/bin is in PATH
echo $PATH

# Add to PATH if needed
export PATH=$PATH:/usr/local/bin

# Make permanent (add to ~/.bashrc or ~/.bash_profile)
echo 'export PATH=$PATH:/usr/local/bin' >> ~/.bashrc
source ~/.bashrc
```

### Missing commands (netstat, ifconfig, etc.)
```bash
# Install net-tools package
# RHEL/CentOS
yum install net-tools
# Ubuntu
apt-get install net-tools
# SUSE
zypper install net-tools
```

## Security Considerations

1. **File Permissions**: Ensure the script is owned by root and not world-writable
   ```bash
   chown root:root /usr/local/bin/hnm-bot
   chmod 755 /usr/local/bin/hnm-bot
   ```

2. **Sudo Access**: Be careful with the `custom` command - it can execute any command
   
3. **Log Files**: Reports may contain sensitive information - protect them appropriately
   ```bash
   chmod 600 system_report_*.txt
   ```

4. **Network Security**: Don't expose the bot over network without proper authentication

## Uninstallation

```bash
# Remove the bot
rm /usr/local/bin/hnm-bot

# Remove any generated reports
rm /root/system_report_*.txt
rm /tmp/system_report_*.txt

# Remove from crontab if added
crontab -e
# Delete the hnm-bot line
```

## Support

For issues or questions, contact:
**Harihar Mishra**  
Email: harihar.mishra@hcltech.com

## Version History

- **v1.0** - Initial release with basic commands
- **v2.0** - Added advanced system information commands
- **v2.1** - Multi-distribution compatibility (RHEL 6+, Ubuntu 16.04+, SUSE 11+)
