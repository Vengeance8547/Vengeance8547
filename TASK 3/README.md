-- TASK 3 --

Objective: Using technologies such as Nessus to identify system vulnerabilities. 

Recommendations: Installation of Nessus is required on Linux/Windows.

Summary: 
1. After downloading and installing Nessus. Go to the URL https://<user>:8834. Log in with the account you created.

2. Go to the scans section on the top left side of the nessus website (New Scan). It will show you a pop-up. In the popup window, select the "basic network scan" option.

3. After selecting options, provide the 
    - Name 
    - Description (if required)
    - Target 
    
4. In discovery, you can choose -- scan all ports. 
    - Otherwise select common port option.(which will give results faster)

5. Then comes the assessment that we should provide. 
    - For faster scanning, use the option to scan for known vulnerabilities. 
    - Alternatively, pick all web vulnerabilities. 

5. Proceeded with everything. 

6. Start the scan; it will take some time.

7. Findings: 
    - A local device scan revealed a minor vulnerability (no risk) that could allow information to be leaked over the network using NetBIOS or SMB protocols.
    -  ![Image Alt](https://github.com/Vengeance8547/Vengeance8547/blob/main/TASK%203/nessus.png)
    - Recommendation: Disable NetBios settings. It is using sophisticated TCP/IP settings.
