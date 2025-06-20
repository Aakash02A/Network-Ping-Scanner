import os
import platform
import ipaddress

# Ping a host
def ping_host(ip):
    print(f"Pinging {ip}...")
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = f"ping {param} 1 {ip} >nul"
    response = os.system(command)
    return response == 0

# Scan first 10 IPs in the subnet
def scan_network(network_cidr):
    network = ipaddress.ip_network(network_cidr, strict=False)
    print(f"\nScanning network: {network}\n")

    ip_list = list(network.hosts())[:10]  # first 10 IPs only
    for ip in ip_list:
        if ping_host(str(ip)):
            print(f"[+] {ip} is alive")
        else:
            print(f"[-] {ip} is down")

# Replace with your actual network, e.g., "192.168.159.0/24"
scan_network("192.168.159.0/24")
