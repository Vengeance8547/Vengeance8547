-- TASk 2 --

Objective: Identify phishing characteristics in a suspicious email sample.
Requirements : A spam mail sample. 

Summary:

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

When analyzing an email, you should be aware of the following:
   1. Email headers: we must examine the email address to see if it is a legitimate email or forgery in order to confirm the email's validity.
  
   2. Since this is an AI-generated email, the headers don't include any metadata that could be used to further examine the headers.
 
   3. Links: At verified now, there was a link.  This will probably take our credentials.
 
   4. Urgency: The subject and body lines in this instance demonstrate the urgency.  to confirm the account, failing which it will be suspended.
 
   5. Findings:
      - First and foremost, the email communicates a sense of urgency.
      - The email address is spoofed.
      - There is a link leads to a phishing website that steals credentials.
      - They've also added an ending to make it more legitimate.
