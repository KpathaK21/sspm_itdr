from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail 
import os

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
SENDER_EMAIL = 'kunjpathak74@gmail.com'
RECIPIENT_EMAIL = 'kunj.pathak1021@gmail.com'

def send_email_alert(subject, content):
    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=RECIPIENT_EMAIL,
        subject=subject,
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        repsonse = sg.send(message)
        print(f"Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error Sending email: {e}")

        
