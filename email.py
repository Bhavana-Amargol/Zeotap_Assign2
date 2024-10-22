import smtplib

def send_email_alert(subject, body, to_email):
    from_email = "your_email@gmail.com"
    password = "your_email_password"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)
    
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(from_email, to_email, message)
    server.quit()

def trigger_email_alerts():
    if alerts_triggered:
        subject = "Weather Alert"
        body = "\n".join(alerts_triggered)
        send_email_alert(subject, body, "recipient@example.com")
