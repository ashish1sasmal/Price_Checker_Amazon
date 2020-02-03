from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN

def whatsapp(msg,to_whatsapp_number):
    client = Client()

    # this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'




    client.messages.create(body=msg,
                           from_=from_whatsapp_number,
                           to='whatsapp:+91'+to_whatsapp_number)
    print(" whatsapp message sent !")
    return
