**-- TASK 2 --**

**Objective:** Identify phishing characteristics in a suspicious email sample.

**Requirements:** A spam mail sample. 

**Summary:**

       "Sample mail:
       
        Subject: 🔥 Your Netflix account has been suspended! Verify now!
        From: netflix-security@support-alerts.com
        Dear Netflix User,
        We regret to inform you that your account has been temporarily suspended due to suspicious activity.
        Please verify your billing information within 24 hours to avoid service interruption.
        Click the secure link below to update your details:
        **👉 Verify Now**
        If you do not respond within 24 hours, your account will be permanently locked.
        Thank you,
        Netflix Support Team
        © 2025 Netflix Inc. All rights reserved. "

When analyzing an email, it's important to consider the following points:

1. **Email Headers**: Examine the email address to determine if it is legitimate or potentially forged. This helps confirm the email's validity.
   
2. **Metadata**: In the case of AI-generated emails, the headers may lack any useful metadata, making it difficult to conduct further analysis.

3. **Links**: Be cautious of links present in the email. For example, there was a link in the email from "verified now," which could potentially lead to a site that steals our credentials.

4. **Urgency**: The subject line and body of the email convey a sense of urgency, indicating that action is required to confirm the account, or it will be suspended.

5. **Findings**:
    - The email creates a strong sense of urgency.
    - The email address appears to be spoofed.
    - There is a link that directs to a phishing website designed to steal credentials.
    - The email includes a sign-off that aims to make it seem more legitimate.
