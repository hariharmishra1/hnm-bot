#!/usr/bin/env python3
"""
HNM Bot - Interactive assistant for Linux system administration tasks

Built by: Harihar Mishra
Email: harihar.mishra@hcltech.com
"""

import subprocess
import sys
import os
from datetime import datetime

class Hnm_Linux_Bot:
    def __init__(self):
        self.detect_os()
        self.commands = {
            'help': self.show_help,
            'disk': self.check_disk_usage,
            'memory': self.check_memory,
            'cpu': self.check_cpu,
            'processes': self.list_processes,
            'users': self.list_users,
            'services': self.check_services,
            'network': self.check_network,
            'logs': self.check_logs,
            'uptime': self.check_uptime,
            'ports': self.check_ports,
            'firewall': self.check_firewall,
            'updates': self.check_updates,
            'system': self.system_info,
            'lvm': self.lvm_info,
            'netconfig': self.network_config,
            'userconfig': self.user_config,
            'samba': self.samba_config,
            'cluster': self.cluster_info,
            'performance': self.performance_report,
            'fullreport': self.full_report,
            'custom': self.run_custom_command,
            'exit': self.exit_bot,
            'quit': self.exit_bot
        }
        
    def detect_os(self):
        """Detect operating system and version"""
        self.os_type = "unknown"
        self.os_version = "unknown"
        
        # Try to detect OS
        if os.path.exists("/etc/redhat-release"):
            self.os_type = "rhel"
            try:
                with open("/etc/redhat-release", "r") as f:
                    self.os_version = f.read().strip()
            except:
                pass
        elif os.path.exists("/etc/SuSE-release"):
            self.os_type = "suse"
            try:
                with open("/etc/SuSE-release", "r") as f:
                    self.os_version = f.read().strip()
            except:
                pass
        elif os.path.exists("/etc/os-release"):
            self.os_type = "debian"
            try:
                with open("/etc/os-release", "r") as f:
                    content = f.read()
                    if "Ubuntu" in content:
                        self.os_type = "ubuntu"
                    for line in content.split('\n'):
                        if line.startswith("PRETTY_NAME="):
                            self.os_version = line.split('=')[1].strip('"')
            except:
                pass
    
    def run_command(self, cmd):
        """Execute shell command and return output"""
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout if result.stdout else result.stderr
        except subprocess.TimeoutExpired:
            return "Command timed out after 30 seconds"
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    def show_help(self):
        """Display available commands"""
        help_text = """
╔════════════════════════════════════════════════════════════╗
║              HNM Bot - Available Commands                  ║
╚════════════════════════════════════════════════════════════╝

  help         - Show this help message
  disk         - Check disk usage and mounted filesystems
  memory       - Display memory usage statistics
  cpu          - Show CPU information and load
  processes    - List top processes by CPU/memory usage
  users        - Show logged in users and last logins
  services     - Check status of system services
  network      - Display network interfaces and connections
  logs         - View recent system logs
  uptime       - Show system uptime and load average
  ports        - List open ports and listening services
  firewall     - Check firewall status and rules
  updates      - Check for available system updates
  system       - Complete system information (hardware, hostname, ILO)
  lvm          - LVM, disk, iSCSI, and multipath information
  netconfig    - Network configuration (bonding, routes, iptables)
  userconfig   - User authentication (NIS, NTP, cron, sudoers)
  samba        - Samba, SSSD, Kerberos configuration
  cluster      - Cluster status (PCS, CRM, HPSG, Veritas)
  performance  - CPU/RAM utilization reports with SAR data
  fullreport   - Generate complete system report (all above)
  custom       - Run a custom Linux command
  exit/quit    - Exit the bot

"""
        return help_text
    
    def check_disk_usage(self):
        """Check disk usage"""
        output = "=== Disk Usage ===\n"
        output += self.run_command("df -h")
        output += "\n\n=== Inode Usage ===\n"
        output += self.run_command("df -i | head -n 10")
        return output
    
    def check_memory(self):
        """Check memory usage"""
        output = "=== Memory Usage ===\n"
        output += self.run_command("free -h")
        output += "\n\n=== Memory Details ===\n"
        output += self.run_command("cat /proc/meminfo | head -n 20")
        return output
    
    def check_cpu(self):
        """Check CPU information"""
        output = "=== CPU Information ===\n"
        output += self.run_command("lscpu | grep -E 'Model name|CPU\\(s\\)|Thread|Core|Socket'")
        output += "\n\n=== CPU Load (1, 5, 15 min) ===\n"
        output += self.run_command("uptime")
        output += "\n\n=== Top CPU Processes ===\n"
        output += self.run_command("ps aux --sort=-%cpu | head -n 11")
        return output
    
    def list_processes(self):
        """List top processes"""
        output = "=== Top Processes by CPU ===\n"
        output += self.run_command("ps aux --sort=-%cpu | head -n 11")
        output += "\n\n=== Top Processes by Memory ===\n"
        output += self.run_command("ps aux --sort=-%mem | head -n 11")
        return output
    
    def list_users(self):
        """List users"""
        output = "=== Currently Logged In Users ===\n"
        output += self.run_command("who")
        output += "\n\n=== Last Logins ===\n"
        output += self.run_command("last -n 10")
        output += "\n\n=== Failed Login Attempts ===\n"
        output += self.run_command("lastb -n 10 2>/dev/null || echo 'Permission denied or no failed logins'")
        return output
    
    def check_services(self):
        """Check system services"""
        output = "=== System Services ===\n"
        # systemd (RHEL 7+, Ubuntu 16.04+, SUSE 12+)
        systemctl_check = self.run_command("which systemctl 2>/dev/null")
        if systemctl_check.strip():
            output += "\n# Failed Services\n"
            output += self.run_command("systemctl --failed")
            output += "\n# Active Services (sample)\n"
            output += self.run_command("systemctl list-units --type=service --state=running | head -n 15")
        else:
            # SysV init (RHEL 6, older systems)
            output += "\n# Running Services (chkconfig)\n"
            output += self.run_command("chkconfig --list 2>/dev/null | grep ':on' | head -n 20 || service --status-all 2>/dev/null | grep running | head -n 20")
        return output
    
    def check_network(self):
        """Check network information"""
        output = "=== Network Interfaces ===\n"
        # Try ip command first (modern), fallback to ifconfig (older systems)
        output += self.run_command("ip addr show 2>/dev/null || ifconfig -a")
        output += "\n\n=== Routing Table ===\n"
        output += self.run_command("ip route 2>/dev/null || route -n")
        output += "\n\n=== Active Connections ===\n"
        # ss (modern), fallback to netstat (older systems)
        output += self.run_command("ss -tuln 2>/dev/null | head -n 20 || netstat -tuln | head -n 20")
        return output
    
    def check_logs(self):
        """Check system logs"""
        output = "=== Recent System Logs ===\n"
        # journalctl (systemd), fallback to /var/log/messages (older systems)
        journalctl_check = self.run_command("which journalctl 2>/dev/null")
        if journalctl_check.strip():
            output += self.run_command("journalctl -n 20 --no-pager")
            output += "\n\n=== Recent Errors ===\n"
            output += self.run_command("journalctl -p err -n 10 --no-pager")
        else:
            output += self.run_command("tail -n 20 /var/log/messages 2>/dev/null || tail -n 20 /var/log/syslog 2>/dev/null || echo 'Log files not accessible'")
            output += "\n\n=== Recent Errors ===\n"
            output += self.run_command("grep -i error /var/log/messages 2>/dev/null | tail -n 10 || grep -i error /var/log/syslog 2>/dev/null | tail -n 10 || echo 'No error logs found'")
        return output
    
    def check_uptime(self):
        """Check system uptime"""
        output = "=== System Uptime ===\n"
        output += self.run_command("uptime")
        output += "\n\n=== Boot Time ===\n"
        output += self.run_command("who -b")
        return output
    
    def check_ports(self):
        """Check open ports"""
        output = "=== Listening Ports ===\n"
        # ss (modern), fallback to netstat (older systems)
        output += self.run_command("ss -tuln 2>/dev/null || netstat -tuln")
        output += "\n\n=== Established Connections ===\n"
        output += self.run_command("ss -tun 2>/dev/null | grep ESTAB | head -n 20 || netstat -tun | grep ESTABLISHED | head -n 20")
        return output
    
    def check_firewall(self):
        """Check firewall status"""
        output = "=== Firewall Status ===\n"
        # Check UFW (Ubuntu)
        ufw_check = self.run_command("which ufw 2>/dev/null")
        if ufw_check.strip():
            output += "\n# UFW Status\n"
            output += self.run_command("ufw status 2>/dev/null || echo 'UFW not available'")
        
        # Check firewalld (RHEL 7+, SUSE 12+)
        firewalld_check = self.run_command("which firewall-cmd 2>/dev/null")
        if firewalld_check.strip():
            output += "\n# Firewalld Status\n"
            output += self.run_command("firewall-cmd --state 2>/dev/null || echo 'firewalld not running'")
        
        # Check SuSEfirewall2 (older SUSE)
        output += "\n# SuSEfirewall2 Status\n"
        output += self.run_command("rcSuSEfirewall2 status 2>/dev/null || echo 'SuSEfirewall2 not available'")
        
        # IPTables (all systems)
        output += "\n# IPTables Rules\n"
        output += self.run_command("iptables -L -n 2>/dev/null | head -n 30 || echo 'Permission denied - run with sudo'")
        return output
    
    def check_updates(self):
        """Check for system updates"""
        output = "=== Checking for Updates ===\n"
        # Detect package manager
        if os.path.exists("/usr/bin/apt") or os.path.exists("/usr/bin/apt-get"):
            # Ubuntu/Debian
            output += "\n# APT Updates\n"
            output += self.run_command("apt list --upgradable 2>/dev/null | head -n 20 || apt-get -s upgrade 2>/dev/null | grep '^Inst' | head -n 20")
        elif os.path.exists("/usr/bin/zypper"):
            # SUSE
            output += "\n# Zypper Updates\n"
            output += self.run_command("zypper list-updates 2>/dev/null | head -n 20")
        elif os.path.exists("/usr/bin/dnf"):
            # RHEL 8+, Fedora
            output += "\n# DNF Updates\n"
            output += self.run_command("dnf check-update 2>/dev/null | head -n 20")
        elif os.path.exists("/usr/bin/yum"):
            # RHEL 6/7
            output += "\n# YUM Updates\n"
            output += self.run_command("yum check-update 2>/dev/null | head -n 20")
        else:
            output += "Package manager not detected"
        return output
    
    def run_custom_command(self):
        """Run a custom command"""
        print("\n⚠️  Warning: Be careful with custom commands!")
        cmd = input("Enter command to execute: ").strip()
        if cmd:
            confirm = input(f"Execute '{cmd}'? (yes/no): ").strip().lower()
            if confirm == 'yes':
                return self.run_command(cmd)
            else:
                return "Command cancelled"
        return "No command entered"
    
    def system_info(self):
        """Complete system information"""
        output = "=== System Information ===\n"
        output += "\n# uname -a\n"
        output += self.run_command("uname -a")
        output += "\n# Server uptime\n"
        output += self.run_command("uptime")
        output += "\n# hostname\n"
        output += self.run_command("hostname")
        output += "\n# hostname -i\n"
        output += self.run_command("hostname -i")
        output += "\n# cat /etc/redhat-release\n"
        output += self.run_command("cat /etc/redhat-release 2>/dev/null || cat /etc/os-release")
        output += "\n# Hardware Info\n"
        output += self.run_command("dmidecode -t 1 2>/dev/null || echo 'Permission denied - run with sudo'")
        output += "\n# hponcfg -w /tmp/ilo.out\n"
        output += self.run_command("hponcfg -w /tmp/ilo.out 2>/dev/null || echo 'hponcfg not available'")
        output += "\n# IPMI Tool\n"
        output += self.run_command("ipmitool lan print 2>/dev/null || echo 'ipmitool not available'")
        output += "\n# cat /etc/resolv.conf\n"
        output += self.run_command("cat /etc/resolv.conf")
        output += "\n# cat /etc/hosts\n"
        output += self.run_command("cat /etc/hosts")
        return output
    
    def lvm_info(self):
        """LVM and storage information"""
        output = "=== LVM & Storage Information ===\n"
        output += "\n# lsblk\n"
        output += self.run_command("lsblk")
        output += "\n# df -hT\n"
        output += self.run_command("df -hT")
        output += "\n# cat /etc/fstab\n"
        output += self.run_command("cat /etc/fstab")
        output += "\n# pvs\n"
        output += self.run_command("pvs 2>/dev/null || echo 'No LVM physical volumes or permission denied'")
        output += "\n# vgs\n"
        output += self.run_command("vgs 2>/dev/null || echo 'No LVM volume groups or permission denied'")
        output += "\n# lvs\n"
        output += self.run_command("lvs 2>/dev/null || echo 'No LVM logical volumes or permission denied'")
        output += "\n# cat /etc/iscsi/initiatorname.iscsi\n"
        output += self.run_command("cat /etc/iscsi/initiatorname.iscsi 2>/dev/null || echo 'iSCSI not configured'")
        output += "\n# iscsiadm -m session\n"
        output += self.run_command("iscsiadm -m session 2>/dev/null || echo 'No iSCSI sessions'")
        output += "\n# sanlun lun show\n"
        output += self.run_command("sanlun lun show 2>/dev/null || echo 'sanlun not available'")
        output += "\n# multipath -ll\n"
        output += self.run_command("multipath -ll 2>/dev/null || echo 'multipath not configured'")
        return output
    
    def network_config(self):
        """Network configuration details"""
        output = "=== Network Configuration ===\n"
        output += "\n# Network Interfaces\n"
        output += self.run_command("ifconfig -a 2>/dev/null || ip addr show")
        output += "\n# Routing Table\n"
        output += self.run_command("route -n 2>/dev/null || ip route")
        
        # Bonding info
        output += "\n# Bonding Status\n"
        output += self.run_command("cat /proc/net/bonding/bond0 2>/dev/null || echo 'bond0 not configured'")
        output += self.run_command("cat /proc/net/bonding/bond1 2>/dev/null || echo 'bond1 not configured'")
        
        # Network config files - RHEL/CentOS style
        if os.path.exists("/etc/sysconfig/network-scripts"):
            output += "\n# Network Scripts (RHEL/CentOS)\n"
            output += self.run_command("cat /etc/sysconfig/network-scripts/ifcfg-bond0 2>/dev/null || echo 'bond0 config not found'")
            output += self.run_command("cat /etc/sysconfig/network-scripts/ifcfg-bond1 2>/dev/null || echo 'bond1 config not found'")
            output += self.run_command("cat /etc/sysconfig/network 2>/dev/null || echo 'File not found'")
        
        # Network config files - SUSE style
        if os.path.exists("/etc/sysconfig/network"):
            output += "\n# Network Config (SUSE)\n"
            output += self.run_command("cat /etc/sysconfig/network/ifcfg-bond0 2>/dev/null || echo 'bond0 config not found'")
            output += self.run_command("cat /etc/sysconfig/network/config 2>/dev/null || echo 'File not found'")
        
        # Network config files - Ubuntu/Debian style
        if os.path.exists("/etc/network/interfaces"):
            output += "\n# Network Interfaces (Ubuntu/Debian)\n"
            output += self.run_command("cat /etc/network/interfaces 2>/dev/null || echo 'File not found'")
        
        # Netplan (Ubuntu 18.04+)
        if os.path.exists("/etc/netplan"):
            output += "\n# Netplan Config (Ubuntu 18.04+)\n"
            output += self.run_command("cat /etc/netplan/*.yaml 2>/dev/null || echo 'No netplan config found'")
        
        output += "\n# IPTables Mangle Rules\n"
        output += self.run_command("iptables -t mangle -nvL 2>/dev/null || echo 'Permission denied - run with sudo'")
        return output
    
    def user_config(self):
        """User and authentication configuration"""
        output = "=== User & Authentication Configuration ===\n"
        output += "\n# cat /etc/passwd\n"
        output += self.run_command("cat /etc/passwd")
        output += "\n# cat /etc/shadow\n"
        output += self.run_command("cat /etc/shadow 2>/dev/null || echo 'Permission denied - run with sudo'")
        output += "\n# cat /etc/sudoers\n"
        output += self.run_command("cat /etc/sudoers 2>/dev/null | grep -v '#' || echo 'Permission denied'")
        output += "\n# User Authentication - NIS\n"
        output += self.run_command("nisdomainname 2>/dev/null || echo 'NIS not configured'")
        output += "\n# NIS config\n"
        output += self.run_command("cat /etc/yp.conf 2>/dev/null || echo 'NIS not configured'")
        output += "\n# ntpq -p\n"
        output += self.run_command("ntpq -p 2>/dev/null || echo 'NTP not running'")
        output += "\n# cat /etc/ntp.conf\n"
        output += self.run_command("cat /etc/ntp.conf 2>/dev/null | grep -v '#' || echo 'NTP not configured'")
        output += "\n# cat /etc/chrony.conf\n"
        output += self.run_command("cat /etc/chrony.conf 2>/dev/null | grep -v '#' || echo 'Chrony not configured'")
        output += "\n# crontab -l\n"
        output += self.run_command("crontab -l 2>/dev/null || echo 'No crontab for current user'")
        return output
    
    def samba_config(self):
        """Samba and domain configuration"""
        output = "=== Samba & Domain Configuration ===\n"
        output += "\n# /etc/sssd/sssd.conf\n"
        output += self.run_command("cat /etc/sssd/sssd.conf 2>/dev/null | grep -v '#' || echo 'SSSD not configured'")
        output += "\n# Kerberos Config\n"
        output += self.run_command("cat /etc/krb5.conf 2>/dev/null || echo 'Kerberos not configured'")
        output += "\n# Samba config\n"
        output += self.run_command("cat /etc/samba/smb.conf 2>/dev/null | grep -v '#' || echo 'Samba not configured'")
        output += "\n# nsswitch config\n"
        output += self.run_command("cat /etc/nsswitch.conf 2>/dev/null | grep -v '#' || echo 'File not found'")
        return output
    
    def cluster_info(self):
        """Cluster status information"""
        output = "=== Cluster Information ===\n"
        output += "\n# PCS Cluster\n"
        output += self.run_command("pcs status 2>/dev/null || echo 'PCS cluster not configured'")
        output += "\n# CRM Cluster\n"
        output += self.run_command("crm status 2>/dev/null || echo 'CRM cluster not configured'")
        output += "\n# HPSG Cluster\n"
        output += self.run_command("cmviewcl -v 2>/dev/null || echo 'HPSG cluster not configured'")
        output += "\n# Veritas Cluster\n"
        output += self.run_command("hastatus -summary 2>/dev/null || echo 'Veritas cluster not configured'")
        return output
    
    def performance_report(self):
        """CPU and RAM utilization reports"""
        output = "=== Performance Reports ===\n"
        output += "\n# RAM Utilization (Current)\n"
        output += self.run_command("free -g 2>/dev/null || free -m")
        output += "\n# CPU Information\n"
        output += self.run_command("lscpu 2>/dev/null || cat /proc/cpuinfo | grep -E 'processor|model name|cpu MHz' | head -n 20")
        
        # Check if SAR is available
        sar_check = self.run_command("which sar 2>/dev/null")
        if sar_check.strip():
            output += "\n# RAM Utilization (last 2 hours - SAR)\n"
            output += self.run_command("sar -r -s $(date --date='2 hours ago' +%T 2>/dev/null) -e $(date +%T) 2>/dev/null || sar -r | tail -n 20")
            output += "\n# CPU Utilization (last 2 hours - SAR)\n"
            output += self.run_command("sar -u -s $(date --date='2 hours ago' +%T 2>/dev/null) -e $(date +%T) 2>/dev/null || sar -u | tail -n 20")
        else:
            output += "\n# SAR not available - Install sysstat package for historical data\n"
            output += "\n# Current CPU Usage (top snapshot)\n"
            output += self.run_command("top -bn1 | head -n 20")
        
        return output
    
    def full_report(self):
        """Generate complete system report"""
        print("\n🔍 Generating full system report... This may take a moment.\n")
        output = "╔════════════════════════════════════════════════════════════╗\n"
        output += "║              COMPLETE SYSTEM REPORT - HNM BOT              ║\n"
        output += "╚════════════════════════════════════════════════════════════╝\n"
        output += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        output += "=" * 60 + "\n\n"
        
        output += self.system_info() + "\n\n"
        output += "=" * 60 + "\n\n"
        output += self.lvm_info() + "\n\n"
        output += "=" * 60 + "\n\n"
        output += self.network_config() + "\n\n"
        output += "=" * 60 + "\n\n"
        output += self.user_config() + "\n\n"
        output += "=" * 60 + "\n\n"
        output += self.samba_config() + "\n\n"
        output += "=" * 60 + "\n\n"
        output += self.cluster_info() + "\n\n"
        output += "=" * 60 + "\n\n"
        output += self.performance_report() + "\n\n"
        
        # Save to file
        filename = f"system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(output)
            output += f"\n✓ Report saved to: {filename}\n"
        except Exception as e:
            output += f"\n⚠️  Could not save report to file: {str(e)}\n"
        
        return output
    
    def exit_bot(self):
        """Exit the bot"""
        print("\n👋 Goodbye! Stay secure!")
        sys.exit(0)
    
    def start(self):
        """Start the chatbot"""
        print("╔════════════════════════════════════════════════════════════╗")
        print("║           🐧 HNM Bot - Your CLI Assistant 🐧              ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print("Built by: Harihar Mishra | harihar.mishra@hcltech.com")
        print(f"Detected OS: {self.os_version if self.os_version != 'unknown' else self.os_type}")
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Compatible: RHEL 6+, Ubuntu 16.04+, SUSE 11+")
        print("Type 'help' for available commands or 'exit' to quit\n")
        
        while True:
            try:
                user_input = input("🐧 hnm-bot> ").strip().lower()
                
                if not user_input:
                    continue
                
                if user_input in self.commands:
                    result = self.commands[user_input]()
                    if result:
                        print(f"\n{result}\n")
                else:
                    print(f"\n❌ Unknown command: '{user_input}'")
                    print("Type 'help' to see available commands\n")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")

if __name__ == "__main__":
    bot = Hnm_Linux_Bot()
    bot.start()
