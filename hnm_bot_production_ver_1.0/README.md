# HNM Bot 🐧

An interactive command-line chatbot designed to help Linux system administrators with common tasks and system monitoring.

**Built by:** Harihar Mishra  
**Email:** harihar.mishra@hcltech.com

## Features

**Basic Monitoring:**
- **Disk Management**: Check disk usage, mounted filesystems, and inode usage
- **Memory Monitoring**: View memory usage and detailed statistics
- **CPU Information**: Display CPU specs, load averages, and top processes
- **Process Management**: List processes by CPU and memory usage
- **User Management**: View logged-in users, login history, and failed attempts
- **Service Monitoring**: Check system services status
- **Network Diagnostics**: View interfaces, routing, and active connections
- **Log Analysis**: Access recent system logs and errors
- **Port Scanning**: List open ports and established connections
- **Firewall Status**: Check UFW, firewalld, and iptables rules
- **Update Checking**: Check for available system updates

**Advanced System Information:**
- **Complete System Info**: Hardware details, hostname, ILO/IPMI configuration
- **LVM & Storage**: Physical volumes, volume groups, logical volumes, iSCSI, multipath
- **Network Configuration**: Bonding, routing tables, iptables mangle rules
- **User Authentication**: NIS, NTP, Chrony, cron jobs, sudoers configuration
- **Samba & Domain**: SSSD, Kerberos, Samba, NSSwitch configuration
- **Cluster Management**: PCS, CRM, HPSG ServiceGuard, Veritas cluster status
- **Performance Reports**: CPU/RAM utilization with SAR historical data
- **Full System Report**: Generate comprehensive report and save to file

**Utilities:**
- **Custom Commands**: Execute any Linux command safely

## Requirements

- Python 3.6 or higher (Python 2.7 compatible with minor modifications)
- Linux operating system
- Appropriate permissions for system commands (some features require sudo)

## Supported Linux Distributions

**Tested and Compatible:**
- Red Hat Enterprise Linux (RHEL) 6.x, 7.x, 8.x, 9.x
- CentOS 6.x, 7.x, 8.x
- Ubuntu 16.04, 18.04, 20.04, 22.04, 24.04
- SUSE Linux Enterprise Server (SLES) 11.x, 12.x, 15.x
- openSUSE Leap 15.x

**Command Compatibility:**
- Automatically detects and uses appropriate commands for each distribution
- Falls back to older commands when modern tools are unavailable
- Supports both systemd (RHEL 7+, Ubuntu 16.04+) and SysV init (RHEL 6, older systems)
- Works with various package managers: yum, dnf, apt, zypper

## Installation

1. Download the script:
```bash
wget https://raw.githubusercontent.com/yourusername/hnm-bot/main/hnm_linux_bot.py
# or
curl -O https://raw.githubusercontent.com/yourusername/hnm-bot/main/hnm_linux_bot.py
```

2. Make it executable:
```bash
chmod +x hnm_linux_bot.py
```

3. (Optional) Move to a directory in your PATH:
```bash
sudo mv hnm_linux_bot.py /usr/local/bin/hnm-bot
```

## Usage

Run the bot:
```bash
python3 hnm_linux_bot.py
# or if installed globally
hnm-bot
```

### Available Commands

**Basic System Checks:**
- `help` - Show all available commands
- `disk` - Check disk usage and mounted filesystems
- `memory` - Display memory usage statistics
- `cpu` - Show CPU information and load
- `processes` - List top processes by CPU/memory usage
- `users` - Show logged in users and last logins
- `services` - Check status of system services
- `network` - Display network interfaces and connections
- `logs` - View recent system logs
- `uptime` - Show system uptime and load average
- `ports` - List open ports and listening services
- `firewall` - Check firewall status and rules
- `updates` - Check for available system updates

**Advanced System Information:**
- `system` - Complete system information (hardware, hostname, ILO, IPMI)
- `lvm` - LVM, disk, iSCSI, and multipath information
- `netconfig` - Network configuration (bonding, routes, iptables)
- `userconfig` - User authentication (NIS, NTP, cron, sudoers)
- `samba` - Samba, SSSD, Kerberos configuration
- `cluster` - Cluster status (PCS, CRM, HPSG, Veritas)
- `performance` - CPU/RAM utilization reports with SAR data
- `fullreport` - Generate complete system report (saves to file)

**Utilities:**
- `custom` - Run a custom Linux command
- `exit` or `quit` - Exit the bot

## Examples

```bash
🐧 hnm-bot> disk
=== Disk Usage ===
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   45G   50G  48% /

🐧 hnm-bot> memory
=== Memory Usage ===
              total        used        free      shared  buff/cache   available
Mem:           15Gi       8.2Gi       2.1Gi       500Mi       5.0Gi       6.5Gi

🐧 hnm-bot> services
=== Failed Services ===
0 loaded units listed.

🐧 hnm-bot> system
=== System Information ===
# uname -a
Linux server01 3.10.0-1160.el7.x86_64 ...

🐧 hnm-bot> fullreport
🔍 Generating full system report... This may take a moment.
✓ Report saved to: system_report_20251205_162345.txt
```

## Security Notes

- Some commands require root/sudo privileges
- The `custom` command allows executing any Linux command - use with caution
- Always review commands before confirming execution
- The bot has a 30-second timeout for long-running commands

## Troubleshooting

**Permission Denied Errors**: Some commands require elevated privileges. Run with sudo:
```bash
sudo python3 hnm_linux_bot.py
```

**Command Not Found**: Ensure the required system utilities are installed (ss, systemctl, journalctl, etc.)

## Contributing

Feel free to add more commands or improve existing functionality!

## Author

**Harihar Mishra**  
Email: harihar.mishra@hcltech.com

## License

MIT License - Free to use and modify
