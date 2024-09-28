#!/usr/bin/env python3

"""
Author: Deekshith
Date: 12-08-2024

This script checks the node health.

Version: v1
"""

import os
import subprocess
import psutil

def get_disk_usage():
    """Prints disk usage in human-readable format (similar to df -h)"""
    print("Disk Usage:")
    subprocess.run(["df", "-h"])

def get_memory_usage():
    """Prints memory usage in gigabytes (similar to free -g)"""
    memory_info = psutil.virtual_memory()
    print(f"\nMemory Usage (GB):\nTotal: {memory_info.total // (1024 ** 3)} GB\n"
          f"Available: {memory_info.available // (1024 ** 3)} GB\n"
          f"Used: {memory_info.used // (1024 ** 3)} GB\n"
          f"Free: {memory_info.free // (1024 ** 3)} GB")

def get_cpu_cores():
    """Prints the number of CPU cores (similar to nproc)"""
    print(f"\nNumber of CPU cores: {os.cpu_count()}")

def get_amazon_processes():
    """Prints the process IDs of processes containing 'amazon' in their command"""
    print("\nAmazon processes (PIDs):")
    result = subprocess.run(["ps", "-ef"], capture_output=True, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if "amazon" in line:
            # Split the line by space and extract the PID (second column)
            pid = line.split()[1]
            print(pid)

if __name__ == "__main__":
    # Set debug and error handling options
    try:
        get_disk_usage()
        get_memory_usage()
        get_cpu_cores()
        get_amazon_processes()
    except Exception as e:
        print(f"An error occurred: {e}")
