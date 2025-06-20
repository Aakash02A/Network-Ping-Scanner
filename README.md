# 🛰️ Basic Network Ping Scanner using Python

This is a beginner-friendly Python project that scans a range of IP addresses and checks which devices are "alive" using the `ping` command.

## 🚀 What it does

- Accepts a network range like `192.168.1.0/24`
- Pings the first 10 IP addresses
- Prints whether each device is online or offline

## 🧰 Tools Used

- Python `os` and `platform` modules
- `ipaddress` for handling subnets
- Works cross-platform (Windows/Linux)

## 🧠 What You Learn

- Basic networking concepts (IP, ICMP, ping)
- How devices are discovered on local networks
- Simple scripting for network tasks

## 🔧 How to Run

1. Open terminal / command prompt
2. Replace the subnet in the script with your real one (use `ipconfig` or `ifconfig`)
3. Run the script:
   ```bash
   python ping_scanner.py
