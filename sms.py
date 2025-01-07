from twilio.rest import Client
import random
# Twilio account credentials
account_sid = ''
auth_token = ''
twilio_phone_number = ''

def send_otp(phone_number):
    client = Client(account_sid, auth_token)
    otp = generate_otp()  

    message = client.messages.create(
        body=f"Click this link to track your order \n ",
        from_=twilio_phone_number,
        to=phone_number
    )

    print(f"OTP sent to {phone_number}. Message SID: {message.sid}")

#Generating OTP through random module
def generate_otp():

    otp = random.randint(999,10000)
    return otp

# Example usage
phone_number = '+917358047659'  # Replace with the desired phone number
send_otp(phone_number)
