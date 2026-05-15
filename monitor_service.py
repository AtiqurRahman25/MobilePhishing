from jnius import autoclass, cast
from android.runnable import run_on_ui_thread
import requests
import json

# অ্যান্ড্রয়েড নেটিভ এসএমএস ক্লাস
Telephony = autoclass('android.provider.Telephony$Sms$Intents')
Intent = autoclass('android.content.Intent')

def handle_incoming_sms(context, intent):
    # এসএমএস ডাটা এক্সট্রাক্ট করা
    messages = Telephony.getMessagesFromIntent(intent)
    for msg in messages:
        sender_number = msg.getDisplayOriginatingAddress() # কার নম্বর থেকে এসেছে
        message_body = msg.getDisplayMessageBody() # মেসেজে কী লেখা আছে
        
        print(f"SMS from {sender_number}: {message_body}")
        
        # আপনার Ngrok সার্ভারে পাঠানো
        send_to_ai_server(sender_number, message_body)

def send_to_ai_server(number, text):
    url = "https://desecrate-elf-snack.ngrok-free.dev/predict"
    data = {
        "number": number,
        "message": text
    }
    try:
        requests.post(url, json=data, timeout=5)
    except:
        print("Server unreachable!")