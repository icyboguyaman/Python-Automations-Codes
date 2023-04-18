import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver email addresses
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"

# Message content
subject = "Automated Email"
body = "Hello, this is an automated email sent using Python."

# Create a message object
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Send the email
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()
    smtp.login(sender_email, 'your_password')
    smtp.send_message(message)

print("Email sent successfully!")
