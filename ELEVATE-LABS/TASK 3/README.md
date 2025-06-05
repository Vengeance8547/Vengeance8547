**-- TASK 3 --**

**Objective:** Use technologies like Nessus to identify system vulnerabilities.

**Recommendations:** Install Nessus on either Linux or Windows.

**Summary:**

1. After downloading and installing Nessus, navigate to the URL: https://<user>:8834. Log in with the account you created.

2. Go to the "Scans" section in the top left corner of the Nessus interface and select "New Scan." A pop-up window will appear. Choose the "Basic Network Scan" option from the pop-up.

3. Within the pop-up, provide the following details:
   - Name
   - Description (if needed)
   - Target

4. In the discovery section, you can either select "Scan All Ports" or the "Common Ports" option, which will yield faster results.

5. For the assessment, you can choose to:
   - Scan for known vulnerabilities for quicker results.
   - Alternatively, select all web vulnerabilities.

6. Review your settings and proceed.

7. Start the scan; this process may take some time.

**Findings:**
- A local device scan revealed a minor vulnerability (no risk) that could potentially allow information to be leaked over the network through NetBIOS or SMB protocols.
  ![Image Alt](https://github.com/Vengeance8547/Vengeance8547/blob/main/TASK%203/nessus.png)
  
- **Recommendation:** Disable NetBIOS settings as it employs a sophisticated TCP/IP configuration.
