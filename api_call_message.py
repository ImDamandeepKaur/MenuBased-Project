from flask import Flask, request, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

@app.route("/call/<phone>", methods = ['GET'])
def initiateCall(phone):
    
    twilio_no = "your_assignedNo"
    call = client.calls.create (
        to = phone,
        from_ = twilio_no,
        url = "https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1"
        )
    success = True
    if success:
        return jsonify({"success": True, "message": f"Message sent to {phone}"}), 200
    else:
        return jsonify({"success": False, "error": "Failed to send message"}), 500


@app.route("/sms/<phone>/<message>", methods=['GET'])
def send_sms(phone,message):
    message_body = message
    message = client.messages.create(body = message_body,
                                     from_="your_assignedNo",
                                     to = phone
                                     )
    success = True
    if success:
        return jsonify({"success": True, "message": f"Message sent to {phone}"}), 200
    else:
        return jsonify({"success": False, "error": "Failed to send message"}), 500

@app.route("/whatmsg/<phone>/<message>", methods=['GET'])
def whatsapp(phone,message):
    import pywhatkit as kit 
    message = f"{message}"
    kit.sendwhatmsg_instantly(phone,message)
    
    success = True
    if success:
        return jsonify({"success": True, "message": f"Message sent to {phone}"}), 200
    else:
        return jsonify({"success": False, "error": "Failed to send message"}), 500
    #return "Message Sent!"
@app.route("/bulkwhatmsg/<msg>", methods =['GET'])
def bulkwhatmsg(msg):
    import numpy as np

    stu_arr = np.array([

            [1,"Damandeep","Jaipur","MUJ","+91965xxxxxx","MyWorkTellMyIdentity"],
            [2,"Kulvinder","Jaipur","GCEK","+91999xxxxx","loading"],
            [3,"Harsh","Jaipur","PoornimaUniversity","+9196xxxxxx","private"],
    ])

    import pywhatkit as pwk
    import time
    #Extract whatsapp no
    whatsappno = stu_arr[:,4]

    message = f"{msg}"

    try:
        pwk.sendwhatmsg_instantly(whatsappno, message)
        print("Message send sucessfully")
    except Exception as e:
        print(f"Failed to send message to {whatsappno}: {e}")
        
    for number in whatsappno:
        whatsapp(number,message)
        time.sleep(10)
    success = True
    if success:
        return "Message Sent!"
    else:
        return jsonify({"success": False, "error": "Failed to send message"}), 500
    return "Message Sent!"
app.run()

    
    
    