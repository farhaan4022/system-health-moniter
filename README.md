# System Health Monitor

## Overview

This repository contains a Python script designed to monitor the health of a Linux system. The script checks key system metrics including CPU usage, memory usage, disk space, and the number of running processes. It logs warnings if any metrics exceed predefined thresholds.

## Features

- **CPU Usage Monitoring**: Alerts when CPU usage exceeds 80%.
- **Memory Usage Monitoring**: Alerts when memory usage exceeds 80%.
- **Disk Space Monitoring**: Alerts when disk space usage exceeds 80%.
- **Process Monitoring**: Logs the total number of running processes.

## Prerequisites

- **Python 3.x**: Ensure Python 3 is installed on your system.
- **psutil**: A Python library for system and process utilities.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/system-health-monitor.git
   cd system-health-monitor
