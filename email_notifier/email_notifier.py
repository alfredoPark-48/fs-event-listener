import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = 'parkalfredojeonghyun@gmail.com'
receiver_email = 'parkalfredojeonghyun@gmail.com'
password = 'ohecjeotduhehhcz'

def send_email_notification(message_text, subject):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = message_text
    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email notification sent successfully")
        server.quit()
    except Exception as e:
        print("Email notification failed to send:", str(e))
