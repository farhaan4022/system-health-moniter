#!/home/farhaan/myenv/bin/python

import psutil
import logging

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")
        print(f"CPU usage is normal: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_info.percent}%")
        print(f"High Memory usage detected: {memory_info.percent}%")
    else:
        logging.info(f"Memory usage is normal: {memory_info.percent}%")
        print(f"Memory usage is normal: {memory_info.percent}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f"Low Disk space available: {disk_info.percent}% used")
        print(f"Low Disk space available: {disk_info.percent}% used")
    else:
        logging.info(f"Disk space usage is normal: {disk_info.percent}% used")
        print(f"Disk space usage is normal: {disk_info.percent}% used")

def check_running_processes():
    processes = psutil.pids()
    logging.info(f"Number of running processes: {len(processes)}")
    print(f"Number of running processes: {len(processes)}")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
