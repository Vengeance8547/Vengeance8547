**-- TASK 4 --**

**Objective:** Set up and use firewalls in Linux.

**Requirement:** UFW (Uncomplicated Firewall), Linux OS.

**Summary:**

1. UFW is not pre-installed on Linux. To install it, use the command: `sudo apt install ufw`.

2. After installation, start UFW by running: `sudo ufw start`. Once started, you can add rules, delete rules, and view the existing rules.

3. To view the firewall rules, type the command: `sudo ufw status`. For a detailed view with numbering, use: `sudo ufw status verbose`.

4. If the console shows nothing, it means there are no rules set.

5. To block a specific port (e.g., port 23), use the command: `sudo ufw deny 23`.

6. To check whether the firewall is working, run the command:

   ```
   ssh kali@192.168.174.142
   ```

   You should see an error message like: `ssh: connect to host 192.168.174.142 port 22: Connection refused`.

7. To allow SSH through the firewall, run the command: `sudo ufw allow ssh`.

8. To check the status of all the rules, use: `sudo ufw status verbose`.

9. To delete a specific rule, you can use the command: `sudo ufw delete deny 23`. Alternatively, you can refer to the rules by their numbers:
   - First, find the numbered list of rules by running: `sudo ufw status numbered`.
   - To delete a rule by its number, use: `sudo ufw delete 1`, if you want to delete rule number 1.

10. To disable the firewall, run: `sudo ufw disable`.

**Key Points:**
1. Setting up the UFW firewall in Linux.
2. Enabling the firewall, adding rules, viewing, and deleting rules.
3. Disabling the firewall.
