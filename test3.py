from twilio.rest import Client

account_sid = 'AC439e4b0f77fd727a91356843af773d4a'
auth_token = '614779f4b34dc2f3404fce9e51bbf3d2'
client = Client(account_sid, auth_token)

try:
    client.api.accounts(account_sid).fetch()
    print("Twilio credentials are valid")
except Exception as e:
    print(f"Error: {e}")
