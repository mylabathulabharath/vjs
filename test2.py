from flask import Flask, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import click

app = Flask(__name__)

def send_sms():
    account_sid = 'AC439e4b0f77fd727a91356843af773d4a'
    auth_token = '6199339f2000e6d8c94875d087aa05dc'
    client = Client(account_sid, auth_token)

    to_number = '+919381666049'
    message_body = 'Your message here'

    try:
        message = client.messages.create(
            body=message_body,
            from_='+16592668431',  # Your Twilio number
            to=to_number
        )
        return jsonify({"status": "success", "message_sid": message.sid}), 200
    except TwilioRestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.cli.command('send-sms')
def send_sms_command():
    with app.app_context():
        response, status_code = send_sms()
        print(response.json, status_code)

if __name__ == '__main__':
    app.run(debug=True)
