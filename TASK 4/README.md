-- TASK 4 -- 

Objective: Setup and use of firewalls in linux.

Requirement: UFW(Uncomplicated Firewall), Linux OS.

Summary:
1. In linux ufw is not pre-installed. To install it we will give the command like "sudo apt install ufw".

2. After installing we need to start "sudo ufw start". After starting it we can add rules, delete it, view etc every rules.

3. To view the firewall rules just type the command "sudo ufw status" or to get detailed view with the numbering we need to type "sudo ufw status verbose".

4. If nothing is there in the console it means there are no rules in it.

5. So to block a port(23) 
    - Type the command "sudo ufw deny 23"

6. To check whether it working or not:

   ┌──(kali㉿kali)-[~]

    └─$ ssh kali@192.168.174.142

     ssh: connect to host 192.168.174.142 port 22: Connection refused

8. To add the ssh allow rule in the firewall
    - "sudo ufw allow ssh"

9. To check the status of all the rules 
    - "sudo ufw status verborse"

10. To delete the certain rule
    - "sudo ufw delete deny 23"
    
    Or you can delete using the numbers 
    - "sudo ufw status numbered" ## which will give you the rules in numbered starting form 1. 
    - "sudo ufw delete 1" ##So if you want to delete the rule 1.

11. To disable the firewall
    - "sudo ufw disable"


key Things:
1. Setting up UFW firewall in linux.
2. Enabling, adding rulees, viewing and deleting rules. 
3. Disabling the firewall. 
