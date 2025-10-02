#!/usr/bin/env python3
import psutil
import datetime

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
LOG_FILE = "system_health.log"

def log_alert(message):
    """Log alert to console and file"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert = f"[{timestamp}] ALERT: {message}"
    print(alert)
    with open(LOG_FILE, "a") as f:
        f.write(alert + "\n")

def check_cpu():
    """Check CPU usage"""
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")
    if cpu_percent > CPU_THRESHOLD:
        log_alert(f"CPU usage is high: {cpu_percent}%")
    return cpu_percent

def check_memory():
    """Check memory usage"""
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    print(f"Memory Usage: {memory_percent}%")
    if memory_percent > MEMORY_THRESHOLD:
        log_alert(f"Memory usage is high: {memory_percent}%")
    return memory_percent

def check_disk():
    """Check disk space"""
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    print(f"Disk Usage: {disk_percent}%")
    if disk_percent > DISK_THRESHOLD:
        log_alert(f"Disk usage is high: {disk_percent}%")
    return disk_percent

def check_processes():
    """Check running processes"""
    processes = len(psutil.pids())
    print(f"Running Processes: {processes}")
    return processes

def main():
    print("=" * 50)
    print("System Health Monitoring")
    print("=" * 50)
    
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()
    
    print("=" * 50)
    
    if cpu < CPU_THRESHOLD and memory < MEMORY_THRESHOLD and disk < DISK_THRESHOLD:
        print("✓ All systems normal")
    else:
        print("⚠ Issues detected - check log file")

if __name__ == "__main__":
    main()
