"""
System Health Check Script

Checks disk usage and memory usage on a Linux system by running
shell commands (df, free) and parsing their output with regex.
"""

import subprocess
import re


def check_disk():
    result = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
    return result.stdout


def check_memory():
    result = subprocess.run(["free", "-h"], capture_output=True, text=True)
    return result.stdout


disk_output = check_disk()
disk_match = re.search(r"(\d+)%", disk_output)
disk_percent = int(disk_match.group(1))
print(f"Disk usage is {disk_percent}%")

memory_output = check_memory()
# free -h prints multiple similar numbers (total, used, free) on one line,
# so anchor on "Mem:" and skip the first match to specifically capture "used"
memory_match = re.search(r"Mem:\s+\d+\.?\d*Gi\s+(\d+\.?\d*)Gi", memory_output)
memory_used = float(memory_match.group(1))
print(f"Current RAM used is {memory_used}Gi")
