# HNM Remote Bot - Remote System Administration Tool

**Built by:** Harihar Mishra

## Overview

HNM Remote Bot allows you to connect to remote Linux systems via SSH and gather system information without logging into each server individually. Perfect for managing multiple servers from a central location.

## Features

- 🌐 Connect to remote Linux systems via SSH
- 🔐 Support for SSH key and password authentication
- 📊 All 24 system commands available remotely
- 📝 Generate reports from remote systems
- 🔄 Switch between multiple remote systems
- 💾 Save reports locally with remote hostname

## Requirements

- Python 3.6 or higher
- SSH client installed
- Network access to remote systems
- SSH access (key or password) to remote systems

## Quick Start

### Step 1: Start the Bot

```bash
python3 hnm_remote_bot.py
```

### Step 2: Connect to Remote System

```
🌐 hnm-remote [not connected]> connect

Enter hostname/IP: server.example.com
Enter username: root
Authentication method (1=SSH Key, 2=Password): 1
Enter SSH key path: ~/.ssh/id_rsa

✓ Successfully connected to root@server.example.com
```

### Step 3: Run Commands

```
🌐 hnm-remote [server.example.com]> disk
🌐 hnm-remote [server.example.com]> memory
🌐 hnm-remote [server.example.com]> system
🌐 hnm-remote [server.example.com]> fullreport
🌐 hnm-remote [server.example.com]> disconnect
```

## Available Commands

### Connection Commands
- `connect` - Connect to remote Linux system
- `disconnect` - Disconnect from remote system
- `status` - Show connection status

### System Commands (24)
All commands from the local bot are available:
- Basic: disk, memory, cpu, processes, users, services, network, logs, uptime, ports, firewall, updates
- Advanced: system, lvm, netconfig, userconfig, samba, cluster, performance, fullreport

## Authentication Methods

### Method 1: SSH Key (Recommended)

**Setup:**
```bash
# Generate SSH key
ssh-keygen -t rsa -b 4096

# Copy to remote server
ssh-copy-id user@remote-server

# Test connection
ssh user@remote-server
```

**Use in Bot:**
```
Authentication method: 1
Enter SSH key path: ~/.ssh/id_rsa
```

### Method 2: Password

```
Authentication method: 2
```
Note: You'll be prompted for password on each command.

## Supported Remote Systems

- RHEL/CentOS 6.x, 7.x, 8.x, 9.x
- Ubuntu 16.04, 18.04, 20.04, 22.04, 24.04
- SUSE Linux 11.x, 12.x, 15.x
- Any Linux with SSH server

## Documentation

- **REMOTE_BOT_GUIDE.md** - Complete user guide
- **REMOTE_QUICK_START.txt** - Quick reference

## Use Cases

1. **Central Monitoring** - Monitor multiple servers from one location
2. **Audit and Compliance** - Collect system information and generate reports
3. **Troubleshooting** - Quick system checks and remote diagnostics
4. **Documentation** - System inventory and configuration backup

## Security

- SSH-based communication (industry standard)
- Encrypted connections
- Secure authentication (SSH key recommended)
- No credentials stored
- Timeout protection

## Troubleshooting

### Connection Failed
```bash
# Test SSH manually
ssh user@remote-server

# Check SSH service
systemctl status sshd
```

### Permission Denied
- Use root user or sudo-enabled user
- Check SSH key permissions: `chmod 600 ~/.ssh/id_rsa`

### Timeout Errors
- Check network connectivity
- Verify remote system is responsive

## Version

Current Version: 1.0.0  
Release Date: December 2024

## License

MIT License - See LICENSE file for details

## Author

Built by: Harihar Mishra

---

For detailed documentation, see REMOTE_BOT_GUIDE.md
