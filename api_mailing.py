from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)

CORS(app)

import smtplib
import time
import schedule
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from datetime import datetime, time, timedelta

# Importing the time module for sleep function

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

@app.route("/instantMail/<recieverid>/<subj>/<body>", methods=['GET'])

def sendinstant_mail(recieverid,subj,body):
 
    sender_email = "damandeepkaur494@gmail.com"
    receiver_email = recieverid
    password = 'your_generated_password'
    subject = subj
    mail_body = body
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(mail_body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    success = True
    if success:
        return jsonify({"success": True, "message": f"Message sent to {receiver_email}"}), 200
    else:
        return jsonify({"success": False, "error": "Failed to send message"}), 500


@app.route("/scheduleMail/<recieverid>/<subj>/<body>/<hour>/<minute>", methods=['GET'])
def sendsheduled_mail(recieverid, subj, body, hour, minute):
    sender_email = 'damandeepkaur494@gmail.com'
    receiver_email = recieverid
    password = 'your_generated_password'
    subject = subj
    body = body
    
    now = datetime.now()
    send_time = time(hour, minute)
    send_datetime = datetime.combine(now.date(), send_time)
    
    if send_datetime <= now:
        send_datetime += timedelta(days=1)  # Send tomorrow if time has passed today
    
    delay = (send_datetime - now).total_seconds()
    success = True
    if success:
        return jsonify({"success": True, "message": f"Message sent to {receiver_email}"}), 200
    else:
        return jsonify({"success": False, "error": "Failed to send message"}), 500

@app.route("/googleresultMail/<senderid>/<recieverid>/<qn>", methods=['GET'])

def googleresult_mail(senderid,recieverid,qn):
    
    from googlesearch import search
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    def get_google_search_results(query, num_results=5):
        return list(search(query, num_results=num_results))

    def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

    def main():
        query = qn
        results = get_google_search_results(query)

        subject = "Top 5 Google Search Results"
        body = "\n".join(results)

        to_email =senderid
        from_email = recieverid
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_user = "damandeepkaur494@gmail.com"
        smtp_password = "your_generated_password"

        send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password)
        return "Email sent!"
    return main()
    

app.run()   
    
    
    