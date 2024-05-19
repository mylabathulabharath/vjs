import requests
import certifi
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/send_sms')
def send_sms():
    # Your Twilio account SID and Auth Token
    account_sid = 'AC439e4b0f77fd727a91356843af773d4a'
    auth_token = '6199339f2000e6d8c94875d087aa05dc'
    twilio_number = '+16592668431'
    to_number = '+919381666049'
    message_body = 'Hello from Flask with SSL!'

    # Twilio API endpoint
    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'

    # Data to be sent to Twilio API
    data = {
        'From': twilio_number,
        'To': to_number,
        'Body': message_body,
    }

    # Send the request to Twilio API with SSL verification
    response = requests.post(url, data=data, auth=(account_sid, auth_token), verify=certifi.where())

    if response.status_code == 201:
        return jsonify({'status': 'Message sent successfully!'})
    else:
        return jsonify({'status': 'Failed to send message', 'error': response.text}), response.status_code

if __name__ == "__main__":
    app.run(ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
