# emal_to_multi

##Do 

One to Multi email sender,

##Python

**server**

if you using gmail replace the code in script.py with the following.
```
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@gmail.com"
    PASSWORD = "your_app_specific_password"
```
enter your email and app-specific password in SENDER_Email and PASSWORD.

*how to get app-specific password*
 -Go to Google Account settings. 
 -Enable 2-Step verification. 
 -Security->App-passwords.
 -Generate a new app-password for mail.
 -Copy and paste that as your app-specific password.

**recipient**

Replace the email and Name with the people who you wanna send the email too.

**subject**

Add the subject of the emails here.

**RUN**
 
To run the file,
```
pip install secure-smtplib
python script.py
```

#GGs    
