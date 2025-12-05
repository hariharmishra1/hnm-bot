# HNM Bot - Commands Reference Guide

## Quick Command Overview

### Basic Commands (16)
| Command | Description |
|---------|-------------|
| `help` | Show all available commands |
| `disk` | Disk usage and mounted filesystems |
| `memory` | Memory usage statistics |
| `cpu` | CPU information and load |
| `processes` | Top processes by CPU/memory |
| `users` | Logged in users and login history |
| `services` | System services status |
| `network` | Network interfaces and connections |
| `logs` | Recent system logs |
| `uptime` | System uptime and load average |
| `ports` | Open ports and listening services |
| `firewall` | Firewall status and rules |
| `updates` | Available system updates |
| `custom` | Run custom Linux command |
| `exit/quit` | Exit the bot |

### Advanced Commands (8)

#### 1. `system` - Complete System Information
Collects:
- `uname -a` - Kernel and system info
- `uptime` - System uptime
- `hostname` and `hostname -i` - Hostname and IP
- `/etc/redhat-release` or `/etc/os-release` - OS version
- `dmidecode -t 1` - Hardware information
- `hponcfg -w /tmp/ilo.out` - HP ILO configuration
- `ipmitool lan print` - IPMI network configuration
- `/etc/resolv.conf` - DNS configuration
- `/etc/hosts` - Host file entries

#### 2. `lvm` - LVM & Storage Information
Collects:
- `lsblk` - Block devices tree
- `df -hT` - Filesystem disk usage
- `/etc/fstab` - Filesystem mount table
- `pvs` - Physical volumes
- `vgs` - Volume groups
- `lvs` - Logical volumes
- `/etc/iscsi/initiatorname.iscsi` - iSCSI initiator name
- `iscsiadm -m session` - iSCSI sessions
- `sanlun lun show` - NetApp SAN LUNs
- `multipath -ll` - Multipath configuration

#### 3. `netconfig` - Network Configuration
Collects:
- `ifconfig -a` or `ip addr show` - All network interfaces
- `route -n` or `ip route` - Routing table
- `/proc/net/bonding/bond0` and `bond1` - Bonding status
- `/etc/sysconfig/network-scripts/ifcfg-bond0` and `bond1` - Bond configs
- `/etc/sysconfig/network` - Network configuration
- `iptables -t mangle -nvL` - IPTables mangle rules

#### 4. `userconfig` - User & Authentication Configuration
Collects:
- `/etc/passwd` - User accounts
- `/etc/shadow` - Password hashes (requires sudo)
- `/etc/sudoers` - Sudo configuration
- `nisdomainname` - NIS domain
- `/etc/yp.conf` - NIS configuration
- `ntpq -p` - NTP peers
- `/etc/ntp.conf` - NTP configuration
- `/etc/chrony.conf` - Chrony configuration
- `crontab -l` - Current user's cron jobs

#### 5. `samba` - Samba & Domain Configuration
Collects:
- `/etc/sssd/sssd.conf` - SSSD configuration
- `/etc/krb5.conf` - Kerberos configuration
- `/etc/samba/smb.conf` - Samba configuration
- `/etc/nsswitch.conf` - Name service switch configuration

#### 6. `cluster` - Cluster Status
Collects:
- `pcs status` - Pacemaker cluster status
- `crm status` - Corosync/Pacemaker status
- `cmviewcl -v` - HP ServiceGuard cluster status
- `hastatus -summary` - Veritas cluster status

#### 7. `performance` - Performance Reports
Collects:
- `free -g` - Current RAM utilization
- `lscpu` - CPU information
- `sar -r` - RAM utilization (last 2 hours)
- `sar -u` - CPU utilization (last 2 hours)

#### 8. `fullreport` - Complete System Report
- Runs ALL above commands
- Generates timestamped report file
- Saves to: `system_report_YYYYMMDD_HHMMSS.txt`
- Perfect for documentation or troubleshooting

## Usage Examples

### Quick Health Check
```bash
🐧 hnm-bot> disk
🐧 hnm-bot> memory
🐧 hnm-bot> services
```

### Network Troubleshooting
```bash
🐧 hnm-bot> network
🐧 hnm-bot> netconfig
🐧 hnm-bot> ports
```

### Storage Investigation
```bash
🐧 hnm-bot> disk
🐧 hnm-bot> lvm
```

### Complete System Audit
```bash
🐧 hnm-bot> fullreport
```

### Performance Analysis
```bash
🐧 hnm-bot> performance
🐧 hnm-bot> cpu
🐧 hnm-bot> processes
```

## Notes

- Some commands require **sudo/root privileges** (marked in output)
- Commands gracefully handle missing tools (ipmitool, hponcfg, etc.)
- SAR data requires `sysstat` package installed
- Full report can take 30-60 seconds to complete
- Report files are saved in current directory

## Permission Requirements

**Standard User:**
- Most basic commands work
- Network information
- Process listing
- Disk usage

**Sudo/Root Required:**
- `/etc/shadow` access
- `dmidecode` hardware info
- `iptables` rules
- Some cluster commands
- IPMI/ILO configuration

## Built by
**Harihar Mishra**  
Email: harihar.mishra@hcltech.com
