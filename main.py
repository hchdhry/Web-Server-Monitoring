import requests
import smtplib
from email.mime.text import MIMEText

def check_server(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return True
    except requests.exceptions.RequestException:
        return False

def send_email(down_servers):
    sender_email = "email"
    receiver_email = "email"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "email"  
    smtp_password = "."  

    message = f"The following servers are down:\n\n{'\n'.join(down_servers)}"
    msg = MIMEText(message)
    msg['Subject'] = "Server Down Notification"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

def main():
    urls = ["http://localhost:3000/"]
    down_servers = []

    for url in urls:
        if not check_server(url):
            down_servers.append(url)

    if down_servers:
        send_email(down_servers)

if __name__ == "__main__":
    main()