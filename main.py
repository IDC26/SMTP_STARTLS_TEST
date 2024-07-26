import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
smtp_host = 'REPLACE'
smtp_port = "REPLACE_WITH_PORT"
smtp_user = 'REPLACE'
smtp_password = 'REPLACE'

# Email details
from_email = 'REPLACE'
to_email = 'REPLACE'  # Replace with the recipient's email address
subject = 'Test Email'
body = 'This is a test email sent from Python script.'

# Create a MIME message
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.ehlo()  # Can be omitted
    server.starttls()
    server.ehlo()  # Can be omitted
    server.login(smtp_user, smtp_password)
    
    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Failed to send email: {e}")

finally:
    if 'server' in locals():
        server.quit()
