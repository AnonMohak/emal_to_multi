import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import List, Dict


class EmailSender:

    def __init__(self, smtp_server: str, smtp_port: int, sender_email: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password


    def read_template(self, template_path: str) -> str:
        with open(template_path, 'r') as file:
            return file.read()


    def personalize_content(self, template: str, name: str) -> str:
        return template.replace('[name]', name)


    def send_emails(self, recipients: Dict[str, str], subject: str, template_path: str) -> List[Dict]:
        template = self.read_template(template_path)
        results = []

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.password)

            for email, name in recipients.items():
                try:
                    msg = MIMEMultipart()
                    msg['From'] = self.sender_email
                    msg['To'] = email
                    msg['Subject'] = subject

                    body = self.personalize_content(template, name)
                    msg.attach(MIMEText(body, 'plain'))

                    server.send_message(msg)

                    results.append({
                        'email': email,
                        'name': name,
                        'status': 'success',
                        'error': None
                    })


                except Exception as e:
                    results.append({
                        'email': email,
                        'name': name,
                        'status': 'failed',
                        'error': str(e)
                    })

            server.quit()
            return results

        except Exception as e:
            raise Exception(f"Failed to establish SMTP connection: {str(e)}")


if __name__ == "__main__":
    #Read README.md for this under Python > Server section

    SMTP_SERVER = "smtp.server.com"
    SMTP_PORT = 587
    SENDER_EMAIL = "your_email@gmail.com"
    PASSWORD = "your_app_specific_password"

    sender = EmailSender(SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, PASSWORD)

    #Read README.md Python > Recipients
    recipients = {

        "abc@gmail.com": "Name1",

        "abc2@yahoo.com": "Name2",

        "abc3@outlook.com": "Name3"

    }

    try:
        results = sender.send_emails(
            recipients=recipients,
            #Read README.md under Python > Subject
            subject="Important Update",
            template_path="email_template.txt"
        )

        for result in results:
            if result['status'] == 'success':
                print(f"✓ Email sent to {result['name']} ({result['email']})")
            else:
                print(f"✗ Failed to send to {result['name']} ({result['email']}): {result['error']}")

    except Exception as e:
        print(f"Error: {str(e)}")
