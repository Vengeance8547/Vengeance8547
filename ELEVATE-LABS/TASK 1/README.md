**-- TASK 1 --**

**Objective:** The main goal of the task is to identify the local IP address and scan the network to identify devices on the network and open ports of devices on the network.

**Requirements:** Linux OS (as Nmap is already installed) and Wireshark (optional).

**Summary:**
1. A Linux operating system was used since Nmap is already installed.

2. To identify the local IP address, you can use commands like "ip a" or "ifconfig."

3. After identifying the local address (usually in the format 192.168.1.0-254/24), we can find out which devices are active on the network using the command "nmap -sS 192.168.1.0/24." This command performs a SYN scan, sending SYN packets to identify open ports on the network without connecting to the systems.

4. Wireshark was utilized to analyze the various types of protocols present. The most common protocols observed were TCP, TLSv1.2, ARP, and IGMPv3.

5. The most common services running on the ports include:
   - Port 21: FTP
   - Port 22: SSH
   - Port 23: Telnet
   - Port 80: HTTP
   - Port 443: HTTPS, among others.

6. There are potential security risks associated with open ports, as attackers can gain unauthorized access through:
   - Misconfigured services.
   - Outdated or unpatched software.
   - Known vulnerabilities and exploits.

