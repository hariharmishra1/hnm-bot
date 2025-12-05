# HNM Bot - Compatibility Guide

## Supported Linux Distributions

### Red Hat Enterprise Linux (RHEL) / CentOS
- **RHEL 6.x** - Full support with SysV init
- **RHEL 7.x** - Full support with systemd
- **RHEL 8.x** - Full support with systemd and dnf
- **RHEL 9.x** - Full support with systemd and dnf

### Ubuntu / Debian
- **Ubuntu 16.04 LTS** - Full support
- **Ubuntu 18.04 LTS** - Full support with netplan
- **Ubuntu 20.04 LTS** - Full support
- **Ubuntu 22.04 LTS** - Full support
- **Ubuntu 24.04 LTS** - Full support
- **Debian 8+** - Full support

### SUSE Linux
- **SLES 11.x** - Full support with SysV init
- **SLES 12.x** - Full support with systemd
- **SLES 15.x** - Full support with systemd
- **openSUSE Leap 15.x** - Full support

## Command Compatibility Matrix

### Network Commands
| Feature | Modern Command | Fallback (Older Systems) |
|---------|---------------|-------------------------|
| Network interfaces | `ip addr show` | `ifconfig -a` |
| Routing table | `ip route` | `route -n` |
| Active connections | `ss -tuln` | `netstat -tuln` |
| Established connections | `ss -tun` | `netstat -tun` |

### Service Management
| Distribution | Command |
|-------------|---------|
| RHEL 7+, Ubuntu 16.04+, SUSE 12+ | `systemctl` |
| RHEL 6, Ubuntu 14.04, SUSE 11 | `chkconfig`, `service` |

### Log Management
| Distribution | Command |
|-------------|---------|
| systemd-based | `journalctl` |
| SysV init | `/var/log/messages`, `/var/log/syslog` |

### Package Management
| Distribution | Command |
|-------------|---------|
| RHEL 8+, Fedora | `dnf` |
| RHEL 6/7, CentOS 6/7 | `yum` |
| Ubuntu, Debian | `apt`, `apt-get` |
| SUSE, openSUSE | `zypper` |

### Firewall Management
| Distribution | Firewall Tool |
|-------------|--------------|
| Ubuntu | `ufw` |
| RHEL 7+, SUSE 12+ | `firewalld` |
| SUSE 11 | `SuSEfirewall2` |
| All | `iptables` (fallback) |

### Network Configuration Files
| Distribution | Location |
|-------------|----------|
| RHEL, CentOS | `/etc/sysconfig/network-scripts/` |
| SUSE | `/etc/sysconfig/network/` |
| Ubuntu 16.04 and earlier | `/etc/network/interfaces` |
| Ubuntu 18.04+ | `/etc/netplan/*.yaml` |

## Feature Availability by Distribution

### Always Available
- System information (uname, hostname, uptime)
- Disk usage (df, lsblk)
- Memory usage (free)
- CPU information (lscpu or /proc/cpuinfo)
- Process listing (ps)
- User information (/etc/passwd)
- Network interfaces
- Routing tables

### Requires Installation
| Feature | Package | Distributions |
|---------|---------|--------------|
| SAR performance data | `sysstat` | All |
| iSCSI information | `iscsi-initiator-utils` (RHEL) / `open-iscsi` (Ubuntu) | All |
| Multipath | `device-mapper-multipath` | All |
| IPMI tools | `ipmitool` | All |
| HP ILO tools | `hponcfg` | HP servers only |
| NetApp tools | `sanlun` | NetApp SAN environments |

### Requires Root/Sudo
- `/etc/shadow` access
- `dmidecode` (hardware info)
- `iptables` rules viewing
- Some cluster commands
- IPMI/ILO configuration
- Firewall status (some distributions)

## Python Version Compatibility

### Python 3.6+
- **Fully supported** - All features work
- Recommended for RHEL 8+, Ubuntu 18.04+, SUSE 15+

### Python 2.7
- **Mostly compatible** with minor modifications:
  - Change `subprocess.run()` to `subprocess.Popen()`
  - Remove type hints if present
  - Adjust string formatting

## Known Limitations

### RHEL 6 / CentOS 6
- No systemd (uses SysV init)
- No journalctl (uses /var/log/messages)
- Older kernel (may lack some /proc entries)
- Python 2.6 by default (upgrade to 2.7 or 3.6 recommended)

### Ubuntu 14.04
- No systemd by default (uses Upstart)
- Limited netplan support
- Older package versions

### SUSE 11
- No systemd (uses SysV init)
- Uses SuSEfirewall2 instead of firewalld
- Older zypper version

## Testing Recommendations

Before deploying in production, test these commands:
```bash
# Test basic functionality
python3 hnm_linux_bot.py
🐧 hnm-bot> help
🐧 hnm-bot> system
🐧 hnm-bot> disk

# Test with sudo for full features
sudo python3 hnm_linux_bot.py
🐧 hnm-bot> firewall
🐧 hnm-bot> userconfig
🐧 hnm-bot> fullreport
```

## Troubleshooting

### "Command not found" errors
- Install missing packages (sysstat, net-tools, etc.)
- Bot will gracefully handle missing commands with fallbacks

### Permission denied errors
- Run with `sudo` for privileged commands
- Check file permissions on config files

### Python version issues
- Ensure Python 3.6+ is installed
- Use `python3` explicitly instead of `python`

## Built by
**Harihar Mishra**  
Email: harihar.mishra@hcltech.com
