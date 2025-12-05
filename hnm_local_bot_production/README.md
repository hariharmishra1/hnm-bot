# HNM Bot - Local System Administration Tool

**Built by:** Harihar Mishra

## Overview

HNM Bot is an interactive command-line tool for Linux system administration. It provides 24 commands to monitor, analyze, and manage Linux systems directly on the local machine.

## Features

### Basic Commands (16)
- **System Monitoring**: disk, memory, cpu, processes
- **User Management**: users, services
- **Network Diagnostics**: network, ports, firewall
- **System Information**: logs, uptime, updates

### Advanced Commands (8)
- **system** - Complete system information (hardware, hostname, ILO, IPMI)
- **lvm** - LVM, disk, iSCSI, and multipath information
- **netconfig** - Network configuration (bonding, routes, iptables)
- **userconfig** - User authentication (NIS, NTP, cron, sudoers)
- **samba** - Samba, SSSD, Kerberos configuration
- **cluster** - Cluster status (PCS, CRM, HPSG, Veritas)
- **performance** - CPU/RAM utilization reports with SAR data
- **fullreport** - Generate complete system report (saves to file)

## Requirements

- Python 3.6 or higher
- Linux operating system
- Root/sudo access for full functionality

## Supported Linux Distributions

- Red Hat Enterprise Linux (RHEL) 6.x, 7.x, 8.x, 9.x
- CentOS 6.x, 7.x, 8.x
- Ubuntu 16.04, 18.04, 20.04, 22.04, 24.04
- SUSE Linux Enterprise Server (SLES) 11.x, 12.x, 15.x
- openSUSE Leap 15.x

## Quick Start

### Installation

```bash
# Make executable
chmod +x hnm_linux_bot.py

# Run
python3 hnm_linux_bot.py
```

### Usage

```bash
python3 hnm_linux_bot.py

🐧 hnm-bot> help
🐧 hnm-bot> disk
🐧 hnm-bot> memory
🐧 hnm-bot> system
🐧 hnm-bot> fullreport
🐧 hnm-bot> exit
```

### Install Globally (Optional)

```bash
sudo cp hnm_linux_bot.py /usr/local/bin/hnm-bot
sudo chmod 755 /usr/local/bin/hnm-bot

# Run from anywhere
hnm-bot
```

## Recommended Packages

For full functionality, install these packages:

**RHEL/CentOS:**
```bash
yum install -y sysstat net-tools ipmitool
# or for RHEL 8+
dnf install -y sysstat net-tools ipmitool
```

**Ubuntu:**
```bash
apt-get install -y sysstat net-tools ipmitool
```

**SUSE:**
```bash
zypper install -y sysstat net-tools ipmitool
```

## Documentation

- **INSTALL.md** - Installation instructions
- **COMMANDS_REFERENCE.md** - Complete command reference
- **COMPATIBILITY.md** - OS compatibility details
- **DEPLOYMENT_GUIDE.md** - Deployment instructions
- **CHANGELOG.md** - Version history

## Security

- Command timeout protection (30 seconds)
- Confirmation prompts for custom commands
- Exception handling throughout
- No network exposure (CLI only)
- Read-only operations for most commands

## Version

Current Version: 1.0.1  
Release Date: December 2024

## License

MIT License - See LICENSE file for details

## Author

Built by: Harihar Mishra

---

For detailed documentation, see the included .md files.
