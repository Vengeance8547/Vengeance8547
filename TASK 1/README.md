-- TASK 1 --

Objective: The main goal of the task is to identify the local IP address and scan the network to identify devices on the network and open ports of devices on the network.

Requirements : Linux OS (as Nmap is already installed) and Wireshark (optional).

Summary:
1. Used Linux OS as Nmap is already installed.

2. To identify the local IP address, you can use commands like "ip a," ifconfig, etc.

3. After identifying the local address. (Usually it is 192.168.1.0-254/24.)
   - We are going to identify what all devices are up on the network using the command "nmap -sS 192.168.1.0/24".
   - It is a SYN scan, as it sends SYN packets to identify the open ports on the network. (not to connect to the system)

4. Used Wireshark to identify what all types of protocols are there.
   - Mostly TCP, TLSv1.2, ARP, IGMPv3

5. Most common services running on the ports
   - Port 21 = FTP
   - Port 22 = SSH
   - Port 23 = Telnet
   - Port 80 = HTTP
   - Port 443 = https, etc....

6. Potential security risk associated with open ports
   - Attackers can gain unauthorized access through
     - Misconfigured services.
     - Outdated software or unpatched software.
     - Known vulnerabilities and exploits.

