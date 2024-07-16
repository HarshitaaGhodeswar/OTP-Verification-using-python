import random
import smtplib
from email.message import EmailMessage

def send_email(subject, message, from_addr, to_addr, password):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_addr, password)
    server.send_message(msg)
    server.quit()

otp = str(random.randint(100000, 999999))
print("Generated OTP:", otp)

from_addr = "your_email@gmail.com"
password = "your_password"
to_addr = input("Enter your email: ")
subject = "OTP Verification"
message = f"Your OTP is: {otp}"

send_email(subject, message, from_addr, to_addr, password)

user_email = input("Enter your email: ")
user_otp = input("Enter the OTP you received: ")

if user_email == to_addr and user_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP or email.")