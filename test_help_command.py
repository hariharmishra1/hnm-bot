#!/usr/bin/env python3
"""Test the help command interactively"""

import hnm_linux_bot

print("="*70)
print("Testing HNM Bot - Help Command")
print("="*70)
print("\nStarting bot and executing 'help' command...\n")

# Create bot instance
bot = hnm_linux_bot.Hnm_Linux_Bot()

# Display bot info
print(f"Bot Class: {bot.__class__.__name__}")
print(f"OS Detected: {bot.os_type}")
print(f"Total Commands: {len(bot.commands)}")

print("\n" + "="*70)
print("Executing: help")
print("="*70)

# Execute help command
help_output = bot.show_help()
print(help_output)

print("="*70)
print("Help Command Test Complete")
print("="*70)
print("\n✓ Help command executed successfully!")
print(f"✓ Output length: {len(help_output)} characters")
lines_with_commands = [line for line in help_output.split('\n') if '-' in line]
print(f"✓ Command lines found: {len(lines_with_commands)}")
