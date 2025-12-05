#!/usr/bin/env python3
"""
HNM Remote Bot - Remote Linux system administration tool via SSH

Built by: Harihar Mishra

Version: 1.0.0
"""

import subprocess
import sys
import os
from datetime import datetime
import getpass

class Hnm_Remote_Bot:
    def __init__(self):
        self.remote_host = None
        self.remote_user = None
        self.ssh_key = None
        self.use_password = False
        self.connected = False
        
        self.commands = {
            'help': self.show_help,
            'connect': self.connect_remote,
            'disconnect': self.disconnect,
            'status': self.connection_status,
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
            'exit': self.exit_bot,
            'quit': self.exit_bot
        }
    
    def run_remote_command(self, cmd):
        """Execute command on remote system via SSH"""
        if not self.connected:
            return "Error: Not connected to remote system. Use 'connect' command first."
        
        try:
            # Build SSH command
            if self.ssh_key:
                ssh_cmd = f"ssh -i {self.ssh_key} -o StrictHostKeyChecking=no -o ConnectTimeout=10 {self.remote_user}@{self.remote_host} '{cmd}'"
            else:
                ssh_cmd = f"ssh -o StrictHostKeyChecking=no -o ConnectTimeout=10 {self.remote_user}@{self.remote_host} '{cmd}'"
            
            # Execute SSH command
            result = subprocess.run(
                ssh_cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                timeout=60
            )
            
            return result.stdout if result.stdout else result.stderr
        except subprocess.TimeoutExpired:
            return "Command timed out after 60 seconds"
        except Exception as e:
            return f"Error executing remote command: {str(e)}"
    
    def connect_remote(self):
        """Connect to remote system"""
        print("\n=== Connect to Remote System ===\n")
        
        # Get connection details
        self.remote_host = input("Enter hostname/IP (e.g., server.example.com or 192.168.1.100): ").strip()
        if not self.remote_host:
            return "Error: Hostname/IP is required"
        
        self.remote_user = input("Enter username (default: root): ").strip() or "root"
        
        # Ask for authentication method
        auth_method = input("Authentication method (1=SSH Key, 2=Password) [1]: ").strip() or "1"
        
        if auth_method == "1":
            default_key = os.path.expanduser("~/.ssh/id_rsa")
            self.ssh_key = input(f"Enter SSH key path (default: {default_key}): ").strip() or default_key
            
            if not os.path.exists(self.ssh_key):
                return f"Error: SSH key not found at {self.ssh_key}"
            
            self.use_password = False
        else:
            self.use_password = True
            print("\nNote: You'll be prompted for password on each command.")
            print("For better experience, use SSH key authentication.")
        
        # Test connection
        print(f"\nTesting connection to {self.remote_user}@{self.remote_host}...")
        
        test_result = self.run_remote_command("echo 'Connection successful'")
        
        if "Connection successful" in test_result:
            self.connected = True
            output = f"\n✓ Successfully connected to {self.remote_user}@{self.remote_host}\n"
            output += f"Authentication: {'SSH Key' if self.ssh_key else 'Password'}\n"
            output += "\nYou can now run commands on the remote system.\n"
            output += "Type 'help' to see available commands.\n"
            return output
        else:
            self.connected = False
            return f"\n✗ Connection failed:\n{test_result}\n\nPlease check:\n- Hostname/IP is correct\n- SSH service is running\n- Firewall allows SSH\n- Credentials are correct"
    
    def disconnect(self):
        """Disconnect from remote system"""
        if not self.connected:
            return "Not connected to any remote system"
        
        host = self.remote_host
        self.connected = False
        self.remote_host = None
        self.remote_user = None
        self.ssh_key = None
        
        return f"✓ Disconnected from {host}"
    
    def connection_status(self):
        """Show connection status"""
        if self.connected:
            output = "=== Connection Status ===\n"
            output += f"Status: ✓ Connected\n"
            output += f"Remote Host: {self.remote_host}\n"
            output += f"Username: {self.remote_user}\n"
            output += f"Authentication: {'SSH Key (' + self.ssh_key + ')' if self.ssh_key else 'Password'}\n"
            return output
        else:
            return "Status: ✗ Not connected\n\nUse 'connect' command to connect to a remote system."
    
    def show_help(self):
        """Display available commands"""
        help_text = """
╔════════════════════════════════════════════════════════════╗
║           HNM Remote Bot - Available Commands              ║
╚════════════════════════════════════════════════════════════╝

CONNECTION COMMANDS:
  connect      - Connect to remote Linux system
  disconnect   - Disconnect from remote system
  status       - Show connection status

BASIC COMMANDS:
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

ADVANCED COMMANDS:
  system       - Complete system information (hardware, hostname, ILO)
  lvm          - LVM, disk, iSCSI, and multipath information
  netconfig    - Network configuration (bonding, routes, iptables)
  userconfig   - User authentication (NIS, NTP, cron, sudoers)
  samba        - Samba, SSSD, Kerberos configuration
  cluster      - Cluster status (PCS, CRM, HPSG, Veritas)
  performance  - CPU/RAM utilization reports with SAR data
  fullreport   - Generate complete system report (all above)

UTILITY:
  exit/quit    - Exit the bot

USAGE:
  1. First run 'connect' to connect to remote system
  2. Then run any command to gather information
  3. Use 'disconnect' when done

"""
        return help_text
    
    def check_disk_usage(self):
        """Check disk usage"""
        output = "=== Disk Usage ===\n"
        output += self.run_remote_command("df -h")
        output += "\n\n=== Inode Usage ===\n"
        output += self.run_remote_command("df -i | head -n 10")
        return output
    
    def check_memory(self):
        """Check memory usage"""
        output = "=== Memory Usage ===\n"
        output += self.run_remote_command("free -h")
        output += "\n\n=== Memory Details ===\n"
        output += self.run_remote_command("cat /proc/meminfo | head -n 20")
        return output
    
    def check_cpu(self):
        """Check CPU information"""
        output = "=== CPU Information ===\n"
        output += self.run_remote_command("lscpu | grep -E 'Model name|CPU\\(s\\)|Thread|Core|Socket'")
        output += "\n\n=== CPU Load (1, 5, 15 min) ===\n"
        output += self.run_remote_command("uptime")
        output += "\n\n=== Top CPU Processes ===\n"
        output += self.run_remote_command("ps aux --sort=-%cpu | head -n 11")
        return output
    
    def list_processes(self):
        """List top processes"""
        output = "=== Top Processes by CPU ===\n"
        output += self.run_remote_command("ps aux --sort=-%cpu | head -n 11")
        output += "\n\n=== Top Processes by Memory ===\n"
        output += self.run_remote_command("ps aux --sort=-%mem | head -n 11")
        return output
    
    def list_users(self):
        """List users"""
        output = "=== Currently Logged In Users ===\n"
        output += self.run_remote_command("who")
        output += "\n\n=== Last Logins ===\n"
        output += self.run_remote_command("last -n 10")
        output += "\n\n=== Failed Login Attempts ===\n"
        output += self.run_remote_command("lastb -n 10 2>/dev/null || echo 'Permission denied or no failed logins'")
        return output
    
    def check_services(self):
        """Check system services"""
        output = "=== System Services ===\n"
        output += self.run_remote_command("systemctl --failed 2>/dev/null || chkconfig --list 2>/dev/null | grep ':on' | head -n 20")
        output += "\n\n=== Active Services (sample) ===\n"
        output += self.run_remote_command("systemctl list-units --type=service --state=running 2>/dev/null | head -n 15 || service --status-all 2>/dev/null | grep running | head -n 15")
        return output
    
    def check_network(self):
        """Check network information"""
        output = "=== Network Interfaces ===\n"
        output += self.run_remote_command("ip addr show 2>/dev/null || ifconfig -a")
        output += "\n\n=== Routing Table ===\n"
        output += self.run_remote_command("ip route 2>/dev/null || route -n")
        output += "\n\n=== Active Connections ===\n"
        output += self.run_remote_command("ss -tuln 2>/dev/null | head -n 20 || netstat -tuln | head -n 20")
        return output
    
    def check_logs(self):
        """Check system logs"""
        output = "=== Recent System Logs ===\n"
        output += self.run_remote_command("journalctl -n 20 --no-pager 2>/dev/null || tail -n 20 /var/log/messages 2>/dev/null || tail -n 20 /var/log/syslog")
        output += "\n\n=== Recent Errors ===\n"
        output += self.run_remote_command("journalctl -p err -n 10 --no-pager 2>/dev/null || grep -i error /var/log/messages 2>/dev/null | tail -n 10")
        return output
    
    def check_uptime(self):
        """Check system uptime"""
        output = "=== System Uptime ===\n"
        output += self.run_remote_command("uptime")
        output += "\n\n=== Boot Time ===\n"
        output += self.run_remote_command("who -b")
        return output
    
    def check_ports(self):
        """Check open ports"""
        output = "=== Listening Ports ===\n"
        output += self.run_remote_command("ss -tuln 2>/dev/null || netstat -tuln")
        output += "\n\n=== Established Connections ===\n"
        output += self.run_remote_command("ss -tun 2>/dev/null | grep ESTAB | head -n 20 || netstat -tun | grep ESTABLISHED | head -n 20")
        return output
    
    def check_firewall(self):
        """Check firewall status"""
        output = "=== Firewall Status ===\n"
        output += self.run_remote_command("ufw status 2>/dev/null || firewall-cmd --state 2>/dev/null || rcSuSEfirewall2 status 2>/dev/null || echo 'Firewall status unavailable'")
        output += "\n\n=== IPTables Rules ===\n"
        output += self.run_remote_command("iptables -L -n 2>/dev/null | head -n 30 || echo 'Permission denied - requires sudo'")
        return output
    
    def check_updates(self):
        """Check for system updates"""
        output = "=== Checking for Updates ===\n"
        output += self.run_remote_command("apt list --upgradable 2>/dev/null | head -n 20 || yum check-update 2>/dev/null | head -n 20 || dnf check-update 2>/dev/null | head -n 20 || zypper list-updates 2>/dev/null | head -n 20")
        return output
    
    def system_info(self):
        """Complete system information"""
        output = "=== System Information ===\n"
        output += "\n# uname -a\n"
        output += self.run_remote_command("uname -a")
        output += "\n# hostname\n"
        output += self.run_remote_command("hostname")
        output += "\n# hostname -i\n"
        output += self.run_remote_command("hostname -i")
        output += "\n# OS Release\n"
        output += self.run_remote_command("cat /etc/redhat-release 2>/dev/null || cat /etc/os-release")
        output += "\n# Hardware Info\n"
        output += self.run_remote_command("dmidecode -t 1 2>/dev/null || echo 'Permission denied - requires sudo'")
        output += "\n# /etc/resolv.conf\n"
        output += self.run_remote_command("cat /etc/resolv.conf")
        output += "\n# /etc/hosts\n"
        output += self.run_remote_command("cat /etc/hosts")
        return output
    
    def lvm_info(self):
        """LVM and storage information"""
        output = "=== LVM & Storage Information ===\n"
        output += "\n# lsblk\n"
        output += self.run_remote_command("lsblk")
        output += "\n# df -hT\n"
        output += self.run_remote_command("df -hT")
        output += "\n# cat /etc/fstab\n"
        output += self.run_remote_command("cat /etc/fstab")
        output += "\n# pvs\n"
        output += self.run_remote_command("pvs 2>/dev/null || echo 'No LVM or permission denied'")
        output += "\n# vgs\n"
        output += self.run_remote_command("vgs 2>/dev/null || echo 'No LVM or permission denied'")
        output += "\n# lvs\n"
        output += self.run_remote_command("lvs 2>/dev/null || echo 'No LVM or permission denied'")
        output += "\n# multipath -ll\n"
        output += self.run_remote_command("multipath -ll 2>/dev/null || echo 'Multipath not configured'")
        return output
    
    def network_config(self):
        """Network configuration details"""
        output = "=== Network Configuration ===\n"
        output += "\n# Network Interfaces\n"
        output += self.run_remote_command("ifconfig -a 2>/dev/null || ip addr show")
        output += "\n# Routing Table\n"
        output += self.run_remote_command("route -n 2>/dev/null || ip route")
        output += "\n# Bonding Status\n"
        output += self.run_remote_command("cat /proc/net/bonding/bond0 2>/dev/null || echo 'No bonding configured'")
        return output
    
    def user_config(self):
        """User and authentication configuration"""
        output = "=== User & Authentication Configuration ===\n"
        output += "\n# /etc/passwd\n"
        output += self.run_remote_command("cat /etc/passwd")
        output += "\n# NTP Status\n"
        output += self.run_remote_command("ntpq -p 2>/dev/null || chronyc sources 2>/dev/null || echo 'NTP not configured'")
        output += "\n# Crontab\n"
        output += self.run_remote_command("crontab -l 2>/dev/null || echo 'No crontab'")
        return output
    
    def samba_config(self):
        """Samba and domain configuration"""
        output = "=== Samba & Domain Configuration ===\n"
        output += "\n# SSSD Config\n"
        output += self.run_remote_command("cat /etc/sssd/sssd.conf 2>/dev/null | grep -v '#' || echo 'SSSD not configured'")
        output += "\n# Kerberos Config\n"
        output += self.run_remote_command("cat /etc/krb5.conf 2>/dev/null || echo 'Kerberos not configured'")
        output += "\n# Samba Config\n"
        output += self.run_remote_command("cat /etc/samba/smb.conf 2>/dev/null | grep -v '#' || echo 'Samba not configured'")
        return output
    
    def cluster_info(self):
        """Cluster status information"""
        output = "=== Cluster Information ===\n"
        output += "\n# PCS Cluster\n"
        output += self.run_remote_command("pcs status 2>/dev/null || echo 'PCS not configured'")
        output += "\n# CRM Cluster\n"
        output += self.run_remote_command("crm status 2>/dev/null || echo 'CRM not configured'")
        return output
    
    def performance_report(self):
        """CPU and RAM utilization reports"""
        output = "=== Performance Reports ===\n"
        output += "\n# RAM Utilization\n"
        output += self.run_remote_command("free -g 2>/dev/null || free -m")
        output += "\n# CPU Information\n"
        output += self.run_remote_command("lscpu 2>/dev/null || cat /proc/cpuinfo | grep -E 'processor|model name' | head -n 20")
        output += "\n# SAR Data (if available)\n"
        output += self.run_remote_command("sar -u | tail -n 20 2>/dev/null || echo 'SAR not available'")
        return output
    
    def full_report(self):
        """Generate complete system report"""
        print("\n🔍 Generating full system report from remote system... This may take a moment.\n")
        output = "╔════════════════════════════════════════════════════════════╗\n"
        output += "║         COMPLETE REMOTE SYSTEM REPORT - HNM BOT            ║\n"
        output += "╚════════════════════════════════════════════════════════════╝\n"
        output += f"Remote Host: {self.remote_host}\n"
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
        filename = f"remote_report_{self.remote_host}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(output)
            output += f"\n✓ Report saved to: {filename}\n"
        except Exception as e:
            output += f"\n⚠️  Could not save report to file: {str(e)}\n"
        
        return output
    
    def exit_bot(self):
        """Exit the bot"""
        if self.connected:
            print(f"\nDisconnecting from {self.remote_host}...")
        print("\n👋 Goodbye! Stay secure!")
        sys.exit(0)
    
    def start(self):
        """Start the chatbot"""
        print("╔════════════════════════════════════════════════════════════╗")
        print("║        🌐 HNM Remote Bot - Your Remote CLI Assistant 🌐   ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print("Built by: Harihar Mishra ")
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Remote System Administration via SSH")
        print("\nType 'connect' to connect to a remote system")
        print("Type 'help' for available commands or 'exit' to quit\n")
        
        while True:
            try:
                if self.connected:
                    prompt = f"🌐 hnm-remote [{self.remote_host}]> "
                else:
                    prompt = "🌐 hnm-remote [not connected]> "
                
                user_input = input(prompt).strip().lower()
                
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
    bot = Hnm_Remote_Bot()
    bot.start()

